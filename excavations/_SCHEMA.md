# Vātūlanātha excavation schema (ported from tantraessays 2026-10-25)

Each lecture -> one file `excavations/<lec>.md`. Idea-units reshuffled into essays/segments.

## Unit shape (all fields required)
- `uid`: `<lec>-<nn>` stable, never reused (e.g. `vat3-01`)
- `timestamp`: `HH:MM:SS-->HH:MM:SS` from CF json seconds or srt (same base as mp3)
- `topics`: 1-4 tags from closed list
- `role`: claim | simile | refutation | story | lineage | method | practice | mantra-gloss | history
- `quote`: Bäumer's words VERBATIM from `vat-text/<lec>.txt` (English only;
  Sanskrit chant/recitation never quoted — card comes from corpus `text/` instead)
- `context`: 1-2 lines what she is answering / before-after
- `grade`: A = clip/essay-ready · B = good with edit · C = do not use (namaskar tails,
  thank-yous, garble, head silence)
- `layer`: `read` = she is voicing the vṛtti (matches `decompile/` text_read) ·
  `explain` = her own words. Drives the 3-layer script (PRIMARY card → PLAIN → BAUMER).
- `essay_use`: one line how this is reused

## Controlled topics (closed; add only with note)
grace, sudden-enlightenment, madhya, speech, sound, senses, kula, guru, recognition,
nonduality, praxis, mantra-gloss, lineage, death-rebirth, ethics, ritual, cosmology, tattva

## Rules
- Quote must grep-verify in `vat-text/<lec>.txt`; timestamp must exist in decompile/srt.
- Every unit inherits its `layer` from a `decompile/` span (provenance: span index).
- End each file with `## Reuse clusters` + `## Cross-links`.
- Grade pyramid target (global): A small, B larger, C largest — do NOT make everything gold.
