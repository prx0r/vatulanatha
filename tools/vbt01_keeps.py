# VBT 1 — INTRODUCTION (75.8 min source). Native seconds.
# Structure: welcome/mangala-def -> Sanskrit mangala recitation (D) -> Kshemaraja title
# etymology+verse translation -> why this text / Shaiva Upanishad -> wrong-reasons/selectivity
# -> importance (masters quote it) -> tantra survey (r2) -> experience+knowledge together
# -> Rudrayamala -> revelation as dialogue (Shiva-Shakti, 5 guru relations) -> four stages
# of word -> descent/ascent (meditation = return to paśyantī) -> Tantra-avatāraka ->
# 112 ways / qualified receiver -> upaya/dhyana semantics -> whatever-is-near (Abhinava)
# -> bee simile. Logistics/translation-biblio/program cut.

KEEPS = [
    (82, 130, 1),        # frame: what a mangala sloka is — blessings, hindrances, hints at the text's meaning [SNAP end after "going to follow"]
    (277, 513, 1),       # Kshemaraja: title etymology (bhaya/remover of fear, bhr/fullness) + full verse translation + yogini=Shakti + "it is your own consciousness, the whole text is in the title"
    (513, 676, 1),       # why this text: hidden in manuscripts 100y, Abhinavagupta calls it Shaiva Upanishad; jnana = mystical knowledge [SNAP end after "given to this text"]
    (676, 803, 1),       # wrong reasons: non-traditional teachers, fanciful interpretations, "enlightenment by sneezing"; oral teaching needed for a brief text
    (1202, 1274, 1),     # importance: all great masters quote Vijnana Bhairava with respect for any account of mystical experience
    (1944, 2045, 1),     # experience + textual knowledge must go together; Lakshmanjoo = scholar+mystic+jeevanmukta; Kashmir Shaivism = synthesis [SNAP end after "philosophy"]
    (2071, 2216, 1),     # Rudrayamala: yama = pair Shiva-Shakti; VBT = essence of it; 163 verses; result = union of Shiva and Shakti
    (2231, 2531, 1),     # GOLD revelation as dialogue: 5 guru-disciple relations down to Shiva-Shakti; dynamic non-dualism vs "brick" Brahman; Sadashiva teaches by Q&A; Shakti provokes Shiva out of compassion
    (2548, 2714, 1),     # revelation as descent of word: para / pasyanti / madhyama / vaikhari; poet's flash; vaikhari manifested in body
    (2739, 2848, 1),     # four stages = revelation; oral for centuries, birch bark, printed 1918 [SNAP end after "printed"]
    (2848, 2961, 1),     # GOLD ascent: written word must lead back to source; meditation = return to origin of thought (pasyanti -> para); descending/ascending complementary
    (2968, 3062, 1),     # Tantra-avatāraka: the redactor — not Shakti but the 10th-c teacher speaks; redacted Shiva [SNAP start after "our very own" filler / end after "redacted Shiva"]
    (3138, 3249, 1),     # 112 ways; qualified receiver — purified by descent of shakti, "not anybody who walks into a shop and buys a book"
    (3257, 3521, 1),     # semantics: tantra says upaya not yoga; dhyana introduced by commentator; Netra Tantra definition — supreme self held firm in consciousness [SNAP end after "definition of dhyana"]
    (3564, 3737, 1),     # GOLD Abhinavagupta: accept whatever means is NEAR to you, discard the far-fetched; equality of all gods/mantras (everything is Shiva); nothing excluded — Buddhism, yoga, tantra all present [SNAP end after "occupy us" (ok as-is)]
    (3812, 3859, 1),     # GOLD bee simile: the fragrant flower is enjoyed only by the bee, not the fly — qualification = sense for it; to be a bee and not a fly [SNAP start after stray "says"]
    # ---- rank 2 (budget fillers / drop-first) ----
    (814, 1017, 2),      # Lakshmanjoo as last authoritative master + Lilian Silburn preface story + Swami Triveni pioneer
    (1017, 1202, 2),     # bibliographic: Hindi commentary tradition, KSTS edition, Kshemaraja commentary preserved to v.23 (her discovery of lost-completion fragments)
    (1283, 1595, 2),     # translation survey: Lakshman Joo's two edited versions, her own translation, book logistics, oral-teaching necessity
    (1595, 1935, 2),     # tantra survey: Malini Vijayottara, Netra yoga chapters, Sharda Tilaka, Paratrivika — how the tantras interrelate
    (3084, 3138, 2),     # every translation limits meaning; Sanskrit matters
    (3889, 3973, 2),     # silence rationale: subtle awareness, live with the text for a week
    (4304, 4419, 2),     # recitation tradition: not read but sung; internalize; 163 verses in 8 days
]

MAJOR = [
    (0.0, 42.0, "music", "opening music"),
    (42.0, 82.0, "intro", "retreat welcome: privilege, invited by Swamiji, enlightened yogis"),
    (130.0, 151.0, "logistics", "file distribution — the mangala text in your handouts"),
    (151.0, 277.0, "recitation", "Sanskrit mangala sloka chanted (Kshemaraja's verse)"),
    (803.0, 814.0, "trim", "transition: who has which text"),
    (3737.0, 3812.0, "repetition", "repeats qualification teaching + program lead-in (bee simile kept)"),
    (3859.0, 4304.0, "logistics", "daily program: timetable, meditation slots, hatha yoga, tea, question times"),
    (4419.0, 4556.0, "logistics", "book distribution, photocopies, Hindi translations, close of introduction"),
]

SUMMARY = ("mangala sloka + Sanskrit recitation -> Kshemaraja: title = your own consciousness -> "
           "Shaiva Upanishad / wrong-reasons selectivity -> masters quote it -> experience+knowledge -> "
           "Rudrayamala -> revelation as Shiva-Shakti dialogue -> descent of the word (para-pasyanti-madhama-vaikhari) -> "
           "ascent: meditation returns word to source -> Tantra-avataraka -> 112 ways/qualified receiver -> "
           "whatever practice is near -> bee simile")

SNAPS = [
    (130, "end", "going to follow"),
    (676, "end", "given to this text"),
    (1944, "start", "so experience and textual knowledge"),
    (2045, "end", "philosophy"),
    (2071, "start", "is a group"),        # skip stray lead-in word
    (2548, "start", "explaining revelation"),
    (2968, "start", "about the way they are transmitted"),
    (3062, "end", "redacted Shiva"),
    (3521, "end", "definition of"),
    (3812, "start", "he has a very nice simile"),
    (3973, "end", "24 hours"),
]
