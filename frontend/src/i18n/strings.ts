/** UI strings for English and French. */
export type Lang = "en" | "fr";

export const strings: Record<Lang, Record<string, string>> = {
  en: {
    appTitle: "UAP Disclosure Game",
    subtitle: "PC — 1920×1080",
    playerName: "Player name",
    character: "Character",
    journalist: "Journalist",
    pilot: "Pilot",
    newGame: "New game",
    joinGame: "Join game",
    gameId: "Game ID (share from host)",
    gameIdPlaceholder: "e.g. a1b2c3d4",
    creating: "Creating…",
    joining: "Joining…",
    newGameButton: "New game (Solo)",
    joinButton: "Join",
    backToLobby: "Back to lobby",
    rollDiceMove: "Roll dice & move",
    spin: "Spin",
    yourTurn: "Your turn",
    waitingFor: "Waiting for",
    turn: "'s turn",
    you: "You",
    continent: "Continent",
    disclosurePath: "Disclosure Path",
    government: "Government",
    military: "Military",
    scientific: "Scientific",
    fullDisclosure: "Full Disclosure! You win.",
    correct: "Correct!",
    wrong: "Wrong.",
    phase: "Phase",
    loadingGame: "Loading game…",
    loadFailed: "Load failed",
    actionFailed: "Action failed",
    noEventMatch: "No event card matches this continent — turn ended.",
    shareGameId: "Share game ID so others can join from the lobby.",
    skepticChallenge: "Skeptic challenge — answer correctly or lose the rest of this turn.",
    debunkerChallenge: "Debunker challenge — answer correctly or lose the rest of this turn.",
    waitingPolling: "Waiting for other players… (updates every 3s)",
    north_america: "North America",
    south_america: "South America",
    europe: "Europe",
    africa: "Africa",
    asia: "Asia",
    oceania: "Oceania",
    spinner_government: "Government",
    spinner_military: "Military",
    spinner_scientific: "Scientific",
    spinner_obstacle: "Obstacle",
    spinner_special: "Special",
    language: "Language",
    english: "English",
    french: "French",
    enterGameId: "Enter a game ID",
    createFailed: "Failed to create game",
    joinFailed: "Failed to join game",
    copy: "Copy",
    copied: "Copied!",
  },
  fr: {
    appTitle: "UAP Disclosure Game",
    subtitle: "PC — 1920×1080",
    playerName: "Nom du joueur",
    character: "Personnage",
    journalist: "Journaliste",
    pilot: "Pilote",
    newGame: "Nouvelle partie",
    joinGame: "Rejoindre",
    gameId: "ID de partie (partagé par l'hôte)",
    gameIdPlaceholder: "ex. a1b2c3d4",
    creating: "Création…",
    joining: "Connexion…",
    newGameButton: "Nouvelle partie (Solo)",
    joinButton: "Rejoindre",
    backToLobby: "Retour au lobby",
    rollDiceMove: "Lancer les dés et avancer",
    spin: "Tourner",
    yourTurn: "À vous de jouer",
    waitingFor: "En attente du tour de",
    turn: "",
    you: "Vous",
    continent: "Continent",
    disclosurePath: "Parcours de divulgation",
    government: "Gouvernement",
    military: "Militaire",
    scientific: "Scientifique",
    fullDisclosure: "Divulgation complète ! Vous gagnez.",
    correct: "Correct !",
    wrong: "Faux.",
    phase: "Phase",
    loadingGame: "Chargement de la partie…",
    loadFailed: "Échec du chargement",
    actionFailed: "Échec de l'action",
    noEventMatch: "Aucune carte événement ne correspond à ce continent — tour terminé.",
    shareGameId: "Partagez l'ID de partie pour que d'autres puissent rejoindre depuis le lobby.",
    skepticChallenge: "Défi sceptique — répondez correctement ou perdez le reste du tour.",
    debunkerChallenge: "Défi débunkeur — répondez correctement ou perdez le reste du tour.",
    waitingPolling: "En attente des autres joueurs… (rafraîchi toutes les 3 s)",
    north_america: "Amérique du Nord",
    south_america: "Amérique du Sud",
    europe: "Europe",
    africa: "Afrique",
    asia: "Asie",
    oceania: "Océanie",
    spinner_government: "Gouvernement",
    spinner_military: "Militaire",
    spinner_scientific: "Scientifique",
    spinner_obstacle: "Obstacle",
    spinner_special: "Spécial",
    language: "Langue",
    english: "English",
    french: "Français",
    enterGameId: "Saisissez un ID de partie",
    createFailed: "Impossible de créer la partie",
    joinFailed: "Impossible de rejoindre la partie",
    copy: "Copier",
    copied: "Copié !",
  },
};

const STORAGE_KEY = "uap_lang";

export function getStoredLang(): Lang {
  try {
    const v = localStorage.getItem(STORAGE_KEY);
    if (v === "fr" || v === "en") return v;
  } catch {
    /* ignore */
  }
  if (typeof navigator !== "undefined" && navigator.language?.toLowerCase().startsWith("fr")) return "fr";
  return "en";
}

export function setStoredLang(lang: Lang): void {
  try {
    localStorage.setItem(STORAGE_KEY, lang);
  } catch {
    /* ignore */
  }
}

export function t(lang: Lang, key: string): string {
  const table = strings[lang] ?? strings.en;
  return table[key] ?? strings.en[key] ?? key;
}

export function continentName(lang: Lang, continentId: string): string {
  const key = continentId as keyof typeof strings.en;
  return t(lang, key) !== key ? t(lang, key) : continentId;
}

export function spinnerLabelKey(result: string): string {
  const map: Record<string, string> = {
    government: "spinner_government",
    military: "spinner_military",
    scientific: "spinner_scientific",
    obstacle: "spinner_obstacle",
    special: "spinner_special",
  };
  return map[result] ?? result;
}
