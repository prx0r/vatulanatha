"""Interleaved render: A/B/C keeps + D blocks (original non-English audio -> English TTS after)."""
import json, os, subprocess, sys
part = sys.argv[1]
D = "/home/box/Downloads/yt/tantraloka-dyczkowski"
TD = "/tmp/opencode/tl_d"
src = f"{D}/tantraloka-bhu-{part}.mp3"
plan = json.load(open(f"{D}/part{part}.cutplan.json"))
# D span index -> TTS files (in order, concatenated after the original audio)
D_TTS = {
  "1": [["tts_p1cap1.mp3"], ["tts_p1cap2.mp3"], ["tts_p1cap3.mp3"], ["tts_p1cap4.mp3"]],
  "2": [["tts_q2.mp3"], ["tts_q3a.mp3","tts_q3b.mp3"], ["tts_q4.mp3"]],
}
items = []
for s in plan["kept_segments"]:
    items.append((s["start"], s["end"], "keep", None))
for i, c in enumerate(plan["d_spans"]):
    items.append((c["start"], c["end"], "d", i))
items.sort(key=lambda x: x[0])
work = f"/tmp/opencode/asm_p{part}"; os.makedirs(work, exist_ok=True)
def enc(inp, out, extra_in=None, ss=None, to=None):
    cmd = ["ffmpeg","-y","-v","error"]
    if ss is not None: cmd += ["-ss", str(ss)]
    cmd += ["-i", inp]
    if to is not None: cmd += ["-t", str(to)]
    cmd += ["-vn","-ac","1","-ar","44100","-c:a","libmp3lame","-b:a","96k", out]
    subprocess.run(cmd, check=True)
files = []
n = 0
for start, end, kind, di in items:
    if kind == "keep":
        f = f"{work}/p{n:03d}.mp3"; enc(src, f, ss=start, to=end-start); files.append(f); n += 1
    else:
        # original non-English audio
        orig = subprocess.run(["bash","-c", f"ls {TD}/p{part}d{di+1}_*.wav 2>/dev/null | head -1"],
                              capture_output=True, text=True).stdout.strip()
        if orig:
            f = f"{work}/p{n:03d}.mp3"; enc(orig, f); files.append(f); n += 1
        for t in D_TTS[str(part)][di]:
            f = f"{work}/p{n:03d}.mp3"; enc(f"{TD}/{t}", f); files.append(f); n += 1
lst = f"{work}/list.txt"
open(lst,"w").write("".join(f"file '{f}'\n" for f in files))
out = f"{D}/tantraloka-bhu-{part}-cut-full-D.mp3"
subprocess.run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",lst,"-c","copy",out], check=True)
d = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out],
                   capture_output=True, text=True).stdout.strip()
print(f"part{part}: {len(files)} pieces -> {out} ({float(d)/60:.1f} min)")
