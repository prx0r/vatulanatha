# CUTTING FORMULA — Dyczkowski @ BHU: Tantrāloka Content & Construction (2 parts)

Same law as the Analayo Nibbāna cuts: **band 20–40 min, aim ~30, take 40 when the
material itself is the gem.** Sources: Part 1(B) lecture 99.7 min, Part 2 Q&A 104 min.
No render until the owner approves.

## Keep-rank
1. **Frame (≤90s):** what the lecture is + its thesis stated once.
2. **Spine:** the passages carrying the lecture's own argument — construction of the
   Tantraloka, prasiddhi, Trika/Malini, padhati, prakāśa-vimarśa, discovery of śakti,
   mantra linguistics, the Mālinīvijayavārttika conclusion.
3. **Unlock (≤6–8 min):** one definition per concept (prasiddhi bottle, nirvikalpa
   pole/tree, aham-bhāva). Second opinions and parallel-history digressions: out.
4. **Close:** the lecture's own close (scripture-claim + liberation line).

## CHANTING RULE (transmission — never lost)
Sanskrit chanting is content, not noise: mangala/invocation verses, recited sūtras,
stotra — these ARE the tradition's transmission. They are **always kept** (D-grade at
minimum, never "cut"), and an **opening mangala/invocation chant is hoisted to the very
head of the render as the intro** — listener hears the homage first, then the frame,
then the teaching. Full length, original audio; English gloss comes from the lecture's
own rendering (or TTS if the lecture doesn't provide one). A recitation mid-lecture
stays in position (chant rule: keep the gap/chant, find the fat elsewhere).
Guard: every recitation MUST have a MAJOR entry kind=recitation/sanskrit, otherwise
the labeler falls through to ranked-out and it would be silently lost.

## Always cut
- host bios, welcomes, applause, tea-break logistics, vote of thanks, presidential remarks
- mic failures, music breaks, Sanskrit recitations (ASR-verified spans)
- banter ("I'll take an hour", "people stand up and leave", Modi/nazi/Harvard jokes)
- lineage/padhati/karma/Bhartrihari history surveys (rank 2 — dropped first)
- second-order examples (bottle-holding-shakti enumeration, vikāsa music examples)
- duplicate question re-asks in Q&A; moderator chatter

## Method (as proven on Analayo)
1. Transcript = `transcripts/partN.txt` (panel ASR, merged cues — ~8–18 s/line).
   Q&A gap regions re-transcribed with faster-whisper (`/tmp/opencode/tl2_gaps_transcripts.json`).
2. Design `KEEPS=[(start,end,rank),...]` in native seconds (mp3 == SRT timebase).
3. `python3 tools/gen_plan_tl.py N tools/tlN_keeps.py` → `partN.cutplan.{json,md}`.
   Asserts kept ≤2400; auto-drops rank>1 largest-first.
4. `python3 tools/audit_seams_tl.py N` — every keep start must read standalone,
   every keep end must not dangle. Iterate.
5. Render-time: snap flagged boundaries to the nearest speech pause (ffmpeg silencer).

## Grades — full coverage map, nothing silently lost
- **A = gold** (rank 1) — killer lines, thesis statements, signature similes
- **B = flow** (rank 2) — doctrinal glue, secondary reads
- **C = technical** (rank 3+) — depth only
- **D = non-English content** — Hindi/Sanskrit spans pulled out of the complement
  (`d_spans` in cutplan.json) as **translation candidates instead of cuts**.
  True noise (music-only, logistics, applause, jokes) stays `cuts` — not D.
- Dial: A → A+B → full. Translation workflow for D is a separate pass.

## Files
- sources: `tantraloka-bhu-{1,2}.mp3` (symlinks), transcripts from
  `../tantraloka-bhu-{1,2}.{en.srt,cues.json}` via `tools/get_panel_subs.py`
- plans: `part{1,2}.cutplan.{json,md}`
- keeps: `/tmp/opencode/tl{1,2}_keeps.py` (copied to tools/ when final)
- videos: Part 1(A) `0jXydYZ3bNo` (13:45, intro segment — not yet downloaded),
  1(B) `lASgAdZnmnc`, 2 `bJIeu5_x2Ek` — channel: DEPARTMENT OF PHILOSOPHY AND RELIGION BHU VARANASI
