#!/usr/bin/env python3
"""Render a section from its manifest + beats (gospel order, audio beds).

Usage: render_vatula.py S1 [--dry-run] [--depth A|B]
Cell:  [PLAIN tts (silence-slot if not generated)] → [1.2s gap] → [Bäumer clip] → [2.5s water]
Opener: [QUESTION tts slot] → [2 breaths = 3.0s] → [TEXT is on-screen (silent)] ...
Settings (12/05): per-clip afade 0.15, full-mix loudnorm -16 LUFS, re-encode concat.
TTS files expected at build/tts/q_{sec}.mp3 and build/tts/{uid}.mp3 (owner credit-
confirm pending — missing files render as clean silence so dry-runs work today).
"""
import json, os, subprocess, sys, tempfile, shutil

sec = sys.argv[1] if len(sys.argv) > 1 else 'S1'
depth = 'A'
if '--depth' in sys.argv: depth = sys.argv[sys.argv.index('--depth') + 1]
dry = '--dry-run' in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
Q = {'S1':'What is realisation?','S2':'What is the self?','S3':'How does realisation happen?',
     'S4':'What does realisation do to experience?','S5':'What is the fruit of realisation?'}
BREATH, WATER, GAP = 1.5, 2.5, 1.2
def tts(path, dur=None):
    """return ffmpeg input spec: file if exists else anullsrc of given dur"""
    if os.path.exists(path): return path, None
    assert dur, f'need dur for silent slot {path}'
    return f'anullsrc=channel_layout=mono:sample_rate=44100', dur
def run(cmd):
    if dry: print('DRY:', ' '.join(cmd)); return
    subprocess.run(cmd, check=True)

# load
rows = [l for l in open(f'build/manifests/{sec}_{depth}.txt') if not l.startswith('#')]
clips = [dict(zip(['uid','start','end','grade','mp3'], l.rstrip('\n').split('\t'))) for l in rows]
beats = {b['audio'].get('uid'): b for b in json.load(open(f'build/seg{sec[1]}_beats.json')) if b['kind']=='unit'}
work = f'/tmp/opencode/render_{sec}_{depth}'; shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
files = []
def seg(inp, dur, out, extra=None, fade=True):
    cmd = ['ffmpeg','-y','-v','error']
    if isinstance(inp, str) and not inp.startswith('anullsrc'):
        cmd += ['-ss', extra[0], '-to', extra[1], '-i', inp]
        af = 'aresample=44100'
        if fade: af += ',afade=t=in:d=0.15,afade=t=out:d=0.15'
        cmd += ['-af', af, '-ac', '1', '-ar', '44100', '-b:a', '96k', out]
    else:
        cmd += ['-f','lavfi','-i',inp if inp.startswith('anullsrc') else 'anullsrc',
                '-t', str(dur), '-ac','1','-ar','44100','-b:a','96k', out]
    run(cmd); files.append(out)
# opener: question slot + pause
qp, qd = tts(f'build/tts/q_{sec}.mp3', dur=len(Q[sec].split())*0.45+0.5)
seg(qp, qd, f'{work}/00_question.mp3', fade=False)
seg('anullsrc', 3.0, f'{work}/01_pause.mp3', fade=False)   # 2 breaths recall window
# clips with plain slots
for i, c in enumerate(clips):
    b = beats.get(c['uid'], {})
    p, pd = tts(f"build/tts/{c['uid']}.mp3", dur=len(b.get('plain',{}).get('tts_line',''))*0.06+0.4)
    seg(p, pd, f'{work}/1{i:02d}_plain.mp3', fade=False)
    seg(c['mp3'], None, f'{work}/2{i:02d}_clip.mp3', extra=(c['start'], c['end']))
    seg('anullsrc', WATER, f'{work}/3{i:02d}_water.mp3', fade=False)
lst = f'{work}/list.txt'
if not dry:
    open(lst, 'w').write(''.join(f"file '{f}'\n" for f in files))
    out = f'build/preview/{sec}_{depth}.mp3'
    os.makedirs('build/preview', exist_ok=True)
    run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst,
         '-af','loudnorm=I=-16:TP=-1.5:LRA=11','-ar','44100','-b:a','96k', out])
    d = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0', out],
                       capture_output=True, text=True).stdout.strip()
    print(f'{out}: {len(clips)} clips, {float(d)/60:.1f} min')
else:
    print(f'{sec}/{depth}: {len(clips)} clips planned, {len(files)} segments (dry-run)')
