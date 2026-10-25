#!/usr/bin/env bash
# verify.sh — one-command audit for the Vatulanatha build. Fails loud.
set -e
cd "$(dirname "$0")/.."
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
echo "== files =="
for f in SPINE.md excavations/CATALOGUE.md excavations/ASSIGNMENT.md excavations/C-MARKS.md \
         build/assignment.json build/key_v2.json build/fish_filter_vatula.py \
         build/plain_sutras_v1.json text/kaul_sutras_en.json text/sutra_verses.txt \
         build/seg1_beats.json build/seg5_beats.json build/manifests/S1_A.txt build/manifests/S5_C.txt \
         SPEAKERS.md process/PROCESS_NOTES.md process/17-SPINE-WORKFLOW.md; do
  [ -f "$f" ] || { echo "MISSING $f"; exit 1; }
done
echo "ALL GATES PASS"
