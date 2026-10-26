# 19 — MACHINE LISTENING (omni as the critic) (2026-10-26)
> Raw pass-by-pass record with verbatim outputs + fix numbers: `20-LISTEN-LOG.md`.

## The point of the listen (what is already guaranteed — never re-check it)

Transcript correctness is **built in**: every window snaps to a transcript-verified
sentence boundary (`process/18-SPACING-AND-SEAMS`), P0 proves order/edges/invariants
(`tools/p0_check.py`). The machine listen therefore **never verifies text**. A model
report that contradicts the transcript + silence maps (round examples: "cut on
'sa…'", "the unbr- cut") is **discarded** — owner rule: *"the transcript is
literally what it says; I want flow and obvious jarring things."*

The listen answers only what transcripts and deterministic checks cannot:

| mode | question the listen answers | evidence form |
|---|---|---|
| **1 Jarring-mechanical** | sudden cutoffs, clicks, volume/room jumps, dead pauses | timestamp ±2s + description |
| **2 Flow vibe** | does it *flow nicely* — do switches feel intentional, do sections breathe, does attention hold | verdict `FLOWS` / bullets per jarring moment |
| **3 Critic (peer review / EBI)** | did the reading *land*? per-section ratings, granular feedback, advice, "even better if…" | 0–10 ratings + ≤2 suggestions per pass |
| **4 Technical ear** | loudness consistency, harshness, noise, room-match between sources — qualitative partner to the engine's numbers | observations; disagreement with engine = the finding |

Modes 1–2 = defect pass (fix list). Mode 3 = the product-as-critic: treat the model
as a reviewer who did NOT see the storyboard, rates sections cold, and is asked
explicitly for advice. Mode 4 = supplements `ebur128`/silence data, never replaces it.

## How to run

```
cd Downloads/yt/baumer
python3 tools/listen.py cut <start_s> <dur_s> <name>   # 40–70s clips from the mix
python3 tools/listen.py ask <name> ["custom question"] # one pass
python3 tools/listen.py ask-all                        # standard prompt over all clips
```

- **Providers, in cost order** (wired in `listen.py`, auto-fallback):
  1. **Gemini flash-lite free tier — $0.00/pass** (key: `audition/.env GEMINI_API_KEY`)
  2. `qwen3.8-omni-flash` on the Alibaba gateway — ~$0.0005/pass ($0.0038/hr @7 tok/s)
  3. `gpt-audio-mini` OpenRouter — $0.003/pass measured (wired only as reference; not used)
  Never pay for a listener when a free tier answers the question.
- **Clip discipline:** cut on block boundaries (use `production_sheet.built.json`
  timeline); 40–70s per clip; every prompt MUST include the excerpt-edge rule
  (audio stopping at the clip's first/last seconds is expected — otherwise the
  model reports clip edges as defects, every time).
- **Timestamps:** relative to clip → add the clip's start offset when triaging.
- **Triage rule:** a flag is actionable only if (a) flow-level per owner spec AND
  (b) corroborated by timeline/silence maps. Transcript-level claims → discard.
  Room-color shifts at voice switches → report to owner, do not auto-fix (two
  sources will always differ in timbre; model is inconsistent about this).
- **Batch discipline:** collect flags → one sheet edit → **one render** → re-listen
  only the changed zones. Renders are never sprinkled.

## Prompt templates (one mode per pass — models dilute with mixed questions)

**Flow (modes 1+2, the standard FLAW_PROMPT in listen.py):**
> Listen for FLOW only. Does this excerpt flow nicely? Report ONLY obviously
> jarring moments with mm:ss: speech interrupted / dead pause · jarring volume
> or room jump · anything that briefly confuses the ear. Ignore minor word-boundary
> and excerpt-edge details. End with FLOWS if it reads naturally.

**Critic (mode 3):** cold reviewer, no storyboard:
> You are a cold reviewer of a produced teaching-audio (bells mark sections, two
> speakers alternate). Rate each section you hear 0–10 on: (a) clarity of the
> pairing, (b) breath/pacing, (c) legibility of speaker changes. Then: did the
> piece communicate its structure without any page? Name the ONE change that
> would most improve it. Give at most two "even better if…" suggestions.

**Technical (mode 4):**
> Focus on sound quality only: loudness consistency across voices, harshness,
> noise floors, any click/rumble. Do not comment on content or flow.

## Calibration — what omni is good/bad at (from our rounds, 2026-10-26)

- **Good:** dead-pause detection, bell-fatigue notes, order confusion, overall
  vibe verdict, flagging real word-release chops when they exist (b05 "sa…" was
  real — silence maps under-detected a sibilant).
- **Unreliable:** ±1–2s timestamps; room-color shifts (flags them as "jumps" in
  one prompt, calls them "expected" in another); invented cuts at quiet zones.
- **Rules that came out of this:** excerpt-edge disclaimer always; one mode per
  pass; never accept a text claim without map corroboration; two disagreeing
  passes on the same clip = unstable, prefer engine evidence.

## Where this sits in the acceptance flow

```
P0 (deterministic, tools/p0_check.py — order/edges/invariants/airs/levels)
  → machine listens (modes 1–2 fix rounds, mode 3 verdict, mode 4 spot-check)
    → OWNER cold listen = final word (never replaced by the model)
```

The machine pre-selects what the owner's ear spends attention on. Owner spec
overrides model opinions; model opinions never override the transcript.
