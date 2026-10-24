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
- **Next:** vat13, vat4, vat7, vat2, vat5, vat6, vat9, vat11 (1.5 A/file discipline)
  → CATALOGUE → clustering + convergence → SPINE slots for "What is realisation?"
  → A/B/C manifests → render (analayo settings: loudnorm −16 LUFS, afade 0.15,
  pause-snap, breath 1.5/water 2.5) → verify.sh.
- **Known gaps:** 17 ear-check spans unreviewed · key_v2 unsigned · Grace film's
  narration unwritten (separate track) · mangala chant handling: chanting rule says
  keep/hoist — decide at manifest time · no Fish TTS yet (plain lines written, not
  filtered; confirm credits before TTS).
- **Repo:** git-committed per stage (see log); push target like the others
  (`prx0r/…`) when owner wants it public.

## 10. STANDARD (owner, 2026-10-25) — record this
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
