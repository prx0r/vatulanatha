# FORMAT REVIEW — the gospel stack, compliance across all beats

Cold audit, 2026-10-25, report-only. Question asked: *is everything
structured as **sanskrit → literal translation → plain english →
archive-voice explanation**, and should it be?*

## Canonical answer: YES — that IS the locked format

| doc | wording |
|---|---|
| `FORMULA.md:35` | Essay-0 7 tests: **question → sanskrit → translation → plain → audio** → stack-read → lock |
| `17-SPINE-WORKFLOW:100` | Beat form: **Q → interlinear (sanskrit+translation on screen) → plain (spoken) → her voice** |
| `ESSAY0-SPINE:8` | 🔊 question → 2 breaths → 📺 **sanskrit + translation (interlinear)** → 🔊 plain → 🎙 Bäumer ≤30s |
| `FORMULA:29` | Sanskrit card lines come from `text/sutra_verses.txt` — **NEVER from whisper** |
| `15-VOICE-GRAMMAR:41` | seats: READER / MASTER / **COMMENTATOR (baumer[, dyczkowski])** — Dyczkowski = declared second commentator |

It is also the traditional order (sūtra line → literal translation →
commentary) and analayo's three-layer (Nanananda-words → plain →
Analayo) with the interlinear card added. **No format change needed.**

## Compliance matrix — all 101 gospel cells (96 units + 5 openers)

| layer | present | notes |
|---|---|---|
| 🔊 question | **101/101** ✓ | provenance = HUMAN/spine (not TTS-composed) |
| 📺 sanskrit | **0/101** ✗ | **THE gap** — verses exist for all 13 sūtras (`sutra_verses.txt`); cells carry no sans field |
| 📺 literal translation | **101/101** ✓ | kaul_sutras_en (OCR-repaired); **wrong-card check: 0 errors** — source index == unit's lecture every time (13 lectures = 13 sūtras, 1:1) |
| 🔊 plain english | **101/101** ✓ | **pure function of the translation**: 13 texts ↔ 13 plains, zero collisions (deterministic gate sha256:2505ed…) |
| 🎙 archive voice | **101/101** ✓ | every unit uid resolves to an excavation with window+mp3; 5 openers carry slot notes |

## Gaps (report-only, queued)

| # | sev | gap |
|---|---|---|
| G-1 | **MEDIUM** | **Sanskrit unwired in every cell.** Fix is mechanical: parse `sutra_verses.txt` (13 lines, keyed by `\|\| N \|\|`), add `sanskrit` field = verse[lecture] to all 96 unit cells + 5 openers. One script; no content decisions. |
| G-2 | MEDIUM | Essay-0 card pool (known 0-1/0-2): only 3 of 5 questions have a sans line; keys misaligned; **T3/P3 pair broken** (P3 ≠ f(T3)). Rebuild as Q1..Q5 → {sans, trans, plain} in one pass. |
| G-3 | note | The 📺 layers are **screen** layers — audio render (render_vatula) rightly skips them; no video pipeline exists yet. Format is defined for the card, wiring is for when video/composite happens. |
| G-4 | note | **Dyczkowski**: correctly declared as second commentator seat, correctly absent from main-essay cells (main walk = Bäumer's own lectures on the text). Supplements (8 indexed lectures) enter later as their own tier — no action now. |
| G-5 | state | question + plain audio = silent slots until TTS (build-state, not format). |

## Verdict
Format = canon, everywhere, correctly ordered; 4 of 5 tiers fully wired
and internally consistent (card→lecture 0 mismatches, plain purity 0
violations). **One real gap: the sanskrit line exists in the corpus but
in no cell** — plus the essay-0 card pool repair. Neither is a
content decision; both are one-script fixes when approved.
