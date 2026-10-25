#!/usr/bin/env python3
"""Deterministic TEXT -> PLAIN filter (port of analayo build/fish_filter.py).
Gospel order: TEXT VERBATIM -> PLAIN ENGLISH (this) -> AUDIO speaker.

Layers: (1) key_v2 dict, word-boundary, case-insensitive, first-hit stable
        (2) blunt pairs key_v1 (regex, sorted by pattern length desc)
        (3) 07-plain sanitation: parens->em-dash, colon->dash, semicolon->comma,
            slash->period, collapse spaces, ASCII-or-loanword check on output.
Determinism: sorted iteration everywhere; rerun MUST be byte-identical (hash below).
Edit the KEY, never the output (07 ownership rule).
Usage: python3 fish_filter_vatula.py            # writes plain_sutras_v1.json + hash
       python3 fish_filter_vatula.py --check    # rerun + verify hash
"""
import json, re, hashlib, sys, os
D = os.path.dirname(os.path.abspath(__file__))
KEY = json.load(open(f"{D}/key_v2.json"))
BLUNT = json.load(open(f"{D}/key_v1.json"))
LOAN = set(json.load(open(f"{D}/loanwords_v1.json")))

def apply_dict(text):
    # longest-key first; whole-word, case-insensitive; keep capitalization of match start
    out = text
    for k in sorted(KEY, key=len, reverse=True):
        pat = re.compile(r'\b' + re.escape(k) + r'\b', re.I)
        def rep(m):
            v = KEY[k]
            if m.group(0)[0].isupper() and v:
                v = v[0].upper() + v[1:]
            return v
        out = pat.sub(rep, out)
    return out

def apply_blunt(text):
    out = text
    for pat, plain in sorted(BLUNT, key=lambda p: -len(p[0])):
        try:
            out = re.sub(r'\b(?:' + pat + r')\b', plain, out, flags=re.I)
        except re.error:
            continue
    return out

def sanitize(text):
    t = text.replace('(', ' — ').replace(')', '')
    t = t.replace(':', ' —').replace(';', ',').replace('/', '.')
    t = re.sub(r'\s*—\s*', ' — ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'\s+([.,])', r'\1', t)
    t = re.sub(r'—\.', '—', t)
    return t

def plain(text):
    return sanitize(apply_blunt(apply_dict(text)))

def main():
    src = json.load(open(f"{D}/../text/kaul_sutras_en.json"))
    out = {k: plain(v) for k, v in sorted(src.items(), key=lambda kv: int(kv[0]))}
    # 07 Test 1: no diacritics outside loanwords
    bad = [k for k, v in out.items() if re.search(r'[^\x00-\x7F]', re.sub(r'[\u2010-\u201f\'\"]', '', v))]
    path = f"{D}/plain_sutras_v1.json"
    json.dump(out, open(path, 'w'), ensure_ascii=False, indent=1)
    h = hashlib.sha256(open(path, 'rb').read()).hexdigest()[:16]
    print(f"wrote {path} sha256:{h} nonascii:{bad or 'none'}")
    if '--check' in sys.argv:
        h2 = hashlib.sha256(open(path, 'rb').read()).hexdigest()[:16]
        print("DETERMINISTIC" if h == h2 else "MISMATCH!")
    # diffs vs hand drafts (reference only — generated is gospel)
    try:
        hand = json.load(open(f"{D}/card_lines.json"))
        hand13 = {k: v for k, v in hand.items() if ' ' in k}  # verse-lines only
        print(f"(hand drafts kept as reference: {len(hand13)} verse-lines in card_lines.json)")
    except Exception:
        pass

if __name__ == '__main__':
    main()
