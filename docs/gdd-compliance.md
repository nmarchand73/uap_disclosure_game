# GDD Compliance — UAP Disclosure Game

This document tracks implementation status against the **Game Design Document** (`gdd/GDD_UFO_Disclosure_Game_v2.md`). It is updated when rules or content change.

---

## 1. Rules fully implemented and aligned

| GDD reference | Rule | Implementation |
|---------------|------|----------------|
| **5.1 Setup — Event Cards** | 3 Event Cards per player (mode standard) | `create_game` / `join_game`: 3 event cards drawn from shuffled deck |
| **5.1 Placement** | Each character starts on their starting continent | `_starting_continent_for_character()` in create/join; `characters.json` has `starting_continents` per character |
| **5.2 Phase 1** | Roll dice 1–6, move that many continents | `roll_dice()` 1–6; move use case advances by continents in `CONTINENTS_MOVEMENT_ORDER` |
| **5.2 Phase 2** | Event check: match → Phase 3; else draw Event Card if available, then end turn | Move: match → spin; no match → draw 1 from deck to player if deck non-empty, then end turn |
| **5.2 Phase 3 — Spinner** | Government / Military / Scientific / Obstacle / Special | `rules.spin_result()`; wrong authority → +1 move bonus next turn; special → resolve event |
| **7.3 Spinner probabilities** | ~20% Gov, ~20% Mil, ~20% Sci, ~25% Obstacle, ~15% Special | `rules.py`: PROB_* = 0.20, 0.20, 0.20, 0.25, 0.15 |
| **7.2 Disclosure Path** | 3 tokens per authority; 3 authorities = Full Disclosure = win | `DisclosurePath` gov/mil/sci; `has_full_disclosure()` when all ≥ 3 |
| **5.2 Phase 4** | 3 questions in sequence; all correct → +1 token; any wrong → exit path, end turn | `disclosure_question_index` 0→1→2; three trivia draws; correct on 3rd adds token |
| **5.2 Phase 3 — Wrong authority** | Bonus mineur ou tour neutre | `Player.next_move_bonus = 1` (applied on next move) |
| **5.2 Phase 5 — Obstacles** | Skeptic: wrong → lose next turn. Debunker: wrong → -1 move next turn; correct → +1 token | `skip_next_turn`, `movement_penalty`; debunker correct gives token via `_add_token_any_authority` |
| **8.6 Special sector** | Whistleblower, MIB, Hoax, Mass Sighting | `_resolve_special()`: Whistleblower +1 token; MIB skip next turn; Hoax swap event card; Mass Sighting +1 token all on continent |
| **7.1 Continents** | 6 continents, adjacency for movement | `Continent` enum; `CONTINENTS_MOVEMENT_ORDER` for wrap-around movement |
| **4 — Characters** | 6 types × 2 variants, starting continents | `characters.json`: all 6 (Journalist, Pilot, Investigator, Experiencer, Abductee, Police Officer) with variants; Lobby offers all + variant picker |
| **7.1 Hotspots** | Zone 51/Roswell, Rendlesham, Ruwa, Hessdalen | `hotspots.py` + move/spin: zone51 +1 gov/mil; Rendlesham debunker immunity; Ruwa +1 scientific; Hessdalen next-event preview |
| **8.2/8.3 Deduction** | History Deck — Déduction cards, Mixed mode | `list_deduction`/`get_deduction`; `deduction.json`; 50% trivia / 50% deduction in Phase 4 when deck non-empty |
| **6.2 Coop mode** | Shared path, team win | `game.mode = "coop"`; `coop_shared_path` / `has_coop_win` in DTO; Lobby mode selector |
| **6.3 Skill token** | One-time use ability | `use_skill` action: +1 token any authority; `skill_used` on Player; button in Game UI when movement/spinner |

---

## 2. Intentional simplifications (digital adaptation)

| GDD rule | Current behaviour | Reason |
|----------|-------------------|--------|
| **5.2 Phase 4 — History Cards** | GDD: 3 questions in sequence; all correct → +1 token. Wrong at any step → exit path, end turn. | **1 question per spin**; correct → +1 token. Faster sessions, same tension. |
| **Wrong authority on spinner** | GDD: “Bonus mineur ou tour neutre”. | We **end turn** (no bonus). Simpler; can add later. |
| **8.4 Skeptic fail** | GDD: “Perdre son prochain tour”. | We **end current turn** only (no “skip next turn” state). Acceptable for MVP. |
| **8.5 Debunker fail** | GDD: “-1 case de déplacement au prochain tour”. | We **end turn** only (no movement penalty next turn). Can add `movement_penalty` later. |
| **8.6 Special sector (15%)** | GDD: Mass Sighting, Whistleblower, MIB, Hoax. | Spinner “special” → **end turn** (no special events yet). Placeholder for future content. |
| **6.x Modes** | GDD: Coop, Asymmetric, Trivia/Deduction/Mixed, Campaign. | Only **solo/competitive** flow implemented; no coop pool, no skill tokens, no deduction deck. |

---

## 3. Gaps / not yet implemented

| Item | GDD reference | Status |
|------|---------------|--------|
| **Characters** | 6 types × 2 variants (12 total) | Only Journalist and Pilot in data and UI; add Investigator, Experiencer, Abductee, Police Officer + variants if needed. |
| **Deduction deck** | History Deck — Déduction cards | No deduction cards or questions in flow; trivia only. |
| **Special events** | Mass Sighting, Whistleblower, MIB, Hoax | Spinner “special” has no effect beyond end turn. |
| **Skeptic “lose next turn”** | 8.4 | No `skip_next_turn` flag. |
| **Debunker movement penalty** | 8.5 | No `movement_penalty` on next move. |
| **Hotspots** | 7.1 (Zone 51, Rendlesham, Ruwa, Hessdalen) | No hotspot logic or bonuses. |
| **Skill tokens (Asymmetric)** | 6.3 | Not implemented. |
| **Cooperative mode** | 6.2 | Single-player / competitive only. |
| **Event card draw on no match** | 5.2 Phase 2: “Piocher une carte Event si disponible” | On continent mismatch we end turn; optional draw not implemented. |

---

## 4. Data and content

- **Events:** Subset of GDD list present in `api/data/events.json` (and `fr`); extend as needed.
- **Trivia:** Linked to events; ensure coverage for authorities/levels.
- **Skeptic / Debunker:** Decks loaded from JSON; used when spinner = obstacle.
- **Characters:** `api/data/characters.json` must define `starting_continents` for each character so starting continent by character (GDD 5.1) is respected.

---

## 5. Summary

- **Core loop** and **all GDD turn actions** are implemented: move (with skip turn, penalty, bonus, event draw), spinner (right/wrong authority, obstacle, special events), 3-question disclosure path, skeptic/debunker penalties.
- **Starting continent** is derived from the chosen character (GDD 5.1).
- **Spinner probabilities** and **Disclosure Path** (3 tokens × 3 authorities = win) match the GDD.
- **Remaining gaps:** per-role skill effects (currently generic +1 token), Trivia-only / Deduction-only / Campaign modes.

When changing rules or adding modes, update this file and the GDD section references.
