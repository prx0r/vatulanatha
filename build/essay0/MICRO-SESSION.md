# ESSAY 0 — the micro-session, exact stack (v3, 2026-10-25)

Stack law (owner): **Sanskrit exact phrase → exact translation as it is → exact plain
English as generated. No summaries, no strips, no composed sentences.** The answer to
"What is realisation?" in the session = her clip; the three tiers are the interlinear
record under it. Audio form: `essay0_{1,2,3}.mp3` (+ `essay0_listen_all.mp3`).

---

## Candidate 1 — unfoldment → `essay0_1.mp3` (30s)

> **What is realisation?**  *(2 breaths)*

> **SANSKRIT (exact):** `mahāsāhasavṛttyā svarūpalābhaḥ`  ·  Vātūlanātha 1
> **TRANSLATION (Kaul 1923, as it is):** "The real nature is acquired by the firm stay in the pre-eminent sahasa."
> **PLAIN (generated, `plain_sutras_v1`):** "The real nature is acquired by the firm stay in the pre-eminent great intensity."

> **HER VOICE (clip 8:54–9:14):** "…attainment means to become what we truly are…
> **the definition of it is the unfoldment of our true being, of our true nature.**"

---

## Candidate 2 — resting → `essay0_2.mp3` (25s)

> **What is realisation?**  *(2 breaths)*

> **SANSKRIT (exact):** `p. 12) devīcatuṣṭayollāsena sadaiva svaviśrāntyavasthitiḥ`  ·  Vātūlanātha 9
> **TRANSLATION (Kaul 1923, as it is):** "Permanence of the immersion in the real self takes place for ever by the full development of the four deities."
> **PLAIN (generated, `plain_sutras_v1`):** "Permanence of the immersion in the real self takes place for ever by the full development of the four deities."

> **HER VOICE (clip 1:40–1:55):** "**what we are all aiming at is a state of
> resting in one's own being**"

---

## Candidate 3 — the definition through her → `essay0_3.mp3` (30s)

> **What is realisation?**  *(2 breaths)*

> **SANSKRIT (exact):** `mahāsāhasavṛttyā svarūpalābhaḥ`  ·  Vātūlanātha 1
> **TRANSLATION (Kaul 1923, as it is):** "The real nature is acquired by the firm stay in the pre-eminent sahasa."
> **PLAIN (generated, `plain_sutras_v1`):** "The real nature is acquired by the firm stay in the pre-eminent great intensity."

> **HER VOICE (clip 7:50–8:10):** "Abhinavagupta gives the briefest definition of
> liberation… **it is the unfolding … of the true nature**" *(ASR middle — ear-check)*

---

Provenance: SANSKRIT = `text/sutra_verses.txt` (Muktabodha corpus) · TRANSLATION =
`text/kaul_sutras_en.json` (OCR-repaired, KSTS 1923) · PLAIN =
`build/plain_sutras_v1.json` (fish_filter_vatula, sha256:2505ed9050b7dc53) ·
clip quotes = `excavations/vat*.md` (verified). Human-composed answer drafts from
earlier rounds: **rejected as bloat** (kept only in git history).

## Lock
`build/essay0_lock.json` → {"pick": "1|2|3|mix", ...} → verify.sh G12 LOCKED.
