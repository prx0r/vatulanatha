#!/usr/bin/env python3
"""Generate a storyboard markdown from a dual-reading manifest (v2).

One row per block: time, block, speaker, event, notes. The listen companion:
read down it while hearing it — every switch and pause is on the page.
"""
import json
import os
import subprocess
import sys

EVENTS = {
    "bowls": ("OPEN", "—", "intro bell: bowls strike + decay"),
    "gap_bowls": ("pause", "—", "settle before first voice"),
    "intro": ("SPEECH", "HAREESH", "the text's own introduction read"),
    "gap_intro": ("pause", "—", "breathe before the sūtra sequence"),
    "long_break_bell": ("LONG BREAK", "—", "section-scale bell before the colophon"),
    "gap_colo": ("pause", "—", "land before colophon"),
    "colo": ("SPEECH", "HAREESH", "colophon / attribution read"),
}


def main():
    manifest_path = sys.argv[1] if len(sys.argv) > 1 else "build/dual_reading/manifest_v2.json"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "build/dual_reading/storyboard_v2.md"
    man = json.load(open(manifest_path))
    tl = man["timeline"]
    sp = man.get("spacing", {})
    v1 = man.get("b_windows_v1", {})

    def mmss(t):
        return f"{int(t // 60)}:{t % 60:04.1f}"

    rows = []
    i = 0
    sutra = 0
    while i < len(tl):
        cur = tl[i]
        name = cur["file"].replace(".wav", "")
        if name.startswith("bell"):
            sutra += 1
            rows.append((cur, f"SŪTRA {sutra} MARKER", "—", "bell", "announces the sūtra; Bäumer speaks after"))
            i += 1
        elif name.startswith("b0") or name.startswith("b1"):
            note = v1.get(str(sutra), ["", "", ""])[2] if isinstance(v1.get(str(sutra)), list) else ""
            rows.append((cur, f"B sūtra {sutra} read", "BAUMER", "SPEECH", note))
            i += 1
            if i < len(tl) and tl[i]["file"].startswith("gap_bh"):
                g = tl[i]
                rows.append((g, "voice switch", "—", "PAUSE",
                             f"{g['dur']:.1f}s gap + piece pads ≈ {g['dur'] + 0.8:.1f}s air — speaker changes need the most"))
                i += 1
        elif name.startswith("h0") or name.startswith("h1"):
            rows.append((cur, f"H translation {sutra}", "HAREESH", "SPEECH", f"his render of sūtra {sutra}"))
            i += 1
            if i < len(tl) and tl[i]["file"].startswith("gap_hb"):
                g = tl[i]
                rows.append((g, "phrase land", "—", "PAUSE",
                             f"{g['dur']:.1f}s + pads — let the translation land before the next bell"))
                i += 1
        else:
            ev, speaker, note = EVENTS.get(name, ("block", "—", ""))
            rows.append((cur, name, speaker, ev, note))
            i += 1

    lines = [
        f"# STORYBOARD — {man.get('product', '?')} v{man.get('version', '?')} "
        f"({man.get('duration_s', 0) / 60:.2f} min)",
        "",
        "Read while listening. Grammar: "
        + man.get("grammar", ""),
        "",
        "Spacing: " + json.dumps(sp),
        "",
        "| time | block | speaker | event | notes |",
        "|---|---|---|---|---|",
    ]
    for cur, label, speaker, event, note in rows:
        lines.append(f"| {mmss(cur['start'])}–{mmss(cur['end'])} | {label} | {speaker} | {event} | {note} |")
    lines += [
        "",
        "Per-junction checklist: topic switch? speaker switch? does it need a pause?",
        "Speaker switches take the biggest air (≈2s), phrase-lands ≈1s, "
        "section breaks get the long bell.",
    ]
    with open(out_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"wrote {out_path} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
