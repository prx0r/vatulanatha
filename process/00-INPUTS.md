# 00 — INPUTS (Vātūlanātha port)

Per unit (13 sūtras + 3 mangalas):
- [x] MP3 per unit — `Vatulanatha_Sutra_N [id].mp3` + mangalas
- [x] Timestamped transcript — srt for 1,2,5,6,9 + mangalas; CF-whisper json for
      3,4,7,8,10,11,12,13 (`transcripts/vat_cf_*.json`), all readable in `vat-text/`
- [x] QUOTATION marking (teacher reading vs explaining) — `decompile/sutraNN.decompile.json`
      (hand-annotated from full reads; explicit quote/end markers where present;
      `needs_earcheck` lists fuzzy boundaries — 17 spans total)
- [x] Primary text per unit — `text/vatula_sNN.txt` (Sanskrit vṛtti) + `text/sutra_verses.txt`
- [x] Transliteration: IAST on cards/keys; ASCII fold for matching (dual scheme, per 08-PORTING §1)
- [ ] voice-role markers inside CF/srt for reading-vs-explaining at cue granularity —
      approximated by decompile spans; refine during ear-check

Timebases: CF json seconds = mp3 seconds (native). srt = mp3 seconds (YT timedtext,
same base). No anchor map needed (unlike analayo YT-only lectures).
