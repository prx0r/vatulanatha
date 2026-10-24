# text/ — the primary source, all layers

| file | what | source |
|---|---|---|
| `vatula_s01..13.txt` | Sanskrit: each sūtra + Anantaśaktipāda vṛtti, per-sūtra chunks | Muktabodha e-text M00099 (KSTS 1923) via patalacheckpoints corpus |
| `sutra_verses.txt` | the 13 sūtra lines only (card source) | parsed from above |
| **`vatula_ksts1923_en.txt`** | **ENGLISH of sūtra + vṛtti + notes (Kaul Shāstrī 1923, PD)** — "Text Sutra N." + Gloss blocks, all 13 + colophon | archive.org `in.ernet.dli.2015.283842` free OCR |
| `vatula_ksts1923_en_dli2.txt` | second DLI scan (backup/parallel) | archive.org `in.ernet.dli.2015.383593` |

OCR quality: readable, some garbage words (ear-check quotes against the PDF scan
`archive.org/download/in.ernet.dli.2015.283842/2015.283842.The-Vatulanatha.pdf` if critical).

## The three English layers (quote rules)
1. **Kaul 1923** (this file) — PD, clean, quotable verbatim in essay/cards. Archaic diction.
2. **Bäumer's spoken renders** — archive audio only (ASR = garbled; quote from
   `vat-text/` with ear-check, never from ASR for print).
3. **Our `build/card_lines.json`** — plain-English for TTS, key-vetted, one line per sūtra.
