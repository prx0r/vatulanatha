# PROCESS — Vātūlanātha / GRACE port (from analayo-nibbana model)

Port of `../analayo-nibbana/process/` (see its 00→08). What differs here:
- Source: Bäumer's 13 Vātūlanātha lectures (117 min, all transcribed) on the
  vṛtti of Anantaśaktipāda (corpus Sanskrit, segmented in `text/`).
- Beat anatomy (per owner): **[Sanskrit card] → [Fish says plain English] → [Bäumer explains]**.
- Film frame: GRACE documentary (`../GRACE-ASSEMBLY.md`) wraps the payload;
  the port here builds the per-sūtra beat files any mode (A/B/C) draws from.
- Voices: ARCHIVE = Bäumer (verbatim, selected never written) · FISH = key lines
  only (07 standard, never a sentence beyond the gloss) · HUMAN = film narration
  with citations (marked human bridges, provenance required).

## Read this first
`PROCESS_NOTES.md` — the living build log: what emerged from the audio,
how the question was measured, correction log, status board.

## Status (2026-10-25)
- [x] 00-INPUTS: 13/13 transcribed (8 CF + 8 srt); decompiled 13/13 (`decompile/`)
      text_read vs explanation spans; ear-check flags recorded (17 spans)
- [x] Sanskrit: 13 sūtra verses + vṛtti chunks (`text/vatula_sNN.txt`, `text/sutra_verses.txt`)
- [x] Key v1: `build/key_v1.json` (49 maps) + `build/loanwords_v1.json` (23) — DRAFT, owner vets
- [x] Sample beats: `build/beats_sutra3.sample.json`
- [x] question rule locked: `12-QUESTION-DEPTH.md` (one question per essay, posed → pause → A-clip answers)
- [ ] owner signs key + ear-check flags
- [ ] full beat files per sūtra (pool → gold), then GRACE modes A/B/C
- [ ] Fish TTS lines (confirm credits), assembly, verify.sh

## Port checklist used
See `08-PORTING.md` (copied verbatim from the model) and `07-PLAIN-ENGLISH-STANDARD.md`.
AXIOMS/MISTAKES/verify.sh also copied unchanged — they carry over.
