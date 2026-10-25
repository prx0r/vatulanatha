# PROCESS — Vātūlanātha / GRACE port (from analayo-nibbana model)

---

# ⬛ CANON v1 — THE ESSAY STRUCTURE (owner-final. Do not re-derive, do not re-scope.)

```
ESSAY 0  = THE SPINE        = the five questions, in order.
                              "What is realisation?" → "What is the self?" →
                              "How does realisation happen?" → "What does realisation
                              do to experience?" → "What is the fruit of realisation?"
ESSAY A  = SPINE EXPANDED    = each question answered with its GOLD clips,
                              sections at speed (artifacts: manifests S1–S5_A ✓)
ESSAY B  = A EXPANDED        = same walk + DEPTH (artifacts: S*_B, selection pending)
ESSAY C  = B EXPANDED        = same walk + TEXTURE (her full lectures, her order,
                              minus C-MARKS exclusions)
```

- **Nesting: 0 ⊂ A ⊂ B ⊂ C — append-only** (never rewrite the inner layer).
- **Essay 0 is the list of QUESTIONS.** Answers, interlinear cards, compressed-answer
  clips and bells are **machinery that lives INSIDE A/B/C** (section openers) — they
  are never "essay 0".
- The spine plays at the head, then re-opens at each layer head: **heard 4×, each
  time answered deeper** (expansion, never new material).
- Artifacts: SPINE.md = essay 0 · S{1..5}_A = essay A · S{1..5}_B = essay B ·
  C-rule + full sources = essay C · `build/essay0/` = A's opener machinery only.

## Lineage — how this maps to the 33-sermons builds (reviewed 2026-10-25)
| theirs (analayo / tantraessays) | ours |
|---|---|
| 6-section argument scaffold (§1 What it is … §6 Remains) + seed (1-sentence motto) | **Essay 0 = the spine (5 questions)** — same job: the skeleton that everything expands |
| essay A (10–20m gold-only) ⊂ B (20–40, contains A) ⊂ C (rest) — FORMULA, append-only | **identical** for our A/B/C |
| V1 pool → V2 gold → V3 core (audio product, ÷3.5/layer) | our C ≈ their pool, our A ≈ their gold; core ≈ the spine-recurrence density |
| motto recurs at layer heads (bells) | the spine re-opens at layer heads (bells) |
| cluster-by-problem, convergence test | identical (S2 method) |

**One sentence, forever:** *essay 0 is the questions; A answers them with gold;
B deepens; C floods with texture; each layer re-opens the same spine wider.*
---


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
