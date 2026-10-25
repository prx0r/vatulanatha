# ESSAY-0 FORMULA — how to pick the question and the response (locked 2026-10-10/25)

Follow in order. Every step is a TEST, not taste. Output = the pick string
`S? T? P? A?` → `build/essay0_lock.json` → G12.

## Step 1 — THE QUESTION (never invented)
- Must be the **measured corpus question**: highest keyword-density, present in
  every lecture (method: PROCESS_NOTES §5). For this text: "What is realisation?"
- Secondary questions come only from SPINE.md (sections already measured).
- Test: could a stranger hearing only the question know what is asked? (clarity law)

## Step 2 — THE SANSKRIT (the text's own compact answer)
Rank candidate phrases 0–2 each; pick top ≤3:
1. **Sūtra-level over gloss-level** (the text's own sentence > commentary phrase) —
   unless the gloss phrase IS the famous line.
2. **Completeness**: phrase must be able to stand as the object of the answer.
3. **Compact**: ≤ 10 words (memorability; card legibility).
4. **Paired**: an exact translation of it must EXIST in our files (Step 3 possible).
Row carries **phrase + source only. No meanings — ever** (9c rule).

## Step 3 — THE TRANSLATION (existing, exact, best available)
Pool = every existing exact rendering of the Step-2 phrases. Pick per phrase:
- **Priority: the lecturer's own translation > critical translation (Kaul) > gloss excerpt.**
  (She taught the text; her rendering is both exact and audible — that's T1.)
- Must complete "Realisation is ___" when read after the question (or pair with a
  Sanskrit whose answer it states).
- Never compose. Weak Kaul line → choose a better existing one, don't repair it.
- One natural S↔T match per column; cross-picks allowed but must not contradict.

## Step 4 — THE PLAIN (mechanical only)
- Output of fish_filter over the chosen translation — nothing else (07 ownership).
- Passes 07: ASCII letters, no forbidden punctuation, ≤ ~25 words.
- Identical to translation = honest no-op (allowed).

## Step 5 — THE AUDIO (gold dust, five tests)
- (a) grade A; (b) ≥80% window inside A-gold (G12); (c) ≤25s;
- (d) after the 2-breath pause, her core sentence **completes the question**
  (definitional sentence beats descriptive);
- (e) needs no term to make sense (07 Test 2) — quote verified (G5).

## Step 6 — THE STACK READ (contradiction check, 9c)
Read top to bottom: S → T → P → her voice. They must be **one thought in
increasing plainness**. Any meaning that exists only in our prose = strip.
Any mismatch between rows = fail, re-pick.

## Step 7 — LOCK
- Owner ear on `essay0_listen_all.mp3` (or per-candidate files).
- `build/essay0_lock.json` = {pick, sanskrit, translation, plain, window, audio}.
- verify.sh G12 → LOCKED; the pick becomes the S1-opener and the model for
  sections 2–5 (same 7 steps, questions from SPINE).

## Recurrence (video law)
The locked essay 0 is heard **4× in the finished video** (head, A, B, C) with
layer-bells at each re-entry — the formula must therefore survive re-hearing:
rhythm over cleverness, ≤25s, no term.
