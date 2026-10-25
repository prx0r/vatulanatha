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

## VIDEO RUN-ORDER — the Russian dolls end to end (owner, locked 2026-10-25)

The finished video plays the nesting **linearly**, with bells marking each threshold:

```
[BELL] → ESSAY 0 → [BELL] → A (sections at speed) → [BELL] → B (+depth) → [BELL] → C (+texture)
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
