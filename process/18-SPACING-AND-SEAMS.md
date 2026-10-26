# 18 — SPACING & SEAMS (craft rules, from the 2026-10-26 dual-reading build)

The difference between "assembled" and "listenable": where cuts land, how
much air sits between blocks, whether every switch is felt as intentional.
Storyboards it, builds it, checks it — same rules every product.

## 1. Seam discipline (where a cut may land)

- **Transcript cue times are not speech.** CF cues / srt line starts lag or
  lead real speech by up to ~1s. Never cut on a cue boundary.
- **Cut on silence.** `silencedetect` on the SOURCE: start `noise=-26dB
  d=0.15`, lower toward −32 for clean studio files, raise to −22 for hissy
  archive ones. The right edge is inside a silence gap, ≥0.15s clear of
  either word.
- **Sentences complete, both sides.** Two failure modes, both caught this
  session: *hot tail* (end lands mid-word — the 2:13 chop) and *orphan
  head* (start lands on the tail of the previous sentence — you hear
  "…nature swarūpa" with its subject missing). Every window edge gets a
  written reason in the manifest.
- Captioned sources (YouTube VTT): word-level `<c>` tags give exact word
  times — trust them over cue spans; cut at word-end +0.1–0.3s into the
  following silence.
- A seam where the sentence *finishes* is free air. A seam where it
  *stops* is a defect, no matter how short the gap.

## 2. Spacing (the pause grammar)

Hierarchy — bigger change gets more air:

| junction | air (incl. piece pads) | mechanism |
|---|---|---|
| speaker switch (B↔H) | ≈1.8–2.1s | 1.0s gap + pads cut into silence |
| phrase land (translation → next marker) | ≈0.9–1.2s | 0.5s gap + pads |
| section break | long bell (4.7s) + 0.6s | `long_break_bell` |
| piece open | bowls 9.8s + 0.8s | `bowls_intro` |
| into first voice | 1.0s | gap |

Rules of thumb: **a pause after a switch > a pause after a stop; never 0s
between speech and a marker; never >2s of dead air without a mark.**
Digital gaps are fine but pieces should carry their own room-tone pads
(cuts inside source silence do this for free).

## 3. Storyboard (before the ear listens)

`tools/storyboard.py manifest_v2.json` → markdown table: time · block ·
speaker · event · notes. One row per block, one row per pause. Per-junction
checklist: **topic switch? speaker switch? does it need a pause?**
Read it while auditioning — if the page and the ear disagree, the page is
wrong first, then the audio.

## 4. Levels

- Speech pieces → one target: **mean −21 dB**, gain = `min(target − mean,
  −1.5 − max)` (peak-safe, no pumping; piece spread collapses ±4.4 → 0).
- SFX roles + their gains live in `sfx/README.md` (kit = the signature).
- Final: mean lands ~−22, peak ≤ −1.5.

## 5. QA (simple, on purpose)

```
python3 skills/skill-tempo-check/engine.py <mix> --manifest <manifest> --pieces <pieces>
```
One PASS/FLAG on spacing & structure: clipping, density, hot speech edges,
pause <0.3s between speech pieces. If it PASSes, the ear judges taste —
not mechanics. (Rhythm science out of scope; this checks "decent spacing,
decent structure".)

## 6. Build hygiene

- Build scripts are persisted (`tools/build_dual_reading_v2.py`), not
  session-inline — every window change goes in the script's table with a
  reason, then manifest_v2 + storyboard regenerate.
- Storyboard → listen with it → fix → re-QA → commit manifest+log+storyboard
  (media stays gitignored).
