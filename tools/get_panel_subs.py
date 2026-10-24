#!/usr/bin/env python3
"""Fetch a YouTube transcript via the get_panel (transcript panel) endpoint.

Bypasses /api/timedtext, which is IP-rate-limited separately.
Two requests per video. Writes SRT (and raw JSON cues).
"""
import base64, json, sys, time, urllib.request

CLIENT_VERSION = "2.20260811.07.00"
PLAYER_URL = "https://www.youtube.com/youtubei/v1/player?prettyPrint=false"
PANEL_URL = "https://www.youtube.com/youtubei/v1/get_panel?prettyPrint=false"
PANEL_ID = "PAmodern_transcript_view"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36")


def varint(v):
    out = bytearray()
    while True:
        b = v & 0x7F
        v >>= 7
        if v:
            out.append(b | 0x80)
        else:
            out.append(b)
            return bytes(out)


def build_params(video_id, mode=2):
    inner = varint(1 << 3 | 2) + varint(len(video_id)) + video_id.encode() + varint(3 << 3 | 0) + varint(mode)
    return base64.b64encode(varint(149 << 3 | 2) + varint(len(inner)) + inner).decode()


def post(url, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method="POST", headers={
        "User-Agent": UA, "Content-Type": "application/json",
        "Origin": "https://www.youtube.com",
        "X-Youtube-Client-Name": "1", "X-Youtube-Client-Version": CLIENT_VERSION,
    })
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(15 * (attempt + 1))
                continue
            raise
    raise RuntimeError("unreachable")


def walk(node, key):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == key:
                yield v
            yield from walk(v, key)
    elif isinstance(node, list):
        for v in node:
            yield from walk(v, key)


def parse_ts(s):
    t = 0
    for p in s.split(":"):
        t = t * 60 + int(p)
    return float(t)


def fmt_srt(i, start, end, text):
    def ts(x):
        ms = int(round(x * 1000))
        h, ms = divmod(ms, 3600000)
        m, ms = divmod(ms, 60000)
        s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
    return f"{i}\n{ts(start)} --> {ts(end)}\n{text}\n"


def main(video_id, out_prefix):
    player = post(PLAYER_URL, {
        "context": {"client": {"clientName": "ANDROID", "clientVersion": "20.10.38", "hl": "en", "gl": "US"}},
        "videoId": video_id,
    })
    status = (player.get("playabilityStatus") or {}).get("status", "OK")
    if status in ("ERROR", "LOGIN_REQUIRED", "UNPLAYABLE"):
        print(f"{video_id}: playability {status}: {(player.get('playabilityStatus') or {}).get('reason')}", flush=True)
        return 1

    renderer = (player.get("captions") or {}).get("playerCaptionsTracklistRenderer") or {}
    tracks = renderer.get("captionTracks") or []
    codes = [t.get("languageCode") for t in tracks]
    lang = "en" if "en" in codes else (codes[0] if codes else None)
    if not lang:
        print(f"{video_id}: no caption tracks", flush=True)
        return 1
    gen = any(t.get("kind") == "asr" and t.get("languageCode") == lang for t in tracks)
    print(f"{video_id}: tracks={codes} using={lang} generated={gen}", flush=True)

    try:
        dur = float((player.get("videoDetails") or {}).get("lengthSeconds") or 0) or None
    except ValueError:
        dur = None

    panel = post(PANEL_URL, {
        "context": {"client": {"clientName": "WEB", "clientVersion": CLIENT_VERSION, "hl": lang, "gl": "US"}},
        "panelId": PANEL_ID,
        "params": build_params(video_id),
    })

    cues = []
    for view in walk(panel, "transcriptSegmentViewModel"):
        text = view.get("simpleText")
        stamp = view.get("timestamp")
        if not text or stamp is None:
            continue
        try:
            cues.append((parse_ts(stamp), " ".join(text.split())))
        except ValueError:
            continue

    if not cues:
        print(f"{video_id}: panel returned no cues", flush=True)
        return 1

    with open(f"{out_prefix}.cues.json", "w") as f:
        json.dump({"video": video_id, "lang": lang, "generated": gen, "duration": dur,
                   "cues": [{"t": t, "x": x} for t, x in cues]}, f, ensure_ascii=False)

    lines = []
    for i, (start, text) in enumerate(cues):
        end = cues[i + 1][0] if i + 1 < len(cues) else (dur if dur and dur > start else start + 5)
        lines.append(fmt_srt(i + 1, start, end, text))
    srt_path = f"{out_prefix}.en.srt"
    with open(srt_path, "w") as f:
        f.write("\n".join(lines))
    print(f"OK {srt_path}: {len(cues)} cues, ~{cues[-1][0]/60:.0f} min", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
