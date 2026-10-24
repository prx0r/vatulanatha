#!/usr/bin/env python3
"""Download all Bäumer audio + transcripts. Resumable; skip existing. Logs progress."""
import json, os, re, subprocess, sys, time
D = "/home/box/Downloads/yt/baumer"
YTDLP = "/home/box/ytsub-env/bin/yt-dlp"
PANEL = "/home/box/Downloads/yt/tantraloka-dyczkowski/tools/get_panel_subs.py"
LOG = f"{D}/download.log"
def log(m):
    print(m, flush=True)
    open(LOG, "a").write(m + "\n")
def slug(title):
    s = re.sub(r"[^\w\s\-\.()]", "", title, flags=re.U)
    s = re.sub(r"\s+", "_", s.strip())
    return s[:120]
rows = [l.rstrip("\n").split("\t", 2) for l in open(f"{D}/manifest.tsv") if l.strip()]
n_audio = n_sub = n_skip = n_err = 0
for i, (vid, dur, title) in enumerate(rows, 1):
    base = f"{D}/{slug(title)} [{vid}]"
    mp3 = base + ".mp3"
    if not (os.path.exists(mp3) and os.path.getsize(mp3) > 100000):
        r = subprocess.run([YTDLP, "-x", "--audio-format", "mp3", "--audio-quality", "5",
            "--extractor-args", "youtube:player_client=web_embedded", "--remote-components", "ejs:github",
            "--impersonate", "chrome", "--retries", "3", "--no-warnings",
            "-o", mp3, f"https://www.youtube.com/watch?v={vid}"],
            capture_output=True, text=True, timeout=900)
        if r.returncode != 0 or not (os.path.exists(mp3) and os.path.getsize(mp3) > 100000):
            # yt-dlp may append extension differently; check glob
            import glob
            g = glob.glob(base + "*")
            if not any(os.path.getsize(f) > 100000 and f.endswith(".mp3") for f in g):
                n_err += 1
                log(f"[{i}/{len(rows)}] AUDIO-FAIL {vid} {title[:50]} :: {(r.stderr or '').strip()[-200:]}")
                continue
        n_audio += 1
        log(f"[{i}/{len(rows)}] audio ok  {title[:60]}")
        time.sleep(2)
    else:
        n_skip += 1
    # transcript
    cues = base + ".cues.json"
    if not (os.path.exists(cues) and os.path.getsize(cues) > 100):
        for attempt in range(3):
            r = subprocess.run(["python3", PANEL, vid, base], capture_output=True, text=True, timeout=180)
            if os.path.exists(cues) and os.path.getsize(cues) > 100:
                n_sub += 1
                log(f"[{i}/{len(rows)}] subs ok   {title[:60]}")
                break
            time.sleep(20 * (attempt + 1))
        else:
            log(f"[{i}/{len(rows)}] SUBS-FAIL {vid} {title[:50]} :: {(r.stderr or r.stdout or '').strip()[-160:]}")
        time.sleep(5)
log(f"DONE audio={n_audio} subs={n_sub} skipped={n_skip} errors={n_err} total={len(rows)}")
