#!/usr/bin/env python3
"""Production sheet engine — make + check. Works for standard and custom compilations.

A sheet is the product: ordered blocks (speech / marker / pause / sfx) with
timed pauses, gains, comments and non-rendered annotations. The audio is a
rendering of the sheet; check validates sheet, audio and their agreement.

  sheet.py render sheet.json            -> mix + built manifest + sheet.md
  sheet.py check  sheet.json [--engine] -> PASS/FLAG report, exit 1 on FLAG

Snap rule (speech blocks): cuts land inside source silence —
start = speech onset - lead (default 0.3s), end = speech end + tail (default
0.15s), searched near the designed window at adaptive silence thresholds
(hissy archive files need louder thresholds than studio ones).
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

THRS = (-26, -32, -38, -44, -22)
PEAK_CLIP = -0.2
MEAN_LO, MEAN_HI = -30.0, -14.0
EDGE_QUIET = -45.0
PAUSE_MAX = -30.0
AIR_TOL = 1.3


def sh(cmd, check=True):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.stderr.write(r.stderr[-2000:] + "\n")
        raise SystemExit(f"cmd failed: {' '.join(cmd[:10])}")
    return r


def ffprobe(path, key="duration"):
    return float(sh(["ffprobe", "-v", "error", "-show_entries", f"format={key}",
                     "-of", "default=noprint_wrappers=1:nokey=1", path],
                    check=False).stdout.strip() or 0)


def vol(path, ss=None, t=None):
    cmd = ["ffmpeg", "-hide_banner", "-nostats"]
    if ss is not None:
        cmd += ["-ss", str(ss), "-t", str(t)]
    cmd += ["-i", path, "-af", "volumedetect", "-f", "null", "-"]
    err = sh(cmd).stderr
    out = {}
    for k in ("mean_volume", "max_volume"):
        m = re.search(rf"{k}: (-?[\d.]+) dB", err)
        out[k] = float(m.group(1)) if m else None
    return out


def sils(path, lo, hi, thr, d=0.12):
    dur = hi - lo
    if dur <= 0.05:
        return []
    err = sh(["ffmpeg", "-hide_banner", "-nostats", "-ss", str(lo), "-t", str(dur),
              "-i", path, "-af", f"silencedetect=noise={thr}dB:d={d}", "-f", "null",
              "-"], check=False).stderr
    out, st = [], None
    for line in err.splitlines():
        m = re.search(r"silence_start: ([\d.]+)", line)
        if m:
            st = lo + float(m.group(1))
        m = re.search(r"silenence_end: ([\d.]+)", line) or re.search(r"silence_end: ([\d.]+)", line)
        if m and st is not None:
            out.append((st, lo + float(m.group(1))))
            st = None
    return out


def any_sils(path, lo, hi):
    for thr in THRS:
        s = sils(path, lo, hi, thr)
        if s:
            return s, thr
    return [], None


def snap(path, s, e, lead, tail, search):
    dur = ffprobe(path)
    s = min(max(s, 0.0), dur)
    e = min(max(e, s + 1.0), dur)
    pre, _ = any_sils(path, max(0.0, s - search), min(dur, s + 1.5))
    containing = [(a, b) for a, b in pre if a <= s <= b]
    if containing:
        a, b = containing[0]
        s = max(a, b - lead) if b - lead >= a else a
    else:
        preceding = [(a, b) for a, b in pre if 0 <= b <= s]
        if preceding and s - max(b for _, b in preceding) < 1.0:
            s = max(b for _, b in preceding) - lead
    post, _ = any_sils(path, max(0.0, e - 1.5), min(dur, e + search))
    ne = e
    for a, b in post:
        if a <= e <= b:
            ne = min(b - 0.02, a + tail)
            if ne <= a:
                ne = a + tail
            break
    if ne == e:
        for a, b in post:
            if a >= e:
                ne = a + tail
                break
    return round(s, 3), round(min(ne, dur), 3)


def extract(src, s, e, dst, af=None, extra=None):
    cmd = ["ffmpeg", "-y", "-v", "error"]
    if extra:
        cmd += extra
    cmd += ["-ss", str(s), "-t", str(e - s), "-i", src]
    if af:
        cmd += ["-af", af]
    cmd += ["-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", dst]
    sh(cmd)


def gain_for(path, target):
    v = vol(path)
    return min(target - v["mean_volume"], -1.5 - v["max_volume"])


def apply_gain(src, g, dst):
    if abs(g) < 0.05:
        if os.path.abspath(src) != os.path.abspath(dst):
            subprocess.run(["cp", src, dst], check=True)
        return
    sh(["ffmpeg", "-y", "-v", "error", "-i", src, "-af", f"volume={g:.2f}dB",
        "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", dst])


def resolve(sheet, key):
    src = sheet["sources"][key]
    path = src["file"]
    if not os.path.isabs(path):
        path = os.path.join(sheet["_base"], path)
    return path, src


def render(sheet_path):
    sheet = json.load(open(sheet_path))
    base = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(sheet_path)),
                                         sheet.get("base", ".")))
    sheet["_base"] = base
    out_dir = os.path.join(base, sheet.get("out_dir", "build/sheet"))
    pieces = os.path.join(out_dir, "pieces")
    os.makedirs(pieces, exist_ok=True)
    fmt = sheet.get("format", {})
    speech_target = fmt.get("speech_target_db", -21.0)
    lead = fmt.get("lead_s", 0.3)
    tail = fmt.get("tail_s", 0.3)
    search = fmt.get("snap_search_s", 6.0)

    room = {}
    for key, src in sheet["sources"].items():
        if src.get("kind") == "room":
            p, _ = resolve(sheet, key)
            rp = os.path.join(pieces, f"tone_{key}.wav")
            a, b = src["span"]
            extract(p, a, b, rp, af="afade=t=in:st=0:d=0.05,afade=t=out:st=0.05:d=0.05"
                   if b - a > 0.2 else None)
            room[key] = rp

    timeline, gains, order, log = [], {}, [], []
    for blk in sheet["blocks"]:
        if not blk.get("render", True):
            continue
        kind = blk["kind"]
        pid = blk["id"]
        ppath = os.path.join(pieces, f"{pid}.wav")
        if kind == "speech":
            spath, ssrc = resolve(sheet, blk["src"])
            s, e = snap(spath, *blk["window"], lead=blk.get("lead", lead),
                        tail=blk.get("tail", tail), search=search)
            extract(spath, s, e, ppath)
            if "gain_db" in blk:
                g = blk["gain_db"]
            else:
                g = gain_for(ppath, blk.get("match_target_db", speech_target))
            # 60ms edge fades on the room pad: no hiss-step at bell/head joins
            # optional per-block "eq" (ffmpeg filter chain) for tone surgery
            df = ffprobe(ppath)
            eq = blk.get("eq", "")
            af = (f"volume={g:.2f}dB" + (f",{eq}" if eq else "") + ","
                  f"afade=t=in:d=0.06,"
                  f"afade=t=out:st={max(0.0, df - 0.07):.3f}:d=0.06")
            sh(["ffmpeg", "-y", "-v", "error", "-i", ppath, "-af", af,
                "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", ppath + ".g.wav"])
            os.replace(ppath + ".g.wav", ppath)
            gains[pid] = round(g, 2)
            log.append(f"speech {pid:16s} [{blk['window'][0]},{blk['window'][1]}] -> [{s},{e}] ({e - s:.2f}s) gain {g:+.2f}dB")
        elif kind == "sfx":
            spath, ssrc = resolve(sheet, blk["src"])
            a, b = blk.get("span", [0, ffprobe(spath)])
            extract(spath, a, b, ppath)
            g = blk.get("gain_db")
            if g is None:
                g = gain_for(ppath, blk.get("match_target_db", speech_target))
            apply_gain(ppath, g, ppath + ".g.wav")
            os.replace(ppath + ".g.wav", ppath)
            gains[pid] = round(g, 2)
            log.append(f"sfx   {pid:16s} [{a},{b}] gain {g:+.2f}dB  {blk.get('comment','')}")
        elif kind == "marker":
            spath, ssrc = resolve(sheet, blk["src"])
            d = blk.get("dur")
            if d:
                extract(spath, 0, d, ppath, af=f"afade=t=out:st={max(0, d - 0.15):.3f}:d=0.15")
            else:
                subprocess.run(["cp", spath, ppath], check=True)
            gains[pid] = None
            log.append(f"marker {pid:15s} dur {d}  {blk.get('comment', '')}")
        elif kind == "pause":
            d = blk["dur"]
            tone = blk.get("tone", "digital")
            if tone == "digital":
                sh(["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
                    "-i", "anullsrc=r=44100:cl=stereo", "-t", f"{d:.3f}",
                    "-c:a", "pcm_s16le", ppath])
            elif tone == "switch":
                # her room first half, his room second half, short fades at the
                # seam: floor is continuous at both voice edges, step hidden mid-gap
                a = round(d / 2, 3)
                b = round(d - a, 3)
                tmpa, tmpb = ppath + ".a.wav", ppath + ".b.wav"
                sh(["ffmpeg", "-y", "-v", "error", "-i", room["room_baumer"],
                    "-t", f"{a:.3f}", "-af", f"afade=t=out:st={max(0, a - 0.08):.3f}:d=0.08",
                    "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", tmpa])
                sh(["ffmpeg", "-y", "-v", "error", "-i", room["room_wallis"],
                    "-t", f"{b:.3f}", "-af", "afade=t=in:d=0.08",
                    "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", tmpb])
                lstp = ppath + ".cat.txt"
                open(lstp, "w").write(f"file '{tmpa}'\nfile '{tmpb}'\n")
                sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", lstp, "-c:a", "pcm_s16le", ppath])
                os.remove(tmpa); os.remove(tmpb); os.remove(lstp)
                got = ffprobe(ppath)
                if abs(got - d) > 0.05:
                    raise SystemExit(f"pause {pid}: rendered {got:.3f}s != spec {d}s")
            else:
                src_tone = room[tone]
                tdur = ffprobe(src_tone)
                reps = int(d // tdur) + 1
                sh(["ffmpeg", "-y", "-v", "error", "-stream_loop", str(reps),
                    "-i", src_tone, "-t", f"{d:.3f}", "-af",
                    "afade=t=in:st=0:d=0.03,afade=t=out:st=%.3f:d=0.03" % max(0, d - 0.03),
                    "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", ppath])
            gains[pid] = None
            log.append(f"pause {pid:16s} {d:.2f}s tone={tone}  {blk.get('comment', '')}")
        else:
            raise SystemExit(f"unknown block kind: {kind}")
        order.append(ppath)
        timeline.append({"id": pid, "kind": kind, "speaker": blk.get("speaker"),
                         "file": os.path.basename(ppath),
                         "comment": blk.get("comment", ""), **{k: timeline_key(blk, k)
                         for k in ()}})
        timeline[-1].update({"dur_expected": blk.get("dur")})

    lst = os.path.join(pieces, "concat_sheet.txt")
    with open(lst, "w") as f:
        for p in order:
            f.write(f"file '{p}'\n")
    out_mp3 = os.path.join(base, sheet["output"])
    sh(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
        "-c:a", "libmp3lame", "-b:a", "192k", out_mp3])

    t = 0.0
    for row in timeline:
        d = ffprobe(os.path.join(pieces, row["file"]))
        row["start"] = round(t, 3)
        row["end"] = round(t + d, 3)
        row["dur"] = round(d, 3)
        t += d
    v = vol(out_mp3)
    built = {**sheet, "timeline": timeline, "gains": gains,
             "duration_s": ffprobe(out_mp3),
             "loudness": {"mean_db": v["mean_volume"], "max_db": v["max_volume"]}}
    built_path = os.path.join(base, sheet.get("built", sheet["output"] + ".built.json"))
    json.dump(built, open(built_path, "w"), indent=1)

    md = ["# PRODUCTION SHEET — %s (%s, v%s)  ·  %.2f min" % (
        sheet["product"], sheet.get("mode", "?"), sheet.get("version", "?"),
        built["duration_s"] / 60), "",
        "Render of record: `%s` · built manifest: `%s`" % (
            sheet["output"], os.path.basename(built_path)), "",
        "| time | block | kind | speaker | dur | comment |", "|---|---|---|---|---|---|"]
    def mmss(x):
        return f"{int(x // 60)}:{x % 60:04.1f}"
    for row in timeline:
        md.append("| %s–%s | %s | %s | %s | %.2fs | %s |" % (
            mmss(row["start"]), mmss(row["end"]), row["id"], row["kind"],
            row["speaker"] or "—", row["dur"], row.get("comment") or ""))
    if sheet.get("annotations"):
        md += ["", "## Annotations (not rendered)", "| at | type | note |", "|---|---|---|"]
        for a in sheet["annotations"]:
            md.append("| %s | %s | %s |" % (a["at"], a["type"], a["note"]))
    md += ["", "Timing rules: %s" % json.dumps(sheet.get("format", {})), ""]
    md_path = os.path.join(base, sheet.get("sheet_md", "production_sheet.md"))
    open(md_path, "w").write("\n".join(md))
    print("\n".join(log))
    print(f"== rendered {out_mp3}  {built['duration_s']:.2f}s  mean {v['mean_volume']} peak {v['max_volume']} dB ==")
    print(f"built manifest: {built_path}\nsheet md: {md_path}")
    return built_path, out_mp3


def timeline_key(blk, k):
    return None


def check(sheet_path, engine=None):
    sheet = json.load(open(sheet_path))
    base = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(sheet_path)),
                                         sheet.get("base", ".")))
    sheet["_base"] = base
    built_path = os.path.join(base, sheet.get("built", sheet["output"] + ".built.json"))
    built = json.load(open(built_path))
    mix = os.path.join(base, sheet["output"])
    flags = []
    tl = built["timeline"]

    total = sum(r["dur"] for r in tl)
    actual = ffprobe(mix)
    if abs(total - actual) > 0.15:
        flags.append(f"CONFORM: timeline sum {total:.2f} vs audio {actual:.2f}")

    for r in tl:
        if r["kind"] != "speech":
            continue
        p = os.path.join(base, sheet.get("out_dir", "build/sheet"), "pieces", r["file"])
        d = ffprobe(p)
        h = vol(p, 0, min(0.04, d))["max_volume"]
        t = vol(p, max(0, d - 0.04), 0.04)["max_volume"]
        if (h is not None and h > EDGE_QUIET) or (t is not None and t > EDGE_QUIET):
            flags.append(f"EDGE {r['file']}: head {h} / tail {t} dB (cut not in silence)")

    for r in tl:
        if r["kind"] != "pause":
            continue
        v = vol(mix, r["start"] + 0.03, max(0.05, r["dur"] - 0.06))
        if v["max_volume"] is not None and v["max_volume"] > PAUSE_MAX:
            flags.append(f"PAUSE {r['id']} @{r['start']:.1f}s: content {v['max_volume']} dB inside timed pause")

    speech = [r for r in tl if r["kind"] == "speech"]
    for i in range(len(speech) - 1):
        a, b = speech[i], speech[i + 1]
        if a["id"] == b["id"]:
            continue
        idx_a = tl.index(a)
        idx_b = tl.index(b)
        between = tl[idx_a + 1:idx_b]
        if not all(x["kind"] == "pause" or x["kind"] == "marker" for x in between) or not between:
            continue
        pauses = [x for x in between if x["kind"] == "pause"]
        if len(pauses) != 1:
            continue
        spec = pauses[0]["dur"]
        err = sh(["ffmpeg", "-hide_banner", "-nostats", "-i", mix, "-af",
                  "silencedetect=noise=-38dB:d=0.1", "-f", "null", "-"], check=False).stderr
        # air measured below once for whole file (loop avoided)
    airs = []
    err = sh(["ffmpeg", "-hide_banner", "-nostats", "-i", mix, "-af",
              "silencedetect=noise=-38dB:d=0.1", "-f", "null", "-"], check=False).stderr
    S, st = [], None
    for line in err.splitlines():
        m = re.search(r"silence_start: ([\d.]+)", line)
        if m:
            st = float(m.group(1))
        m = re.search(r"silence_end: ([\d.]+)", line)
        if m and st is not None:
            S.append((st, float(m.group(1))))
            st = None
    for i in range(len(speech) - 1):
        a, b = speech[i], speech[i + 1]
        idx_a, idx_b = tl.index(a), tl.index(b)
        between = tl[idx_a + 1:idx_b]
        if len(between) != 1 or between[0]["kind"] != "pause":
            continue
        spec = between[0]["dur"]
        containing = [s for s in S if s[0] - 0.15 <= a["end"] and s[1] + 0.15 >= b["start"]]
        if not containing:
            flags.append(f"AIR {a['id']}->{b['id']}: no measurable silence across pause")
            continue
        air = max(s[1] - s[0] for s in containing)
        airs.append((between[0]["id"], round(air, 2), spec))
        if air < spec + 0.1 or air > spec + 1.3:
            flags.append(f"AIR {between[0]['id']}: {air:.2f}s vs spec {spec}s (+pads band)")

    v = vol(mix)
    if v["max_volume"] is None or v["max_volume"] >= PEAK_CLIP:
        flags.append(f"CLIP: peak {v['max_volume']} dB")
    if v["mean_volume"] is not None and not (MEAN_LO <= v["mean_volume"] <= MEAN_HI):
        flags.append(f"LEVEL: mean {v['mean_volume']} dB outside [{MEAN_LO},{MEAN_HI}]")

    if engine and os.path.exists(engine):
        r = subprocess.run(["python3", engine, mix, "--manifest", built_path],
                           capture_output=True, text=True)
        if r.returncode != 0:
            flags += [ln.strip() for ln in r.stdout.splitlines()
                      if ln.strip().startswith(("SEAM", "SPACE", "PACE", "BREATH", "CLIP", "LEVEL"))]

    print(f"== SHEET CHECK: {sheet['product']} ({sheet.get('mode')}) ==")
    print(f"blocks {len(tl)} | audio {actual:.2f}s | mean {v['mean_volume']} peak {v['max_volume']} dB")
    if airs:
        sw = [a for a in airs if a[0].startswith("sw")]
        ld = [a for a in airs if a[0].startswith("land")]
        if sw:
            xs = [a[1] for a in sw]
            print(f"switch airs: n={len(xs)} min/med/max {min(xs):.2f}/{sorted(xs)[len(xs)//2]:.2f}/{max(xs):.2f}s")
        if ld:
            xs = [a[1] for a in ld]
            print(f"land airs:   n={len(xs)} min/med/max {min(xs):.2f}/{sorted(xs)[len(xs)//2]:.2f}/{max(xs):.2f}s")
    if flags:
        print("-- FLAGS --")
        for f in flags:
            print("  " + f)
    print("== VERDICT:", "FLAG" if flags else "PASS", "==")
    return 1 if flags else 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("render")
    r.add_argument("sheet")
    c = sub.add_parser("check")
    c.add_argument("sheet")
    c.add_argument("--engine", default="/home/box/Documents/patala/skills/skill-tempo-check/engine.py")
    args = ap.parse_args()
    if args.cmd == "render":
        render(args.sheet)
        sys.exit(0)
    sys.exit(check(args.sheet, args.engine))


if __name__ == "__main__":
    main()
