# ESSAY 0 — REVIEW (cold read, 2026-10-25, report-only)

**Verdict: STANDALONE — YES.** All five questions parse cold (no jargon, no
cross-dependence), and together they form a complete argument arc:
what it is → what the self is → how it happens → what it does → what it
brings. Each question carries attached answer-dust (ESSAY0-SPINE table);
G0 5/5 pass; question wording identical in SPINE.md, FORMULA, render tool,
and all 101 gospel beat cells.

Read against: `SPINE.md`, `build/essay0/ESSAY0-SPINE.md`,
`build/essay0/manifest.json`, `spine_read.json`.

## Issues

| # | sev | finding |
|---|-----|---------|
| 0-1 | MEDIUM | **Interlinear card pool incomplete + misaligned.** `manifest.json` has only 3 sanskrit cards for 5 questions, and the keys don't track the questions: the `S2` card (`kasyacit kvacit kadācit akasmādeva` — "somewhere, sometime, unexpectedly") is *how-happens* material, i.e. Q3's card, not Q2's ("What is the self?"). Q2 and Q4/Q5 have no card at all. |
| 0-2 | MEDIUM | **T3/P3 pair is broken.** `T3` = "by the mode of great intensity one attains one's true nature" but `P3` = "Permanence of the immersion in the real self … four deities" — P3 is not the filter of T3 (every other Pn = f(Tn)). P3 is an orphan of a translation that isn't in the file. Determinism claim can't hold for this pair. |
| 0-3 | LOW | **Q5 dust is recognition-flavoured, not fruit-flavoured.** "All what I feel now, I was already feeling that" answers Q5 as *recognition of the already-given*. S5's own gold offers two more literal fruit answers: no-rebirth/freedom (vat12-02) and silence-wonder (vat13-01). Pick stands; ear may swap. |
| 0-4 | LOW | Q2 dust is a two-clause sentence (~25–30s) — longest of the five; fits the cap but leaves least room. |
| 0-5 | STATE | Build state, not defects: Q1 built as full beat (`essay0_1.mp3`, 38.6s); Q2–Q5 = opener cuts exist; `spine_preview.mp3` = bells+silence placeholders (no TTS); `build/essay0_lock.json` not written. |

## Notes (no action)
- Answer-candidates are correctly scoped as *A's section-opener machinery*,
  not Essay 0 itself (ESSAY0-SPINE canon, consistent).
- The five questions as a sequence are the "most fundamental progression
  possible" per the standalone-clarity law — confirmed cold: a stranger
  hearing only the list knows exactly what the film will argue.

## Suggested next step (owner)
When cards are wired: rebuild manifest.json as a per-question map
(Q1..Q5 → sans + trans + plain), completing 0-1/0-2 in one pass.
