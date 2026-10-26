# DONE — definition of done + findings rulings (2026-10-26)

## RULING: `vatula_full_dual_reading` v3 = **DONE (by rule)**

Evidence on the final artifact (622.58s, sheet==master):

| gate | result |
|---|---|
| `p0_check.py` | **PASS** — order/edges/invariants, switch airs 1.83–2.06s, −18.0 LUFS, −1.7 dBTP |
| whole-mix machine pass #2 | 5 findings, all non-blocking classes |
| whole-mix machine pass #3 (final) | verdict FLOWS, 4 findings, all adjudicated below → **2 consecutive passes, 0 blocking = convergence** |
| verbatim spot-transcriptions | intro prose clean — both "repetition" claims **refuted** |

## Definition of Done (standard-compilation pattern — closes future products)

A product is DONE when **all four** hold:
1. `p0_check` PASS (order==sheet, quiet edges, invariants, airs, levels);
2. two consecutive whole-mix flow passes with **zero blocking findings after adjudication** (pinned prompt + model + effort);
3. every raw finding is classed and ruled in a ledger (below);
4. timings inside the signed policy (airs/pauses/loudness targets).

**The raw model verdict is never the gate.** Fixture run (both directions):
- v1 (seeded-defect file) → 3 × "jarring cut" findings *and still said FLOWS*;
- v3 → findings that mostly dissolve under cross-check.
→ The token alone is unreliable in BOTH directions; **adjudication is the
gate**: mechanical claims → p0_check/silence maps; text claims → verbatim
transcription (verbatim wins); then count blocking findings.
Next product of this pattern auto-closes on gates 1+2 unless a **novel**
finding class appears (new class → ledger row → rule).

## Findings ledger (v3 and carried rulings)

| finding | class | ruling |
|---|---|---|
| 2:13 mid-sentence chop (v1, caught by owner) | mechanical | fixed in v2+; now a P0 edge check; **fixture: v1 must keep flagging** |
| switch room-color differences (archive↔studio) | flow/inherent | **accepted** — two real sources; owner informed; wood-tick softening = deferred policy (owner) |
| "sa…" (b05) / "the unbr-" (intro) word-cut claims | transcript-level | **out of scope per owner** — transcript guaranteed by construction |
| "repetition of taught / is" | unstable | **refuted by verbatim transcription** — discard rule: verbatim wins |
| "slightly abrupt" analysis→quote arrivals ×4 + colophon | taste | **accepted by design** — bell-marked section arrivals; severity "slightly"; non-blocking class |
| dead air after long-break bell | taste | partly fixed (land 0.6→0.3); remainder = the long break the owner requested |

## Taxonomy (blocking rules)

mechanical → **block** · structural → **block** · flow-with-evidence →
adjudicate (maps/cross-checks) · taste → policy row (once, never re-litigated)
· transcript-level → discard (owner rule) · unstable → discard when refuted
by verbatim.

## Ear-regression fixtures (run on any model/prompt/engine change)

- `vatula_full_dual_reading_v1.mp3` (kept) — must produce **cut-class findings**
  (raw run 2026-10-26: ✓ 3 × "jarring cut"; note verdict token said FLOWS →
  findings, not token, are the signal);
- `vatula_full_dual_reading.mp3` (v3) — must PASS p0 + zero blocking after
  adjudication.
