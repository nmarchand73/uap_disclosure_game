/**
 * API client: base URL from env (same origin in prod, proxy in dev).
 */
import { getLogger } from "../utils/logger";

const log = getLogger("api");
const base = import.meta.env.VITE_API_URL ?? "";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const method = (options?.method ?? "GET").toUpperCase();
  const url = path.startsWith("http") ? path : `${base}${path}`;
  log.debug("request", { method, path });
  const res = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options?.headers,
    },
  });
  if (!res.ok) {
    const text = await res.text();
    let message = text;
    try {
      const json = JSON.parse(text) as { detail?: string };
      if (typeof json.detail === "string") message = json.detail;
    } catch {
      /* use raw text */
    }
    log.warn("request failed", { method, path, status: res.status, message });
    throw new Error(message);
  }
  log.debug("response", { method, path, status: res.status });
  return res.json() as Promise<T>;
}

export const api = {
  health: () => request<{ status: string }>("/api/health"),
  getEvents: (lang = "en") => request<unknown[]>("/api/cards/events?lang=" + lang),
  getCharacters: (lang = "en") => request<unknown[]>("/api/cards/characters?lang=" + lang),
  getContinents: (lang = "en") => request<unknown[]>("/api/cards/continents?lang=" + lang),
  createGame: (body: { player_name: string; character_id: string; character_variant: string; lang?: string }) =>
    request<GameState>("/api/games", { method: "POST", body: JSON.stringify(body) }),
  joinGame: (gameId: string, body: { player_name: string; character_id: string; character_variant: string }) =>
    request<GameState>(`/api/games/${gameId}/join`, { method: "POST", body: JSON.stringify(body) }),
  getGame: (gameId: string) => request<GameState>(`/api/games/${gameId}`),
  gameAction: (gameId: string, action: Record<string, unknown>) =>
    request<GameState>(`/api/games/${gameId}/action`, { method: "POST", body: JSON.stringify(action) }),
  getQuestion: (gameId: string) =>
    request<TriviaQuestion | null>(`/api/games/${gameId}/question`),
};

export interface GameState {
  id: string;
  preferred_lang?: string;
  players: Array<{
    id: string;
    name: string;
    character_id: string;
    continent: string;
    disclosure_path: { government: number; military: number; scientific: number };
    event_card_ids: string[];
  }>;
  current_turn_index: number;
  phase: string;
  created_at: string;
  turn_state?: {
    dice_roll?: number;
    spinner_result?: string;
    pending_question_id?: string;
    pending_authority?: string;
    answer_correct?: boolean;
    correct_index?: number;
    no_event_match?: boolean;
    is_skeptic?: boolean;
  };
}

export interface TriviaQuestion {
  id: string;
  question: string;
  answers: Array<{ text: string }>;
  level?: number;
  authority?: string;
  is_skeptic?: boolean;
  obstacle_type?: "skeptic" | "debunker";
}
