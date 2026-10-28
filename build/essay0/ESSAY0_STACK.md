# ESSAY-0 STACK v2 — Hareesh-spoken trusted tier (2026-10-28)

Re-stacks the five spine cells on `build/template_13.json`. Trust order
(ported from prx0r/shiva-sutras STANDARD §0, owner-locked): **text >
Hareesh (spoken, archive verbatim) > Kaul 1923 (PD check) > Baumer (voice).**

## Cell order (fixed — supersedes the old Q→S→T→P→A stack)

1. **QUESTION** — HUMAN/TTS (spine wording, locked)
2. **SANSKRIT** — card, screen: `sanskrit_exact` (corpus KSTS 1923)
3. **HAREESH** — his archive audio reads the sūtra (window in
   `template_13.hareesh_window_s`, dual-reading provenance); his words +
   Kaul's line as the screen interlinear beneath the Sanskrit
4. **PLAIN** — Fish speaks `plain` (= deterministic filter of his spoken
   wording, `build/plain_hareesh_v1.json`)
5. **BÄUMER** — her A-grade answer clip (≤25s, completes the question)

Nothing composed; every tier traceable to template row or archive window.

## The five cells

### 1 · What is realisation? — sūtra 1
- **SANSKRIT:** `mahāsāhasavṛttyā svarūpalābhaḥ`
- **HAREESH (spoken):** "through the activity of the great spontaneous immediacy one discovers one's true nature"
- **KAUL 1923 (screen check):** "The real nature is acquired by the firm stay in the pre-eminent sahasa."
- **PLAIN:** "through the activity of the great spontaneous immediacy one discovers one's true nature" *(honest no-op — already plain)*
- **BÄUMER:** vat1-05 window 526–552 — "attainment means to become what we truly are… the definition of it is the unfoldment of our true being"

### 2 · What is the self? — sūtra 4
- **SANSKRIT:** `yugmagrāsānniravakāśasaṃvinniṣṭhā`
- **HAREESH (spoken):** "through devouring the pair there is abiding in continuous occasionless consciousness"
- **KAUL:** "The firm stay in the universal consciousness is brought about by the destruction of the couple."
- **PLAIN:** "through devouring the pair there is abiding in continuous occasionless consciousness" *(no-op)*
- **BÄUMER:** vat4-03 @4:59 — "the object of experience is ever-present in the experiencing subject… and the subject is ever-present in the object"

### 3 · How does realisation happen? — sūtra 8
- **SANSKRIT:** `rasatritayāsvādanenānicchocchalitaṃ vigatabandhaṃ paraṃ brahma`
- **HAREESH (spoken):** "by savoring the three flavors the Supreme absolute utterly free surges up spontaneously"
- **KAUL:** "On the enjoyment of the triple happiness, the unfettered supreme Brahman of the involuntary and sudden appearance (comes to revelation)."
- **PLAIN:** "by savoring the three flavors the Supreme absolute utterly free surges up spontaneously" *(no-op)*
- **BÄUMER:** vat8-01 @0:52 — "happen spontaneously by an inner inspirational impulse"

### 4 · What does realisation do to experience? — sūtra 10
- **SANSKRIT:** `dvādaśavāhodayena mahāmarīcivikāsaḥ`
- **HAREESH (spoken):** "through the arising of the flow of the twelve there is the expansion of the great rays of consciousness"
- **KAUL:** "The play of the big rays follows the emanation of the twelve currents."
- **PLAIN:** "through the arising of the flow of the twelve there is the expansion of the great rays of consciousness" *(no-op)*
- **BÄUMER:** vat10-07 @6:15 — "his divinized senses attain the state of pure consciousness which radiates throughout the universe"

### 5 · What is the fruit of realisation? — sūtra 13
- **SANSKRIT:** `akathanakathābalena mahāvismayamudrā- prāptyā khasvaratā`
- **HAREESH (spoken):** "through the power of the inexpressible oral teaching there is the discovery of the Seal of great Wonder through that the Resonance of the Void is known"
- **KAUL:** "The attainment of the unity takes place, through the acquisition of the mudra of great wonderment, by virtue of the concentration on the real nature."
- **PLAIN:** "through the power of the inexpressible oral teaching there is the discovery of the Seal of great Wonder through that the Resonance of the Void is known" *(no-op)*
- **BÄUMER:** vat13-06 @13:49 — "All what I feel now, I was already feeling that"

## What changed vs stack v1
- Translation tier: Baumer's spoken renders → **Hareesh's spoken renders**
  (objective modern translator; her voice moves to the answer seat only)
- Kaul demoted from card-primary to screen check (PD, archaic diction)
- Plain regenerates from Hareesh (`plain_hareesh_v1.json`, hash-pinned);
  old `plain_sutras_v1.json` (filter of Kaul) stays for the standard line
- Baumer clips unchanged (A-grade, flow-tested seed on cell 1)

## Still open
- Owner ear on the new stack (listen: Hareesh audio from dual reading
  markers + Baumer clips — the mp3 concat needs TTS for question+plain)
- `build/essay0_lock.json` still pending — lock picks the STACK VERSION
  (v2 = hareesh-spoken) not just the answer clip
- ESSAY0-FORMULA step 3 wording update ("lecturer > critical" →
  "critical/spoken > lecturer-as-voice") — owner sign

---

## BUILD RECORD — essay0_full_v2.mp3 (2026-10-28, DONE by rule)

Rendered: **251.3s · −18.2 LUFS · −1.7 dBTP · p0 PASS · 2 machine passes 0 blocking**
(ledger: `DONE.md` § essay0 · listens: `process/20-LISTEN-LOG.md` §4)

- Sheet: `build/essay0/production_sheet.json` (sheet.py render|p0_check essay0 mode)
- Hareesh audio: dual-reading H windows (webm), reasons inherited from manifest_v2
- Baumer answers: cell1 = G12 gold-dust 526–552 (Sutra_1) · cells 2–5 = excavation
  units vat4-03 / vat8-01 / vat10-07 / vat13-06 (b04 head widened for snap lead)
- Questions: Fish TTS "Narrator" `0327fdb5…` (provisional HUMAN seat — owner may
  swap to own voice clone later); task ids q1–q5 in fish tasks 2026-10-28
- Plains: Fish TTS Guyzo `8ec9973…` p1–p5 exist but **render=false** — when
  filter(hareesh)==hareesh the gloss is screen-only (E1 ruling); Guyzo remains
  the PLAIN seat for body beats whose card text ≠ spoken T
- Plain source of truth: `build/plain_hareesh_v1.json` (hash c862a8e8e355ffc4)
- Template: `build/template_13.json` (sanskrit_exact + hareesh_spoken + kaul_1923)
