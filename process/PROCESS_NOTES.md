# PROCESS NOTES — 13 Vātūlanātha lectures → "What is realisation?"
Living handover doc (our analogue of analayo's 33-sermons build). Written as we go,
2026-10-25. Update this after every stage; keep the correction log honest.

## 0. Starting state
- **Source:** 16 mp3s in this repo root — 13 sūtra lectures (117 min) + 3 mangala/intro/
  recitation (18 min), channel `@bettinasharadabaumer174`, Vātūlanātha Sūtras 2021.
  `.gitignore`: mp3s local-only (as in analayo until they pushed theirs).
- **Transcripts:** 8 had YT caption tracks (srt + cues, panel endpoint) · 8 had **zero
  tracks, not even ASR** → Cloudflare whisper-large-v3-turbo queue (`vat_cf.log`,
  73 min audio, ~10 min wall) → `transcripts/vat_cf_*.json` · readable all 13 in
  `vat-text/*.txt` (timestamped lines).
- **Primary text:** Muktabodha e-text (KSTS 1923, Anantaśaktipāda vṛtti) at
  `patalacheckpoints/data/corpus/sources/vatulanathasutra/vatulanathasutra.txt`.
- **Prior artifacts:** `VAT-ANALYSIS.md` (8-sūtra gold extraction), `GRACE-ASSEMBLY.md`
  (film frame), `shaktipata_grace_spectrum_pack.zip` (rendered animation, elsewhere).
- **Models pulled:** `../analayo-nibbana` (process/00–11, math, stickiness, core v4),
  `../tantraessays` (FORMULA A⊂B⊂C, PROCESS_NOTES, trika_key 46, excavation schema).

## 1. Decompile — voice-role marking (the load-bearing step)
- Regex on quote/end-markers **FAILED** (8/8 mismatched — ASR drops or garbles "quote",
  nested quotes, unclosed). Lesson: hand-annotate from full transcript reads, use regex
  only as candidate-suggester.
- Output: `decompile/vatNN.decompile.json` ×13 — `text_read` vs `explanation` spans,
  confidence + `needs_earcheck` (17 spans flagged). Payload density measured:
  **she reads the source 24–71% of every lecture** (that's the primary-text layer
  for free — her voice reading the vṛtti, analogous to Analayo reading Nanananda).
- Timebases: CF seconds == srt seconds == mp3 seconds. No anchor maps needed
  (analayo's YT-only problem doesn't exist here).

## 2. Sanskrit source segmentation
- 13 verse anchors content-matched (wrapped lines `…praveśa / ḥ || 3 ||`, split markers
  `|| 2 / ||`, gloss-endings filtered by `arthaḥ|saṃbandhaḥ|bhavatīti`, editorial
  brackets `[cchuritā yu]` kept as-is) → `text/vatula_sNN.txt` + `text/sutra_verses.txt`.
- **Sanskrit never comes from whisper** (confirmed needed: ASR gives `google`=guru,
  `maternati`, `france`, doubled `boards boards`).

## 3. Keys
- `build/key_v1.json` (49 draft maps) → merged onto `tantraessays/plain_english/trika_key.json`
  (46 owner-vetted) → **`build/key_v2.json` (92)** + `build/card_lines.json` (13 card
  renderings) + `build/loanwords_v1.json` (23). Status: key_v2 = proposal until owner signs.

## 4. Excavations (schema: `excavations/_SCHEMA.md`, +`layer` field)
- Units = idea-units, quote must be verbatim substring of `vat-text/*.txt` after
  timestamp-strip + whitespace-normalize. Verification discipline caught, in order:
  missing commas (`Brahman, emerges`), ASR duplications (`two boards boards`),
  misremembered words (`sometime`→`anytime`). **Every unit passes mechanically or
  it doesn't ship.**
- Grade rhythm: grace-heavy five files ran 3.2 A/file; remaining 8 must average ≤1.5
  → projected global **≈27 A** (band per tantraessays pyramid: A small, B larger).
- **Status: 5/13 done — 16A / 22B** (vat1, vat3, vat8, vat10, vat12), 4 commits.

## 5. FINDING THE QUESTION (the emergence moment — why this doc exists)
Owner's test, borrowed from the nibbana build: *the intro question must be what the
33 sermons are actually ON* ("What is Nibbana?" works because they're on nibbana).
So the question is **measured, not assigned**:

| vocabulary (all 13 transcripts) | hits | spread |
|---|---|---|
| attainment / resting-in / own-being / establishment | **42** | every lecture |
| true nature / own nature / svarūpa | **23** | peaks sūtra 1/2/13 |
| guru / transmission | 15 | |
| spontaneous / not-by-will / causeless | 13 | |
| sudden / sahasā / unexpected | 13 | **0 in sūtras 4–12** |
| grace / śaktipāta | 12 | partial thread |
| enlightenment | 10 | |
| recognition | 2 | wrong corpus (that's PH) |

- ❌ **"What is grace?"** — mechanism *inside* the series (12 hits), shoehorns sūtra
  4/7/9/11. **Reassigned:** grace = our separate commentary film (TĀ ch13 + LOGICVID
  thesis + her clips as evidence) — commentary asks its own question; no collision.
- ❌ **"What is sudden enlightenment?"** — the playlist title, but the word **dies for
  nine straight lectures**. A running question can't vanish mid-series.
- ✅ **"What is realisation?"** — 65 combined hits, present in every lecture, and the
  13 sūtras are already its aspects: what it is (1–2) → where it lives, the between
  (3–6) → how it flows, speech & senses (7–11) → what it does to ethics & death (12)
  → what it lands as, wonder-silence (13). One-sentence answer already A-graded:
  *"attainment does not mean to get something which we do not have — it means to
  become what we truly are"* (vat1-05).

## 6. Beat grammar (locked: `process/12-QUESTION-DEPTH.md`)
`[question line] → [pause = 2 breaths = recall window] → [A-clip answers]` at each
A⊂B⊂C depth; question = HUMAN voice, never Fish. Science: testing/generation +
retrieval-cue + spaced revisiting (analayo 11-STICKINESS). *Update pending:* recorded
three provisional questions there — corpus question now measured (§5), refresh that doc.

## 7. Order: what emerges vs what is built
- **Her order is the sort key at every scale** (analayo 10-MATHEMATICS invariant 1;
  the text has authorial order — sūtra 1 contains all, 13 returns to 1, her words in
  vat1-08/vat13). **C-version = her order**, untouched minus namaskar/thank-you/head-silence.
- **A/B versions are BUILT explanations** (nibbana §1–6 analogue): arc slots like
  ①open ②what-it-is ③problem ④mechanism ⑤condition ⑥close — units *assigned* to
  slots at SPINE time; units fitting no slot = C-texture, not argument. Her order
  governs only *within* a slot.

## 8. Structure verdict — PENDING clustering (correction log)
- ❌ pre-measurement: "3 essays (GRACE/BETWEEN/SPEECH)" — hypothesis made before the
  keyword data existed; recorded here so nobody rebuilds on it blindly.
- Current read: corpus product ≈ **ONE built explanation of "What is realisation?"**
  (A/B/C depths) + **the GRACE commentary film** as product 2. Final call after:
  all 13 excavated → `excavations/CATALOGUE.md` (topics→uids) → cluster by A-density
  → **convergence test** (do topic buckets independently land where A-units landed?
  "two dissections, one elephant") → SPINE.md written from the winning clusters.

## 9. Repro / status / gaps
```bash
# unit count + grades
grep -c '^### ' excavations/*.md; grep -ho '\[A\]\|\[B\]' excavations/vat*.md | sort | uniq -c
# quotes verify (rerun each build; see git history for the verifier snippet)
# durations
ffprobe -v error -show_entries format=duration -of csv=p=0 <mp3>
```
- **Done:** inputs, decompile ×13, Sanskrit ×13, key_v2 draft, FORMULA, question rule,
  question measurement, excavations 5/13, supplements (Wallis/Sarvapriyananda/Sanderson
  batch), **Secret Supreme text landed** (`supplements/lakshmanjoo/`: OCR txt 43k words
  + 172p PDF — book = edited form OF the 1971 audio recordings, chapter-aligned, so it
  serves as the transcript/index for the $0 audio when it arrives).
- **S2 DONE** (convergence PASSED, 2 logged review rounds → 20 overrides total).
- **S3 DONE:** `SPINE.md` — 5 standalone-clarity questions, fundamental progression,
  anchors, sūtra-order; standalone-clarity + fundamental-progression laws locked.
- **S4 (essays/compressed answers):** pattern locked (Q → TEXT → PLAIN → AUDIO per
  question); **master opener auditioned-pending owner** (`build/essay0_audition/`).
- **S5 DONE:** Russian-doll manifests ×5 sections (append-only verified, her-order);
  **KNOWN: B-superset overrun 86m vs FORMULA 20–40m → depth-selection at flow-read**
  (documented in manifests/README). A total 17.8m ✓ in band.
- **S6 DONE:** gospel beats `build/seg{1..5}_beats.json` (101 beats, resolved windows);
  filter `fish_filter_vatula.py` deterministic (sha256:2505ed9050b7dc53); plain 13/13.
- **S7 PREP DONE:** `SPEAKERS.md` (5 seats), `process/verify.sh` **ALL GATES PASS**
  (G1 totals 96/85.9m · G5 provenance 96/96 · G6 TTS clean · hash · files);
  `tools/render_vatula.py` + **A-previews rendered**: S1 2.3m · S2 4.6m · S3 9.2m ·
  S4 1.8m · S5 4.1m (~22m with beds; content 17.8m in band).

**Correction log (2026-10-25 evening):**
- B-as-superset was the wrong construction direction (86m — owner: "B is way too
  long"). New law: **essay 0 first, build outward** (see 17 BUILD ORDER LAW).
  Supersets are only raw pools for selection, never ship artifacts.
- Essay 0 upgraded from raw audition windows to BUILT form
  (`build/essay0/essay0_{1,2,3}.mp3`, question→pause→plain→answer, 25–30s).

- **CROSS-PROJECT LAYER (new):** `~/Downloads/yt/corpus/` — unified unit DB
  (4 axes: TEXT × TOPIC × GRADE × QUESTION). 242 units live (vatula 96 +
  tantraessays 146), cross-text compile demo works (death-rebirth returns
  vatula + dyczkowski in one query). Embeddings = phase 2 (needs local model).
  Every future port loads into it — see corpus/UNIFIED-SCHEMA.md.

**THE GOAL (owner, 2026-10-25): get the Bäumer VIDEO fully done and polished.**
Everything below serves that; embeddings/cross-project growth parked until then.

**FINISHED STATE (autonomous run complete, 2026-10-25):**
- CANON locked in every doc (0=spine questions · A=expansion=S*_A built+rendered ·
  B=+depth **SELECTED 34.6m in band, G10 PASS** · C=+texture rule+manifests ✓)
- Spine-read artifact: `build/essay0/spine_read.json` + `spine_preview.mp3` (39s,
  bells + 5 question slots silent until TTS)
- Section openers cut: `opener_S2..S5.mp3` (formula picks: vat4-03, vat8-01,
  vat10-07, vat13-06) + beat1 sample `essay0_1.mp3`
- Machinery done: interlinear cards, plain filter (deterministic), manifests
  (A/B ship-lists, C rule), B-SELECTION hold-up log, verify.sh G0–G12 green
- **ALL GATES PASS in dev mode.**

**OWNER-ONLY remaining (everything else is built):**
1. Ear: listen `spine_preview.mp3` + `essay0_listen_all.mp3` + `opener_S*.mp3`
   → approve/override picks → write `build/essay0_lock.json` (unblocks --ship).
2. TTS credits confirm (Guyzo) → fill question/plain slots → re-render.
3. G8 listen pass on A/B masters → then full assembly (0→A→B→C + bells).
4. Upload package (titles/credits) — final step.


## 10. STANDARD (owner, 2026-10-25) — record this
- **The formula (owner, verbatim):** *audio of a genius talking about a text —
  using their voice as the excuse to finish analyzing a tough text.* Dependency runs
  both ways: text makes the audio citable/scholarly; the genius voice makes the hard
  text ingestible. Grammar is text-agnostic → every text x voice pair = next project.
- **Bäumer = the host series** (complete on disk): PH 12/12 (recognition = next
  project after Vātūlanātha), Vātūlanātha 13+3 (current), Spanda 16, Śivastotrāvalī 12,
  VBT 16, Parātrīśikā 10; Śiva Sūtras 14 on R2. Text shelf per series tracked in 14.
- One project = **one primary source, covered completely** (33-sermons standard:
  the goal was covering the sermons, not mining clips). Our project's primary source
  = the Vātūlanāthasūtra + vṛtti → goal: FULL coverage (all 13, nothing missed —
  run the coverage-audit: every decompile span has a unit or an explicit C-mark).
- Same grammar everywhere → remixable later (voice grammar 15 + FORMULA + key
  standard carry across projects: future projects = Secret Supreme own-series,
  Tantrāloka, PH…).
- Supplements (Lakshmanjoo/Sanderson/Wallis) stay OUTSIDE the Vātūlanātha coverage
  ledger — they feed the overlap-map for multi-voice assembly, they don't excuse
  coverage gaps in the primary source.

## 9d. THE JOURNEY TO THE FIVE QUESTIONS (full chain, 2026-10-25)

1. **Measurement** (§5): keyword counts across all 13 transcripts — the corpus
   answers "What is realisation?" (65 hits, every lecture); grace/sudden were
   measured as sub-questions, not the master.
2. **First preview (S2 attempt log):** five sections drafted — including the
   rejected **"Where does it happen — what is the between?"**
3. **Correction 1 — standalone-clarity:** "the between" = insider coinage a
   stranger can't parse → S2 became "What is the void full of?" (7d2e9e9).
4. **Correction 2 — fundamental progression:** the five must be the most basic
   progression → S2 swapped to **"What is the self?"** (a910174); order locked:
   is → self → how → does → fruit.
5. **Correction 3 — cutting audit:** sharpened variants tested; two failed
   standalone: "Where do you end?" (vague, no object), "Why can't you make it
   happen?" (make WHAT? — pronoun + objectless verb). Owner's fix established
   the **explicit-object rule**: "Why can't you force **realisation**?"
6. **Mechanization:** `process/validate_questions.py` → verify.sh **G0**
   (interrogative · ≤9 words · explicit content noun · no unresolved pronouns).
   Rejections reproduce mechanically; final five = 5/5 PASS.
7. **Final set locked** (SPINE.md) + **3 validated variants per row** added so
   the owner picks the sharpest wording of each (menu: SPINE.md PICK matrix).

Binding rules born on this road: standalone-clarity (law), fundamental
progression (law), explicit-object (sharpening), G0 gate (mechanical).

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


---

## 2026-10-26 — TWO-COMPILATION LAW (ported from `prx0r/shiva-sutras` naming lock d5cdc3b)

- **STANDARD COMPILATION** = the text's own structure leads: every unit in the
  text's order, uniform block pattern, no reordering/selectivity/argument.
  The fidelity object. *This repo:* the dual reading (13 sūtras in order,
  B-read → H-translation each; manifest_v2 + storyboard_v2).
- **CUSTOM COMPILATION** = our spine & cutting: the five questions, A/B/C
  layers; selection and order ours. *This repo:* the essays (CANON).
- **Law of the split:** nothing composed for custom enters standard; nothing
  in standard is cut to flatter custom. Standard proves we heard the text;
  custom proves we understood it.
- **STANDARD FIRST — owner rule.** The standard pass is where the beautiful
  structured data comes from: stamped units, windows, transcripts, coverage
  ledger = the substrate every custom cut draws on (selection stays cheap and
  provable). Plus credibility: the remix is trusted because the complete pass
  sits underneath. Standard first, custom second, never the reverse.
- Full law: `process/README.md` § TWO COMPILATIONS. Apparatus reference:
  `prx0r/shiva-sutras` `process/00–10` (+ BUILD_ENGINE.md).
