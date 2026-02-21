import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../../api/client";
import { useLanguage } from "../../i18n/LanguageContext";
import type { Lang } from "../../i18n/strings";
import { getLogger } from "../../utils/logger";

const log = getLogger("lobby");

const styles = {
  section: { marginTop: "1.5rem" as const },
  label: { display: "block" as const, marginBottom: "0.5rem", fontWeight: 600 as const },
  input: {
    padding: "0.6rem 0.75rem",
    width: "100%",
    maxWidth: 320,
    background: "var(--bg-main)",
    color: "var(--text-main)",
    border: "1px solid var(--accent-secondary)",
    borderRadius: "var(--radius)",
    fontSize: "1rem",
  },
  button: {
    marginTop: "1rem",
    marginRight: "0.5rem",
    padding: "0.75rem 1.5rem",
    background: "var(--accent-primary)",
    color: "var(--bg-main)",
    border: "none",
    borderRadius: "var(--radius)",
    cursor: "pointer",
    fontWeight: 600,
    fontSize: "1rem",
  },
  buttonSecondary: {
    marginTop: "1rem",
    padding: "0.75rem 1.5rem",
    background: "var(--accent-secondary)",
    color: "var(--text-main)",
    border: "none",
    borderRadius: "var(--radius)",
    cursor: "pointer",
    fontWeight: 600,
    fontSize: "1rem",
  },
};

const CHARACTER_IDS = ["journalist", "pilot", "investigator", "experiencer", "abductee", "police_officer"] as const;
const CHARACTER_VARIANTS: Record<string, string[]> = {
  journalist: ["investigation", "terrain"],
  pilot: ["military", "civil"],
  investigator: ["mufon", "ex_agent"],
  experiencer: ["visual", "contact"],
  abductee: ["classic", "modern"],
  police_officer: ["rural", "urban"],
};

export default function Lobby() {
  const { lang, setLang, t } = useLanguage();
  const [playerName, setPlayerName] = useState("Player");
  const [characterId, setCharacterId] = useState("journalist");
  const [characterVariant, setCharacterVariant] = useState("investigation");
  const [mode, setMode] = useState<"solo" | "coop">("solo");
  const [gameIdToJoin, setGameIdToJoin] = useState("");
  const [loading, setLoading] = useState(false);
  const [joinLoading, setJoinLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const variants = CHARACTER_VARIANTS[characterId] ?? ["investigation"];
  const effectiveVariant = variants.includes(characterVariant) ? characterVariant : variants[0];

  const handleNewGame = async () => {
    setLoading(true);
    setError(null);
    try {
      const game = await api.createGame({
        player_name: playerName,
        character_id: characterId,
        character_variant: effectiveVariant,
        mode,
        lang,
      });
      log.info("Game created", { game_id: game.id, lang });
      sessionStorage.setItem(`uap_player_${game.id}`, "0");
      navigate(`/game/${game.id}`);
    } catch (e) {
      log.warn("Create game failed", { error: e instanceof Error ? e.message : String(e) });
      setError(e instanceof Error ? e.message : t("createFailed"));
    } finally {
      setLoading(false);
    }
  };

  const handleJoinGame = async () => {
    const id = gameIdToJoin.trim();
    if (!id) {
      setError(t("enterGameId"));
      return;
    }
    setJoinLoading(true);
    setError(null);
    try {
      const game = await api.joinGame(id, {
        player_name: playerName,
        character_id: characterId,
        character_variant: effectiveVariant,
      });
      log.info("Joined game", { game_id: id, player_index: game.players.length - 1 });
      sessionStorage.setItem(`uap_player_${id}`, String(game.players.length - 1));
      navigate(`/game/${id}`);
    } catch (e) {
      log.warn("Join game failed", { game_id: id, error: e instanceof Error ? e.message : String(e) });
      setError(e instanceof Error ? e.message : t("joinFailed"));
    } finally {
      setJoinLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: 600 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: "0.5rem" }}>
        <h1 style={{ color: "var(--accent-primary)", fontFamily: "Orbitron, sans-serif", margin: 0 }}>
          {t("appTitle")}
        </h1>
        <div style={{ display: "flex", gap: "0.25rem" }} role="group" aria-label={t("language")}>
          <button
            type="button"
            onClick={() => setLang("en" as Lang)}
            style={{
              padding: "0.35rem 0.75rem",
              borderRadius: "var(--radius)",
              background: lang === "en" ? "var(--accent-primary)" : "var(--bg-main)",
              color: lang === "en" ? "var(--bg-main)" : "var(--text-main)",
              border: "1px solid var(--accent-secondary)",
              cursor: "pointer",
              fontWeight: 600,
            }}
          >
            {t("english")}
          </button>
          <button
            type="button"
            onClick={() => setLang("fr" as Lang)}
            style={{
              padding: "0.35rem 0.75rem",
              borderRadius: "var(--radius)",
              background: lang === "fr" ? "var(--accent-primary)" : "var(--bg-main)",
              color: lang === "fr" ? "var(--bg-main)" : "var(--text-main)",
              border: "1px solid var(--accent-secondary)",
              cursor: "pointer",
              fontWeight: 600,
            }}
          >
            {t("french")}
          </button>
        </div>
      </div>
      <p style={{ color: "var(--text-main)" }}>{t("subtitle")}</p>

      <div style={styles.section}>
        <label style={styles.label} htmlFor="player-name">
          {t("playerName")}
        </label>
        <input
          id="player-name"
          type="text"
          value={playerName}
          onChange={(e) => setPlayerName(e.target.value)}
          style={styles.input}
          autoComplete="name"
          aria-describedby={error ? "lobby-error" : undefined}
        />
      </div>
      <div style={styles.section}>
        <label style={styles.label} htmlFor="character">
          {t("character")}
        </label>
        <select
          id="character"
          value={characterId}
          onChange={(e) => {
            const id = e.target.value;
            setCharacterId(id);
            const v = CHARACTER_VARIANTS[id] ?? ["investigation"];
            setCharacterVariant(v[0]);
          }}
          style={styles.input}
          aria-label={t("character")}
        >
          {CHARACTER_IDS.map((id) => (
            <option key={id} value={id}>{t(id)}</option>
          ))}
        </select>
        <label style={{ ...styles.label, marginTop: "0.75rem" }} htmlFor="variant">
          {t("variant")}
        </label>
        <select
          id="variant"
          value={effectiveVariant}
          onChange={(e) => setCharacterVariant(e.target.value)}
          style={styles.input}
          aria-label={t("variant")}
        >
          {variants.map((v) => (
            <option key={v} value={v}>{t("variant_" + v)}</option>
          ))}
        </select>
        <label style={{ ...styles.label, marginTop: "0.75rem" }} htmlFor="mode">
          {t("mode")}
        </label>
        <select
          id="mode"
          value={mode}
          onChange={(e) => setMode(e.target.value as "solo" | "coop")}
          style={styles.input}
          aria-label={t("mode")}
        >
          <option value="solo">{t("modeSolo")}</option>
          <option value="coop">{t("modeCoop")}</option>
        </select>
      </div>

      <section style={{ ...styles.section, marginTop: "2rem" }}>
        <h2 style={{ fontSize: "1.1rem" }}>{t("newGame")}</h2>
        <button
          data-testid="lobby-new-game"
          onClick={handleNewGame}
          disabled={loading}
          style={{ ...styles.button, cursor: loading ? "not-allowed" : "pointer" }}
        >
          {loading ? t("creating") : t("newGameButton")}
        </button>
      </section>

      <section style={{ ...styles.section, marginTop: "2rem" }}>
        <h2 style={{ fontSize: "1.1rem" }}>{t("joinGame")}</h2>
        <label style={styles.label} htmlFor="game-id-join">
          {t("gameId")}
        </label>
        <input
          id="game-id-join"
          data-testid="lobby-game-id-input"
          type="text"
          value={gameIdToJoin}
          onChange={(e) => setGameIdToJoin(e.target.value)}
          placeholder={t("gameIdPlaceholder")}
          style={styles.input}
          autoComplete="off"
        />
        <button
          data-testid="lobby-join"
          onClick={handleJoinGame}
          disabled={joinLoading || !gameIdToJoin.trim()}
          style={{
            ...styles.buttonSecondary,
            cursor: joinLoading || !gameIdToJoin.trim() ? "not-allowed" : "pointer",
          }}
        >
          {joinLoading ? t("joining") : t("joinButton")}
        </button>
      </section>

      {error && (
        <p id="lobby-error" role="alert" style={{ color: "var(--danger)", marginTop: "1rem", fontWeight: 600 }}>
          {error}
        </p>
      )}
    </div>
  );
}
