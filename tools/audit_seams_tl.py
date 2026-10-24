"""Audit seam safety: print transcript context at every keep boundary.
Usage: python3 audit_seams_tl.py <part>
"""
import json, re, sys, os
part = str(int(sys.argv[1]))
D = "/home/box/Downloads/yt/tantraloka-dyczkowski"
plan = json.load(open(f"{D}/part{part}.cutplan.json"))
tf = f"{D}/transcripts/part{part}.txt"
segs = []
for line in open(tf, errors="replace"):
    m = re.search(r"(\d+(?:\.\d+)?)-\s*(\d+(?:\.\d+)?)\s+(.+)", line)
    if m:
        segs.append((float(m.group(1)), float(m.group(2)), m.group(3).strip()))
segs.sort()
def mm(s):
    return f"{int(s//60)}:{s%60:04.1f}"
for k in plan["kept_segments"]:
    a, b = k["start"], k["end"]
    prev = [s for s in segs if s[1] <= a + 0.15][-2:]
    nxt = [s for s in segs if s[0] >= b - 0.15][:2]
    print(f"\n== KEEP {mm(a)}-{mm(b)} [{k['grade']}] ==")
    for s in prev:
        print(f"  PRE  {mm(s[0])}-{mm(s[1])}  {s[2][:110]}")
    for s in nxt:
        print(f"  POST {mm(s[0])}-{mm(s[1])}  {s[2][:110]}")
