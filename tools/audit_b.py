"""Seam audit. Usage: audit_b.py <cutplan.json> <transcript.txt>"""
import json, re, sys
plan = json.load(open(sys.argv[1]))
segs = []
for line in open(sys.argv[2], errors="replace"):
    m = re.search(r"(\d+(?:\.\d+)?)-\s*(\d+(?:\.\d+)?)\s+(.+)", line)
    if m: segs.append((float(m.group(1)), float(m.group(2)), m.group(3).strip()))
segs.sort()
def mm(s): return f"{int(s//60)}:{s%60:04.1f}"
for k in plan["kept_segments"]:
    a,b = k["start"], k["end"]
    prev = [s for s in segs if s[1] <= a+0.15][-2:]
    nxt = [s for s in segs if s[0] >= b-0.15][:2]
    print(f"\n== KEEP {mm(a)}-{mm(b)} [{k['grade']}] ==")
    for s in prev: print(f"  PRE  {mm(s[0])}-{mm(s[1])}  {s[2][:110]}")
    for s in nxt:  print(f"  POST {mm(s[0])}-{mm(s[1])}  {s[2][:110]}")
