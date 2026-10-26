# 20 — LISTEN LOG (the actual back-and-forth: every pass, fix, number) (2026-10-26)

Protocol = `19-MACHINE-LISTENING.md` · rulings = `../DONE.md` · craft rules = `18-SPACING-AND-SEAMS.md`.
This file is the raw record: what the ears said, what we changed because of it,
and what the meters read after — the rhythm-and-handoff story in order.

## 0. How the rhythm actually got built (credit list)

1. **Transcripts gave the content rhythm** — every cut on a sentence edge
   (silence-snapped, never cue-trusted); the text's own breath = the piece's breath.
2. **Silence maps gave real pause points** — `silencedetect` per source at
   adaptive thresholds (−26…−44; hissy archive needed −22), so gaps are *inside*
   the source's own room tone, not invented.
3. **Owner set the spacing hierarchy** (18: switch > land > section) — taste,
   ratified once, encoded as numbers.
4. **Single-variable loop**: one change → render → meters → ears → repeat.
   Nothing was tuned by feel; every step has a before/after number below.
5. **The machine ear nagged; adjudication judged.** Ears find candidates;
   maps/verbatim decide (this is why v1's "FLOWS" token never fooled us).
6. **Room continuity was the handoff trick** — the floors of the two archives
   meet *inside* the gap (bridge), so the voice change arrives on continuous
   air instead of a floor-cliff.

## 1. Pass-by-pass log (verbatim outputs)

### P0 — structure determinism (`p0_check.py`, repeated after every render)
Snapshots: `612.34s → 612.00s → 616.52s → 616.23s → 622.58s`.
Final: `blocks 72 | 622.58s | −18.0 LUFS | −1.7 dBTP | pauses 222 |
switch airs 1.83/1.93/2.06 (spec 1.6+pads) | PASS`.
Intermediate FAILS (kept for the record): 33 edge flags on first run
(threshold taught to us: her floor sits at −25…−35, speech at −5…−11 →
quiet-map at −22dB); pause-duration FAILS during the crossfade bug hunt
(`sw01 dur 1.1 != spec 1.3`, `sw10 rendered 0.243 != 1.3`) → deterministic
half+fade gap builder replaced `acrossfade`.

### P1 — round 1, 4 clips, qwen3.8-omni (data-URI), strict defect prompt
- `open` — **CLEAN**: "speech begins cleanly after a brief natural pause
  (~00:09–00:10) … even pacing, no clicks, volume jumps, or abrupt mid-word cuts"
- `sw1` — **CLEAN**: "Transitions are properly marked by bells, speaker
  alternation is clear, pauses between sections are appropriate"
- `end` — **CLEAN**
- `fix3` — 3 findings:
  - "00:08 – Sudden background-noise change/volume jump (transition from
    archive recording to clean studio voice)"
  - "00:38 – Sentence cut off abruptly (female speaker ends mid-thought on 'sahasra')"
  - "00:39 – Sudden background-noise change … archive → studio"

### P2 — round 2, 8 clips (zones + 3 clean sweeps), qwen, same prompt
- `mid1` **CLEAN** ("final truncation … occurs at the very last second and is
  expected per the excerpt rule")
- `mid2` **CLEAN**
- `mid3` **CLEAN** — "Noise-floor shift between archive and studio segments is
  expected, not a defect" ← the same thing P1 flagged at 00:08/00:39 (ear
  inconsistency, logged as calibration data)
- `sw1` — 3 findings: dead/long pause at switch, room shift to him, room shift back
- `fix3` — 1: "00:34 – female speaker cut off after 'first sutra, sa…'"
- `late` — 2: hiss disappears at him (00:42), hiss "returns abruptly" after bell (00:53)
- `end` — 2: archive→studio jump (00:09); "pause too long/dead after the bell" (00:25)
- `open2` — 2: "word cut off ('the unbr-')" (00:02); "click / dead air" (00:22)

### P3 — whole mix #1 (one request, entire piece), flow-only prompt, thinking=low
**25 findings — one family:** every join called "abrupt/jarring/disjointed"
(speaker + room). Sample: "03:23 transition between speakers is abrupt and
there is a noticeable difference in audio quality, making it feel disjointed";
"05:09 the transition … and the shift in audio quality are very noticeable";
~25 such rows mapping to *every* switch and marker→B join.
→ Diagnosis: joins = hard-edged (floor-cliff + too little air). Fix batch:
switch gaps 1.3→1.6s; B-block leads 0.3→0.5s (both already had room bridges
+ 60ms edge fades from the P1/P2 fix batch).

### P4 — whole mix #2 (post-air rework)
**5 findings, all mild, none about rooms anymore:**
- "03:08 confusingly abrupt transition … introduction of the new quote (slightly disjointed)"
- "03:40 … quote → analysis is a bit abrupt"
- "05:24 … transition into the quote is abrupt"
- "07:06 … analysis → next quote is slightly disjointed"
- "09:36 … into the final 'postscript' is slightly abrupt"
→ All map to **bell-marked arrivals** (b03/b04/b07/b10/colo heads; b10's
07:06 is her *inner* read structure — one uncut block, no seam exists).
Class = taste, severity "slightly". Ruling: accepted-by-design (DONE.md).

### P5 — whole mix #3 (final confirmation)
```
- 00:30: jarring repetition of the word "taught".
- 01:23: jarring pause and repetition of the word "is".
- 02:28: jarring shift in speaker, audio quality, and tone.
- 05:34: jarring cut/shift in audio and speech.
FLOWS
```
Adjudication: 00:30/01:23 → verbatim test (§3) → **refuted**. 02:28 = bell→b02
arrival (taste-accepted class). 05:34 = *inside* continuous b07 (412–340… block
has no seam; P0 quiet edges) → source-internal delivery, out of product scope.
**Blocking = 0, second consecutive pass → convergence met.**

### P6 — verbatim refutations (the "repetition" claims)
`ask check30` (00:25–00:45, verbatim request):
> "mere words being beyond all doctrines, and then taught him through these
> sutras, the extraordinary, unbroken, highest reality which is free of the
> stain of all the following dualities, process and immediacy."
→ one "taught", clean prose. Claim dead.

`ask check83` (01:18–01:32):
> "perished by the ultimate secret. What I just read is my translation of the
> introductory prose to the 13 Sutras, the prose written by the uh comma…"
→ single "is". Claim dead. Rule recorded: **verbatim beats verdict.**

### P7 — ear regression fixtures (both directions, final)
- **v1 (seeded-defect file)** → `01:23 jarring cut. 05:39 jarring cut.
  09:10 jarring cut.` + verdict **FLOWS** — instrument finds cut-class on
  known-bad, *and proves the token alone is unreliable*.
- **v3** → P0 PASS + P5 = FLOWS/0 blocking.
→ Done-rule = adjudicated blocking count (DONE.md), not the token.

## 2. Fix ledger (finding → evidence → change → measured after)

| # | finding (source) | evidence | change | after |
|---|---|---|---|---|
| 1 | 2:13 mid-sentence chop (owner, v1) | CF cue lag vs silence: cut at153 inside "…sudden inspiration" (sentence ends 142.16) | window153→143 | clean sentence end; fixture |
| 2 | 12 window defects: orphan heads + mid-sentence ends | silence maps per source | **snap-to-silence engine** (adaptive thresholds, lead 0.3/0.5, tail 0.3) | all 28 edges carry written reasons (manifest_v2) |
| 3 | H mid-word cuts (h04 "consciousness", h08 "spontaneously", colo "viewpoints") | word tags: ends landed < word-end | snap + tail 0.3 | e.g. h04 end 546.7→547.1 (into silence 547.27) |
| 4 | floor-cliff at switches: gaps −91 dB digital vs room −53 (P1: "noise change") | silence + volumedetect | switch gap = **half her room + half his room**, 80ms fades | gap floor ≈ room; P4: zero room complaints |
| 5 | "hiss returns abruptly" after bell (P2) | edge scans | **60ms in/out fades on speech pieces' room pads** | join steps masked; P4/P5 silent on it |
| 6 | airs too tight *and* inconsistent (P2 sw1 "dead/long" both ways; P3 every join) | air stats | sw gap 1.3→1.6, B lead 0.3→0.5 | airs **1.47–1.65 → 1.83–2.06** (spec 1.6+pads) |
| 7 | dead tail after long-break bell (P2 00:25) | bell decay −26dB@4.0s, land 0.6 | gap_colo 0.6→0.3 | total post-bell breath ≈ bell itself (by design) |
| 8 | "repetition" claims (P5) | verbatim transcription | none — refuted | ledger row "unstable → discard" |
| 9 | "sa…"/"unbr-" cut claims (P1/P2) | transcript guarantee + mix silence 60.5–62.3 = *source's own* 1.8s pause | none — **owner: transcript-level out of scope** | taxonomy row |
| 10 | bell source lost in disk cleanup | sheet render abort | recovered from mix marker span → `sfx/bell_880.wav` (tracked) | never losable again |

Loudness (one-shot, never touched again): per-piece `gain = min(−21 − mean,
−1.5 − max)` from raw spreads **+1.6…−4.4 dB** → final **−18.0 LUFS,
B −18.0 vs H −17.5 (Δ0.5 LU), TP −1.7 dBTP, LRA 8.8**.

Air/meter evolution (whole product):

| build | duration | switch airs (min/med/max) | machine verdict |
|---|---|---|---|
| v2 | 615.2s | (v2-era, gaps1.0) 0.94/1.32/1.94 | — (audit found them) |
| v3-a | 612.3s | 1.47/1.60/1.65 | round1/2 clips: 3 CLEAN + fixed flagged zones |
| v3-b (bridges) | 616.5s | 1.53/1.60/1.76 (crossfade bug: 0.36 min, caught by P0) | — |
| v3-c (air) | **622.6s** | **1.83/1.93/2.06** | P3 25 → P4 5 → P5 FLOWS/0 blocking |

## 3. What the owner ratified, in order (the taste inputs)

1. "watch storage" → all intermediates regenerable, `build/*/pieces*/` ignored, raws auto-deleted.
2. "transcript is perfect by construction — flow and obvious jarring only" → prompt + taxonomy rule.
3. "wood blocks = future" → ticks flagged as lever, not shipped.
4. "two exemplars on purpose" → tool duplication = calibration, not drift.
5. "never need to listen" → DONE rule (convergence + adjudication) replaced ear-as-gate.
6. Final: **"how did u get the rhythm and handoffs so perfect"** → answered by §0+§1+§2 of this file.
