# Manifests — Russian dolls per spine section (S5 collate)

TSV: `uid  start  end  grade  mp3` (seconds = mp3 timebase).
- `Sn_A.txt` gold only (sections at speed)
- `Sn_B.txt` A + depth (append-only superset, order-preserving — asserted)
- `Sn_C.txt` A+B listed + texture rule: full sources in HER order minus C-MARKS
Order inside all three = her sūtra order (fractal law). 96 units = Σ pool (asserted).

## KNOWN ISSUE (found by stats, 2026-10-25): B-OVERRUN
- A total = 17.8m ✓ (FORMULA A band 10–20m)
- B files currently = A + ALL B units = 86m ✗ (FORMULA B band 20–40m)
- Fix rule (FORMULA): "adjust windows, not quotes, to hit runtimes" —
  B rebuild at flow-read stage: keep A unchanged, SELECT depth clips (~+12–17m)
  per section with the G4 hold-up read (does the depth prime the A?); unselected
  B units drop to C texture. Current `Sn_B.txt` = **B-SUPERSET draft**, not ship list.
- C: full sources her-order minus C-MARKS ≈ pool (expected; C band = "rest").

## RUNTIME TABLE (measured 2026-10-25, enforced by verify.sh G9–G12)
| essay | content | rendered/bands | FORMULA band | gate |
|---|---|---|---|---|
| **A** | **17.6m** (28 clips) | 22.1m with beds (previews S1–S5) | 10–20m | G9 ✓ PASS |
| **B** | 85.9m superset-draft (96 clips) | — | 20–40m | G10 **KNOWN-FAIL** until depth-selection (flow-read) writes `B_DEPTH_SELECTED.flag` |
| **C** | ~104.1m est (full 117.2 − 13.1m head/tail excl.) = 89% | — | "rest", ≥85% | G11 ✓ PASS |
| **Essay 0** | 3 candidates, 15–20s each | — | ≤25s, ≥80% inside A-gold | G12 ✓ (lock pending owner ear → blocks --ship) |

Ratios vs analayo math: pool→A ÷6.7 (theirs ÷3.3 — our A is the tighter cut, correct
for the FORMULA essay bands; their constant measured a different artifact).

## Logged rules from the read-through (2026-10-25)
- **SEED-CAP:** `vat1-05` excluded from S1 section lists — plays only at LAYER
  HEADS (essay0). Stacking it right after essay0 = analayo's stacked-motto bug (G3).
- **PROMOTION:** `vat10-01` B→A (noted in excavation) — S4 had no opener stating
  its thesis; read-through found the hole.
- **FLAG for G8:** S2 opens on `vat2-02` (simultaneity) — weakest joint under
  "What is the self?"; her-order keeps it for now; if it jars → move to B.
