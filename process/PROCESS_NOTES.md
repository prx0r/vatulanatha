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

**Remaining (owner-dependent first):**
1. Ear: essay-0 pick/mix from **`build/essay0/`** → write `build/essay0_lock.json` (unblocks video head).
2. TTS credits confirm (Guyzo voice) → generate question+plain tracks → re-render filled.
3. B depth-selection flow-read **growing outward from the locked essay0** (86m superset → 20–40m ship list; every clip must deepen the essay0 answer).
4. G8 listen pass on previews; then C texture + full assembly.
5. Parked: Secret Supreme $0 checkout; Sanderson batch stopped by owner; baumer
   channel download stopped at 91/147 (resume: download_all.py).

## 9b. HOW THE SANSKRIT-FIRST RULE WAS FOUND (essay-0 screen text, 2026-10-25)

The path, kept honest — three owner rejections in one sitting:
1. **v1 TEXT seat** = Kaul's full 1923 sentence ("The real nature is acquired by the
   firm stay in the pre-eminent sahasa"). Owner: *not catchy, not profound* — an
   old translator's stiff full clause, not a hook.
2. **v2 TEXT seat** = famous phrases mined from the gloss around it ("Sahasa
   literally means an unexpected happening", "waveless, limitless, unlocalised and
   touchless", "quicker than the quick"). Better English — but the owner caught the
   **circularity**: we were quoting Kaul *defining* the Sanskrit word (sāhasa) when
   the card could just SHOW the Sanskrit. *"...whats the sanskrit for that then."*
3. **v3 rule**: for a primary-source essay the screen answer must come from the
   PRIMARY LANGUAGE. Dig the Sanskrit chunks (`text/vatula_s*.txt`) → the answer
   vocabulary fell out of sūtra 1's own vṛtti:
   - `mahāsāhasavṛttyā svarūpalābhaḥ` — sūtra 1: "by the workings of great
     sudden-force, one's true nature is attained" (= her spoken translation)
   - `kasyacit kvacit kadācit akasmādeva` — the vṛtti's grace-formula = the Sanskrit
     behind Kaul's "somewhere, sometime, unexpectedly" (`akasmāt` = without-cause →
     same word as our vat10-03 "without any cause" unit)
   - `jhaṭiti` (in a flash) · `akṛtaka` (the unmade) · `sadaiva svaviśrāntyavasthitiḥ`
     (sūtra 9 = the "resting in one's own being" Sanskrit)

**Reusable lessons:**
- TEXT seat = source language first; English only as gloss beneath. Never a full
  old-translation sentence as the hook.
- Mine the *gloss/commentary around* a sūtra for catchy lines — but quote the TERM,
  not the translator's definition of the term (definitions = circular).
- The text answering its own question lives in ITS OWN words: find the Sanskrit
  (or primary-language) answer before reaching for any English.
- Verification habit kept: every Sanskrit line printed = checked against
  `text/vatula_s*.txt` (corpus Muktabodha), IAST per card rules.

## 9c. ERROR LOG — the composed-gloss leak (three occurrences, owner-caught)

**Pattern:** my own words keep leaking into tiers that must hold only exact text.
1. v1 screen: Kaul's full clunkly sentence promoted as "the hook" (wrong tier use).
2. v2 screen: added strips + composed answer plains ("Realisation isn't acquired…
   unfolding of what you already are" — summary/bloat; rejected).
3. **v4 S-row: wrote a composed MEANING** ("by great sudden-force, one's true
   nature is attained") **next to a translation row that said something clunkier**
   — my gloss posing as the translation, two rows contradicting (owner: "so why is
   that not the translation in essay 0???").

**Root cause:** when a tier needs a meaning I generate one instead of ROUTING to
the tier that already holds it (the translation row) — and I annotate "helpfully".

4. **v5 stack assembly: cross-translation contamination** — translation tier held
   Bäumer's rendering while the plain tier held a Kaul-derived line (the plains
   were pre-baked from `kaul_sutras_en.json`, not from the PICKED T). Two
   different translations of one sūtra stacked (owner caught instantly).

**Rules (now binding):**
- Sanskrit row = phrase + source pointer. **No meanings, ever.** Meaning = TIER B.
- If the exact translation for a pick is weak (Kaul's clunkliness), the fix is to
  choose a BETTER EXISTING exact translation (e.g. Bäumer's own — now T1 default),
  never to compose a fresh gloss.
- Contradiction check before shipping any menu/doc: does every stated meaning come
  from a file? If it exists only in my prose → strip it (git history keeps it).
- **P = filter(CHOSEN T), always** (9c-4): the plain tier is generated FROM the
  picked translation at lock time — never a pre-baked line from a different source.
  `plain_sutras_v1.json` = reference set for Kaul picks only.

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
