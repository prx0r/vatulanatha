# ESSAY 0 — the micro-session, written whole (2026-10-25)

One unit: **question → pause → text (screen) → plain answer (spoken) → her voice lands it.**
Written so it reads complete on the page — audio slots fill when TTS lands (credits
pending), her clip plays always. Plain answers are HUMAN-composed to complete
"Realisation is ___", each sentence backed by the verbatim quoted underneath
(provenance: human-line + archive-quote; 07 rules: plain words, no jargon).

---

## Candidate 1 — unfoldment  →  `essay0_1.mp3` (30s)

> **What is realisation?**
> *(2 breaths — 3.0s)*
>
> **ON SCREEN (TEXT):** "The real nature is acquired by the firm stay in the pre-eminent sahasa." — Vātūlanāthasūtra 1, Kaul tr. 1923
>
> **SPOKEN (PLAIN):** "Realisation is not something you acquire. It is the unfolding of what you already are — becoming what you truly are."
>
> **HER VOICE lands it (clip, 8:54–9:14):**
> "…attainment means to become what we truly are… **the definition of it is the unfoldment of our true being, of our true nature.**"

Backing verbatim: vat1 (decompile read/explain) — quote verified.

---

## Candidate 2 — resting  →  `essay0_2.mp3` (25s)  *[shortest = purest gold]*

> **What is realisation?**
> *(2 breaths — 3.0s)*
>
> **ON SCREEN (TEXT):** "Permanence of the immersion in the real self takes place for ever by the full development of the four deities." — Vātūlanāthasūtra 9, Kaul tr.
>
> **SPOKEN (PLAIN):** "Realisation is a state of resting in your own being."
>
> **HER VOICE lands it (clip, 1:40–1:55):**
> "**what we are all aiming at is a state of resting in one's own being**"

Backing verbatim: vat9-02 (A) — quote verified.

---

## Candidate 3 — Abhinavagupta through her  →  `essay0_3.mp3` (30s)

> **What is realisation?**
> *(2 breaths — 3.0s)*
>
> **ON SCREEN (TEXT):** "The real nature is acquired…" (sūtra 1, Kaul) + card: *Abhinavagupta's definition — "the unfolding of true nature"*
>
> **SPOKEN (PLAIN):** "Abhinavagupta gives the briefest definition of liberation: the unfolding, the revelation, the expansion of your true nature."
>
> **HER VOICE lands it (clip, 7:50–8:10):**
> "Abhinavagupta gives the briefest definition of liberation… **it is the unfolding of … to nature — this unfolding or revelation or expansion of the true nature**" *(ASR rough middle — final wording ear-checked against audio)*

Backing verbatim: vat1-09 context (word-analysis; Abhinavagupta's definition).

---

## Lock procedure
1. Owner listens to the three `essay0_*.mp3` **while reading this page** (the written
   form is the session; the audio is its rhythm).
2. Pick (or name a mix — e.g. 3's master-quote into 1's her-voice definition).
3. Write `build/essay0_lock.json`: `{"pick": "1|2|3|mix:...", "plain": "<final spoken line>", "text": "<final screen line>", "window": [s,e] or list}`
4. verify.sh G12 switches to LOCKED; --ship unblocks this gate; the locked plain
   line becomes the S1 section-opener plain (and the model for sections 2–5's
   micro-sessions, same pattern: question → text → plain → archive).
