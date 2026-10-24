"""Generic rank-fit cut-plan generator. Usage: gen_plan_b.py <mp3> <keepfile.py> <outbase>
KEEPS=[(start,end,rank),...] native seconds; complement labeled via MAJOR (D_KINDS -> d_spans).
Writes <outbase>.cutplan.{json,md}. Band: kept <=2400 (analayo law).
"""
import json, sys, subprocess, importlib.util, os
mp3, keepf, outbase = sys.argv[1], sys.argv[2], sys.argv[3]
spec = importlib.util.spec_from_file_location("kf", keepf)
kf = importlib.util.module_from_spec(spec); spec.loader.exec_module(kf)
dur = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",mp3]).strip())
D_KINDS = {"hindi", "recitation", "sanskrit", "tibetan", "french"}
keeps = [tuple(k) for k in kf.KEEPS]
kept = sum(b-a for a,b,_ in keeps)
drops = []
while kept > 2400:
    cands = [k for k in keeps if k[2] > 1]
    if not cands: break
    k = max(cands, key=lambda x: (x[2], x[1]-x[0]))
    keeps.remove(k); kept -= k[1]-k[0]; drops.append(k)
assert kept <= 2400, f"cannot fit without cutting rank-1 (r1={kept})"
cuts, pos = [], 0.0
for a,b,_ in sorted(keeps):
    if a-pos > 0.3: cuts.append((pos,a))
    pos = max(pos,b)
if dur-pos > 0.3: cuts.append((pos,dur))
MAJOR = getattr(kf, "MAJOR", [])
def label(a,b):
    pts = {a,b}
    for m in MAJOR:
        if a < m[0] < b: pts.add(m[0])
        if a < m[1] < b: pts.add(m[1])
    out = []
    for x,y in zip(sorted(pts), sorted(pts)[1:]):
        best, ov = None, 0.0
        for m in MAJOR:
            o = max(0.0, min(y,m[1]) - max(x,m[0]))
            if o > ov: ov, best = o, m
        if best and ov >= 0.6*(y-x): k,r = best[2],best[3]
        elif y-x >= 8: k,r = "ranked-out","content ranked below the 20-40min budget"
        else: k,r = "trim","short span inside removed region"
        if out and out[-1][0]==k and out[-1][1]==r and abs(out[-1][3]-x)<0.01: out[-1][3]=y
        else: out.append([k,r,x,y])
    return out
GRADE = {1:"A",2:"B",3:"C",4:"C",5:"C"}
raw = []
for a,b in cuts:
    for k,r,x,y in label(a,b):
        raw.append({"start":round(x,2),"end":round(y,2),"kind":k,"reason":r})
d_spans = [c for c in raw if c["kind"] in D_KINDS]
e_cuts  = [c for c in raw if c["kind"] not in D_KINDS]
plan = {"source": os.path.basename(mp3), "target_min": 30, "source_min": round(dur/60,1),
        "kept_sec": round(kept,1), "kept_pct": round(kept/dur*100),
        "d_sec": round(sum(c["end"]-c["start"] for c in d_spans),1),
        "timebase": {"native": "mp3"},
        "dropped_spans": [{"start":round(a,1),"end":round(b,1),"rank":r} for a,b,r in drops],
        "cuts": e_cuts, "d_spans": d_spans,
        "keep_summary": getattr(kf, "SUMMARY", ""),
        "kept_segments": [{"start":round(a,1),"end":round(b,1),"grade":GRADE.get(r,"B")} for a,b,r in sorted(keeps)],
        "grade_counts": {}, "grade_minutes": {}}
gc = {g: sum(1 for x in plan["kept_segments"] if x["grade"]==g) for g in "ABC"}
gm = {g: round(sum(x["end"]-x["start"] for x in plan["kept_segments"] if x["grade"]==g)/60,1) for g in "ABC"}
gc["D"], gm["D"] = len(d_spans), round(plan["d_sec"]/60,1)
plan["grade_counts"], plan["grade_minutes"] = gc, gm
json.dump(plan, open(outbase+".cutplan.json","w"), indent=1)
def mm(s): return f"{int(s//60)}:{int(s%60):02d}"
md = [f"# {os.path.basename(outbase)} — cut plan\n",
      f"Source {plan['source_min']} min → **kept {kept/60:.1f} min ({plan['kept_pct']}%)** · {len(e_cuts)} cuts · band 20–40 ✓"]
if drops: md.append("_auto-dropped: " + "; ".join(f"{mm(a)}-{mm(b)}(r{r})" for a,b,r in drops) + "_\n")
md.append("\n## Kept (A/B/C)")
for c in plan["kept_segments"]: md.append(f"- {mm(c['start'])}–{mm(c['end'])}  [{c['grade']}]")
md.append("\n## Cuts")
for c in e_cuts: md.append(f"- {mm(c['start'])}–{mm(c['end'])}  [{c['kind']}]  {c['reason']}")
md.append("\n## D — non-English (translation candidates)")
for c in d_spans: md.append(f"- {mm(c['start'])}–{mm(c['end'])}  [{c['kind']}]  {c['reason']}  ({(c['end']-c['start'])/60:.1f} min)")
if plan["keep_summary"]: md.append(f"\n**Keeps:** {plan['keep_summary']}")
md.append(f"\nGrades: A={gc['A']}({gm['A']}m) B={gc['B']}({gm['B']}m) C={gc['C']}({gm['C']}m) D={gc['D']} spans ({gm['D']}m)")
open(outbase+".cutplan.md","w").write("\n".join(md)+"\n")
print(f"kept {kept/60:.1f}min ({plan['kept_pct']}%) cuts={len(e_cuts)} D={len(d_spans)} drops={len(drops)} ✓")
