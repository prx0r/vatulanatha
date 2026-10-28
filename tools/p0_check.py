#!/usr/bin/env python3
"""P0 structure check: does it work? One decode pass, no bells and whistles.

  p0_check.py [sheet.json]

Proofs: (1) audio == sheet blocks/order/durations  (2) every speech block edge
sits inside silence  (3) structure invariants: marker before B, pause between
speakers, timed pauses actually silent, switch air >= spec.
Exit 0 = PASS.
"""
import json
import os
import re
import subprocess
import sys

SHEET = sys.argv[1] if len(sys.argv) > 1 else "build/dual_reading/production_sheet.json"
sheet = json.load(open(SHEET))
base = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(SHEET)),
                                     sheet.get("base", ".")))
built = json.load(open(os.path.join(base, sheet.get("built", sheet["output"] + ".built.json"))))
mix = os.path.join(base, sheet["output"])
tl = built["timeline"]
flags = []

# pass 1: pauses + integrated loudness + true peak (content map)
err = subprocess.run(
    ["ffmpeg", "-hide_banner", "-nostats", "-i", mix,
     "-af", "silencedetect=noise=-38dB:d=0.1,ebur128=peak=true", "-f", "null", "-"],
    capture_output=True, text=True).stderr
S, st = [], None
for line in err.splitlines():
    m = re.search(r"silence_start: ([\d.]+)", line)
    if m:
        st = float(m.group(1))
    m = re.search(r"silence_end: ([\d.]+)", line)
    if m and st is not None:
        S.append((st, float(m.group(1))))
        st = None
# pass 2: source-aware quiet map (hissy archive floors count as quiet; real
# speech chops are >= -20 dB and fail this)
err2 = subprocess.run(
    ["ffmpeg", "-hide_banner", "-nostats", "-i", mix,
     "-af", "silencedetect=noise=-22dB:d=0.1", "-f", "null", "-"],
    capture_output=True, text=True).stderr
Q, st = [], None
for line in err2.splitlines():
    m = re.search(r"silence_start: ([\d.]+)", line)
    if m:
        st = float(m.group(1))
    m = re.search(r"silence_end: ([\d.]+)", line)
    if m and st is not None:
        Q.append((st, float(m.group(1))))
        st = None
I = re.findall(r"I:\s*(-?[\d.]+) LUFS", err)
TP = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", err)
audio_dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                  "format=duration", "-of",
                                  "default=noprint_wrappers=1:nokey=1", mix],
                                 capture_output=True, text=True).stdout.strip())

def sil_cover(a, b, min_frac=1.0):
    cov = sum(max(0.0, min(b, y) - max(a, x)) for x, y in S)
    return cov / max(b - a, 1e-6) >= min_frac

def sil_contains(t, before=0.0, after=0.0):
    return any(x <= t - before and y >= t + after for x, y in S)

def quiet_region(a, b, min_frac=0.9):
    cov = sum(max(0.0, min(b, y) - max(a, x)) for x, y in Q)
    return cov / max(b - a, 1e-6) >= min_frac

# (1) order & durations
spec = [b for b in sheet["blocks"] if b.get("render", True)]
if len(spec) != len(tl):
    flags.append(f"ORDER: {len(spec)} sheet blocks vs {len(tl)} in audio")
for i, (want, got) in enumerate(zip(spec, tl)):
    if want["id"] != got["id"] or want["kind"] != got["kind"]:
        flags.append(f"ORDER: pos {i} expected {want['id']}/{want['kind']} got {got['id']}/{got['kind']}")
        break
    if want["kind"] == "pause" and abs(want["dur"] - got["dur"]) > 0.03:
        flags.append(f"ORDER: pause {got['id']} dur {got['dur']} != spec {want['dur']}")
total = sum(r["dur"] for r in tl)
if abs(total - audio_dur) > 0.15:
    flags.append(f"ORDER: timeline {total:.2f}s vs audio {audio_dur:.2f}s")

# (2) speech edges quiet (source-aware map: catches chops, tolerates hiss floors)
for r in tl:
    if r["kind"] != "speech":
        continue
    if not quiet_region(r["start"] + 0.02, r["start"] + 0.14):
        flags.append(f"EDGE {r['id']}: head has content (chop start?)")
    if not quiet_region(r["end"] - 0.14, r["end"] - 0.02):
        flags.append(f"EDGE {r['id']}: tail has content (chop end?)")

# (3) invariants
mode = sheet.get("mode", "standard")
kinds = [(r["kind"], r.get("speaker"), r) for r in tl]
if mode == "essay0":
    # essay0 grammar: every speech block must follow a pause or marker
    for i, (k, sp, r) in enumerate(kinds):
        if k != "speech":
            continue
        prev = kinds[i - 1] if i else None
        if i == 0:
            continue  # first speech may follow sfx open
        if not prev or prev[0] not in ("pause", "marker"):
            flags.append(f"INV {r['id']}: speech not preceded by pause/marker (got {prev[0] if prev else 'none'})")
else:
    for i, (k, sp, r) in enumerate(kinds):
        if sp == "BAUMER":
            prev = kinds[i - 1] if i else None
            if not prev or prev[0] != "marker":
                flags.append(f"INV {r['id']}: Baumer block not preceded by marker")
        if sp == "HAREESH" and r["id"] != "intro" and r["id"] != "colo":
            prev = kinds[i - 1] if i else None
            if not prev or prev[0] != "pause":
                flags.append(f"INV {r['id']}: Hareesh block not preceded by pause (voice switch air missing)")
for r in tl:
    if r["kind"] == "pause":
        if not sil_cover(r["start"] + 0.03, r["end"] - 0.03, 0.85):
            flags.append(f"INV {r['id']}: timed pause not silent (content in pause)")
airs = []
for i in range(len(tl) - 1):
    a, b = tl[i], tl[i + 1]
    if a["kind"] == "speech" and b["kind"] == "pause" and tl[i + 2]["kind"] == "speech" \
            if i + 2 < len(tl) else False:
        pass
for i, r in enumerate(tl[:-2]):
    if r["kind"] == "speech" and tl[i + 1]["kind"] == "pause" and tl[i + 2]["kind"] == "speech":
        spec_d = tl[i + 1]["dur"]
        span = [s for s in S if s[0] <= r["end"] + 0.2 and s[1] >= tl[i + 2]["start"] - 0.2]
        if not span:
            flags.append(f"AIR {tl[i + 1]['id']}: no measurable air across switch")
            continue
        air = max(y - x for x, y in span)
        airs.append((tl[i + 1]["id"], round(air, 2), spec_d))
        if air < spec_d + 0.1:
            flags.append(f"AIR {tl[i + 1]['id']}: {air:.2f}s < spec {spec_d}s + pads")

if I and (float(I[-1]) < -30 or float(I[-1]) > -14):
    flags.append(f"LEVEL: integrated {I[-1]} LUFS out of range")
if TP and float(TP[-1]) > -1.0:
    flags.append(f"LEVEL: true peak {TP[-1]} dBTP > -1.0")

print(f"== P0 STRUCTURE: {sheet['product']} v{sheet.get('version')} ({sheet.get('mode')}) ==")
print(f"blocks {len(tl)} | audio {audio_dur:.2f}s | {I[-1] if I else '?'} LUFS | TP {TP[-1] if TP else '?'} dBTP | pauses {len(S)}")
if airs:
    xs = [a[1] for a in airs]
    print(f"switch airs n={len(xs)} min/med/max {min(xs):.2f}/{sorted(xs)[len(xs)//2]:.2f}/{max(xs):.2f}s (spec {[a[2] for a in airs][0]}+pads)")
for f in flags:
    print("  FLAG " + f)
print("== P0:", "FLAG" if flags else "PASS", "==")
sys.exit(1 if flags else 0)
