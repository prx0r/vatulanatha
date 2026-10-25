# SPEAKERS — the seats (port of analayo SPEAKER-RULES + our 15-VOICE-GRAMMAR)

## Seats
1. **BAUMER (archive)** — her audio, untouched: readings AND explanations.
   Owns ALL Sanskrit spoken aloud (her sūtra/commentary reads). Never written,
   never re-ordered inside a clip. Cuts only at unit boundaries (sentence edges).
2. **PLAIN (key)** — spoken gloss. Generated ONLY by `build/fish_filter_vatula.py`
   over key_v2/key_v1. No free text, ever; edits go in the KEY, never the output
   (07 ownership). ASCII letters only; diacritics live on TEXT cards only.
3. **HUMAN (owner)** — section QUESTIONS (the spine) + rare marked bridges.
   The only seat that originates sentences; each provenance-marked in the beat.
   Essay-0 question lines live here.
4. **PENDING seats** (per 15, activate when audio lands):
   READER = Sanderson (`supplements/sanderson-*`, I ✓ local) ·
   MASTER = Lakshmanjoo (Secret Supreme $0 checkout — owner).
   Same archive rules as Baumer.
5. Sanskrit ON-SCREEN (card) is not a seat — text field, IAST allowed (07 Test-1
   exception: on-screen-only field).

## Beat gospel (locked, 17)
`[QUESTION → 2-breath pause] → [TEXT VERBATIM] → [PLAIN ENGLISH] → [AUDIO speaker]`
Same order in A, B, C. Never reorder.

## TTS
Fish voice pending owner credit-confirm (Guyzo `8ec9973300874562962bbcb300f82213`
per CUT-QUEUE notes) — until then PLAIN lines are build artifacts only, spoken
tracks at S7.

## Output files (beats)
`build/seg{1..5}_beats.json` — question + text + plain + audio windows + provenance.
