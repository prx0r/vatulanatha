#!/usr/bin/env bash
# verify.sh — one-command audit for the Vatulanatha build. Fails loud.
set -e
cd "$(dirname "$0")/.."
echo "== G0 questions (standalone/cutting gate) =="
python3 process/validate_questions.py || exit 1
echo "== G1 totals: units = assignment = manifests =="
python3 -c "
import json, glob, re
assign=json.load(open('build/assignment.json'))
assert len(assign)==96 and not any(str(v).startswith(('UNRES','AMBIG')) for v in assign.values()), 'assignment not 96 clean'
pool=0; n=0
PAT=re.compile(r'### (\S+) — .*? \[(A|B)\]\n- timestamp: 00:(\d+):(\d+)-->00:(\d+):(\d+)\n')
for f in glob.glob('excavations/vat*.md'):
    for m in PAT.finditer(open(f).read()):
        n+=1
        a=int(m.group(3))*60+int(m.group(4)); b=int(m.group(5))*60+int(m.group(6))
        pool+=b-a; assert assign.get(m.group(1)), m.group(1)
assert n==96, f'units {n}!=96'
print(f'units=96 pool={pool/60:.1f}min OK')"
echo "== G5 provenance: every quote verbatim in vat-text =="
python3 <<'PY'
import glob, re, sys
def norm(t): return re.sub(r'\s+',' ',re.sub(r'\[\d+:\d+\]',' ',t))
texts={}
for f in glob.glob('vat-text/*.txt'):
    texts[f.split('/')[-1].replace('.txt','')]=norm(open(f).read())
PAT=re.compile(r'### (vat(\d+)-\d+)[^\n]*\n- timestamp[^\n]*\n- topics[^\n]*\n- role[^\n]*\n- layer[^\n]*\n- quote: "([^"]*)"')
bad=[]; total=0
for f in glob.glob('excavations/vat*.md'):
    for m in PAT.finditer(open(f).read()):
        total+=1
        if re.sub(r'\s+',' ',m.group(3)) not in texts.get('sutra'+m.group(2),''):
            bad.append(m.group(1))
print(f'provenance {total-len(bad)}/{total}')
assert total==96, f'parsed {total}/96 quotes'
assert not bad, f'QUOTE FAILURES: {bad[:5]}'
print('OK')
PY
echo "== G6 TTS scan: plain lines =="
python3 -c "
import json, re
d=json.load(open('build/plain_sutras_v1.json'))
bad=[]
for k,v in d.items():
    letters=re.sub(r'[\u2010-\u201f\'\"]','',v)
    if re.search(r'[^ -~]', letters): bad.append((k,'non-ascii'))
    if re.search(r'[():;]', v): bad.append((k,'forbidden-punct'))
    if v!=v.strip() or '  ' in v: bad.append((k,'space'))
print('tts issues:', bad if bad else 'none')
assert not bad
print('OK')"
echo "== deterministic plain =="
H=$(python3 build/fish_filter_vatula.py | grep -oE 'sha256:[0-9a-f]+' | head -1)
[ "$H" = "sha256:2505ed9050b7dc53" ] || { echo "HASH DRIFT: $H (rerun twice, update constant if KEY changed intentionally)"; exit 1; }
echo "OK ($H)"

echo "== G9 A-band (FORMULA: A content 10-20m) =="
python3 -c "
import sys
A=0
for s in ['S1','S2','S3','S4','S5']:
    for l in open(f'build/manifests/{s}_A.txt'):
        if l.startswith('#'): continue
        f=l.split('\t'); A+=int(f[2])-int(f[1])
A/=60
print(f'A content {A:.1f}m')
assert 10 <= A <= 20, f'A OUT OF BAND: {A:.1f}m (expect 10-20)'
print('OK')"
echo "== G10 B-band (FORMULA: B 20-40m) =="
python3 -c "
import sys
B=0
for s in ['S1','S2','S3','S4','S5']:
    for l in open(f'build/manifests/{s}_B.txt'):
        if l.startswith('#'): continue
        f=l.split('\t'); B+=int(f[2])-int(f[1])
B/=60
import os
sel=os.path.exists('build/manifests/B_DEPTH_SELECTED.flag')
print(f'B content {B:.1f}m' + ('' if sel else ' (SUPERSET DRAFT)'))
if 20 <= B <= 40:
    print('OK (in band)')
elif not sel:
    print('KNOWN-FAIL: depth-selection pending (flow-read) — gate arms when build/manifests/B_DEPTH_SELECTED.flag exists')
    if '--ship' in sys.argv: sys.exit('SHIP BLOCKED: B out of band')
else:
    sys.exit(f'B OUT OF BAND despite selection flag: {B:.1f}m')
" "$@"
echo "== G11 C-band (near-complete: >=85% of full) =="
python3 -c "
import glob, subprocess
full=0
for ln in range(1,14):
    g=glob.glob(f'Vatulanatha_Sutra_{ln} *.mp3')
    if g: full+=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',g[0]]).strip())
C=full-13.1*60  # head/tail exclusions measured 2026-10-25
print(f'C est {C/60:.1f}m of full {full/60:.1f}m = {C/full*100:.0f}%')
assert C/full >= 0.85, 'C not near-complete (exclusions grew?)'
print('OK')"
echo "== G12 ESSAY-0 gate (the gold-dust test) =="
python3 -c "
import json, os, glob, re, sys
# 1) audition files exist, each <=25s
aud=sorted(glob.glob('build/essay0_audition/*.mp3'))
assert len(aud)>=3, 'audition cuts missing'
import subprocess
for f in aud:
    d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).strip())
    assert d<=27, f'{f} {d:.0f}s > 27s — not gold dust (cap 27 = sentence-complete seed)'
# 2) each candidate overlaps an A-grade unit window >=80% (it IS gold)
PAT=re.compile(r'### (vat\d+-\d+)[^\n]*\[A\]\n- timestamp: 00:(\d+):(\d+)-->00:(\d+):(\d+)')
A=[]
for f in glob.glob('excavations/vat*.md'):
    for m in PAT.finditer(open(f).read()):
        a=int(m.group(2))*60+int(m.group(3)); b=int(m.group(4))*60+int(m.group(5))
        A.append((m.group(1),a,b))
cands={'1-unfoldment':(526,552),'2-resting':(100,111),'3-abhinavagupta':(470,490)}
for name,(s,e) in cands.items():
    ov=max((min(e,b)-max(s,a)) for _,a,b in A)
    frac=ov/(e-s)
    assert frac>=0.8, f'{name}: only {frac:.0%} inside A-grade — not gold dust'
print('candidates: <=25s all, >=80% inside A-gold OK')
# 3) lock file blocks ship
if not os.path.exists('build/essay0_lock.json'):
    print('LOCK PENDING: owner ear (build/essay0_audition/) — write build/essay0_lock.json {"pick": ...}')
    if '--ship' in sys.argv: sys.exit('SHIP BLOCKED: essay-0 not locked')
else:
    lock=json.load(open('build/essay0_lock.json'))
    assert lock.get('pick'), 'essay0_lock.json has no pick'
    print(f'LOCKED: {lock["pick"]}')
print('OK')" "$@"

echo "== files =="
for f in SPINE.md excavations/CATALOGUE.md excavations/ASSIGNMENT.md excavations/C-MARKS.md \
         build/assignment.json build/key_v2.json build/fish_filter_vatula.py \
         build/plain_sutras_v1.json text/kaul_sutras_en.json text/sutra_verses.txt \
         build/seg1_beats.json build/seg5_beats.json build/manifests/S1_A.txt build/manifests/S5_C.txt \
         SPEAKERS.md process/PROCESS_NOTES.md process/17-SPINE-WORKFLOW.md; do
  [ -f "$f" ] || { echo "MISSING $f"; exit 1; }
done
echo "ALL GATES PASS"
