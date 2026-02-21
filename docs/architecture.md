# UFO Disclosure Game — Architecture (C4 + Mermaid)

Simple C4-style documentation for the system. Diagrams are in [Mermaid](https://mermaid.js.org/); they render on GitHub, GitLab, and in any Mermaid-compatible viewer.

---

## C4 Level 1 — System Context

Who uses the system and what external systems it talks to.

```mermaid
flowchart LR
    subgraph users[" "]
        P[("Players\n(2–6)")]
    end
    subgraph system["UFO Disclosure Game"]
        direction TB
        WEB["Web App\n(React SPA)"]
        API["Game API\n(FastAPI)"]
        WEB --- API
    end
    EXT[(Supabase\noptional)]
    P -->|"Play in browser"| WEB
    API -.->|"Store game state"| EXT
```

| Element | Description |
|--------|--------------|
| **Players** | 2–6 people playing in a desktop browser (1920×1080). |
| **Web App** | React + TypeScript + Vite SPA: lobby, game screen, i18n (EN/FR). |
| **Game API** | Python FastAPI: create/join game, actions (move, spin, answer), card content. |
| **Supabase** | Optional: persists game state; without it, state is in-memory. |

---

## C4 Level 2 — Containers

High-level runnable building blocks.

```mermaid
flowchart TB
    subgraph browser["Browser"]
        SPA["Frontend\n(Vite + React)"]
    end
    subgraph server["Server / Netlify"]
        API["API\n(FastAPI + Mangum)"]
    end
    subgraph external["External"]
        DB[(Supabase\nPostgreSQL)]
    end
    SPA -->|"REST /api/*"| API
    API -.->|"games table"| DB
```

| Container | Tech | Responsibility |
|-----------|------|-----------------|
| **Frontend** | Vite, React, TypeScript | Lobby (create/join), game UI, language, polling. Proxies `/api` to API in dev. |
| **API** | FastAPI, Mangum (Netlify) | REST: games, cards, actions. Clean Architecture: domain, application, infrastructure. |
| **Supabase** | PostgreSQL | Optional: `games(id, state, updated_at)`. Used when env vars are set. |

---

## C4 Level 3 — Components (inside the API)

Structure of the backend: domain, application, infrastructure.

```mermaid
flowchart TB
    subgraph infrastructure["Infrastructure"]
        R["Routes\n(games, cards)"]
        DI["DI\n(repos)"]
        GM["GameRepo\n(Memory/Supabase)"]
        CR["CardRepo\n(JSON files)"]
    end
    subgraph application["Application"]
        UC["Use cases\n(create, join, game_action, get_cards)"]
        PT["Ports\n(IGameRepository, ICardRepository)"]
        LANG["lang\n(normalize_lang)"]
    end
    subgraph domain["Domain"]
        G["game\n(Game, Player, TurnPhase)"]
        RL["rules\n(spin, dice, win)"]
        C["cards\n(Authority, Continent)"]
    end
    R --> UC
    UC --> PT
    UC --> G
    UC --> RL
    UC --> C
    UC --> LANG
    PT --> DI
    DI --> GM
    DI --> CR
    CR --> C
    GM --> G
```

Dependencies point **inward**: domain ← application ← infrastructure.

| Layer | Contents |
|-------|----------|
| **Domain** | `game.py` (Game, Player, DisclosurePath, TurnPhase), `rules.py` (spin_result, roll_dice, has_full_disclosure), `cards.py` (Authority, Continent, value object helpers). No I/O. |
| **Application** | Ports (interfaces): `IGameRepository`, `ICardRepository`. Use cases: create_game, join_game, perform_move, spin_spinner, submit_answer, get_pending_question, get_cards. `lang.normalize_lang` for i18n. |
| **Infrastructure** | Routes (FastAPI): `/api/games`, `/api/cards`, `/api/health`. DI: chooses GameRepo (memory vs Supabase) and CardRepo (JSON). Persistence: JSON under `api/data/`, optional Supabase table. |

---

## Deployment (Netlify)

```mermaid
flowchart LR
    subgraph netlify["Netlify"]
        CDN["CDN\n(frontend/dist)"]
        F["Python Function\n(Mangum)"]
    end
    U[("Users")] --> CDN
    CDN --> F
    F -.-> DB[(Supabase)]
```

- **Build:** `cd frontend && npm ci && npm run build` → publish `frontend/dist`.
- **Functions:** `api/` as Python runtime; `/api/*` routed to the function.
- **Redirects:** `netlify.toml` sends `/api/*` to the function and `/*` to the SPA.

---

## Data flow (simplified)

Create game and one action:

```mermaid
sequenceDiagram
    participant P as Player
    participant SPA as Frontend
    participant API as API
    participant Repo as Game Repo

    P->>SPA: New game (name, lang)
    SPA->>API: POST /api/games
    API->>Repo: create(game)
    API-->>SPA: game (id, players, phase)
    SPA->>SPA: Store player index, navigate to game
    P->>SPA: Roll dice & move
    SPA->>API: POST /api/games/:id/action { action: "move" }
    API->>Repo: get(id), save(game)
    API-->>SPA: updated game
    SPA-->>P: Show dice, continent, phase
```

---

## Where to find what

| Concern | Path |
|---------|------|
| Game rules, entities | `api/src/domain/` |
| Use cases, ports | `api/src/application/` |
| HTTP, persistence, DI | `api/src/infrastructure/` |
| Card content (EN/FR) | `api/data/`, `api/data/fr/` |
| Lobby & game UI | `frontend/src/features/` |
| API client | `frontend/src/api/client.ts` |
