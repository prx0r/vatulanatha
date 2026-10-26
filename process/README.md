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

## THE TWO COMPILATIONS (locked 2026-10-26 — ported verbatim from `prx0r/shiva-sutras` naming lock)

Every text we decode gets **two compilations, in this order, never blended:**

**STANDARD COMPILATION (text-led).** The text's own structure, untouched —
every unit in the text's order, uniform block pattern, no reordering, no
selectivity, no argument imposed. The fidelity object.
*In this repo:* the **dual reading** (13 sūtras in order → B-read →
Hareesh-translation per sūtra; artifacts `manifest_v2` + `storyboard_v2`)
is our standard compilation.

**CUSTOM COMPILATION (spine).** Built AFTER the standard, from its
findings: our five questions, our A/B/C layers — selection and order are
ours; the text's order is not binding here.
*In this repo:* the essays (CANON above: SPINE, S*_A/B, essay 0).

**Law of the split:** nothing composed for the custom compilation enters
the standard one; nothing in the standard is cut to flatter the custom.
**The standard proves we heard the text; the custom proves we understood it.**

**Why standard first (owner, 2026-10-26):** *it gives us the beautiful
structured data.* One stamped unit per passage, transcript, window,
coverage ledger — the substrate every later cut draws on. Custom
selection then becomes cheap and provable (every clip traces to a stamped
unit; we never re-derive the text's shape), and the selective product is
credible because the complete pass exists underneath it.
**Decode any text this way: standard first, custom second, never the reverse.**

Mapping: excavations/coverage/spine (00–04-equivalent) serve both · essays
argue custom only · dual reading = standard · `18-SPACING-AND-SEAMS` +
`sfx/` + storyboard serve both. Stage apparatus reference: `prx0r/shiva-sutras`
`process/00–10` (it is ahead of us on apparatus; same law).


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
`18-SPACING-AND-SEAMS.md` — cut/pause/level craft rules (2026-10-26).

## FINAL GOAL (owner, 2026-10-26) — where this all builds to
**Any text we care about can be poured into this format and comes out as
structured audio + its companion text** — same spine & blocks grammar,
signature timing (our spacing values), section structure, SFX marks: a
meditative pedagogy product, not a one-off render. **Order: standard
compilation first — that pass is where the beautiful structured data comes
from — custom compilation second.** Text → units → spine → layers →
spaced, marked, loudness-matched audio, read alongside its
storyboard. Vātūlanātha is project 2 (after Śiva Sūtras); each project
hardens the recipe until the recipe is the product. Everything in
`process/` accumulates toward that — no separate side-quest, the work we
are already doing is the path.

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
