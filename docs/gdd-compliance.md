# GDD Compliance — UAP Disclosure Game

This document tracks implementation status against the **Game Design Document** (`gdd/GDD_UFO_Disclosure_Game_v2.md`). It is updated when rules or content change.

---

## 1. Rules fully implemented and aligned

| GDD reference | Rule | Implementation |
|---------------|------|----------------|
| **5.1 Setup — Event Cards** | 3 Event Cards per player (mode standard) | `create_game` / `join_game`: 3 event cards drawn from shuffled deck |
| **5.1 Placement** | Each character starts on their starting continent | `_starting_continent_for_character()` in create/join; `characters.json` has `starting_continents` per character |
| **5.2 Phase 1** | Roll dice 1–6, move that many continents | `roll_dice()` 1–6; move use case advances by continents in `CONTINENTS_MOVEMENT_ORDER` |
| **5.2 Phase 2** | Event check: continent matches an Event Card → Phase 3; else end turn (or draw) | Move use case: if current continent in event card continent → spin; else end turn |
| **5.2 Phase 3 — Spinner** | Government / Military / Scientific / Obstacle / Special | `rules.spin_result()` returns government, military, scientific, obstacle, special |
| **7.3 Spinner probabilities** | ~20% Gov, ~20% Mil, ~20% Sci, ~25% Obstacle, ~15% Special | `rules.py`: PROB_* = 0.20, 0.20, 0.20, 0.25, 0.15 |
| **7.2 Disclosure Path** | 3 tokens per authority; 3 authorities = Full Disclosure = win | `DisclosurePath` gov/mil/sci; `has_full_disclosure()` when all ≥ 3 |
| **5.2 Phase 4 (simplified)** | Correct answer on Path → +1 token; wrong → exit path, end turn | One trivia per spin; correct → +1 token for that authority; wrong → end turn |
| **5.2 Phase 5 — Obstacles** | Skeptic / Debunker: answer correctly or penalty | Obstacle → skeptic or debunker card; correct → continue; wrong → end turn |
| **7.1 Continents** | 6 continents, adjacency for movement | `Continent` enum; `CONTINENTS_MOVEMENT_ORDER` for wrap-around movement |
| **4 — Characters** | Attributes, variants, starting continents | `characters.json`: Journalist, Pilot with variants and `starting_continents`; 2 of 6 GDD types implemented |

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

- **Core loop (move → event check → spinner → trivia/obstacle → tokens)** is implemented and aligned with the GDD.
- **Starting continent** is derived from the chosen character (GDD 5.1).
- **Spinner probabilities** and **Disclosure Path** (3 tokens × 3 authorities = win) match the GDD.
- **Simplifications** (1 question per spin, no special events, no next-turn penalties) are documented above and can be refined in later iterations.
- **Gaps** (extra characters, deduction, special events, hotspots, coop, asymmetric) are listed for roadmap or backlog.

When changing rules or adding modes, update this file and the GDD section references.
