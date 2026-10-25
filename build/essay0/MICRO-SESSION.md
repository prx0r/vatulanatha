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
> **ON SCREEN (TEXT — Sanskrit first):**
> **`mahāsāhasavṛttyā svarūpalābhaḥ`**  ·  Vātūlanātha sūtra 1
> gloss: "by the workings of great sudden-force — one's true nature is attained"
> strip: **`kasyacit kvacit kadācit akasmādeva`** — "to someone, somewhere, sometime, of its own accord" (vṛtti)
>
> **SPOKEN (PLAIN):** "Realisation isn't acquired. It happens — somewhere, sometime, of its own accord: the unfolding of what you already are."
>
> **HER VOICE lands it (clip, 8:54–9:14):**
> "…attainment means to become what we truly are… **the definition of it is the unfoldment of our true being, of our true nature.**"

Backing verbatim: vat1 (decompile read/explain) — quote verified.

---

## Candidate 2 — resting  →  `essay0_2.mp3` (25s)  *[shortest = purest gold]*

> **What is realisation?**
> *(2 breaths — 3.0s)*
>
> **ON SCREEN (TEXT — Sanskrit first):**
> **`sadaiva svaviśrāntyavasthitiḥ`**  ·  Vātūlanātha sūtra 9
> gloss: "for ever, abidance in one's own repose"  (= resting in one's own being)
> strip: `devīcatuṣṭayollāsena` — "by the rejoicing of the four goddesses"
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
> **ON SCREEN (TEXT — Sanskrit first):**
> **`akasmādeva · jhaṭiti · akṛtaka`**  (vṛtti on sūtra 1)
> gloss: "of its own accord · in a flash · the unmade"
> card: `mahāsāhasavṛttyā svarūpalābhaḥ` — the sūtra that "contains the whole teaching" (her claim)
>
> **SPOKEN (PLAIN):** "Abhinavagupta gives the briefest definition of liberation: the unfolding, the revelation, the expansion of your true nature."
>
> **HER VOICE lands it (clip, 7:50–8:10):**
> "Abhinavagupta gives the briefest definition of liberation… **it is the unfolding of … to nature — this unfolding or revelation or expansion of the true nature**" *(ASR rough middle — final wording ear-checked against audio)*

Backing verbatim: vat1-09 context (word-analysis; Abhinavagupta's definition).

---

## Sanskrit-first policy (owner correction, 2026-10-25)
Screen TEXT = the **Sanskrit answer from the text**, English only as gloss beneath.
Kaul's full sentences are reference, not cards. Vocabulary of the answer:
`svarūpalābhaḥ` (attainment of true nature) · `akasmādeva` (of its own accord) ·
`jhaṭiti` (in a flash) · `akṛtaka` (the unmade) · `svaviśrāntyavasthitiḥ` (abiding in one's own repose).

## Why these screen lines (found in the gloss, 2026-10-25)
The full Kaul sentence IS clunky — but the gloss around it carries the famous phrases:
- **"Sahasa literally means an unexpected happening."** (line 706) — the text's own plain-English zinger
- **"waveless, limitless, unlocalised and touchless … somewhere, sometime, unexpectedly"** (778–779) — the attribute-sequence of realisation
- **"quicker than the quick"** (788) — grace at speed
- `mahāsāhasavṛttyā svarūpalābhaḥ` — sūtra 1 = "the whole teaching in a nutshell" (her claim), IAST card

## Lock procedure
1. Owner listens to the three `essay0_*.mp3` **while reading this page** (the written
   form is the session; the audio is its rhythm).
2. Pick (or name a mix — e.g. 3's master-quote into 1's her-voice definition).
3. Write `build/essay0_lock.json`: `{"pick": "1|2|3|mix:...", "plain": "<final spoken line>", "text": "<final screen line>", "window": [s,e] or list}`
4. verify.sh G12 switches to LOCKED; --ship unblocks this gate; the locked plain
   line becomes the S1 section-opener plain (and the model for sections 2–5's
   micro-sessions, same pattern: question → text → plain → archive).
