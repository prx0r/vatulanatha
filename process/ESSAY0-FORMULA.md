# ESSAY-0 FORMULA — how to pick the question and the response (locked 2026-10-10/25)

Follow in order. Every step is a TEST, not taste. Output = the pick string
`S? T? P? A?` → `build/essay0_lock.json` → G12.

## Step 1 — THE QUESTION (never invented) — four criteria, all mandatory
1. **Standalone**: stranger hears it cold and knows exactly what is asked
   (clarity law — no coinages, no shorthand, no cross-references).
2. **Cutting**: the most incisive, insight-loaded form the content supports —
   it should cut through an assumption (a sharp question presupposes the text's
   own answer), not just name a topic. "Clear" without "sharp" = fail.
3. **Content-grounded**: the corpus must actually answer it (measured density,
   present in every lecture for the master — PROCESS_NOTES §5 method).
4. **Topic-anchored (the senses-rule)**: every question varies on S1's topic —
   the realisation-domain (realisation / self). Sharpening that DROPS the anchor
   to go generic = fail (owner-rejected: "What happens to the senses?" — worse;
   it stops being about realisation). The sharpen must keep the anchor AND gain
   the explicit object.
5. **Enquiry-chaining**: together with the other section questions it forms ONE
   logical enquiry — each question follows from the answer-space of the previous,
   and essay-0's response must OPEN the enquiry (invites depth), not close it.
   Recurrence test: after essay 0, the listener should still lean in ("…and
   then what / how / why") — that pull carries A→B→C.
- Master stays **"What is realisation?"** (owner: clear, not verbose — perfect).
- Sharpening rule (owner, from the audit): sharpened questions must keep the
  EXPLICIT OBJECT — "Why can't you force **realisation**?" ✓, not "make it
  happen?" (pronoun, objectless) and never place-vague ("where do you end?").
- **GATE: `process/validate_questions.py` runs as verify.sh G0** — interrogative,
  ≤9 words, explicit content noun, no unresolved pronouns. Fails loud; SPINE set
  currently 5/5 PASS.

## Step 1b — enquiry-open test (on the whole essay-0 stack)
Read the locked stack aloud: does it close the question dead, or open it?
Required: the response is complete enough to satisfy, sharp enough to raise the
next lean-in (the four recurrences then feel earned, not repetitive).

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

**Tier order (confirmed): SANSKRIT + TRANSLATION (screen interlinear) → PLAIN (spoken) → BÄUMER.**

## Step 4 — THE PLAIN (mechanical only)
- Output of fish_filter over **the chosen translation T** — regenerated at pick time,
  never a pre-baked line from a different source (9c-4). Nothing else (07 ownership).
- Passes 07: ASCII letters, no forbidden punctuation, ≤ ~25 words.
- Identical to translation = honest no-op (allowed).

## Step 5 — THE AUDIO (gold dust, five tests)
- (a) grade A; (b) ≥80% window inside A-gold (G12); (c) ≤25s;
- (d) after the 2-breath pause, her core sentence **completes the question**
  (definitional sentence beats descriptive);
- (e) needs no term to make sense (07 Test 2) — quote verified (G5).

## Step 5b — THE FLOW TEST (owner, the deciding criterion)
The response must be the **SEED of 0→A→B→C**: read the five section questions as
the elaboration of this one response — does each section open a facet of IT?
(A = sides of the seed, B = its mechanics, C = the seed heard inside the source.)
A response that is merely true but doesn't seed the walk loses to one that does.
The deeper reason (FORMULA.md THE UNFOLDING): the essay PERFORMS its doctrine —
realisation unfolds rather than accumulates, so the explanation must unfold the
same single sentence outward, never swap in new ideas per layer.
2026-10-25 result: the original (unfoldment-definition) passes; thematic
one-offers (all-at-once / unnameable / awakening) kept as alternates only.

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

## AUDIT — cutting-test on the locked set (2026-10-25) + sharpened candidates
| # | current (standalone ✓) | cutting verdict | sharpened candidate (content-grounded) |
|---|---|---|---|
| 1 | What is realisation? | clear, not cutting — names a topic | **"What is realised, if nothing is attained?"** (vat1-05: attainment ≠ getting; vat8/11: nothing by method) |
| 2 | What is the self? | basic — under-asks | **"Where do you end?"** (vat4-03 co-presence; vat5 union — the section literally dissolves the boundary) |
| 3 | How does realisation happen? | neutral how-to | **"Why can't you make it happen?"** (vat11-02 beyond-upāya, vat8-01 not-by-will, vat3-01 the glance) |
| 4 | What does realisation do to experience? | wordy | **"What happens to the senses?"** (vat10-07 radiance, vat11 five-modes) |
| 5 | What is the fruit of realisation? | serviceable | **"What survives realisation?"** (vat12-02 not-reborn, vat13-01 silence, vat13-06 already-feeling) |

Sharpened set chains as one enquiry: if nothing is attained → where do you end →
why can't you make it → what happens to the senses → what survives.
Essay-0 under #1's sharpened form: the response ITSELF (her unfoldment/resting
clip) answers "if nothing is attained" — opening the how/where/why that follow.
**Owner picks: current set, sharpened set, or mix per row.**
