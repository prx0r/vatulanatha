# HANDOFF — session 2026-10-25 (review pass + sanskrit wiring + side project)

**State: TEXT-COMPLETE, PRODUCT-BLOCKED (owner queue + TTS).**
`verify.sh` = ALL GATES PASS. All essays cold-read line-by-line and
flow-audited; verdict = every essay is argument, not random statements.
8 commits today (41d0993..cf95e51) — **not pushed yet**.

---

## 1. Incident + recovery (closed)
Consciousness 6-question spine (meant for a SEPARATE essay, not ours)
was mistakenly imposed on this repo — **fully recovered**: `git restore`
+ stray S6 files removed + `spine_preview.mp3` re-rendered (38.9s, the 5
realisation questions). Nothing was ever committed/pushed from the bad
state. Leftover patch (not ours to use): `/tmp/opencode/vatula-remap-abort.patch`.

## 2. Review suite — `build/reviews/` (read these first)
| file | verdict |
|---|---|
| ESSAY{0,A,B,C}_REVIEW + _SCRIPT | 0/A/B/C standalone YES; script mirrors of each |
| LINE_BY_LINE | every joint + **all 122 C seams**: 0 random statements, no non-sequiturs |
| ARGUMENT_FLOW | chains read as prose; 3 order bugs found (below) |
| SEGMENT_FIT | all 96 units vs their question: S5 7/7 · S3 19/20 · S2 half-weak |
| FORMAT_REVIEW | gospel stack = canon; tiers: question/translation/plain/voice 101/101 |
| SANSKRIT_CHECK | 13/13 verse→literal→plain aligned (sandhi-resolved sūtra 12; grāsa note sūtra 4) |
| COVERAGE_REVIEW | 117.2 full · 83.5 units · 26.5 marks · **7.3 unclassified**; C keeps 89% under gate rule vs 77% under canon shorthand |
| EXPANSION_Q1 | Q1 unfolds 0→A→C, **flat at A→B** (S1 never flow-read) |
| ESSAYC_SEAMS, FIT_INPUT | raw reads (evidence) |

## 3. What changed in build (all sanctioned mechanical)
- **Sanskrit wired into 101/101 cells** (`text.sanskrit` = verse[lecture],
  source-tagged PDF-never-whisper) — commit `dc0a37b`.
- **essay0/manifest.json rebuilt**: 5 stacks by owner rule (*card =
  sūtra of the answer-unit*: Q1→1, Q2→4, Q3→8, Q4→10, Q5→13); old
  broken keys kept as `legacy_old_keys`.
- Nothing else touched (all content decisions report-only).

## 4. DECISION QUEUE (owner — each is one sentence)
| # | decision | where |
|---|---|---|
| 1 | **3 order bugs — say "fix"**: S2_B `4-07`→after 4-02; S4_B `7-08`→after 7-03; S5_B `12-06`→before 12-02 (their own g1-gap specs + butt-join transcripts prove positions) | ARGUMENT_FLOW |
| 2 | **vat4-07 home = S2** (content + B-list + siblings all say S2; only assignment says S4) — resolves B-1/C-1 append break | ESSAYC_REVIEW |
| 3 | **Lock C rule to FORMULA wording** (exclude only namaskar/thank-you/head-silence) — kills the 77%/lossy shorthand reading (13.4m at risk) | C-3, COVERAGE |
| 4 | Fix C-MARKS header: 85.9/31.2 → **83.5/26.5**; add 7.3m gaps as KEEP rows; add L-2's 3 unmarked tails (vat7 thank-you, vat12 next-session, vat9 namaskaya) | COVERAGE, LINE_BY_LINE |
| 5 | **L-1 texture-ownership rule for C** (interleaved lectures: skip-with-breath vs leak-sibling) — blocks C render | LINE_BY_LINE |
| 6 | `vat6-01` (asks "what blocks") in S3: keep / move to head / demote | A-1 |
| 7 | S2 opener (`vat2-02` weak) + `vat5-05` (ethics, fits S5) | A-2, A-3 |
| 8 | **S1 flow-read for B** — T-1: S1_B = A exactly; candidates vat1-08 + vat13-04 + vat1 8:17–8:46 bridge (+1m); **B has +5.4m headroom to 40m gate** | EXPANSION_Q1, COVERAGE |
| 9 | vat12-06 fruit-naming → A? (2.4m > 2.2m headroom — needs window trim per FORMULA "adjust windows not quotes") | B-2 |

## 5. Blocked on others (unchanged)
- **TTS**: Guyzo credit-confirm → ~5 questions + plain lines (silent slots everywhere). Then: essay-0 beats 2–5, section renders, G8 listen.
- **Lock**: `build/essay0_lock.json` after hearing essay 0.
- **C render path**: unproven (G11 = ffprobe estimate only) — needs #3+#5 first.
- Final assembly: **NOT NEEDED** (owner, 2026-10-25). Definition of done = text makes sense as cohesive flow argument → **met**, pending queue above.

## 6. Side project — DONE (Beth Upton)
`~/Downloads/beth_upton_dependent_origination_42min.mp4` — 42:00, 133MB.
Visuals (silent master) + her audio (re-pulled `AbKJuW-icyM` 96k, NOT the
1:57 URL given) + two-pass loudnorm −16 LUFS (verified, no clip) + mux
(video stream-copy). **Sync verified 5/5 anchors** (her exact words on
screen at 3:15/12:15/21:00/30:15/41:15).
Support files kept: `beth_upton_dhammadena_source.webm`,
`beth_upton_norm.flac` (360MB re-mux master), `beth_src.en.json3`
(transcript), `beth_spot_*` (sync eyeball pairs), `/tmp/opencode/sync/`.

## 7. Immediate next actions (suggested order)
1. Owner runs the decision queue (§4) — ~30 min, mostly one-liners.
2. Me: fire mechanical batch on "fix" (3 reorders + ledger numbers).
3. Owner: S1 flow-read + B headroom picks (or say "spend it").
4. Owner: TTS credit-confirm → my render pass → G8 listen → lock.
5. C: rule (#3/#5) → build render path → G11 real render.
6. `git push` (8 commits waiting — not pushed this session).
