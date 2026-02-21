# 🛸 The UAP Disclosure Game

> *"A board game of truth, mystery, and investigation. Step into the shoes of journalists, pilots, and investigators as you unravel real UFO cases—one clue at a time."*

A **digital adaptation** of the board game where 2–6 players race to achieve **Full Disclosure**: convince the three Authorities (Government, Military, Scientific) by answering trivia on real UAP cases, moving across continents, and facing Skeptics and Debunkers. Logic meets history in a strategic, educational race.

---

## What is it?

- **Real cases, real history** — Events and questions are based on documented incidents (Roswell, Nimitz/Tic-Tac, Ruwa school, Hessdalen, Grusch testimony, etc.).
- **Disclosure Path** — Each player must earn **3 confirmation tokens** on each of the three Authorities (9 total) to win.
- **Turn flow** — Roll the dice → move across continents → if your location matches an Event Card, spin the wheel → land on an Authority and answer trivia to gain a token, or hit an Obstacle (Skeptic/Debunker) and answer to avoid penalties.
- **Bilingual** — Full English and French (UI and card content). Choose your language in the lobby.
- **Play solo or with friends** — Create a game, share the Game ID, and others can join the same game in the same browser session.

---

## How to play (in 30 seconds)

1. **Lobby** — Pick your language, create a new game (or join with a Game ID), choose your character (e.g. Journalist or Pilot) and variant.
2. **Your turn** — Roll the dice (1–6), then move that many continents on the world map.
3. **Event check** — If your continent matches one of your 3 Event Cards, you spin the Flying Saucer wheel.
4. **Spinner result** — **Government / Military / Scientific**: answer a trivia question; correct → +1 token on that authority. **Obstacle**: answer a Skeptic or Debunker question or end your turn.
5. **Win** — First player to get 3 tokens on each of the three authorities achieves Full Disclosure and wins.

---

## Tech stack & run locally

**Stack:** Python backend (FastAPI + Mangum for Netlify), React + TypeScript + Vite frontend. Optional: Netlify deploy, Supabase persistence. **Platform:** desktop browser (e.g. 1920×1080).

You need **two terminals**: one for the API, one for the frontend. The frontend proxies `/api` to the local API.

### Prerequisites

- **Python 3.11+** (API)
- **Node.js 18+** and **npm** (frontend)

### 1. Backend (API)

From the **project root**:

```bash
cd api
pip install -r requirements.txt
```

Start the API:

```bash
# From project root
python api/run_local.py
```

API runs at **http://127.0.0.1:9999**. Optional: **http://127.0.0.1:9999/docs** for Swagger UI.

### 2. Frontend

In a **second terminal**, from the project root:

```bash
cd frontend
npm install
npm run dev
```

Open **http://localhost:5173** in your browser.

**Important:** Start the API (step 1) before or together with the frontend. The frontend expects the API at `http://127.0.0.1:9999`.

---

## Tests

**Backend (pytest)** — From project root:

```powershell
# PowerShell
$env:PYTHONPATH = "api"
pytest api/tests -v
```

```bash
# Bash / Linux / macOS
PYTHONPATH=api pytest api/tests -v
```

**E2E (Playwright)** — Create game, join game, play one turn. API and frontend must be running. From `frontend/`:

```bash
npm install
npx playwright install chromium   # first time only
npm run test:e2e
```

Optional: `npm run test:e2e:ui`. See `docs/critical-user-journeys.md` for CUJ details.

---

## Deploy (Netlify)

1. Connect the repo to Netlify.
2. **Build:** `cd frontend && npm ci && npm run build`
3. **Publish:** `frontend/dist`
4. **Functions:** `api` (Netlify uses `api/requirements.txt`).
5. **Optional env:** `SUPABASE_URL`, `SUPABASE_KEY` for persistent game state; `VITE_API_URL` if API is on another domain.

Redirects in `netlify.toml`: `/api/*` → serverless function, `/*` → SPA.

**Supabase persistence** — Without it, games are in-memory (lost on cold start). Create a Supabase project and set `SUPABASE_URL` and `SUPABASE_KEY` in Netlify. The table definition is shown below.

Example `games` table for Supabase:

```sql
create table if not exists games (
  id text primary key,
  state jsonb not null default '{}',
  updated_at timestamptz not null default now()
);
```

**Local full stack:** `netlify dev` runs frontend + API as a Netlify function.

---

## Project layout

| Path | Description |
|------|-------------|
| `api/` | Python backend: FastAPI, Clean Architecture (domain, use cases, infrastructure). |
| `api/data/` | JSON content: events, trivia, characters, continents, skeptic, debunker. French in `api/data/fr/`. |
| `api/run_local.py` | Run API with uvicorn on port 9999. |
| `frontend/` | Vite + React + TypeScript: lobby, game screen, i18n (EN/FR). |
| `gdd/` | Game design document (full rules, lore, content). |
| `docs/` | Architecture, critical user journeys, GDD compliance. |

**i18n:** Game language is set when creating a game (`lang`: `"en"` or `"fr"`). UI and cards follow that language. Lobby language is stored in `localStorage` (`uap_lang`).

---

## Credits & design

Game design based on **The UFO Disclosure Game** (Kenneth Media LTD, 2025)—a board game of truth, mystery, and investigation. This repo is an independent digital adaptation. Full design and content notes: `gdd/GDD_UFO_Disclosure_Game_v2.md` and `docs/gdd-compliance.md`.
