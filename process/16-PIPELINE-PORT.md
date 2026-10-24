# 16 — PIPELINE PORT. Analayo 01–06 → Vātūlanātha (reviewed 2026-10-25).

## Their chain (what 33 sermons actually did)
00 inputs → 01 transcribe/cutplans (≤40m/unit, grades, seam audit) →
02 segment (keyword scorer, every span ONE section, totals reconcile,
cluster-by-theme) → 03 gold→core (A-only; top killer/cluster; READ AS
SCRIPT = flow audit) → 04 three-layer (verbatim pads + PROVENANCE two-
method; plain = deterministic key, byte-identical reruns; TTS lines
punctuation-grammar; speakers locked; beat = intro→bell→fish→clip→water)
→ 05 render LAST (+0.15 handles, anchor-map+pause-snap, breath/water
beds, loudnorm −16, fades) → 06 gates G1 totals · G2 seams · G3 motto-cap
· G4 hold-up READ test · G5 provenance · G6 TTS scan · G7 slop · G8 listen.

## Port map for "the whole text × plain english × baumer"
| their step | our equivalent | status |
|---|---|---|
| 00 inputs | mp3+transcripts+decompile(quotation-marked)+Sanskrit+Kaul-EN | ✅ |
| 01 cutplans | replaced by **units-as-pool**: 83 excavated units (graded, timestamped) + decompile spans (the full-pool complement = C) | ✅ units |
| 01 seam audit | unit boundaries = transcript sentence edges (quote-verified) — spot-audit at G2 | partial |
| 02 segment | **CATALOGUE (topics→uids) + clustering + convergence test** (question-emergence already done) | ❌ next |
| 03 gold/core | gold = 28A in cluster order; core = killers per cluster; flow-read | ❌ after 02 |
| 04 pads | **card = Sanskrit (corpus) + Kaul-EN (PD) on screen**; provenance = our verify discipline + Kaul quotes get the same substring test | ❌ build |
| 04 plain | deterministic filter over key_v2 (word-boundary, rerun byte-identical) → `build/fish_filter_vatula.py` (port of fish_filter.py) + blunt pairs from key_v1 | ❌ build |
| 04 TTS lines | gloss → punctuation grammar (no parens/colons, English-first) | ❌ |
| 04 speakers | BAUMER (archive owns Sanskrit aloud) · PLAIN (key lines only) · HUMAN (question+intros) · [READER=Sanderson later per 15] | rules in 12+15 |
| 04 beat | our cell: [question → 2-breath pause → PLAIN line → Bäumer clip → water] + card on screen | locked in 12 |
| 05 render | ffmpeg same settings; manifest txts per segment (manifest_sN style) | ❌ last |
| 06 gates | G1=coverage audit (decompile spans unit'd or C) · G2 seams · G4 hold-up (plain primes clip) · G5 provenance · G6 TTS scan · G8 listen; wire `verify.sh` | G1 now |

## Anti-drift rules inherited (from their MISTAKES/AXIOMS)
- no hand-written sentence in any script file (provenance or slop)
- plain edits go in the KEY, never in the output
- overrides are normal; UNLOGGED overrides are slop
- thin clusters are structural — never pad to quota
- audio last; missing audio never blocks text work
