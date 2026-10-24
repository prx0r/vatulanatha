"""Render cutplan: concat kept_segments (A/B/C dial, default A+B=all) from source mp3."""
import json, os, subprocess, sys
part = sys.argv[1]
dial = sys.argv[2] if len(sys.argv) > 2 else "full"   # A | AB | full
D = "/home/box/Downloads/yt/tantraloka-dyczkowski"
src = f"{D}/tantraloka-bhu-{part}.mp3"
plan = json.load(open(f"{D}/part{part}.cutplan.json"))
keep = {"A": {"A"}, "AB": {"A","B"}, "full": {"A","B","C"}}[dial]
segs = [s for s in plan["kept_segments"] if s["grade"] in keep]
work = f"/tmp/opencode/render_p{part}"; os.makedirs(work, exist_ok=True)
files = []
for i, s in enumerate(segs):
    f = f"{work}/seg{i:03d}.mp3"
    subprocess.run(["ffmpeg","-y","-v","error","-ss",str(s["start"]),"-to",str(s["end"]),
                    "-i",src,"-c","copy",f], check=True)
    files.append(f)
lst = f"{work}/list.txt"
open(lst,"w").write("".join(f"file '{f}'\n" for f in files))
out = f"{D}/tantraloka-bhu-{part}-cut-{dial}.mp3"
subprocess.run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",lst,"-c","copy",out], check=True)
d = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out],
                   capture_output=True, text=True).stdout.strip()
print(f"part{part} [{dial}]: {len(segs)} segs -> {out} ({float(d)/60:.1f} min)")
