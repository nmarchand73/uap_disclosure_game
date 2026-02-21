# UFO Disclosure Game

Digital board game (2–6 players): trivia + deduction, race to validate 3 Authorities (Government, Military, Scientific).  
**Stack:** Python backend (FastAPI + Mangum), React + TypeScript + Vite frontend. Optional: Netlify deploy, Supabase persistence. **Platform:** PC (desktop browser, 1920×1080).

---

## How to run it locally

You need **two terminals**: one for the API, one for the frontend. The frontend proxies `/api` to the local API.

### 1. Prerequisites

- **Python 3.11+** (for the API)
- **Node.js 18+** and **npm** (for the frontend)

### 2. Backend (API)

From the **project root**:

```bash
cd api
pip install -r requirements.txt
```

Start the API (still from project root, or ensure you're in the repo root when running the next command):

```bash
# From project root (e.g. C:\DATA\DEV\PROJETS\uap_disclosure_game)
python api/run_local.py
```

Leave this running. You should see something like:

```
INFO:     Uvicorn running on http://127.0.0.1:9999
```

The API serves on **http://127.0.0.1:9999**. Optional: open **http://127.0.0.1:9999/docs** for Swagger UI.

### 3. Frontend

Open a **second terminal**, from the project root:

```bash
cd frontend
npm install
npm run dev
```

Leave this running. You should see:

```
  VITE v5.x.x  ready in xxx ms
  ➜  Local:   http://localhost:5173/
```

### 4. Play

Open **http://localhost:5173** in your browser.

- Choose **English** or **Français** in the lobby.
- **New game (Solo)** creates a game and puts you in. Share the **Game ID** if you want others to join.
- **Join game**: paste the Game ID and click Join.
- In game: **Roll dice & move** → land on a continent → if you have a matching event card, **Spin** → answer trivia or skeptic/debunker questions. First to 3 tokens in each authority wins.

**Important:** The frontend expects the API at `http://127.0.0.1:9999`. Start the API (step 2) before or at the same time as the frontend (step 3).

---

## Running tests

From the **project root**, with the `api` folder on `PYTHONPATH`:

**PowerShell:**

```powershell
$env:PYTHONPATH = "api"
pytest api/tests -v
```

**Bash / Linux / macOS:**

```bash
PYTHONPATH=api pytest api/tests -v
```

All tests should pass (domain rules, game action helpers, integration).

---

## E2E (Playwright) tests

Critical User Journey (CUJ) tests live in `frontend/e2e/` and use [Playwright](https://playwright.dev/). They cover: **create game**, **join game**, and **play one turn (roll dice & move)**.

**Prerequisites:** API and frontend must be running (see [How to run it locally](#how-to-run-it-locally)). E2e tests run with one worker so create, join, and move hit the same API process; use a single local API (e.g. `python api/run_local.py`), not a serverless deployment with per-request in-memory state.

From the **frontend** folder:

```bash
cd frontend
npm install
npx playwright install chromium   # first time only
npm run test:e2e
```

Optional: `npm run test:e2e:ui` for the Playwright UI. Set `PLAYWRIGHT_BASE_URL` (default `http://localhost:5173`) or `PLAYWRIGHT_API_URL` (default `http://127.0.0.1:9999`) if your URLs differ.

---

## Logging

- **Backend:** Python `logging` is configured at startup. Each HTTP request is logged (method, path, status, duration). Game events (create, join, action) are logged with `game_id` and phase. Set `LOG_LEVEL` to `DEBUG`, `INFO` (default), `WARN`, or `ERROR`.
- **Frontend:** Browser logger in `src/utils/logger.ts` with namespaces (`api`, `lobby`, `game`). In dev, default level is `debug`; in production, `info`. Set `VITE_LOG_LEVEL=debug` (or `info`/`warn`/`error`) in `.env` to override.

---

## Deploy to Netlify

1. Connect this repo to Netlify.
2. **Build command:** `cd frontend && npm ci && npm run build`
3. **Publish directory:** `frontend/dist`
4. **Functions directory:** `api` (Netlify uses `api/requirements.txt` for the Python runtime).
5. **Environment variables** (optional):
   - `SUPABASE_URL`, `SUPABASE_KEY` (or `SUPABASE_SERVICE_KEY`) — if set, game state is stored in Supabase instead of in-memory.
   - `VITE_API_URL` — leave empty for same-origin; the app is served from the same domain and `/api` is redirected to the function.

Redirects are in `netlify.toml`: `/api/*` → serverless function, `/*` → `index.html` (SPA).

### Optional: Supabase persistence

Without Supabase, game state is **in-memory** (lost when the function cold-starts or restarts). To persist games:

1. Create a Supabase project and get the project URL and service (or anon) key.
2. In Netlify, set `SUPABASE_URL` and `SUPABASE_KEY` (or `SUPABASE_SERVICE_KEY`).
3. In the Supabase SQL editor, run:

```sql
create table if not exists games (
  id text primary key,
  state jsonb not null default '{}',
  updated_at timestamptz not null default now()
);
```

Enable RLS if you need it; the server uses the service key for backend access.

---

## Full stack with Netlify CLI (optional)

To run the full Netlify setup locally (frontend + serverless functions + redirects):

```bash
npm install -g netlify-cli
netlify dev
```

This starts the frontend and the API as a Netlify function; no need to run `python api/run_local.py` separately.

---

## Project layout

| Path | Description |
|------|-------------|
| `api/` | Python backend: FastAPI app, Mangum for Netlify. Clean Architecture: domain, application (ports + use cases), infrastructure (routes, persistence). |
| `api/data/` | JSON card content: events, trivia, characters, continents, skeptic, debunker. French in `api/data/fr/`. |
| `api/run_local.py` | Runs the API with uvicorn on port 9999 (for local dev). |
| `frontend/` | Vite + React + TypeScript SPA: lobby, game screen, i18n (EN/FR). |
| `gdd/` | Game design document. |
| `netlify.toml` | Build, publish dir, functions dir, redirects. |

**i18n:** Game language is set when creating a game (`lang`: `"en"` or `"fr"` in the create-game body). UI and card content follow that language. The lobby has a language switcher; the choice is stored in `localStorage` (`uap_lang`).

**API docs:** When the API is running locally, open **http://127.0.0.1:9999/docs** for interactive Swagger UI.
