#!/usr/bin/env python3
"""Validate spine/essay questions — the Step-1 gate of ESSAY0-FORMULA.

Criteria (owner-law):
  1. interrogative form, ends with '?'
  2. NOT verbose: <= 9 words
  3. STANDALONE: contains >=1 explicit CONTENT noun (domain whitelist) — no
     vague place/existence questions that need context ("where do you end?")
  4. no unresolved pronouns / objectless verbs ("make it happen?" — what?);
     demonstratives (this/that/these/those/it) flagged as context-dependencies
Usage: python3 validate_questions.py            # checks the SPINE set
       python3 validate_questions.py "Q1?" "Q2?" ...   # check arbitrary questions
Exit 0 = all pass, 1 = failures (loud).
"""
import re, sys, pathlib

CONTENT = {  # explicit domain nouns — a question must name one
 'realisation','realization','realise','realized','self','senses','sense','experience',
 'silence','fruit','grace','void','nature','attainment','method','force','sound','word',
 'guru','sudden','upaya','realised','karma','worth','end-result','survives'  # survives->needs noun too
}
PRONOUNS = {'it','this','that','these','those','them','they','he','she','his','her'}
OBJLESS_HINT = re.compile(r'\b(happen|happens|do it|does it|make it|go|goes|end up|turn out)\b', re.I)

def words(q): return re.findall(r"[A-Za-z']+", q)

def check(q):
    fails = []
    ws = words(q); low = [w.lower().strip("'") for w in ws]
    if not q.strip().endswith('?'): fails.append("no '?'")
    if not low or low[0] not in {'what','why','how','where','which','who','when','is','are','was',
                                 'can','could','do','does','did','should','would','has','have','may'}:
        fails.append("not interrogative form")
    if len(ws) > 9: fails.append(f"verbose ({len(ws)} words > 9)")
    content = [w for w in low if w in CONTENT or w.rstrip('s') in CONTENT]
    if not content: fails.append("no explicit content noun (vague/context-dependent)")
    pron = [w for w in low if w in PRONOUNS]
    if pron: fails.append(f"unresolved pronoun(s): {','.join(sorted(set(pron)))}")
    if OBJLESS_HINT.search(q) and not content:
        fails.append("objectless verb (make what happen?)")
    return fails

def spine_from_md():
    p = pathlib.Path('SPINE.md')
    qs = re.findall(r'^## S\d+\. (.+?)\s*$', p.read_text(), re.M)
    return qs

if __name__ == '__main__':
    qs = sys.argv[1:] or spine_from_md()
    bad = 0
    for q in qs:
        f = check(q)
        mark = 'FAIL' if f else 'PASS'
        if f: bad += 1
        print(f"  {mark}  {q}" + ("" if not f else "   -> " + "; ".join(f)))
    print(f"{len(qs)-bad}/{len(qs)} pass")
    sys.exit(1 if bad else 0)
