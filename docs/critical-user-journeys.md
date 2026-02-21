# Critical User Journeys (CUJs)

Identified from the UAP Disclosure Game codebase for e2e coverage. Limit 3–5; these are High-Traffic / core-action journeys.

---

## CUJ 1: Create a new game (solo) and reach the game screen

| Component | Content |
|-----------|---------|
| **User** | First-time or returning player (solo). |
| **Goal** | When I want to play alone, I create a new game so I can see the game board and take my first turn. |
| **Tasks** | 1. Open lobby (/). 2. Optionally set player name. 3. Click "New game (Solo)". 4. **MOT:** Redirect to /game/:id. 5. See game screen: heading with game id, "Disclosure Path" section, phase. 6. Optional: "Roll dice & move" visible when it’s my turn. |
| **MOTs** | Create game API succeeds; navigation to /game/:id; game screen content visible. |

**Entry URL:** `/`  
**Success:** URL matches `/game/[a-z0-9-]+`, "Disclosure Path" or "Phase" visible.

---

## CUJ 2: Join an existing game

| Component | Content |
|-----------|---------|
| **User** | Second (or later) player with a game ID from the host. |
| **Goal** | When I have a game ID, I join the game so I can play with others. |
| **Tasks** | 1. Open lobby (/). 2. Enter game ID in the join field. 3. Click "Join". 4. **MOT:** Redirect to /game/:id. 5. See game screen; "Waiting for" or "Your turn" and two players in state. |
| **MOTs** | Join API succeeds; navigation to /game/:id; game screen shows joined state. |

**Entry URL:** `/`  
**Success:** URL matches `/game/:id`, game loaded (no "Load failed" alert). Test creates a game via API first to get a valid game ID.

---

## CUJ 3: Complete one turn (roll dice and move)

| Component | Content |
|-----------|---------|
| **User** | Player in an existing game (their turn). |
| **Goal** | When it’s my turn, I roll dice and move so I can advance on the board. |
| **Tasks** | 1. Be on game screen (game created via API; sessionStorage set for player index). 2. Click "Roll dice & move". 3. **MOT:** Phase changes from lobby/movement to spinner or end_turn; dice value or "No event" visible. |
| **MOTs** | Move action succeeds; phase and turn_state update in UI. |

**Entry URL:** `/game/:id` (with valid game and player index in sessionStorage).  
**Success:** Phase is "spinner" or "end_turn"; "Dice:" or "No event card matches" (or Spinner label) visible.
