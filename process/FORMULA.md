# EXACT FORMULA — locked

For any essay source set (e.g. Essay 1 = Karma 93.9m + Markji 36.8m = 130.7m original):

- A = 10-20 min. All gold, nothing else. Verbatim Mark cores + minimal bridges to play standalone. Must make sense alone. Highest signal only.
- B = 20-40 min. Contains ALL of A, plus depth/explanation. Adds silver argument, origins, bridges. A plays inside B unchanged.
- C = rest to near-complete. Contains ALL of A and ALL of B, plus texture (anecdotes, Q&A, asides, alternate opens). Closest to full lecture without chant/tech/filler.

Rules:
1. A ⊂ B ⊂ C. Always. Never rewrite A inside B, never rewrite B inside C. Append only.
2. Quotes verbatim from txt, timestamps from srt. Mantra Sanskrit via PDF only, never whisper transliteration.
3. C excludes: chant runs, mic-checks, room noise, fan/water breaks. Those stay in source, never in essay.
4. Every clip block retains: AUDIO path, TRANSCRIPT path, TIMESTAMP, EXCAVATION file. No clip without source.
5. Grades are essay-local: A=gold must-use, B=silver should-include, C=mention worth-keeping. Global pyramid across corpus: A small (25), B larger (55), C largest (66).

Essay 1 calibration: 130.7m original → A ~15m full-section play (~1m verbatim + bridges), B ~30m, C ~45m. Adjust windows, not quotes, to hit runtimes.

Essay 1 calibration (locked 2026-10-24): 130.7m original (Karma 93.9 + Markji 36.8) → A 7 clips ~15m windows (~3m verbatim), B +3 clips ~27m, C +3 clips ~42m. A⊂B⊂C append-only verified.

33-sermon alignment (2026-10-24): budgets A 10-20 / B 20-40 / C rest (their 20-40 aim 30 adapted to essay brevity). Keep-rank: cold open / spine / unlock / close. Always-cut: chant/tech/mic/fan/Q&A tails/bio/recap/2nd telling. Seam: block after cut reads standalone, pause-snapped, never mid-sentence. Timebase: srt-native = audio (no YT/DS map needed). Cutplan.json per essay: target/kept/timebase/seam/grades. Speakers: Mark archive / Human cold-open+bridges ~2-3 min / Plain key-only (trika_key.json). Verbatim: audio windows are truth, md quotes are pointers with ... allowed only if render expands to sentence boundaries. Render (port analayo when needed): concat keeps, loudnorm -16 LUFS, afade 0.15s, bell -20dB, cough micro-cuts ±0.3s, pause breath 1.5s / water 2.5s.

## Vātūlanātha calibration (ported 2026-10-25)
- Source set: 13 sūtra lectures 117m + mangalas 18m = 135m original, all transcribed,
  decompiled (text_read vs explanation), Sanskrit vṛtti segmented per sūtra.
- A = 10-20m (GRACE-cold: the glance + grace claims) · B = 20-40m (A + the sūtra argument)
  · C = rest (A+B + full commentary readings, minus namaskar/thank-you/head-silence).
- A ⊂ B ⊂ C append-only. Quote source = `vat-text/*.txt` (timestamped), timestamps =
  CF json seconds == mp3 seconds == srt seconds (no anchor map needed).
- Sanskrit card lines come from `text/sutra_verses.txt` (corpus), NEVER from whisper.
- Speakers: BAUMER (archive, reading vs explaining per `decompile/`) · PLAIN (key-only,
  written lines) · HUMAN (film narration with citations, marked bridges).

---

Essay-0 selection follows `process/ESSAY0-FORMULA.md` (7 tests, question → sanskrit → translation → plain → audio → stack-read → lock).

## THE UNFOLDING — form mirrors content (owner, 2026-10-25)

The keystone: **the essay does not DESCRIBE unfoldment — it PERFORMS it.**
- ESSAY 0 = THE SPINE — the five questions in order (what is realisation → what
  is the self → how does it happen → what does it do → what is the fruit).
  ESSAY A = the spine EXPANDED: each question answered with its gold (sections at
  speed). ESSAY B = A expanded (+ depth). ESSAY C = B expanded (+ texture, her walk).
  Russian dolls: 0 ⊂ A ⊂ B ⊂ C. Machinery (interlinear cards, compressed answers,
  bells) lives INSIDE the expansions — it is not a separate essay.
- A, B, C = the same seed unfolding at growing depth — exactly as realisation
  unfolds from what-you-already-are; the listener's understanding grows the way
  the text says realisation grows: not by addition, by expansion of the same thing.
- THREE mirrors of one shape (the fractal made doctrine):
  1. her text: sūtra 1 contains all → the vṛtti unfolds it → detail (her own claim);
  2. the teaching: unfoldment, not acquisition (vat1-05 — the seed itself);
  3. our essay: 0 → A → B → C, re-heard 4×, each hearing WIDER not different.
- Consequences: never replace the seed with a NEW idea at each layer (that would
  be accumulation = the wrong ontology) — each layer only EXPANDS the same
  sentence; bells = the rings of the unfolding; ending on C = the seed complete.

## VIDEO RUN-ORDER — the Russian dolls end to end (owner, locked 2026-10-25)

The finished video plays the nesting **linearly**, with bells marking each threshold:

```
[BELL] → ESSAY 0 (the five questions, ~30–60s) → [BELL] → A (answers expand) (sections at speed) → [BELL] → B (+depth) → [BELL] → C (+texture)
```

- **Essay 0 recurs FOUR times** — at the head, then re-entered at the head of A,
  of B, and of C: **the same compressed answer, heard at expanding depth** (the
  seed re-lands as each layer opens; by the end of C the listener has it 4×).
- Bells: question-bell opens each section (12 grammar); **layer-bell** at each
  0→A→B→C threshold (analayo 09-BELLS-ZOOM pattern: motto-bell 880Hz/2.5s for
  sections, zoom-bell 220Hz/6.0s for layer crossings — same units, port at render).
- Append-only holds: A never rewrites essay0, B never rewrites A, C never rewrites B —
  the recursion is RE-HEARING, not re-editing.
- This is the ship shape: one video, four passes of the same core, bells as the map.

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

