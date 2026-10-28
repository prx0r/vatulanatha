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

---

# SESSION 2026-10-26 — dual reading v2 (SEAMS FIXED, ONE LISTEN AWAY)

**State: v2 built + QA PASS. Next action = owner listens to
`build/dual_reading/vatula_full_dual_reading.mp3` (10:25) with
`build/dual_reading/storyboard_v2.md` as the page.** v1 kept as `_v1.mp3`.

## What happened
- **Seam audit (transcript+silence, all 28 cuts)**: v1 had 12 real defects —
  the 2:13 chop (sūtra 1 window overshot into her mangala aside) + mid-word
  cuts (H line 8 inside "spontaneously", colophon inside "viewpoints",
  intro before "commentator") + 5 orphan heads (window began on the previous
  sentence's tail) + 6 mid-sentence ends (unfinished translations in
  sūtra 4/6/10/11/12). All fixed by silence-snapping — every window edge
  now carries a written reason (`manifest_v2.json`, `build_log_v2.txt`).
- **Spacing rework**: voice switch ≈1.8s air (was ~1.35 with a chop),
  phrase-land ≈1s (was 0 — H slammed into the next bell), bowls open the
  piece, long-break bell before the colophon.
- **Levels**: per-piece gain to −21 dB mean, peak −1.5 cap → spread ±4.4 → 0.
  Final: mean −22.2, peak −1.7, density 80%, no flags.
- **SFX kit** (`sfx/`, pushed as `8cda10b`): bowls / ding / long-break bell /
  2 wood-block cuts + README roles & strike maps — the pause grammar for
  future builds (blocks = attention hits inside pauses, future work).
- **Tools persisted**: `tools/build_dual_reading_v2.py` (reproducible build),
  `tools/storyboard.py` (manifest → storyboard), QA engine at
  `patala/skills/skill-tempo-check/`.
- **Docs**: `process/18-SPACING-AND-SEAMS.md` (craft rules), FINAL GOAL
  section in `process/README.md`, storyboard shipped.

## Next actions (superseded — see 2026-10-26 LATER block below)

---

# 2026-10-26 LATER — production sheet + machine listening (state now)

**State: DONE by rule — see `DONE.md` (P0 PASS + 2 converged whole-mix passes,
all findings adjudicated, fixtures run both directions). Owner listen is now a
pleasure-listen, not a gate: `build/dual_reading/vatula_full_dual_reading.mp3`
(10:23) with `production_sheet.md` as the page.**

- **Sheet engine:** `tools/sheet.py render|check` — snap-to-silence cuts
  (uniform 0.3-0.5s leads, 0.3s tails), room-tone/switch-crossfade gaps,
  60ms edge fades, gains by target; `tools/p0_check.py` = one/two-pass
  structure proof (order/edges/invariants/airs/levels) — currently PASS.
- **Machine listening:** `tools/listen.py cut|ask|ask-all|whole` — Gemini
  free tier first ($0), qwen3.8-omni fallback (~$0.0005/pass, thinking
  effort=low), flow-only prompt per owner spec. Protocol written up:
  `process/19-MACHINE-LISTENING.md` (point of the listen = flow/jarring/
  critic ratings — NOT transcript re-checks; transcript guaranteed by build).
- **Flow rounds (whole-mix, 10:22 in ONE request):** baseline 25 flags,
  all "abrupt/jarring speaker+room transitions at every join" → after air
  rework (switch gap 1.6s, B leads 0.5s, room bridges, fades): **5 mild
  "slightly" notes** (quote-arrivals at bells + colophon). Structure legible
  throughout (every alternation named correctly by a cold listener-model).
- **Decided/skipped:** wood-block attention ticks at switches = the evidence-
  backed NEXT lever (owner deferred blocks to future — flagged, not done);
  room-color differences between the two archive sources = inherent, owner call.
- Decision queue §4 (essays) still open, separate from this product.
- Uncommitted: sheet+storyboard+tools+process docs (18/19) here; patala has
  `skills/skill-tempo-check/`.

---

# SESSION 2026-10-28 — essay 0 v2 BUILT + DONE (Hareesh trusted tier)

**State: `build/essay0/essay0_full_v2.mp3` (4:11) = DONE by rule. Custom
compilation now has its spine piece audible.**

- **Trust order upgraded** (owner): text > Hareesh spoken > Kaul 1923 > Baumer
  (voice). `build/template_13.json` = 13 rows (sanskrit_exact · hareesh_spoken
  from vtt increment-join · kaul · plain). Spoken Hareesh ≠ blog wording at
  ~5 sūtras (earlier pass) — **spoken is gospel** per owner.
- **Essay-0 stack v2**: Q(Narrator TTS) → 3s recall → Hareesh reads sūtra →
  Baumer answers · bells between · bowls/long-bell bookends. Plain = screen-only
  when no-op (E1). 5 H windows + 5 Baumer unit windows, all reason-carried.
- **p0_check essay0 mode** added (speech must follow pause/marker; standard
  dual-reading invariants preserved).
- **Gates**: p0 PASS · machine pass1 FLOWS (1 design finding fixed) · pass2 9
  findings all by-design/inherent → convergence. Ledger in DONE.md §essay0.
- TTS spend: ~660 fish credits (5 questions + 5 plains; plains now screen-only
  but kept for body-beat reuse). Guyzo credits confirmed live.
- Still owner-only: essay0_lock.json (lock = stack v2 + this artifact) ·
  Narrator-voice swap if wanted · decision queue §4 (essays A/B/C) unchanged.
