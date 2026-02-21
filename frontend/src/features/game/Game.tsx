import { useCallback, useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { api, type GameState, type TriviaQuestion } from "../../api/client";
import { useLanguage } from "../../i18n/LanguageContext";
import { continentName, spinnerLabelKey, t as tRaw, type Lang } from "../../i18n/strings";
import { getLogger } from "../../utils/logger";

const log = getLogger("game");

const TOKEN_MAX = 3;
const buttonBase = {
  padding: "0.6rem 1.25rem",
  borderRadius: "var(--radius)",
  fontWeight: 600,
  fontSize: "1rem",
  border: "none",
  cursor: "pointer",
} as const;

export default function Game() {
  const { gameId } = useParams<{ gameId: string }>();
  const navigate = useNavigate();
  const { lang: userLang } = useLanguage();
  const [game, setGame] = useState<GameState | null>(null);
  const [question, setQuestion] = useState<TriviaQuestion | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<string | null>(null);
  const [copyFeedback, setCopyFeedback] = useState(false);

  const copyGameId = useCallback(() => {
    if (!game?.id) return;
    navigator.clipboard.writeText(game.id).then(() => {
      setCopyFeedback(true);
      setTimeout(() => setCopyFeedback(false), 2000);
    });
  }, [game?.id]);

  const lang: Lang = (game?.preferred_lang === "fr" || game?.preferred_lang === "en") ? game.preferred_lang : userLang;
  const t = (key: string) => tRaw(lang, key);

  const fetchGame = useCallback(() => {
    if (!gameId) return;
    api
      .getGame(gameId)
      .then((data) => {
        setGame(data);
        setError(null);
      })
      .catch((e) => {
        log.warn("Fetch game failed", { game_id: gameId, error: e instanceof Error ? e.message : String(e) });
        setError(e instanceof Error ? e.message : tRaw(userLang, "loadFailed"));
      });
  }, [gameId, userLang]);

  const fetchQuestion = () => {
    if (!gameId) return;
    api.getQuestion(gameId).then((q) => setQuestion(q ?? null));
  };

  useEffect(() => {
    fetchGame();
  }, [fetchGame]);

  useEffect(() => {
    if (game?.phase === "question") fetchQuestion();
    else setQuestion(null);
  }, [game?.phase, gameId]);

  // Multiplayer: poll for game state when 2+ players and not in lobby
  useEffect(() => {
    if (!gameId || !game || game.players.length < 2 || game.phase === "lobby") return;
    const interval = setInterval(fetchGame, 3000);
    return () => clearInterval(interval);
  }, [gameId, game?.players?.length, game?.phase]);

  const onAction = async (action: string, payload: Record<string, unknown> = {}) => {
    if (!gameId || !game) return;
    setLoading(action);
    setError(null);
    try {
      const body = { action, ...payload };
      log.info("Game action", { game_id: gameId, action });
      const updated = await api.gameAction(gameId, body);
      setGame(updated);
      log.debug("Game state updated", { phase: updated.phase });
      if (updated.phase === "question") fetchQuestion();
      else setQuestion(null);
    } catch (e) {
      log.warn("Game action failed", { game_id: gameId, action, error: e instanceof Error ? e.message : String(e) });
      setError(e instanceof Error ? e.message : tRaw(lang, "actionFailed"));
    } finally {
      setLoading(null);
    }
  };

  const submitAnswer = (answerIndex: number) => {
    onAction("submit_answer", { answer_index: answerIndex });
  };

  if (error && !game) {
    return (
      <div style={{ padding: "2rem", maxWidth: 600 }}>
        <p role="alert" style={{ color: "var(--danger)", fontWeight: 600, marginBottom: "1rem" }}>
          {error}
        </p>
        <button onClick={() => navigate("/")} style={{ ...buttonBase, background: "var(--accent-primary)", color: "var(--bg-main)" }}>
          {t("backToLobby")}
        </button>
      </div>
    );
  }
  if (!game) {
    return (
      <div style={{ padding: "2rem", maxWidth: 600 }} aria-live="polite">
        <p style={{ color: "var(--text-muted)" }}>{t("loadingGame")}</p>
        <div className="loading-spinner" style={{ marginTop: "1rem" }} aria-hidden />
      </div>
    );
  }

  const myIndex = gameId ? parseInt(sessionStorage.getItem(`uap_player_${gameId}`) ?? "0", 10) : 0;
  const currentPlayer = game.players[game.current_turn_index] ?? game.players[0];
  const isMyTurn = game.current_turn_index === myIndex;
  const isCoop = game.mode === "coop";
  const path = isCoop && game.shared_path
    ? game.shared_path
    : (game.players[myIndex] ?? game.players[0])?.disclosure_path ?? { government: 0, military: 0, scientific: 0 };
  const won = game.won ?? (path.government >= 3 && path.military >= 3 && path.scientific >= 3);
  const currentPlayerData = game.players[game.current_turn_index] ?? game.players[0];
  const canUseSkill = isMyTurn && !currentPlayerData?.skill_used && (game.phase === "movement" || game.phase === "spinner" || game.phase === "end_turn");

  const ts = game.turn_state ?? {};
  const spinnerLabel = ts.spinner_result ? t(spinnerLabelKey(ts.spinner_result)) : null;

  const renderTokenBar = (label: string, value: number) => (
    <div key={label} style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "0.35rem" }}>
      <span style={{ minWidth: 100, fontSize: "0.95rem" }}>{label}</span>
      <div style={{ display: "flex", gap: "0.25rem" }}>
        {Array.from({ length: TOKEN_MAX }, (_, i) => (
          <span
            key={i}
            style={{
              width: 20,
              height: 20,
              borderRadius: 4,
              background: i < value ? "var(--accent-primary)" : "var(--accent-secondary)",
              opacity: i < value ? 1 : 0.35,
            }}
            aria-hidden
          />
        ))}
      </div>
      <span style={{ color: "var(--text-muted)", fontSize: "0.9rem" }}>{value}/{TOKEN_MAX}</span>
    </div>
  );

  return (
    <div style={{ padding: "2rem", maxWidth: 900 }}>
      <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "space-between", alignItems: "center", gap: "1rem", marginBottom: "1rem" }}>
        <h1 style={{ color: "var(--accent-primary)", fontFamily: "Orbitron, sans-serif", margin: 0, fontSize: "1.5rem" }}>
          Game {game.id}
        </h1>
        <button onClick={() => navigate("/")} style={{ ...buttonBase, background: "transparent", color: "var(--accent-secondary)", border: "1px solid var(--accent-secondary)" }}>
          {t("backToLobby")}
        </button>
      </div>

      {error && (
        <p data-testid="game-error" role="alert" style={{ color: "var(--danger)", fontWeight: 600, marginBottom: "0.75rem" }}>
          {error}
        </p>
      )}

      {game.players.length >= 2 && (
        <p style={{ color: isMyTurn ? "var(--success)" : "var(--accent-secondary)", fontWeight: 600, marginBottom: "0.5rem" }}>
          {isMyTurn ? t("yourTurn") : `${t("waitingFor")} ${currentPlayer?.name ?? "other"}${lang === "en" ? t("turn") : ""}`}
        </p>
      )}
      <p style={{ color: "var(--text-main)", marginBottom: "0.5rem" }}>
        {t("you")}: {game.players[myIndex]?.name ?? currentPlayer?.name} — {game.players[myIndex]?.character_id ?? currentPlayer?.character_id}
      </p>
      <p style={{ color: "var(--accent-primary)", fontWeight: 600, marginBottom: "0.5rem" }}>
        {t("position")}: {continentName(lang, (game.players[myIndex] ?? currentPlayer)?.continent ?? "")}
      </p>
      {ts.dice_roll != null && (
        <p style={{ color: "var(--success)", fontWeight: 600, marginBottom: "0.25rem" }}>
          {t("youMovedTo")} {continentName(lang, (game.players[game.current_turn_index] ?? game.players[0])?.continent ?? "")} ({ts.dice_roll}{ts.steps != null && ts.steps !== ts.dice_roll ? ` → ${ts.steps} ${t("steps")}` : ""})
        </p>
      )}
      {ts.skipped_turn && (
        <p style={{ color: "var(--accent-secondary)", marginBottom: "0.25rem" }}>{t("turnSkipped")}</p>
      )}
      {ts.no_event_match && (
        <p style={{ color: "var(--accent-secondary)", marginBottom: "0.25rem" }}>{t("noEventMatch")}{ts.drew_event ? ` ${t("drewEventCard")}` : ""}</p>
      )}
      {ts.special && (
        <p style={{ color: "var(--accent-primary)", marginBottom: "0.25rem" }}>
          {t(ts.special === "whistleblower" ? "specialWhistleblower" : ts.special === "mib" ? "specialMIB" : ts.special === "hoax" ? "specialHoax" : "specialMassSighting")}
        </p>
      )}
      {spinnerLabel && game.phase !== "question" && (
        <p style={{ color: "var(--accent-primary)", marginBottom: "0.25rem" }}>Spinner: {spinnerLabel}</p>
      )}

      <section data-testid="game-disclosure-path" style={{ marginTop: "1.25rem", padding: "1rem", background: "rgba(123, 47, 190, 0.12)", borderRadius: "var(--radius)", border: "1px solid var(--accent-secondary)" }}>
        <h2 style={{ marginTop: 0, marginBottom: "0.75rem", fontSize: "1.1rem" }}>{t("disclosurePath")}</h2>
        {renderTokenBar(t("government"), path.government)}
        {renderTokenBar(t("military"), path.military)}
        {renderTokenBar(t("scientific"), path.scientific)}
        {won && (
          <p style={{ color: "var(--success)", fontWeight: "bold", marginTop: "0.75rem", marginBottom: 0 }}>
            {t("fullDisclosure")}
          </p>
        )}
      </section>

      {game.turn_state?.answer_correct !== undefined && (
        <p style={{ color: game.turn_state.answer_correct ? "var(--success)" : "var(--danger)", fontWeight: 600, marginTop: "0.5rem" }}>
          {game.turn_state.answer_correct ? t("correct") : t("wrong")}
        </p>
      )}

      {!won && (
        <section style={{ marginTop: "1.5rem" }}>
          <p data-testid="game-phase" style={{ color: "var(--text-muted)", marginBottom: "0.5rem" }}>{t("phase")}: {game.phase}</p>
          {game.players.length >= 2 && !isMyTurn && game.phase !== "lobby" && (
            <p style={{ color: "var(--accent-secondary)", marginBottom: "0.5rem" }}>{t("waitingPolling")}</p>
          )}
          {(game.phase === "lobby" || game.phase === "movement" || game.phase === "end_turn") && isMyTurn && (
            <>
              <button
                data-testid="game-roll-dice"
                onClick={() => onAction("move")}
                disabled={!!loading}
                style={{ ...buttonBase, marginRight: "0.5rem", background: "var(--accent-primary)", color: "var(--bg-main)" }}
              >
                {loading === "move" ? "…" : t("rollDiceMove")}
              </button>
              {canUseSkill && (
                <button
                  onClick={() => onAction("use_skill")}
                  disabled={!!loading}
                  style={{ ...buttonBase, background: "var(--accent-secondary)", color: "var(--text-main)" }}
                >
                  {loading === "use_skill" ? "…" : t("useSkill")}
                </button>
              )}
            </>
          )}
          {game.phase === "spinner" && isMyTurn && (
            <>
              <button
                onClick={() => onAction("spin")}
                disabled={!!loading}
                style={{ ...buttonBase, marginRight: "0.5rem", background: "var(--accent-primary)", color: "var(--bg-main)" }}
              >
                {loading === "spin" ? "…" : t("spin")}
              </button>
              {canUseSkill && (
                <button
                  onClick={() => onAction("use_skill")}
                  disabled={!!loading}
                  style={{ ...buttonBase, background: "var(--accent-secondary)", color: "var(--text-main)" }}
                >
                  {loading === "use_skill" ? "…" : t("useSkill")}
                </button>
              )}
            </>
          )}
        </section>
      )}

      {game.phase === "question" && question && isMyTurn && (
        <section style={{ marginTop: "1.5rem", padding: "1.25rem", border: "1px solid var(--accent-secondary)", borderRadius: "var(--radius)", background: "rgba(0, 255, 170, 0.06)" }}>
          {!question.is_skeptic && (game.turn_state?.disclosure_question_index ?? 0) >= 0 && (
            <p style={{ color: "var(--accent-secondary)", marginBottom: "0.5rem", fontSize: "0.9rem" }}>
              {t("questionXofY").replace("%1", String((game.turn_state?.disclosure_question_index ?? 0) + 1)).replace("%2", "3")}
            </p>
          )}
          {question.is_skeptic && (
            <p style={{ color: "var(--danger)", marginBottom: "0.5rem", fontWeight: 600 }}>
              {question.obstacle_type === "debunker" ? t("debunkerChallenge") : t("skepticChallenge")}
            </p>
          )}
          <h3 style={{ marginTop: 0, marginBottom: "0.75rem" }}>{question.question}</h3>
          <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
            {question.answers?.map((a, i) => (
              <button
                key={i}
                type="button"
                onClick={() => submitAnswer(i)}
                disabled={!!loading}
                style={{
                  ...buttonBase,
                  padding: "0.75rem 1rem",
                  textAlign: "left",
                  background: "var(--bg-main)",
                  color: "var(--text-main)",
                  border: "1px solid var(--accent-primary)",
                }}
              >
                {a.text}
              </button>
            ))}
          </div>
        </section>
      )}

      {game.players.length < 6 && game.phase === "lobby" && (
        <div style={{ marginTop: "1.5rem", padding: "1rem", background: "rgba(123, 47, 190, 0.12)", borderRadius: "var(--radius)", border: "1px solid var(--accent-secondary)" }}>
          <p style={{ marginTop: 0, marginBottom: "0.5rem", fontSize: "0.95rem", color: "var(--text-main)" }}>
            {t("shareGameId")}
          </p>
          <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", flexWrap: "wrap" }}>
            <code data-testid="game-id" style={{ padding: "0.4rem 0.6rem", background: "var(--bg-main)", borderRadius: "var(--radius)", fontFamily: "monospace", fontSize: "1.1rem", letterSpacing: "0.05em" }}>
              {game.id}
            </code>
            <button
              type="button"
              onClick={copyGameId}
              style={{ ...buttonBase, background: copyFeedback ? "var(--success)" : "var(--accent-secondary)", color: "var(--text-main)" }}
            >
              {copyFeedback ? t("copied") : t("copy")}
            </button>
          </div>
        </div>
      )}

      {won && (
        <div style={{ marginTop: "1.5rem" }}>
          <button onClick={() => navigate("/")} style={{ ...buttonBase, background: "var(--success)", color: "var(--bg-main)", padding: "0.75rem 1.5rem" }}>
            {t("backToLobby")}
          </button>
        </div>
      )}
    </div>
  );
}
