#!/usr/bin/env python3
"""Dual reading v2 build: seam-fixed windows + spacing + SFX kit + loudness match."""
import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(ROOT, "build", "dual_reading")
PIECES = os.path.join(WORK, "pieces")
OUT_MP3 = os.path.join(WORK, "vatula_full_dual_reading.mp3")
SPEECH_TARGET = -21.0
PEAK_CAP = -1.5

B_WINDOWS = {
    1: (105.0, 143.0, "end153->143: chop fix (cut mid 'sudden inspiration'); both translations complete at 142.16; start on silence before 'maha sahasa' (speech 105.35)"),
    2: (22.5, 47.3, "start20->22.5: v1 began on orphan 'nature swarupa' tail; clean sentence start 22.92; end gloss sentence ends 46.69"),
    3: (47.0, 64.4, "start kept (in silence 46.27-47.4); end pad into 63.6-65.5 gap after 'great voidness'"),
    4: (91.0, 121.3, "end117->121.3: v1 chopped LJ translation before 'where there is no room for any other agency' (ends 120.8)"),
    5: (64.6, 84.15, "start65->64.6:0.4 lead before speech onset 64.98; end83->84.15: completes 'of the first sutra' (speech ends 83.97)"),
    6: (262.0, 275.6, "end270->275.6: v1 cut the payoff 'the inexpressible stage of transcendental consciousness is revealed' (ends 275.16)"),
    7: (48.8, 68.6, "start48->48.8: lead before 'Sutra 7' onset 49.19; end70->68.6: translation ends 68.03, drop 2s dead air"),
    8: (158.0, 176.15, "start kept (silence to 159.52, 'Rasa Tritaya' onset); end after 'emerges spontaneously' (speech ends 175.84)"),
    9: (45.9, 55.25, "start46->45.9: 0.1 lead before onset 46.0; end55->55.25: keep full 'oneself' (silence 55.1-55.41)"),
    10: (43.9, 69.3, "start43->43.9: v1 began on orphan prev-sentence tail; speech starts 44.27; end68->69.3: completes 'great rays of consciousness' (speech ends 68.83)"),
    11: (311.65, 350.3, "start311->311.65: v1 included 'process.' tail; end345->350.3: v1 chopped mid-sentence; 'is entered into' ends 349.87"),
    12: (97.6, 113.0, "start94->97.6: v1 began mid 'beyond good and evil'; Sanskrit+EN per unit note (speech 98.28); end112->113.0: completes 'with good and evil' (speech ends 112.47)"),
    13: (697.5, 718.0, "start696->697.5: v1 included orphan 'straightforward.' tail; 'Let us first listen' starts 698.16; end kept (silence 717.2-718.91)"),
}

H_WINDOWS = {
    "intro": (320.55, 403.6, "end402.7->403.6: v1 cut before the word 'commentator' (402.96-403.5); start kept (silence to 320.89)"),
    1: (492.99, 502.54, "kept: 0.3 lead (speech 493.31), 0.3 tail (speech ends 502.22)"),
    2: (507.87, 518.02, "kept: clean both edges (508.16 / 517.30)"),
    3: (523.05, 534.5, "end534.16->534.5: word-tail margin after 'spaciousness' (silence 534.71)"),
    4: (538.19, 546.7, "kept: clean (538.92 / word ends ~546.6)"),
    5: (552.03, 561.5, "end561.04->561.5: word-tail margin after 'arises' (silence 561.89)"),
    6: (568.29, 576.55, "end576.34->576.55: margin after 'state' (silence 576.62)"),
    7: (586.29, 596.14, "kept: clean (586.63 / 595.73)"),
    8: (602.19, 612.25, "end611.62->612.25: MID-WORD fix, v1 cut inside 'spontaneously' (word starts 610.92, silence 612.33)"),
    9: (618.09, 628.93, "end628.84->628.93: margin after 'oneself' (silence 628.96)"),
    10: (636.45, 645.2, "end645.1->645.2: margin after 'consciousness' (silence 645.28)"),
    11: (652.11, 658.96, "end658.9->658.96: margin after 'waveless' (silence 658.99)"),
    12: (664.47, 672.46, "kept: clean (664.69 / 672.07)"),
    13: (678.99, 694.36, "kept: clean (679.19 / 693.96)"),
    "colo": (715.64, 761.85, "end761.56->761.85: keeps full 'viewpoints' (word ends ~761.7, silence 761.75)"),
}

SPACING = {"bowls_gap": 0.8, "intro_gap": 1.0, "bh_gap": 1.0, "hb_gap": 0.5, "colo_gap": 0.6}


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-2000:] + "\n")
        raise SystemExit(f"ffmpeg failed: {' '.join(cmd[:8])}")
    return r.stderr


def vol(path):
    err = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "volumedetect", "-f", "null", "-"])
    out = {}
    for k in ("mean_volume", "max_volume"):
        m = re.search(rf"{k}: (-?[\d.]+) dB", err)
        out[k] = float(m.group(1)) if m else None
    return out["mean_volume"], out["max_volume"]


def extract(src, s, e, dst):
    run(["ffmpeg", "-y", "-v", "error", "-ss", str(s), "-t", str(e - s), "-i", src,
         "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", dst])


def gain_for(path, target):
    mean, mx = vol(path)
    return min(target - mean, PEAK_CAP - mx)


def apply_gain(src, g, dst):
    if abs(g) < 0.05:
        if src != dst:
            subprocess.run(["cp", src, dst], check=True)
            if src.endswith("_raw.wav") and os.path.exists(src):
                os.remove(src)
        return
    run(["ffmpeg", "-y", "-v", "error", "-i", src, "-af", f"volume={g:.2f}dB",
         "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", dst])
    if src.endswith("_raw.wav") and os.path.exists(src) and os.path.abspath(src) != os.path.abspath(dst):
        os.remove(src)


def silence(dst, dur):
    run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
         "-t", f"{dur:.3f}", "-c:a", "pcm_s16le", dst])


def ensure_bell():
    src = os.path.join(PIECES, "bell1.wav")
    if os.path.exists(src):
        return src
    dst = os.path.join(PIECES, "bell_synth.wav")
    run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
         "-i", "aevalsrc=sin(2*PI*880*t)*exp(-1.5*t)*0.6:s=44100:d=2.5",
         "-ac", "2", "-c:a", "pcm_s16le", dst])
    return dst


def main():
    os.makedirs(PIECES, exist_ok=True)
    os.chdir(ROOT)
    b_src = {n: glob.glob(f"Vatulanatha_Sutra_{n} *.mp3")[0] for n in range(1, 14)}
    h_src = "supplements/wallis-vatulanatha.webm"
    bowls_src, bowls_meta = "sfx/bowls_intro.wav", (4.0, 13.75)
    longbell_src = "sfx/long_break_bell.wav"
    bell = ensure_bell()

    report = {"speech": {}, "gains": {}}
    for n in range(1, 14):
        s, e, _ = B_WINDOWS[n]
        raw = os.path.join(PIECES, f"b{n:02d}_raw.wav")
        extract(b_src[n], s, e, raw)
        g = gain_for(raw, SPEECH_TARGET)
        apply_gain(raw, g, os.path.join(PIECES, f"b{n:02d}.wav"))
        report["speech"][f"b{n:02d}"] = round(g, 2)
    for name in ["intro", "colo"] + list(range(1, 14)):
        s, e, _ = H_WINDOWS[name]
        key = name if isinstance(name, str) else f"h{name:02d}"
        raw = os.path.join(PIECES, f"{key}_raw.wav")
        extract(h_src, s, e, raw)
        g = gain_for(raw, SPEECH_TARGET)
        apply_gain(raw, g, os.path.join(PIECES, f"{key}.wav"))
        report["speech"][key] = round(g, 2)

    bowls_cut = os.path.join(PIECES, "bowls_cut.wav")
    extract(bowls_src, bowls_meta[0], bowls_meta[1], bowls_cut)
    g = gain_for(bowls_cut, SPEECH_TARGET - 5.0)
    apply_gain(bowls_cut, g, os.path.join(PIECES, "bowls.wav"))
    report["gains"]["bowls"] = round(g, 2)
    g = gain_for(longbell_src, SPEECH_TARGET - 6.0)
    apply_gain(longbell_src, g, os.path.join(PIECES, "long_break_bell.wav"))
    report["gains"]["long_break_bell"] = round(g, 2)

    order = []
    def add(p):
        order.append(p)
    add(os.path.join(PIECES, "bowls.wav"))
    for tag, d in [("gap_bowls", SPACING["bowls_gap"]), ("gap_intro", SPACING["intro_gap"]),
                   ("gap_colo", SPACING["colo_gap"])]:
        silence(os.path.join(PIECES, f"{tag}.wav"), d)
    add(os.path.join(PIECES, "gap_bowls.wav"))
    add(os.path.join(PIECES, "intro.wav"))
    add(os.path.join(PIECES, "gap_intro.wav"))
    for n in range(1, 14):
        add(bell)
        add(os.path.join(PIECES, f"b{n:02d}.wav"))
        add(os.path.join(PIECES, "gap_bh.wav") if not os.path.exists(os.path.join(PIECES, "gap_bh.wav")) else os.path.join(PIECES, "gap_bh.wav"))
        add(os.path.join(PIECES, f"h{n:02d}.wav"))
        add(os.path.join(PIECES, "gap_hb.wav"))
    add(os.path.join(PIECES, "long_break_bell.wav"))
    add(os.path.join(PIECES, "gap_colo.wav"))
    add(os.path.join(PIECES, "colo.wav"))

    silence(os.path.join(PIECES, "gap_bh.wav"), SPACING["bh_gap"])
    silence(os.path.join(PIECES, "gap_hb.wav"), SPACING["hb_gap"])

    lst = os.path.join(PIECES, "concat_v2.txt")
    with open(lst, "w") as f:
        for p in order:
            f.write(f"file '{p}'\n")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
         "-c:a", "libmp3lame", "-b:a", "192k", OUT_MP3])

    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=noprint_wrappers=1:nokey=1", OUT_MP3],
                         capture_output=True, text=True).stdout.strip()
    mean, mx = vol(OUT_MP3)
    timeline = []
    t = 0.0
    for p in order:
        d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                  "-of", "default=noprint_wrappers=1:nokey=1", p],
                                 capture_output=True, text=True).stdout.strip())
        timeline.append({"file": os.path.basename(p), "start": round(t, 3),
                         "end": round(t + d, 3), "dur": round(d, 3)})
        t += d
    manifest = {
        "product": "vatula_full_dual_reading",
        "version": 2,
        "grammar": "bowls -> [H intro] -> x13: [bell880 -> Baumer sutra-read -> bh_gap -> Hareesh translation -> hb_gap] -> long_break_bell -> H colophon",
        "spacing": SPACING,
        "speech_target_mean_db": SPEECH_TARGET,
        "peak_cap_db": PEAK_CAP,
        "b_windows_v2": {str(n): list(B_WINDOWS[n]) for n in B_WINDOWS},
        "h_windows_v2": {str(k): list(H_WINDOWS[k]) for k in H_WINDOWS},
        "b_windows_v1": json.load(open(os.path.join(WORK, "manifest.json")))["b_windows"],
        "sfx": {
            "bowls": {"source": "sfx/bowls_intro.wav", "span": list(bowls_meta), "role": "piece opener"},
            "bell_880": {"source": bell, "role": "x13 sutra marker"},
            "long_break_bell": {"source": longbell_src, "role": "before colophon"},
        },
        "piece_gains_db": report,
        "timeline": timeline,
        "duration_s": float(dur),
        "loudness": {"mean_db": f"{mean}", "max_db": f"{mx}"},
    }
    with open(os.path.join(WORK, "manifest_v2.json"), "w") as f:
        json.dump(manifest, f, indent=1)

    log = []
    for n in range(1, 14):
        old = json.load(open(os.path.join(WORK, "manifest.json")))["b_windows"][str(n)]
        s, e, why = B_WINDOWS[n]
        log.append(f"B{n:02d} [{old[0]},{old[1]}] -> [{s},{e}] ({e - s:.1f}s)  {why}")
    for key, (s, e, why) in H_WINDOWS.items():
        log.append(f"H {str(key):6s} -> [{s},{e}] ({e - s:.1f}s)  {why}")
    log.append(f"== DONE v2: {dur}s ({float(dur) / 60:.2f} min), mean {mean} dB, max {mx} dB ==")
    log.append(f"gains: {json.dumps(report)}")
    with open(os.path.join(WORK, "build_log_v2.txt"), "w") as f:
        f.write("\n".join(log) + "\n")
    print("\n".join(log))


if __name__ == "__main__":
    main()
