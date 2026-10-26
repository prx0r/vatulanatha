# 21 — VOICE & SFX APIS (operator notes: ElevenLabs + Fish) (2026-10-26)

Keys: both live in `~/repos/characters/audition/.env` (`ELEVENLABS_API_KEY`,
`FISH_API_KEY`) — never copy keys out of it. Docs distilled from
elevenlabs.io/docs + local `~/characters/docs/fish/` (full Fish docs incl.
openapi.json live there).

## ElevenLabs — the SFX + music machine

### SFX: `POST https://api.elevenlabs.io/v1/sound-generation`
- body: `text` (prompt), `duration_seconds` (0.5–30; omit = auto), `loop`
  (seamless loop for beds), `prompt_influence` (0–1, default 0.3 literal-ish),
  `model_id`: `eleven_text_to_sound_v2` | `_v3`
- header: `xi-api-key: $ELEVENLABS_API_KEY`
- **cost: 40 credits/second** (duration mode) → 10k credits ≈ $1 →
  2s marker ≈ $0.008 · 10s bowl ≈ $0.04 · 30s loop bed ≈ $0.12
- output: `output_format` query (`mp3_44100_128` default; wav needs Pro+)
- prompting vocabulary that works: *impact, whoosh, ambience, one-shot, loop,
  drone, braam* + concrete object language ("small dry temple woodblock, single
  strike, close-mic")

### Music: Eleven Music (API, cookbooks: `/docs/eleven-api/guides/cookbooks/music`)
- text→music, 3s–**5 min**, `model_id: music_v2_5`, inpainting (fix a section),
  **Audio Reference** (≤30s reference upload steers style — route: upload our
  bowls/strike kit → music in *our* sonic identity), commercial-cleared
- billed separately — check elevenlabs.io/pricing/api before long beds

### What we'd generate first (starter batch, ≈$0.10–0.40)
markers (dry tick / warm block / bamboo resonant) · tingsha pair · small gong ·
air-bow for switch pauses · brush-stroke on paper (visual-engine ink foley) ·
seal stamp · one `loop:true` temple-courtyard bed.

## Fish — voices, faces, frames (MCP + REST)

- **Plan: plus · package balance 241,598 credits** (cycle ends 2026-11-14) ·
  TTS ≤15,000 text bytes/call · 1 credit = 1 UTF-8 byte of speech text
- MCP tools (this session): `text_to_speech` (models `s2.1-pro`, **`drama-3`**
  with delivery tags `[pause] [sigh] [whispering] [emphasis] …`), `search_voices`,
  `create_voice_clone` (rights rule applies), `speech_to_text`, asset/image/video
  generation, `get_credit_balance`
- **No SFX endpoint** — Fish is voice/image/video; vocal texture = drama-3 tags
  (use sparingly). SFX = ElevenLabs.
- Known voice: Guyzo `8ec9973300874562962bbcb300f82213` (essay PLAIN seat
  candidate — credits now confirmed available)

## Placement map (which API lands where in our products)

| placement | API |
|---|---|
| marker palette / page-turn foley / air-bow / loop beds | Eleven SFX |
| per-text signature bed, chapter themes | Eleven Music (Audio Reference = our kit) |
| PLAIN gloss + bridges (essay seats) | Fish TTS (drama-3 / designed voice) |
| HUMAN narration voice | Fish clone (owner voice) or Eleven voice design |
| covers, stills, book-stage art | Fish image / wan2.7 on the Alibaba key |

Related: `18-SPACING-AND-SEAMS.md` (where marks sit) · `20-LISTEN-LOG.md`
(how changes are verified) · book stage spec lives in
`~/essay-visual-engine/docs/SPEC-BOOK-STAGE.md` (parked).
