# ESSAY C — REVIEW (cold read, 2026-10-25, report-only)

**Verdict: STANDALONE — YES structurally; two documentation breaks and
one inheritance break must be decided before render.**
C = the same walk + texture = her full lectures, her order, minus
exclusions. Listed unit walk = 95 clips (96 − seed vat1-05, seed-cap ✓),
83.2m listed + surrounding texture; G11 estimate 104.1m of 117.2m = 89% ✓.

Read against: `build/reviews/ESSAYC_SCRIPT.md`, `excavations/C-MARKS.md`
(full), FORMULA C-rules (lines 7, 26, 87).

## Issues

| # | sev | finding |
|---|-----|---------|
| C-1 | **HIGH** | **C does not contain all of B.** `vat4-07` ∈ `S2_B` but ∉ `S2_C` (it's in `S4_C` per assignment). FORMULA line 7: "C contains ALL of A and ALL of B" — false today for S2. Same root cause as B-1; fixing B-1 fixes this. Until decided, essay C silently drops a clip essay B plays, under a different section. |
| C-2 | **HIGH (doc)** | **C-MARKS header arithmetic is wrong.** Header claims "31.2 min C-marked" (and 85.9 + 31.2 ≈ 117.2), but the table's 33 windows sum to **26.5m** (head-C 10.0m + mid/tail-C 16.4m). ~4.7m marked time is either unlisted in the table or the header is stale. Nothing mechanical reads the header today, but it is the stated coverage ledger — one of the two numbers must go. |
| C-3 | MEDIUM | **Three different exclusion numbers coexist:** FORMULA:26 (precise: *minus namaskar/thank-you/head-silence*), G11 gate (`full − 13.1m`, "head/tail measured 2026-10-25" ≈ head-C 10.0m + thank-you tails ✓ consistent with FORMULA), and the CANON shorthand "*minus C-MARKS exclusions*" (ESSAY0-SPINE / 17 / FORMULA:87) which reads as **all** marks → C = 90.7m = 77% → **G11 would fail**. Gate is right per FORMULA:26; the CANON line overstates. Report: canon wording should say "minus the FORMULA exclusions (namaskar/thank-you/head-silence); other marks stay as texture". |
| C-4 | MEDIUM | **C's playback assembly has never been proven.** `Sn_C.txt` lists unit windows only; the actual texture rule (concat full sources per her order, cut head/tail exclusions, section-collated) has no exercised render path — G11 is an ffprobe estimate. Not a text defect; a build gap to close at render time. |
| C-5 | LOW | **C-MARKS header says "97 units"** — actual unit count is 96 everywhere else. Stale count in line 3. |
| C-6 | LOW | Texture beyond listed units keeps each source lecture whole except marked windows ✓; excluded heads (namaskar/recap) are genuinely boilerplate (spot-checked vat2/vat3/vat5/vat8/vat13 heads). |

## Seam spot-reads (C texture, transcript-level)

| spot | result |
|---|---|
| vat3 5:32→5:40 (after A-end, before vat3-05) | ✓ texture "And the point of the practice is awareness." stands alone; vat3-05 opens "In his handwritten note on the sutras…" standalone. |
| vat10 6:44→6:48 (after vat10-07) | ⚠ ASR repeat-loop in transcript at 6:48 ("but his divinized senses" ×5) — likely transcript artifact, but same window as flag A-7; one listen covers both. |
| vat1 14:00 (after vat1-08) | inconclusive (sparse transcript line "meditation") — no dangling markers found. |

## Per-section C walk sizes (honest texture shape)
S1 5u/2.7m · S2 34u/26.3m · S3 20u/16.1m · S4 29u/29.0m · S5 7u/9.1m.
S4's texture dominates (long uncut commentary fills — vat7-07 4:27,
vat13-07 3:26); S1 stays thin (only 2 lectures' units). By design.

---

# CROSS-ESSAY AUDIT (0 ⊂ A ⊂ B ⊂ C)

| check | result |
|---|---|
| A ⊆ B (per section) | ✓ all five |
| B ⊆ C (per section) | ✗ **S2 fails (vat4-07)** — see B-1/C-1 |
| duplicate clips across sections | ✓ none at any depth |
| C members match assignment.json | ✓ all 95 |
| question wording identical (SPINE / FORMULA / render tool / 101 beat cells) | ✓ all five, verbatim |
| G0 questions | ✓ 5/5 pass (verify.sh) |
| G9/G10/G11 bands | ✓ A 17.8m · B 34.6m · C 89% |
| consciousness-spine residue from the aborted remap | ✓ none in working tree |
| stale counts | ⚠ C-MARKS "97 units" (96 actual), header 31.2m (rows 26.5m) |

**Decision queue for the owner (report-only, nothing changed):**
1. `vat4-07` home: S2 (recommended — siblings + hold-up) or S4 (assignment today).
2. C-MARKS: fix header to row-sum (26.5m) or add the missing 4.7m rows.
3. Canon wording: scope "C-MARKS exclusions" to the FORMULA kinds.
4. S5 promotion candidate: vat12-06 (names the fruit) → A?
5. S3's off-question clip vat6-01: keep / move to head / demote (A-1).
6. S2 opener A-2 + vat5-05 fit A-3 (Essay A issues).
