# 🛸 THE UFO DISCLOSURE GAME
## Game Design Document — Version 2.0
### Document Complet de Conception Jeu Vidéo

> *"La vérité n'attend pas qu'on soit prêt à l'entendre."*

**Basé sur :** The UFO Disclosure Game — Kenneth Media LTD (Londres, UK, 2025)  
**Type original :** Jeu de plateau modulaire coopératif / compétitif  
**Source :** Kickstarter officiel + documentation de campagne (campagne annulée le 2 juin 2025 — 4 445 € collectés sur 9 147 € d'objectif, 58 contributeurs)  
**Version GDD :** 2.0 — Enrichie & Précisée  
**Langue :** Français  

---

## TABLE DES MATIÈRES

1. [Vision & Positionnement](#1-vision--positionnement)
2. [Lore & Contexte Narratif](#2-lore--contexte-narratif)
3. [Joueurs Cibles & Expérience Attendue](#3-joueurs-cibles--expérience-attendue)
4. [Personnages Jouables — Fiches Complètes](#4-personnages-jouables--fiches-complètes)
5. [Structure d'une Partie](#5-structure-dune-partie)
6. [Modes de Jeu — Détail Complet](#6-modes-de-jeu--détail-complet)
7. [Le Plateau — Disclosure Path & Monde](#7-le-plateau--disclosure-path--monde)
8. [Système de Cartes — Règles Détaillées](#8-système-de-cartes--règles-détaillées)
9. [Mécaniques de Jeu — Arbre Décisionnel Complet](#9-mécaniques-de-jeu--arbre-décisionnel-complet)
10. [Les Trois Autorités — Approfondissement](#10-les-trois-autorités--approfondissement)
11. [Base de Données des Cas Réels](#11-base-de-données-des-cas-réels)
12. [Questions Trivia — Banque Enrichie](#12-questions-trivia--banque-enrichie)
13. [Questions Déduction — Banque Enrichie](#13-questions-déduction--banque-enrichie)
14. [Équilibre & Game Feel](#14-équilibre--game-feel)
15. [Adaptation Jeu Vidéo — Architecture Complète](#15-adaptation-jeu-vidéo--architecture-complète)
16. [UI/UX — Système Complet](#16-uiux--système-complet)
17. [Système Audio & Ambiance](#17-système-audio--ambiance)
18. [Progression, Méta & Rejouabilité](#18-progression-méta--rejouabilité)
19. [Architecture Technique](#19-architecture-technique)
20. [Roadmap & Contenu Post-Lancement](#20-roadmap--contenu-post-lancement)
21. [Annexes](#21-annexes)

---

## 1. VISION & POSITIONNEMENT

### 1.1 Pitch

> *"A Board Game of Truth, Mystery, and Investigation. Step into the shoes of journalists, investigators, pilots, and experiencers as you unravel real UFO cases, one clue at a time. Logic meets history in a thrilling race toward disclosure."*

**The UFO Disclosure Game** est un jeu éducatif et stratégique dans lequel 2 à 6 joueurs incarnent des enquêteurs tentant de faire éclater la vérité sur les phénomènes aériens non identifiés (UAP/OVNI). Pour gagner, chaque joueur doit compléter son **Disclosure Path** en obtenant la validation de **3 Autorités** (Gouvernement, Militaire, Scientifique) grâce à des réponses correctes à des questions de trivia et de déduction.

### 1.2 Piliers de Design

| Pilier | Description | Indicateur de Succès |
|---|---|---|
| **Fidélité factuelle** | Chaque cas est basé sur des événements documentés et vérifiables | 100% des cas sourcés officiellement |
| **Accessibilité** | Trivia pour grand public, Déduction pour joueurs analytiques | Score de satisfaction ≥ 4/5 par profil |
| **Rejouabilité** | 100+ cartes Trivia, 100+ Déduction, cas variés à chaque partie | Variance garantie sur 10 parties |
| **Tension narrative** | Sceptiques, Debunkers, MIB bloquent constamment la progression | Courbe de tension montante jusqu'à la fin |
| **Valeur éducative** | Le jeu apprend la vraie histoire des UAP au fil du jeu | Joueurs capables de citer 5 cas réels après une partie |

### 1.3 Références & Inspirations

| Jeu | Ce qu'on retient |
|---|---|
| **Ticket to Ride** | Déplacement continental simple et satisfaisant |
| **Pandemic** | Coopératif sous pression, sentiment d'urgence partagé |
| **Trivial Pursuit** | Structure trivia par thèmes, validation par secteurs |
| **Sherlock Holmes Consulting Detective** | Déduction narrative à partir de sources réelles |
| **Dead of Winter** | Atmosphère de suspicion, mécanique de trahison potentielle |
| **Timeline** | Cartes historiques pédagogiques, format accessible |

### 1.4 Proposition de Valeur Unique

- Seul jeu de plateau/vidéo entièrement dédié aux cas OVNI/UAP **réels et documentés**
- Mélange unique de **trivia factuelle** et de **raisonnement déductif**
- Thème d'une actualité brûlante (témoignages Congrès US 2023, AARO, déclassifications)
- Fonctionne comme un **outil pédagogique** déguisé en jeu compétitif

---

## 2. LORE & CONTEXTE NARRATIF

### 2.1 Contexte du Monde

Depuis 1947, des milliers de témoins crédibles — pilotes militaires, astronautes, policiers, civils de toutes nations — ont rapporté des observations d'objets aux comportements inexplicables par les technologies humaines connues.

Des programmes gouvernementaux secrets (Project Sign, Project Grudge, Project Blue Book, AATIP, Majestic-12) ont tenté de cataloguer ces phénomènes — et parfois de les dissimuler activement au public.

En 2017, le New York Times révèle l'existence de l'AATIP, programme militaire secret de 22 millions de dollars. En 2020, le Pentagone déclassifie officiellement trois vidéos militaires montrant des UAP. En 2021, l'ODNI publie un rapport officiel admettant 144 incidents inexpliqués. En 2023, David Grusch témoigne sous serment devant le Congrès que les États-Unis détiennent des "engins de fabrication non-humaine".

**La fenêtre de la Disclosure est entrouverte. Vous pouvez la pousser.**

### 2.2 Factions

#### Les Enquêteurs (Joueurs)
Six archétypes de personnes qui, pour des raisons différentes, cherchent à établir la vérité. Chacun dispose de compétences uniques et d'un point de départ géographique différent.

#### Les Trois Autorités (Objectifs à convaincre)
- 🏛️ **Gouvernement** — Institutions politiques, agences, élus
- ⚔️ **Militaire** — Forces armées, pilotes de combat, radars
- 🔬 **Scientifique** — Université, recherche académique, médecine

#### Les Obstacles (Antagonistes systémiques)
- 🤨 **Sceptiques** — Remettent en question sans mauvaise foi
- 🚫 **Debunkers** — Cherchent activement à invalider vos preuves
- 🕴️ **Men in Black (MIB)** — Agents de suppression, intimidateurs
- 🎭 **Hoaxes** — Fausses pistes qui gaspillent votre temps

### 2.3 Timeline Canonique du Jeu

```
ERA 1 : LES ORIGINES (1947–1969)
├── 1947 — Kenneth Arnold : premier "flying saucer"
├── 1947 — Incident de Roswell
├── 1952 — Vague de Washington D.C.
├── 1952 — Création de Project Blue Book
├── 1961 — Enlèvement Betty & Barney Hill
├── 1964 — Incident de Socorro (Lonnie Zamora)
└── 1969 — Fermeture de Project Blue Book

ERA 2 : LES TÉMOINS (1970–1989)
├── 1975 — Enlèvement de Travis Walton
├── 1979 — Incident de Kaikoura (Nouvelle-Zélande)
├── 1980 — Forêt de Rendlesham (UK)
└── 1989 — Affaire Bob Lazar / Zone 51

ERA 3 : LES PREUVES (1990–2016)
├── 1989–1990 — Vague belge (F-16 vs Triangle)
├── 1994 — École de Ruwa, Zimbabwe
├── 1997 — Lumières de Phoenix
├── 2004 — Incident Nimitz / Tic-Tac
└── 2006 — Observation O'Hare Airport

ERA 4 : THE DISCLOSURE (2017–Présent)
├── 2017 — Révélation AATIP (New York Times)
├── 2020 — Déclassification officielle Pentagone (3 vidéos)
├── 2021 — Rapport UAP ODNI (144 incidents non expliqués)
├── 2023 — Témoignage David Grusch au Congrès
└── En cours — Enquêtes AARO, auditions parlementaires
```

---

## 3. JOUEURS CIBLES & EXPÉRIENCE ATTENDUE

### 3.1 Profils Joueurs

| Profil | Description | Mode recommandé |
|---|---|---|
| **Le Curieux** | Intéressé par les OVNI mais sans connaissance approfondie | Coopératif, Trivia, Facile |
| **L'Expert** | Connaît les cas, veut être challengé | Compétitif, Mixte, Expert |
| **Le Stratège** | Aime l'optimisation et les systèmes | Asymétrique, Déduction |
| **Le Narrateur** | Cherche une expérience immersive et d'histoire | Campagne Solo, Audiobook activé |
| **Le Social** | Joue pour l'interaction et le débat | Coopératif 4-6 joueurs |

### 3.2 Courbe d'Apprentissage

```
PARTIE 1 (Découverte)
  → Comprendre le plateau et les déplacements
  → Découvrir le mécanisme de la toupie
  → Répondre aux premières questions Trivia

PARTIES 2-5 (Maîtrise)
  → Optimiser le chemin vers les 3 Autorités
  → Gérer les obstacles stratégiquement
  → Utiliser les capacités de son personnage

PARTIES 6+ (Expertise)
  → Jouer en mode Asymétrique et Expert
  → Anticiper les coups des adversaires
  → Maîtriser les questions Déduction avancées
```

### 3.3 Session de Jeu

| Mode | Joueurs | Durée estimée |
|---|---|---|
| Solo Campagne | 1 | 30–45 min |
| Compétitif standard | 2–4 | 45–75 min |
| Coopératif | 2–6 | 60–90 min |
| Mixed + Asymétrique | 3–6 | 75–120 min |

---

## 4. PERSONNAGES JOUABLES — FICHES COMPLÈTES

### Système de Personnages

Le jeu propose **6 types de personnages**, chacun avec **2 variantes**, soit **12 personnages uniques**. En mode Asymétrique, chaque personnage dispose d'un **Skill Token** activant ses capacités spéciales.

Chaque personnage possède 5 attributs notés de 1 à 5 étoiles :
- **Force Gouvernement** : facilité à valider l'Autorité politique
- **Force Militaire** : facilité à valider l'Autorité de défense
- **Force Scientifique** : facilité à valider l'Autorité académique
- **Mobilité** : capacités de déplacement sur le plateau
- **Résistance** : tolérance aux obstacles (Skeptic, Debunker, MIB)

---

### 🎙️ JOURNALISTE

*"La vérité a un droit d'être publiée. Et je m'assurerai qu'elle le soit."*

**Concept :** Professionnel des médias exploitant ses réseaux d'information pour exposer les preuves. Fort en mobilité et en contournement des Debunkers.

| Attribut | Note |
|---|---|
| Force Gouvernement | ★★★ |
| Force Militaire | ★★ |
| Force Scientifique | ★★ |
| Mobilité | ★★★★ |
| Résistance | ★★★ |

**Capacités Actives (Mode Asymétrique) :**
- **Publication Express** : Peut jouer une carte Whistleblower pour annuler l'effet d'une Debunker Card (1x par partie)
- **Réseau de Sources** : Pioche 1 carte supplémentaire lors d'un événement Mass Sighting
- **Couverture Terrain** : +1 case de déplacement si une Event Card est active dans la région de destination

**Continent de départ :** Europe ou Amérique du Nord

**Variante A — Journaliste d'Investigation :**
Spécialisé dans les fuites gouvernementales et les documents classifiés. Peut regarder la carte du dessus du Deck Sceptique avant qu'elle soit retournée. Bonus de +1 sur toutes les questions liées aux programmes secrets (Blue Book, AATIP, Majestic-12).

**Variante B — Journaliste de Terrain :**
Spécialisé dans le reportage direct et le témoignage. Peut bouger d'un continent supplémentaire si une Event Card est active dans la région de destination. Fort sur les questions de témoins oculaires.

---

### ✈️ PILOTE

*"J'ai vu ce que j'ai vu. J'ai 14 ans de vol militaire. Je n'hallucine pas."*

**Concept :** Témoin direct d'observations aériennes, bénéficiant d'une crédibilité institutionnelle forte auprès des autorités militaires.

| Attribut | Note |
|---|---|
| Force Gouvernement | ★★ |
| Force Militaire | ★★★★★ |
| Force Scientifique | ★★ |
| Mobilité | ★★★★ |
| Résistance | ★★★ |

**Capacités Actives (Mode Asymétrique) :**
- **Rapport de Vol** : Obtient automatiquement +1 token de confirmation sur l'axe Militaire au début de la partie
- **Immunité Technique** : Ignore complètement les effets des Hoax Cards (les retourne sans conséquence)
- **Navigation Directe** : Peut choisir sa destination sans lancer le dé, une fois par partie

**Continent de départ :** Amérique du Nord

**Variante A — Pilote de Chasse Militaire :**
Référence directe aux pilotes comme David Fravor (Nimitz) ou les pilotes belges de 1990. Peut annuler une question Sceptique, une fois par partie ("Mon témoignage radar est irréfutable"). Bonus fort sur les cas militaires.

**Variante B — Pilote Civil Commercial :**
Moins crédible militairement mais ancré dans les réseaux civils internationaux. +1 case de mouvement sur toutes les destinations. Fort sur les cas d'observation commerciale (JAL 1628, O'Hare 2006).

---

### 🔍 INVESTIGATEUR UFO

*"Chaque cas a une explication. Ma mission est de trouver la vraie."*

**Concept :** Expert spécialisé dans l'analyse des phénomènes aériens. La connaissance encyclopédique est son arme principale.

| Attribut | Note |
|---|---|
| Force Gouvernement | ★★ |
| Force Militaire | ★★ |
| Force Scientifique | ★★★ |
| Mobilité | ★★ |
| Résistance | ★★★★ |

**Capacités Actives (Mode Asymétrique) :**
- **Choix Éclairé** : Peut choisir entre une question Trivia ou Déduction (au lieu du tirage aléatoire)
- **Indice Préliminaire** : Reçoit un indice contextuel avant de répondre à une question Déduction
- **Récupération d'Enquête** : Peut convertir un échec face à une Skeptic Card en "pause technique" sans perte de tour (1x par partie)

**Continent de départ :** Amérique du Nord

**Variante A — Chercheur MUFON :**
Lié au plus grand réseau d'enquêteurs civils au monde. En mode coopératif, peut partager ses preuves avec un autre joueur (lui transmettre un token de confirmation). Fort sur les bases de données de cas.

**Variante B — Ex-Agent Gouvernemental :**
Ancien employé d'un programme classifié. Accès direct aux questions de niveau Avancé avec un bonus de +1 sur la marge de réussite. Peut lire la Debunker Card avant de décider s'il la défend ou l'absorbe.

---

### 👁️ EXPERIENCER (Témoin)

*"Ce que j'ai vécu ne peut pas être expliqué. Mais je ne suis pas fou."*

**Concept :** Personne ayant vécu un contact ou une observation directe. Sa connaissance est intuitive, pas académique — mais son témoignage de première main a une valeur unique.

| Attribut | Note |
|---|---|
| Force Gouvernement | ★★ |
| Force Militaire | ★ |
| Force Scientifique | ★★★ |
| Mobilité | ★★ |
| Résistance | ★★ |

**Capacités Actives (Mode Asymétrique) :**
- **Vision Réduite** : Voit seulement 2 options de réponse sur les cartes Trivia (au lieu de 4), augmentant ses chances de réussite
- **Immunité MIB** : Les Men in Black l'ignorent une fois par partie ("ils ne savent pas que je parle")
- **Témoignage Direct** : Bonus de +1 sur l'axe Scientifique (la science étudie les témoignages de première main)

**Continent de départ :** Variable selon l'expérience vécue

**Variante A — Témoin Visuel :**
A observé un OVNI de près, en plein jour, avec des traces physiques. Fort sur les questions d'observation sensorielle, de physique des phénomènes et de cas avec landing traces.

**Variante B — Contact Psychique :**
Prétend avoir reçu des informations lors d'un contact mental. Peut "deviner" une réponse sans conséquence en cas d'échec, une fois par partie. Controversé mais crédible pour l'Autorité Scientifique dans le cadre des études sur la conscience.

---

### 🛸 ABDUCTEE (Enlevé)

*"Ils m'ont ramené. Ce qu'ils m'ont montré change tout ce qu'on croit savoir."*

**Concept :** Personne ayant vécu une expérience d'abduction. Connaissance unique mais crédibilité institutionnelle faible — sauf auprès de la science médicale et psychiatrique.

| Attribut | Note |
|---|---|
| Force Gouvernement | ★ |
| Force Militaire | ★ |
| Force Scientifique | ★★★★ |
| Mobilité | ★★ |
| Résistance | ★★ |

**Capacités Actives (Mode Asymétrique) :**
- **Connaissance Intérieure** : Peut accéder directement aux questions de niveau Avancé sans prérequis
- **Retournement Psychique** : Peut retourner une Debunker Card sans l'appliquer, une fois par partie ("je connais la vérité de l'intérieur")
- **Spécialité Abduction** : Bonus automatique sur tous les cas d'abduction et d'implants

**Continent de départ :** Amérique du Nord ou Europe

**Variante A — Abductee Classique (1970–1989) :**
Travis Walton, Betty Hill — expériences de l'ère "classique". Fort sur les cas historiques et les questions médicales liées aux abductions.

**Variante B — Abductee Moderne (Post-2000) :**
Expériences récentes, souvent corrélées aux incidents militaires. Fort sur les cas post-2000 et les questions sur les UAP militaires.

---

### 👮 OFFICIER DE POLICE

*"Mon rapport officiel est dans le dossier depuis 30 ans. Quelqu'un devrait le lire."*

**Concept :** Représentant de la loi ayant témoigné d'une observation. Sa crédibilité institutionnelle est maximale auprès du Gouvernement.

| Attribut | Note |
|---|---|
| Force Gouvernement | ★★★★★ |
| Force Militaire | ★★★ |
| Force Scientifique | ★ |
| Mobilité | ★★ |
| Résistance | ★★★★ |

**Capacités Actives (Mode Asymétrique) :**
- **Rapport Officiel** : Les confirmations de l'Autorité Gouvernementale nécessitent une question de moins (2 au lieu de 3)
- **Protection Légale** : En mode coopératif, peut "protéger" un autre joueur d'une Men in Black Card
- **Crédibilité Institutionnelle** : Bonus de +1 sur tous les jets liés au Gouvernement

**Continent de départ :** Amérique du Nord ou Europe

**Variante A — Shérif Rural (Cas Classiques) :**
Référence à Lonnie Zamora (Socorro 1964). Spécialisé sur les anciennes affaires. Fort sur les questions pré-1980, en particulier les cas avec landing traces et témoins isolés.

**Variante B — Officier Urbain (Cas Modernes) :**
Témoin d'un cas récent dans un contexte urbain ou aéroportuaire. Fort sur les questions post-1990, notamment les phénomènes technologiques et les cas avec vidéos.

---

### 4.1 Tableau Comparatif Complet

| Rôle | Gouv. | Mil. | Sci. | Mob. | Rés. | Difficulté recommandée |
|---|---|---|---|---|---|---|
| Journaliste | ★★★ | ★★ | ★★ | ★★★★ | ★★★ | Débutant / Intermédiaire |
| Pilote | ★★ | ★★★★★ | ★★ | ★★★★ | ★★★ | Intermédiaire |
| Investigateur | ★★ | ★★ | ★★★ | ★★ | ★★★★ | Intermédiaire / Avancé |
| Experiencer | ★★ | ★ | ★★★ | ★★ | ★★ | Débutant |
| Abductee | ★ | ★ | ★★★★ | ★★ | ★★ | Avancé |
| Officier Police | ★★★★★ | ★★★ | ★ | ★★ | ★★★★ | Débutant / Intermédiaire |

---

## 5. STRUCTURE D'UNE PARTIE

### 5.1 Setup Complet

```
ÉTAPE 1 — CHOIX DES RÔLES
├── Chaque joueur sélectionne parmi les 6 types de personnages
├── Chaque type a 2 variantes → 12 personnages uniques
├── En mode Asymétrique : activer le Skill Token correspondant
└── Règle optionnelle : draft des personnages (chacun en bannit un)

ÉTAPE 2 — PLACEMENT DES PIONS
└── Chaque personnage commence sur son continent de départ
   (voir fiche de personnage — peut varier selon scénario)

ÉTAPE 3 — DISTRIBUTION DES COMPOSANTS
├── 1 Disclosure Path mini-plateau individuel par joueur
├── 3 Confirmation Tokens translucides par joueur
├── 1 Pion par joueur
└── 1 Skill Token par joueur (mode asymétrique uniquement)

ÉTAPE 4 — DISTRIBUTION DES EVENT CARDS
├── Mode Standard : 3 Event Cards par joueur (face cachée)
├── Mode Rapide : 2 Event Cards par joueur
├── Mode Expert : 4 Event Cards par joueur
└── En coopératif : poolées sur la table, partagées

ÉTAPE 5 — PRÉPARATION DES DECKS
├── Deck Événements (Event Deck) — face cachée, battu
├── Deck Histoire (History Deck) :
│   ├── Mode Trivia pur : 50 cartes Trivia seulement
│   ├── Mode Déduction pur : 50 cartes Déduction seulement
│   └── Mode Mixte : les deux decks mélangés
├── Deck Sceptique (Skeptic Deck) — face cachée, battu
└── Deck Debunker — face cachée, battu

ÉTAPE 6 — OUTILS PARTAGÉS
├── Toupie Flying Saucer Spinner — centre de la table
└── Dé à 6 faces — centre de la table

ÉTAPE 7 — CHOIX DU MODE
├── Compétitif ou Coopératif
├── Trivia, Déduction, ou Mixed Mode
└── Symétrique ou Asymétrique (Skill Tokens actifs)
```

### 5.2 Déroulement d'un Tour Complet

```
═══════════════════════════════════════════════════
               TOUR D'UN JOUEUR (5 PHASES)
═══════════════════════════════════════════════════

PHASE 1 — DÉPLACEMENT
  └─ Lancer le dé (1–6) OU utiliser une capacité spéciale
  └─ Se déplacer sur autant de continents adjacents
  └─ Option : dépenser 1 token pour bouger d'un extra

PHASE 2 — VÉRIFICATION EVENT CARD
  └─ Le continent d'arrivée correspond-il à une Event Card ?
      OUI ─► Entrer en Phase 3
      NON ─► Piocher une carte Event si disponible, ou
              passer au joueur suivant (tour neutre)

PHASE 3 — LANCER DE LA TOUPIE (FLYING SAUCER SPINNER)
  └─ Faire tourner la toupie
  └─ Résultat ?
      🏛️ GOUVERNEMENT ─► Voir Phase 4 (si Autorité recherchée)
      ⚔️ MILITAIRE ─────► Voir Phase 4 (si Autorité recherchée)
      🔬 SCIENTIFIQUE ──► Voir Phase 4 (si Autorité recherchée)
      ─── Mauvaise Autorité ─► Bonus mineur ou tour neutre
      ⚠️  OBSTACLE ──────► Piocher Skeptic OU Debunker Card
      ⭐  SPÉCIAL ───────► Activer événement Mass Sighting /
                           Whistleblower / MIB / autre

PHASE 4 — DISCLOSURE PATH (si toupie = bonne Autorité)
  ┌─ Question History Card 1
  │   ├─ BONNE RÉPONSE ──► Question 2
  │   └─ MAUVAISE RÉPONSE ─► Sortir du Path, fin du tour
  ├─ Question History Card 2
  │   ├─ BONNE RÉPONSE ──► Question 3
  │   └─ MAUVAISE RÉPONSE ─► Sortir du Path, fin du tour
  └─ Question History Card 3
      ├─ BONNE RÉPONSE ──► +1 Confirmation Token sur cet axe
      └─ MAUVAISE RÉPONSE ─► Sortir du Path, fin du tour

  NOTE : 3 Confirmation Tokens sur un axe = Autorité CONFIRMÉE

PHASE 5 — GESTION DES OBSTACLES (si toupie = Obstacle)
  ├─ Skeptic Card ──► Répondre correctement OU perdre 1 tour
  ├─ Debunker Card ─► Défendre les preuves OU pénalité de mouvement
  ├─ Men in Black ──► Sauter 1 tour + Event Card bloquée
  └─ Hoax Card ─────► Tour gaspillé, piocher nouvelle Event Card

═══════════════════════════════════════════════════
```

### 5.3 Conditions de Victoire

**Mode Compétitif :**
Le premier joueur à compléter son Disclosure Path en intégralité (3 Confirmation Tokens sur chacun des 3 axes = 9 tokens au total) gagne la partie et déclenche la **Full Disclosure**.

**Mode Coopératif :**
L'équipe gagne si elle parvient collectivement à réunir le nombre requis de confirmations avant que le Deck Events ne soit épuisé. Défaite collective si le deck se vide avant la victoire.

**Condition de défaite individuelle (optionnel, mode hardcore) :**
Un joueur est éliminé s'il échoue à 3 Skeptic Cards consécutives (sa crédibilité est détruite).

---

## 6. MODES DE JEU — DÉTAIL COMPLET

### 6.1 MODE COMPÉTITIF — "Race to Disclosure"

**Concept :** Chaque joueur joue pour lui-même. Premier arrivé, premier gagnant.

**Règles spécifiques :**
- Les Debunker Cards peuvent être jouées contre un adversaire (en compétitif uniquement)
- Il est possible de "bloquer" la progression d'un adversaire via des cartes spéciales
- La toupie crée de l'aléatoire stratégique — vous ne contrôlez pas quelle Autorité elle désigne

**Tensions compétitives :**
- Choisir entre avancer soi-même vs ralentir un adversaire
- Gérer son pool de cartes spéciales (quand jouer son Skill Token ?)
- Bluffer sur ses Event Cards actives

**Variante "Course Rapide" :** Chaque Autorité ne nécessite que 2 tokens au lieu de 3.

---

### 6.2 MODE COOPÉRATIF — "Operation Disclosure"

**Concept :** Toute l'équipe forme un groupe d'enquêteurs. Victoire ou défaite collective.

**Mécaniques spécifiques :**
- **Collaborative Clues** : Les joueurs peuvent s'échanger des indices avant de répondre
- **Pooling de Tokens** : Les Confirmation Tokens sont partagés sur un plateau central
- **Défense Collective** : Plusieurs joueurs peuvent contribuer à répondre à une Debunker Card difficile
- **Spécialisation** : Chaque personnage prend en charge les questions de sa spécialité

**Condition de défaite :**
- Le Deck Events est épuisé avant la Full Disclosure collective
- OU tous les joueurs sont bloqués simultanément par les MIB

**Variante "Hard Mode" :** Les questions ne peuvent être discutées qu'en 10 secondes avant réponse.

---

### 6.3 MODE ASYMÉTRIQUE

**Concept :** Superposition sur le mode Compétitif ou Coopératif — active les capacités spéciales de chaque rôle.

**Activation :**
- Chaque joueur reçoit son Skill Token au début de la partie
- Certaines capacités sont passives (toujours actives), d'autres sont actives (à dépenser)
- Le Skill Token retourné indique qu'une capacité active a été utilisée

**Équilibre :**
- Les capacités actives ne sont utilisables qu'une fois par partie (token retourné)
- Les capacités passives s'appliquent toujours mais de façon limitée
- L'Investigateur UFO (le plus puissant en knowledge) a les mobilités les plus faibles

---

### 6.4 MODE TRIVIA PUR

- Seules les 50 cartes Trivia du History Deck
- Questions factuelles : dates, noms, lieux, événements
- Idéal pour les connaisseurs du sujet ou comme mode d'introduction
- Format rapide (45 min pour 4 joueurs)

---

### 6.5 MODE DÉDUCTION PUR

- Seules les 50 cartes Déduction du History Deck
- Scénarios logiques à analyser, puzzles physiques
- Idéal pour les profils analytiques et les joueurs stratégiques
- Format légèrement plus long (60 min pour 4 joueurs)

---

### 6.6 MODE MIXTE — "Mixed Mode"

- Les deux decks mélangés — chaque tirage est une surprise
- Expérience la plus variée et la plus équilibrée
- Recommandé pour les groupes expérimentés
- Format standard (60–90 min pour 4 joueurs)

---

### 6.7 MODE CAMPAGNE SOLO (Extension jeu vidéo)

Progression narrative en 5 actes basée sur la timeline réelle des UAP :

| Acte | Période | Personnage conseillé | Cas principaux |
|---|---|---|---|
| Acte 1 — "Les Origines" | 1947–1952 | Journaliste, Officier | Roswell, Arnold, Blue Book |
| Acte 2 — "La Vague" | 1952–1969 | Pilote, Investigateur | Washington DC, Zamora, Blue Book |
| Acte 3 — "Les Témoins" | 1970–1989 | Abductee, Experiencer | Betty Hill, Walton, Lazar |
| Acte 4 — "Les Preuves" | 1990–2017 | Tous disponibles | Rendlesham, Phoenix, Nimitz, AATIP |
| Acte 5 — "The Disclosure" | 2017–Présent | Tous disponibles | Rapport UAP, Grusch, AARO |

---

## 7. LE PLATEAU — DISCLOSURE PATH & MONDE

### 7.1 Le Plateau Principal (Carte du Monde)

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CARTE DU MONDE — UFO DISCLOSURE                 │
│                                                                     │
│  ┌─────────────────┐   ┌──────────────┐   ┌───────────────┐        │
│  │  AMÉRIQUE       │   │   EUROPE     │   │     ASIE      │        │
│  │  DU NORD        │   │              │   │               │        │
│  │  ★ Zone 51      │   │ ★ Rendlesham │   │ ★ JAL 1628   │        │
│  │  ★ Roswell      │   │ ★ Hessdalen │   │               │        │
│  └─────────────────┘   └──────────────┘   └───────────────┘        │
│                                                                     │
│  ┌─────────────────┐   ┌──────────────┐   ┌───────────────┐        │
│  │  AMÉRIQUE       │   │   AFRIQUE    │   │   OCÉANIE     │        │
│  │  DU SUD         │   │              │   │               │        │
│  │  ★ Villas Boas  │   │ ★ Ruwa ZW   │   │ ★ Kaikoura   │        │
│  └─────────────────┘   └──────────────┘   └───────────────┘        │
│                                                                     │
│  LÉGENDE : ★ = Zone Hotspot (bonus de confirmation si on s'y rend)  │
│  Les continents sont reliés par des routes maritimes et aériennes   │
└─────────────────────────────────────────────────────────────────────┘
```

**Zones Spéciales (Hotspots) :**
Les hotspots sont des cases bonus sur certains continents associées à des cas emblématiques. Atterrir dessus confère un avantage :
- **Zone 51 / Roswell** : +1 token Gouvernement ou Militaire gratuit (1x par partie par joueur)
- **Rendlesham Forest** : Immunité aux Debunkers pour ce tour
- **École de Ruwa** : Peut poser une question au deck Scientifique gratuitement
- **Hessdalen** : Voir la prochaine Event Card avant de lancer la toupie

**Règles de Déplacement :**
- Les continents sont adjacents selon la carte réelle (l'Amérique du Nord est adjacente à l'Europe et à l'Amérique du Sud)
- Chaque lancer de dé permet de se déplacer d'autant de continents
- Passer par un continent ≠ s'y arrêter (sauf si une Event Card le requiert)

---

### 7.2 Le Disclosure Path (Mini-Plateau Individuel)

Chaque joueur possède son propre Disclosure Path — un mini-plateau de suivi de progression.

```
╔═══════════════════════════════════════════════════════╗
║           DISCLOSURE PATH — [NOM DU JOUEUR]          ║
║           Rôle : [PERSONNAGE] — [VARIANTE]            ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║  🏛️  GOUVERNEMENT   [ ○ ] [ ○ ] [ ○ ]  → ✓ CONFIRMÉ ║
║                                                       ║
║  ⚔️  MILITAIRE      [ ○ ] [ ○ ] [ ○ ]  → ✓ CONFIRMÉ ║
║                                                       ║
║  🔬  SCIENTIFIQUE   [ ○ ] [ ○ ] [ ○ ]  → ✓ CONFIRMÉ ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║  FULL DISCLOSURE : 3 axes confirmés = VICTOIRE       ║
╚═══════════════════════════════════════════════════════╝
```

- `○` = Slot vide
- `●` = Confirmation Token placé
- 3 tokens sur un axe = Autorité confirmée
- 3 Autorités confirmées = Full Disclosure = Victoire

---

### 7.3 La Toupie Flying Saucer Spinner — Mécanique Détaillée

La toupie est l'outil de randomisation principal. Elle est lancée quand un joueur atterrit sur un continent correspondant à une de ses Event Cards actives.

**Secteurs de la toupie (répartition indicative) :**

| Secteur | Probabilité approx. | Effet |
|---|---|---|
| 🏛️ GOUVERNEMENT | 20% | Validation politique possible |
| ⚔️ MILITAIRE | 20% | Validation défense possible |
| 🔬 SCIENTIFIQUE | 20% | Validation académique possible |
| ⚠️ OBSTACLE | 25% | Piocher Skeptic ou Debunker |
| ⭐ SPÉCIAL | 15% | Mass Sighting, Whistleblower, MIB |

**Note de design :** La probabilité de tomber sur la "bonne" Autorité est de ~20% par lancer. Cela crée une tension réelle — il faut parfois s'y reprendre à plusieurs fois. Les capacités des personnages permettent de contourner ou de modifier ce hasard.

---

## 8. SYSTÈME DE CARTES — RÈGLES DÉTAILLÉES

### 8.1 EVENT CARDS

**Quantité :** 70 cartes (selon le contenu officiel Kickstarter)  
**Distribution :** 3 par joueur en début de partie (mode standard)

**Anatomie d'une Event Card :**

```
┌──────────────────────────────────────────────────────┐
│  🛸 EVENT CARD                        NIVEAU : ●●●  │
│  ─────────────────────────────────────────────────   │
│  [ILLUSTRATION DU CAS]                               │
│                                                      │
│  TITRE : Incident Nimitz / Tic-Tac                  │
│  ANNÉE : 2004                                        │
│  CONTINENT : Amérique du Nord                        │
│  AUTORITÉ REQUISE : ⚔️ Militaire                    │
│                                                      │
│  ─────────────────────────────────────────────────   │
│  DESCRIPTION :                                       │
│  Des pilotes de F/A-18 de l'USS Nimitz filment       │
│  un objet elliptique aux capacités impossibles       │
│  au large de San Diego, Californie.                  │
│                                                      │
│  EFFET :                                             │
│  Quand vous êtes en Amérique du Nord, lancez         │
│  la toupie pour tenter la confirmation Militaire.   │
│                                                      │
│  BONUS HOTSPOT :                                     │
│  +1 case de mouvement si vous venez d'une zone       │
│  militaire américaine.                               │
└──────────────────────────────────────────────────────┘
```

**Règles des Event Cards :**
- En mode compétitif : les cartes restent secrètes jusqu'à leur activation
- En mode coopératif : les cartes peuvent être partagées et discutées ouvertement
- Une carte peut être abandonnée (défaussée) pour en piocher une nouvelle, mais seulement si une Hoax Card force cela
- Les cartes n'expirent pas — elles restent valides jusqu'à leur résolution ou abandon

**Liste complète des Event Cards (25 cartes de base illustrées) :**

| # | Titre | Continent | Autorité | Niveau |
|---|---|---|---|---|
| E01 | Roswell Crash (1947) | Amér. Nord | Gouvernement | ★ |
| E02 | Observation Kenneth Arnold (1947) | Amér. Nord | Gouvernement | ★ |
| E03 | Vague de Washington D.C. (1952) | Amér. Nord | Gouvernement | ★★★ |
| E04 | Enlèvement Betty & Barney Hill (1961) | Amér. Nord | Scientifique | ★★ |
| E05 | Incident de Socorro / Zamora (1964) | Amér. Nord | Gouvernement | ★ |
| E06 | Crash de Shag Harbour (1967) | Amér. Nord | Militaire | ★★ |
| E07 | Enlèvement Travis Walton (1975) | Amér. Nord | Scientifique | ★★ |
| E08 | Incident de Rendlesham Forest (1980) | Europe | Militaire | ★★ |
| E09 | Affaire Bob Lazar / Zone 51 (1989) | Amér. Nord | Gouvernement | ★★★ |
| E10 | Vague belge — F-16 vs Triangle (1989–90) | Europe | Militaire | ★★ |
| E11 | Incident de l'École de Ruwa (1994) | Afrique | Scientifique | ★★ |
| E12 | Lumières de Phoenix (1997) | Amér. Nord | Gouvernement | ★★ |
| E13 | Incident Nimitz / Tic-Tac (2004) | Amér. Nord | Militaire | ★★★ |
| E14 | Observation O'Hare Airport (2006) | Amér. Nord | Gouvernement | ★ |
| E15 | Vidéos Go Fast & Gimbal — US Navy (2015) | Amér. Nord | Militaire | ★★ |
| E16 | Révélation AATIP — NYT (2017) | Amér. Nord | Gouvernement | ★★★ |
| E17 | Rapport UAP ODNI (2021) | Amér. Nord | Gouvernement | ★★★ |
| E18 | Témoignage David Grusch au Congrès (2023) | Amér. Nord | Gouvernement | ★★★ |
| E19 | Flight JAL 1628 (1986) | Asie | Militaire | ★★ |
| E20 | Lumières de Hessdalen (permanent) | Europe | Scientifique | ★★★ |
| E21 | Enlèvement Antonio Villas Boas (1957) | Amér. Sud | Scientifique | ★★★ |
| E22 | Crop Circles de Wiltshire | Europe | Scientifique | ★★ |
| E23 | Great Airship Wave 1896–97 | Amér. Nord | Gouvernement | ★★★ |
| E24 | Crash de Kecksburg (1965) | Amér. Nord | Militaire | ★★ |
| E25 | Fastwalkers NORAD | Amér. Nord | Militaire | ★★★ |

---

### 8.2 HISTORY CARDS — TRIVIA (50 cartes)

**Format :** Question + 4 réponses en choix multiple + contexte éducatif affiché après réponse

**Niveaux de difficulté :**
- ★ Débutant : faits généraux largement connus
- ★★ Intermédiaire : dates précises, noms de programmes, détails techniques
- ★★★ Avancé : nuances, controverses, informations déclassifiées récentes

*(Voir section 12 pour la banque de questions enrichie)*

---

### 8.3 HISTORY CARDS — DÉDUCTION (50 cartes)

**Format :** Scénario avec éléments logiques + question de raisonnement + explication après réponse

**Types de scénarios :**
- Analyse physique d'un phénomène observé (vitesse, G-forces, signatures radar)
- Croisement de témoignages indépendants
- Interprétation de données d'enquête
- Raisonnement par élimination sur les explications alternatives

*(Voir section 13 pour la banque de questions enrichie)*

---

### 8.4 SKEPTIC CARDS (~40 cartes selon Kickstarter)

**Déclencheur :** Toupie → zone Obstacle OU événement spécifique

**Mécanique :**
- Question à répondre correctement pour continuer
- **Succès** → Investigation continue normalement
- **Échec** → Perdre son prochain tour (l'enquête est mise en pause)

**Thèmes des Skeptic Cards :**
- Biais cognitifs et psychologie du témoignage
- Explications alternatives plausibles (météo, drones, ballons)
- Limites méthodologiques des enquêtes ufologiques
- Critiques académiques légitimes

**Exemple de Skeptic Card :**
```
┌──────────────────────────────────────────────────────┐
│  🤨 SKEPTIC CARD                                     │
│  ─────────────────────────────────────────────────   │
│  UN SCEPTIQUE INTERROGE VOS PREUVES :                │
│                                                      │
│  "Les observations nocturnes de lumières sont        │
│  souvent confondues avec des phénomènes naturels.    │
│  Quel phénomène atmosphérique peut créer des         │
│  lumières lentement mouvantes la nuit ?"             │
│                                                      │
│  A) Le feu Saint-Elme                                │
│  B) La lune des moissons                             │
│  C) Les plasma balls de Hessdalen    ✓               │
│  D) Les éclairs en boule                             │
│                                                      │
│  ✅ Succès : Continuez votre investigation           │
│  ❌ Échec : Perdez votre prochain tour               │
└──────────────────────────────────────────────────────┘
```

---

### 8.5 DEBUNKER CARDS (~40 cartes selon Kickstarter)

**Déclencheur :** Toupie → zone Obstacle OU jouée par un adversaire (mode compétitif)

**Mécanique :**
- Plus agressives que les Skeptic Cards
- **Défense réussie** → Continuer + bonus +1 token (optionnel selon règles)
- **Défense échouée** → Ralentissement : -1 case de déplacement au prochain tour

**Exemple de Debunker Card :**
```
┌──────────────────────────────────────────────────────┐
│  🚫 DEBUNKER CARD                                    │
│  ─────────────────────────────────────────────────   │
│  UN DEBUNKER ATTAQUE VOS PREUVES :                   │
│                                                      │
│  "Les Lumières de Phoenix en 1997 ont été            │
│  officiellement expliquées par des fusées            │
│  éclairantes militaires. Ce cas est résolu."         │
│                                                      │
│  DÉFENDEZ-VOUS :                                     │
│  Quel élément technique de l'observation rend        │
│  l'explication par fusées éclairantes insuffisante ? │
│                                                      │
│  A) Les lumières avançaient trop vite                │
│  B) La V-formation a été observée des heures avant   │
│     les fusées, par des témoins différents  ✓       │
│  C) Les fusées laissent une traînée visible          │
│  D) Les militaires ont nié avoir effectué des        │
│     exercices ce soir-là                             │
│                                                      │
│  ✅ Défense réussie : Continuez + bonus token        │
│  ❌ Défense échouée : -1 déplacement prochain tour   │
└──────────────────────────────────────────────────────┘
```

---

### 8.6 CARTES ÉVÉNEMENTS SPÉCIAUX

#### MASS SIGHTING CARD
```
DÉCLENCHEUR : Toupie → zone Spéciale ★

EFFET : Tous les joueurs présents sur le même continent
peuvent avancer d'1 case sur leur Disclosure Path
(n'importe quel axe de leur choix).

EXEMPLE DE CAS : Lumières de Phoenix 1997 —
observées par des milliers de personnes simultanément.

CONDITION : S'active uniquement si au moins 2 joueurs
sont sur le même continent.
```

#### WHISTLEBLOWER CARD
```
DÉCLENCHEUR : Toupie → zone Spéciale ★ (rare)

EFFET : Le joueur actif gagne +1 Confirmation Token
sur n'importe quel axe de son choix — sans répondre
à une question.

EXEMPLE : David Grusch témoigne au Congrès — une
source interne parle enfin publiquement.

LIMITE : 1 seule Whistleblower Card active à la fois.
```

#### MEN IN BLACK (MIB) CARD
```
DÉCLENCHEUR : Toupie → zone Spéciale ★ (négatif)

EFFET : La cible désignée (le joueur actif ou le joueur
en tête) doit :
1. Sauter son prochain tour complet
2. Ne peut pas utiliser ses Event Cards ce tour-là

CONTRE-MESURE : L'Officier de Police peut protéger
un allié (mode coopératif). L'Experiencer est immunisé
une fois par partie.

EXEMPLE : Intimidation de témoins par des agents
non identifiés après des observations sensibles.
```

#### HOAX CARD
```
DÉCLENCHEUR : Zones spécifiques du plateau

EFFET :
1. Le joueur actif doit défausser son Event Card active
2. Pioche une nouvelle Event Card en remplacement
3. Son tour est terminé (aucune autre action possible)

EXEMPLE : Un faux témoignage dilue l'enquête et fait
perdre du temps et des ressources à l'investigateur.

CONTRE-MESURE : Le Pilote est immunisé aux Hoax Cards.
```

---

## 9. MÉCANIQUES DE JEU — ARBRE DÉCISIONNEL COMPLET

### 9.1 Arbre Complet du Tour

```
START : Début du tour d'un joueur
        │
        ▼
[PHASE 1] Lancer le dé (1–6) / Utiliser capacité de mouvement
        │
        ▼
[PHASE 2] Se déplacer vers un continent
        │
    ┌───▼───┐
    │Event  │ Le continent correspond-il à une Event Card ?
    │Check  │
    └───┬───┘
     OUI│              NON
        │               └──► [Fin de tour : passer au suivant]
        ▼                     OU [Piocher une Event Card]
[PHASE 3] Lancer la toupie FLYING SAUCER SPINNER
        │
        ├──► 🏛️ GOUVERNEMENT
        │         ├─ Autorité cherchée = GOV ?
        │         │   OUI → [PHASE 4] Disclosure Path
        │         │   NON → Bonus mineur (+1 mouvement futur) / Tour neutre
        │
        ├──► ⚔️ MILITAIRE
        │         ├─ Autorité cherchée = MIL ?
        │         │   OUI → [PHASE 4] Disclosure Path
        │         │   NON → Bonus mineur / Tour neutre
        │
        ├──► 🔬 SCIENTIFIQUE
        │         ├─ Autorité cherchée = SCI ?
        │         │   OUI → [PHASE 4] Disclosure Path
        │         │   NON → Bonus mineur / Tour neutre
        │
        ├──► ⚠️ OBSTACLE
        │         ├─ Piocher une carte : Skeptic OU Debunker (50/50)
        │         └─ [PHASE 5] Résolution de l'obstacle
        │
        └──► ⭐ SPÉCIAL
                  ├─ Piocher dans le deck Événements Spéciaux
                  └─ Appliquer l'effet (Mass Sighting, Whistleblower, MIB, Hoax)

─────────────────────────────────────────────────────

[PHASE 4] DISCLOSURE PATH (Séquence 3 questions)
        │
        ▼
   Question 1 (History Card tirée aléatoirement ou choisie par l'Investigateur)
        │
   ┌────▼────┐
   │ TIMER   │ (30s standard / 15s Expert / 45s Facile)
   └────┬────┘
   BONNE RÉPONSE        MAUVAISE RÉPONSE
        │                     │
        ▼                     └──► Sortie du Path — fin du tour
   Question 2                      (tentative au prochain tour)
        │
   BONNE RÉPONSE        MAUVAISE RÉPONSE
        │                     │
        ▼                     └──► Sortie du Path — fin du tour
   Question 3
        │
   BONNE RÉPONSE        MAUVAISE RÉPONSE
        │                     │
        ▼                     └──► Sortie du Path — fin du tour
   +1 CONFIRMATION TOKEN sur l'axe correspondant
        │
        ▼
   Cet axe a-t-il maintenant 3 tokens ?
   OUI → AUTORITÉ CONFIRMÉE ✓
   NON → Progression partielle sauvegardée

─────────────────────────────────────────────────────

[PHASE 5] RÉSOLUTION D'OBSTACLE
        │
   ┌────▼─────────────────────────────────┐
   │ TYPE D'OBSTACLE ?                    │
   └────┬─────────────────────────────────┘
        │
        ├──► SKEPTIC CARD
        │         │
        │    Lire la question de défense
        │         │
        │    BONNE RÉPONSE → Continuer normalement
        │    MAUVAISE RÉPONSE → Perdre le prochain tour
        │
        ├──► DEBUNKER CARD
        │         │
        │    (Mode compétitif : un adversaire peut la jouer)
        │    Lire la question de défense
        │         │
        │    BONNE RÉPONSE → Continuer + bonus optionnel
        │    MAUVAISE RÉPONSE → -1 déplacement tour suivant
        │
        ├──► MEN IN BLACK
        │         │
        │    Sauter le prochain tour complet
        │    Bloquer l'Event Card active
        │    (L'Officier de Police peut protéger un allié)
        │
        └──► HOAX CARD
                  │
             Défausser Event Card active
             Piocher une nouvelle Event Card
             Fin du tour immédiate
```

---

### 9.2 Interactions Spéciales entre Mécaniques

| Situation | Règle |
|---|---|
| Deux joueurs sur le même continent lors d'un Mass Sighting | Les deux bénéficient de l'effet |
| Un Officier de Police tente de protéger contre un MIB | Jet de dé : 4–6 = succès, 1–3 = échec |
| Un Investigateur choisit Déduction alors qu'une Debunker est active | Il peut d'abord résoudre la Debunker, puis entrer dans le Path |
| Plusieurs Debunkers accumulées | Maximum 2 Debunkers actives simultanément sur un joueur |
| Le deck History est épuisé | Le mélanger à nouveau (pas de limite de pioche) |
| Le deck Event est épuisé | Mode Coopératif : condition de défaite imminente |

---

## 10. LES TROIS AUTORITÉS — APPROFONDISSEMENT

### 10.1 GOUVERNEMENT 🏛️

**Définition :** Validation par les institutions politiques, les agences gouvernementales et les représentants élus.

**Pourquoi c'est difficile :** Les gouvernements ont historiquement nié, minimisé ou classifié les informations UAP. Les avancées récentes (rapport ODNI 2021, auditions Congrès 2023) représentent une rupture majeure.

**Exemples de validation gouvernementale :**
- Déclarations officielles du Pentagone sur les UAP
- Rapports déclassifiés (NARA, GAO, ODNI)
- Auditions devant le Congrès américain ou d'autres parlements
- Programmes officiels d'investigation (Blue Book, AATIP, AARO)

**Types de questions Gouvernement :**
- Histoire des programmes secrets (noms, dates, budgets, responsables)
- Procédures de déclassification
- Relations internationales autour des UAP
- Whistleblowers et lanceurs d'alerte (Grusch, Elizondo)
- Textes législatifs (NDAA, UAP Disclosure Act)

**Cas emblématiques pour cette Autorité :**
E01 Roswell, E03 Washington 1952, E07 Projet Blue Book, E16 AATIP, E17 Rapport ODNI, E18 Grusch

---

### 10.2 MILITAIRE ⚔️

**Définition :** Validation par les forces armées, les pilotes de combat, les systèmes de détection radar et les institutions de défense.

**Pourquoi c'est difficile :** Les militaires sont tenus au secret et à la discrétion. Les témoignages de pilotes sont particulièrement crédibles car ces professionnels sont formés à l'observation précise.

**Exemples de validation militaire :**
- Témoignages de pilotes militaires (Fravor, Dietrich, Slaight)
- Données radar officielles (AN/SPY-1, AEGIS)
- Incidents impliquant des bases nucléaires
- Vidéos FLIR déclassifiées

**Types de questions Militaire :**
- Technologie radar et systèmes de détection FLIR
- Protocoles militaires lors d'observations (scramble, règles d'engagement)
- Incidents aux abords d'installations nucléaires
- Témoignages de pilotes spécifiques et leurs descriptions techniques

**Cas emblématiques pour cette Autorité :**
E06 Shag Harbour, E08 Rendlesham, E10 Vague belge, E13 Nimitz, E15 Go Fast/Gimbal

---

### 10.3 SCIENTIFIQUE 🔬

**Définition :** Validation par la communauté académique — physiciens, médecins, psychiatres, chercheurs en astrobiologie.

**Pourquoi c'est difficile :** La science exige des preuves reproductibles et vérifiables. Les phénomènes UAP sont par nature éphémères et difficiles à documenter selon les standards académiques.

**Exemples de validation scientifique :**
- Études médicales sur les abductees (Dr John Mack, Harvard)
- Analyses chimiques de traces au sol (landing traces)
- Programme SETI et recherche de signatures technologiques
- Rapport Condon (1969) et ses limites méthodologiques
- Rapport d'étude NASA UAP (2023)

**Types de questions Scientifique :**
- Physique des phénomènes (vitesses, G-forces, accélérations impossibles)
- Méthodologie scientifique appliquée aux UAP
- Astrobiologie et probabilités de vie extraterrestre
- Analyses chimiques et biologiques (traces, implants, modifications cellulaires)
- SETI, signatures technologiques (technosignatures)

**Cas emblématiques pour cette Autorité :**
E04 Betty Hill, E07 Travis Walton, E09 Ruwa, E20 Hessdalen, E21 Villas Boas

---

## 11. BASE DE DONNÉES DES CAS RÉELS

### 11.1 Cas Niveau DÉBUTANT (★)

---

**CAS 001 — Kenneth Arnold (1947)**
- **Date :** 24 juin 1947 | **Lieu :** État de Washington, USA | **Continent :** Amérique du Nord
- **Témoin :** Kenneth Arnold, pilote privé expérimenté
- **Autorité :** Gouvernement | **Niveau :** ★
- **Résumé :** Arnold observe 9 objets brillants en formation près du mont Rainier. Il les décrit se déplaçant "comme une assiette qui rebondirait sur l'eau" — formule qui donnera naissance au terme "flying saucer" (soucoupe volante), repris par les médias. Vitesse estimée : 1 700 mph.
- **Statut :** Non expliqué officiellement. Considéré comme le point de départ de l'ère OVNI moderne.

**CAS 002 — Incident de Roswell (1947)**
- **Date :** Juillet 1947 | **Lieu :** Roswell, Nouveau-Mexique, USA | **Continent :** Amérique du Nord
- **Autorité :** Gouvernement / Militaire | **Niveau :** ★
- **Résumé :** Un objet s'écrase sur le ranch de Mac Brazel. Les militaires annoncent d'abord récupérer une "soucoupe volante", puis parlent d'un ballon-sonde (Project Mogul). En 1994, un rapport du GAO révèle que des fichiers de communication militaires de juillet 1947 ont été mystérieusement détruits — une anomalie sans explication officielle.
- **Statut :** Explication officielle très contestée. L'une des affaires les plus documentées de l'histoire ufologique.

**CAS 003 — O'Hare Airport (2006)**
- **Date :** 7 novembre 2006 | **Lieu :** Aéroport O'Hare, Chicago, USA | **Continent :** Amérique du Nord
- **Témoins :** Personnel United Airlines (mécaniciens, pilotes, agents de piste)
- **Autorité :** Gouvernement | **Niveau :** ★
- **Résumé :** Un objet métallique circulaire stationnaire est observé à faible altitude pendant plusieurs minutes. Il disparaît soudainement vers le haut, laissant un trou parfait dans la couche nuageuse. La FAA nie d'abord, puis confirme avoir reçu des signalements officiels.
- **Statut :** La FAA ne dispose d'aucune explication. Un des cas les plus récents avec de nombreux témoins professionnels.

---

### 11.2 Cas Niveau INTERMÉDIAIRE (★★)

---

**CAS 004 — Enlèvement de Betty et Barney Hill (1961)**
- **Date :** 19–20 septembre 1961 | **Lieu :** New Hampshire, USA | **Continent :** Amérique du Nord
- **Témoins :** Betty Hill et Barney Hill (couple interracial, fonctionnaires)
- **Autorité :** Scientifique | **Niveau :** ★★
- **Résumé :** Premier cas d'abduction documenté dans l'histoire américaine. Sous régression hypnotique (méthode controversée), les deux témoins décrivent des expériences convergentes : examens médicaux à bord d'un engin, présence d'êtres non-humains, et une carte stellaire que Betty Hill dessine de mémoire. Cette carte sera corrélée en 1969 par Marjorie Fish au système Zeta Reticuli.
- **Élément clé :** Les deux récits obtenus indépendamment sous hypnose présentent des concordances troublantes.
- **Statut :** Cas d'étude majeur. La valeur probatoire de la régression hypnotique reste débattue par les psychologues.

**CAS 005 — Incident de Rendlesham Forest (1980)**
- **Date :** 26–28 décembre 1980 | **Lieu :** Suffolk, UK (base USAF Bentwaters/Woodbridge) | **Continent :** Europe
- **Témoins :** Lt. Col. Charles Halt et son équipe militaire US
- **Autorité :** Militaire | **Niveau :** ★★
- **Résumé :** Pendant trois nuits consécutives, des militaires américains observent des lumières dans la forêt adjacente à la base. Le Lt. Col. Halt enregistre ses observations en temps réel sur dictaphone ("Je suis directement dans le beam maintenant..."). Des traces triangulaires au sol et des niveaux de radiation anormaux sont mesurés. Le chef de la base a écrit un mémo officiel adressé au Ministère de la Défense britannique.
- **Élément clé :** Enregistrement audio original disponible. Mémo officiel déclassifié.
- **Statut :** L'un des cas militaires les mieux documentés. Toujours inexpliqué officiellement.

**CAS 006 — Lumières de Phoenix (1997)**
- **Date :** 13 mars 1997 | **Lieu :** Arizona + Nevada, USA | **Continent :** Amérique du Nord
- **Témoins :** Plusieurs milliers, dont le gouverneur Fife Symington
- **Autorité :** Gouvernement | **Niveau :** ★★
- **Résumé :** Deux événements distincts en une seule nuit. D'abord, une formation en V de lumières traverse 500 km du Nevada à Tucson, observée sur toute la trajectoire. Ensuite, des lumières stationnaires en arc apparaissent au-dessus de Phoenix. L'armée américaine attribue ces secondes lumières à des fusées éclairantes du 104th Fighter Squadron — explication contestée par les chronologies et les témoignages.
- **Élément clé :** Le gouverneur Symington avait d'abord tourné l'affaire en dérision publiquement, avant d'admettre en 2007 avoir lui-même vu quelque chose d'inexplicable ce soir-là.
- **Statut :** Explication officielle contestée par des milliers de témoins.

**CAS 007 — École de Ruwa, Zimbabwe (1994)**
- **Date :** 16 septembre 1994 | **Lieu :** École Ariel, Ruwa, Zimbabwe | **Continent :** Afrique
- **Témoins :** 62 enfants âgés de 5 à 12 ans
- **Autorité :** Scientifique | **Niveau :** ★★
- **Résumé :** Pendant la récréation, 62 enfants observent l'atterrissage de plusieurs objets et l'apparition d'êtres à grands yeux noirs. Le Dr John Mack de Harvard mène une enquête approfondie. Les dessins réalisés séparément par les enfants sont remarquablement cohérents malgré l'absence de communication entre eux. Documenté dans le film "Ariel Phenomenon" (2022).
- **Élément clé :** Le Dr Mack était convaincu de l'authenticité des témoignages et publie ses conclusions.
- **Statut :** Impossible à expliquer par une panique collective ordinaire selon les psychiatres consultés.

---

### 11.3 Cas Niveau AVANCÉ (★★★)

---

**CAS 008 — Incident Nimitz / Tic-Tac (2004)**
- **Date :** 14 novembre 2004 | **Lieu :** Pacifique, large de San Diego (groupe USS Nimitz) | **Continent :** Amérique du Nord
- **Témoins :** Cmdr. David Fravor, Lt. Cmdr. Jim Slaight, WSO Alex Dietrich + équipage radar USS Princeton
- **Autorité :** Militaire | **Niveau :** ★★★
- **Détails techniques :**
  - Détecté par radar AN/SPY-1 de l'USS Princeton pendant plusieurs semaines avant l'interception
  - Objet elliptique blanc (~12 m), sans ailes, sans système de propulsion visible
  - Descend de 28 000 pieds à quelques dizaines de mètres en quelques secondes
  - Accélérations incompatibles avec toute technologie connue
  - Anticipe le mouvement des chasseurs F/A-18 comme s'il était conscient de leur présence
  - Filmé par caméra FLIR — vidéo déclassifiée officiellement par le Pentagone en avril 2020
- **Statut :** Officiellement déclassifié. Fravor décrit l'objet comme "la chose la plus avancée que j'aie jamais vue".

**CAS 009 — Témoignage David Grusch au Congrès (2023)**
- **Date :** 26 juillet 2023 | **Lieu :** Capitole, Washington D.C., USA | **Continent :** Amérique du Nord
- **Témoin :** David Grusch, ancien officier du renseignement (NRO, NGA), liaison AATIP
- **Autorité :** Gouvernement | **Niveau :** ★★★
- **Résumé :** Grusch témoigne sous serment devant le Congrès américain que les États-Unis possèdent depuis des décennies des "engins de fabrication non-humaine" récupérés après des crashes. Il affirme avoir eu connaissance de "pilotes biologiques non-humains récupérés". Il a déposé une plainte officielle de lanceur d'alerte protégé auprès de l'Inspecteur Général du Renseignement avant de témoigner publiquement. Témoins également : David Fravor (Nimitz) et Ryan Graves (observations Navy 2014–2015).
- **Contexte légal :** Témoigner sous serment et mentir constitue un parjure fédéral passible de 5 ans d'emprisonnement.
- **Statut :** Enquête en cours par le Congrès. Première déclaration sous serment de ce type dans l'histoire américaine.

**CAS 010 — Affaire Bob Lazar / Zone 51 (1989)**
- **Date :** Révélations en 1989 | **Lieu :** Zone 51 / S-4, Nevada, USA | **Continent :** Amérique du Nord
- **Témoin :** Bob Lazar, ingénieur
- **Autorité :** Gouvernement / Scientifique | **Niveau :** ★★★
- **Points clés :**
  - Lazar affirme avoir travaillé à rétro-ingénierer 9 vaisseaux extraterrestres dans une installation secrète nommée S-4
  - Décrit un système de propulsion basé sur un "element 115" (non connu en 1989)
  - L'élément 115, baptisé Moscovium, est synthétisé pour la première fois en 2003 et officiellement nommé en 2016
  - Son numéro de sécurité sociale et ses diplômes avaient initialement été niés par les institutions — certains ont ensuite été retrouvés
- **Statut :** Très controversé. La confirmation de l'Element 115 constitue un point de corroboration partielle impossible à ignorer.

**CAS 011 — Rapport UAP du Pentagone (2021)**
- **Date :** 25 juin 2021 | **Origine :** Office of the Director of National Intelligence (ODNI)
- **Autorité :** Gouvernement / Militaire | **Niveau :** ★★★
- **Contenu du rapport :**
  - 144 incidents UAP entre 2004 et 2021 examinés
  - 1 seul expliqué (ballon)
  - 18 incidents présentent des "schémas de vol ou de performance inhabituels" (trajectoires, vitesses, absence de contrôle de vol conventionnel)
  - 11 cas impliquent des quasi-collisions avec des avions militaires
  - Le rapport reconnaît explicitement que les UAP représentent un "défi pour la sécurité aérienne et nationale"
- **Signification historique :** Premier document officiel américain admettant publiquement que les UAP sont réels, non expliqués et potentiellement dangereux.

---

## 12. QUESTIONS TRIVIA — BANQUE ENRICHIE

### Niveau DÉBUTANT (★)

**T001**
**Q :** Quel terme officiel a remplacé "OVNI" dans le vocabulaire du Pentagone américain depuis 2020 ?
- A) NHI (Non-Human Intelligence)
- B) **UAP (Unidentified Aerial Phenomenon)** ✓
- C) AEO (Aerial Enigmatic Object)
- D) AUF (Aerial Unidentified Flying)
*Contexte : Le terme "UAP" a été adopté pour éviter le stigmate culturel associé à "OVNI" et pour encourager des signalements sérieux par les militaires.*

---

**T002**
**Q :** En quelle année le programme américain "Project Blue Book" a-t-il été officiellement fermé ?
- A) 1953
- B) **1969** ✓
- C) 1975
- D) 1982
*Contexte : Blue Book a enquêté sur 12 618 cas. Sa fermeture suivit le rapport Condon (1969) qui concluait que les OVNI ne méritaient pas d'investigation scientifique — conclusion contestée par de nombreux chercheurs.*

---

**T003**
**Q :** Comment les pilotes de l'USS Nimitz ont-ils surnommé l'UAP qu'ils ont intercepté en 2004 ?
- A) Le Disque
- B) La Pastille
- C) **Le Tic-Tac** ✓
- D) L'Ellipse
*Contexte : La forme blanche allongée sans ailes et sans propulsion visible de l'engin leur rappelait un bonbon Tic-Tac. Commander David Fravor l'a décrit ainsi dans tous ses témoignages ultérieurs.*

---

**T004**
**Q :** Quelle agence américaine a publié le premier rapport officiel sur les UAP en juin 2021 ?
- A) CIA
- B) NASA
- C) FBI
- D) **ODNI (Office of the Director of National Intelligence)** ✓
*Contexte : Ce rapport reconnaissait 144 incidents non expliqués entre 2004 et 2021 — une première historique dans la communication officielle américaine sur le sujet.*

---

### Niveau INTERMÉDIAIRE (★★)

**T005**
**Q :** Quel ingénieur américain a affirmé en 1989 avoir travaillé sur la rétro-ingénierie de vaisseaux extraterrestres à S-4, près de la Zone 51 ?
- A) Edgar Mitchell
- B) Nick Pope
- C) **Bob Lazar** ✓
- D) Gordon Cooper
*Contexte : Lazar a notamment décrit l'utilisation d'un "élément 115" inconnu — l'élément 115 (Moscovium) a été synthétisé 14 ans plus tard, en 2003.*

---

**T006**
**Q :** Combien d'enfants ont témoigné d'une observation d'OVNI à l'école Ariel au Zimbabwe en 1994 ?
- A) 12
- B) 34
- C) **62** ✓
- D) 89
*Contexte : Le Dr John Mack de Harvard, psychiatre spécialisé, a enquêté et conclu que les témoignages étaient authentiques. Le cas est documenté dans le film "Ariel Phenomenon" (2022).*

---

**T007**
**Q :** Quel programme américain secret de 22 millions de dollars étudiait les UAP entre 2007 et 2012 avant d'être révélé par le New York Times en 2017 ?
- A) Project Aquarius
- B) Project Serpo
- C) **AATIP (Advanced Aerospace Threat Identification Program)** ✓
- D) AARO
*Contexte : L'AATIP était dirigé par Luis Elizondo. Sa révélation publique a ouvert la voie aux auditions officielles et aux déclassifications suivantes.*

---

**T008**
**Q :** Lors de l'incident de Rendlesham Forest en 1980, comment le Lt. Col. Halt a-t-il documenté ses observations en temps réel ?
- A) Il a pris des photos avec un appareil militaire
- B) Il a dessiné les objets observés
- C) **Il a enregistré ses observations sur un dictaphone** ✓
- D) Il a envoyé un télex crypté à la base
*Contexte : L'enregistrement original de Halt, réalisé dans la forêt, est disponible publiquement. Il dit notamment "Je suis directement dans le beam maintenant" — une preuve audio unique.*

---

**T009**
**Q :** Quel gouverneur américain a d'abord tourné les Lumières de Phoenix (1997) en dérision, avant d'admettre des années plus tard avoir lui-même vu quelque chose d'inexplicable ce soir-là ?
- A) Janet Napolitano
- B) **Fife Symington** ✓
- C) Jane Hull
- D) Bruce Babbitt
*Contexte : Symington avait organisé une conférence de presse humoristique avec un homme déguisé en alien pour se moquer de l'affaire. En 2007, il a reconnu avoir personnellement observé un énorme objet triangulaire dans le ciel.*

---

### Niveau AVANCÉ (★★★)

**T010**
**Q :** Quelle anomalie dans les archives nationales américaines fut découverte en 1994 concernant l'incident de Roswell ?
- A) Des photos classifiées de 1947 ont disparu des dossiers
- B) Un rapport médical d'autopsie a été retrouvé
- C) **Des fichiers de communication militaires de juillet 1947 avaient été mystérieusement détruits** ✓
- D) Un témoignage secret de Truman a été découvert
*Contexte : Un rapport du Government Accountability Office (GAO) commandé par le Congrès a confirmé la destruction inexpliquée d'archives — une anomalie sans justification officielle dans les règles de conservation.*

---

**T011**
**Q :** En juillet 2023, sous quel statut légal David Grusch a-t-il déposé ses révélations avant de témoigner publiquement au Congrès ?
- A) Témoin anonyme protégé par le FBI
- B) Informateur volontaire sans protection
- C) Consultant externe du Congrès
- D) **Lanceur d'alerte protégé (Intelligence Community Whistleblower Protection Act)** ✓
*Contexte : Grusch a d'abord déposé une plainte auprès de l'Inspecteur Général du Renseignement, puis informé les comités de supervision du Congrès. Ce statut le protège légalement contre les représailles.*

---

**T012**
**Q :** Quel radar spécifique a détecté l'UAP du groupe USS Nimitz pendant plusieurs semaines avant l'interception officielle de 2004 ?
- A) AN/TPS-75
- B) APG-73 du F/A-18
- C) **AN/SPY-1 de l'USS Princeton** ✓
- D) NORAD BMEWS
*Contexte : Le radar du croiseur USS Princeton trackait les objets depuis plusieurs semaines avant que les pilotes soient envoyés à l'interception. L'opérateur radar Kevin Day a témoigné que les objets apparaissaient à haute altitude puis descendaient soudainement.*

---

**T013**
**Q :** Quel bureau du Pentagone a été créé en 2022 pour centraliser officiellement les investigations sur les UAP, succédant à l'UAPTF ?
- A) AATIP
- B) ODNI-UAP
- C) **AARO (All-domain Anomaly Resolution Office)** ✓
- D) AFOSI
*Contexte : L'AARO a été créé par le NDAA de 2022. Il est chargé de centraliser les signalements UAP de tous les services armés et agences de renseignement, et de publier des rapports publics réguliers.*

---

## 13. QUESTIONS DÉDUCTION — BANQUE ENRICHIE

### Niveau INTERMÉDIAIRE (★★)

**D001**
**SCÉNARIO :** Un radar militaire détecte un objet à 28 000 pieds. En 1,2 seconde, l'objet est à 50 pieds au-dessus de l'eau. Des pilotes de F/A-18 confirment visuellement l'objet. L'objet est blanc, elliptique, sans ailes ni propulsion visible. Il se déplace ensuite à vitesse hypersonique vers l'est et disparaît des capteurs.

**Q :** Quel aspect physique de cette observation est le plus impossible à expliquer avec les technologies humaines connues ?
- A) La vitesse de déplacement horizontal
- B) **L'accélération instantanée verticale de 28 000 pieds à 50 pieds** ✓
- C) L'absence de signature acoustique
- D) La forme elliptique sans empennage

*Explication : La descente de 28 000 pieds en ~1 seconde implique une accélération de plusieurs milliers de G. Un corps humain perd connaissance au-delà de 9G, et aucune structure métallique connue ne résiste à de telles forces. C'est la caractéristique physiquement la plus inexplicable du cas Nimitz.*

---

**D002**
**SCÉNARIO :** Deux groupes de témoins séparés par 400 km rapportent la même observation à la même heure. Le premier groupe (zone rurale, sans téléphone) décrit : objet triangulaire, lumières aux 3 angles, pas de son, vol lent. Le second groupe (ville) décrit exactement la même chose. Les deux rapports arrivent indépendamment à la police dans un intervalle de 20 minutes.

**Q :** Quel élément rend ces témoignages particulièrement solides d'un point de vue scientifique ?
- A) Le nombre total de témoins (plus de 50)
- B) La précision des descriptions individuelles
- C) **L'impossibilité de contamination préalable entre les deux groupes** ✓
- D) La cohérence de la chronologie

*Explication : En épistémologie des témoignages, la convergence indépendante est le critère le plus fort. Deux groupes sans communication possible qui décrivent les mêmes détails spécifiques (forme triangulaire, disposition des lumières) constituent une corroboration scientifiquement significative — contrairement à des témoignages obtenus après que les médias aient diffusé les premières descriptions.*

---

**D003**
**SCÉNARIO :** Un pilote militaire signale un objet qui, lors de son approche, "semble conscient" de sa présence. Chaque fois qu'il tente de se positionner derrière l'objet pour une meilleure observation, l'objet pivote instantanément pour lui faire face, sans phase d'accélération préalable.

**Q :** Quelle hypothèse scientifique sérieuse pourrait expliquer ce comportement réactif ?
- A) L'objet est contrôlé par un humain depuis le sol via un signal radio
- B) Il s'agit d'un phénomène de plasma atmosphérique avec propriétés électromagnétiques
- C) **L'objet est équipé de capteurs qui détectent les radars ou les systèmes de guidage des chasseurs** ✓
- D) Le pilote souffre d'une illusion d'optique due à la vitesse

*Explication : Parmi les hypothèses scientifiques sérieuses, la plus parcimonieuse est que l'objet possède un système de détection des émissions radar ou des capteurs IR capables de détecter l'approche d'un aéronef. Cela implique une technologie de détection passive avancée — étrange mais pas fondamentalement impossible.*

---

### Niveau AVANCÉ (★★★)

**D004**
**SCÉNARIO :** En 1989, Bob Lazar décrit un élément chimique "115" utilisé comme source d'énergie, dont il ne connaît que les propriétés observées (stable à cette masse atomique, émetteur d'antimatière). En 2003, des physiciens russo-américains synthétisent pour la première fois l'élément 115. En 2016, il est officiellement nommé Moscovium et intégré au tableau périodique.

**Q :** Quelle est la conclusion logique correcte sur les affirmations de Lazar à la lumière de cette découverte ?
- A) La découverte prouve que Lazar avait raison sur tous ses témoignages
- B) C'est une simple coïncidence sans valeur probatoire
- C) Lazar avait accès à des recherches en physique nucléaire théorique en 1989
- D) **La confirmation partielle d'un détail scientifiquement imprévisible en 1989 rend l'ensemble du témoignage plus difficile à rejeter en bloc** ✓

*Explication : En logique de l'évaluation des témoignages, quand un élément hautement spécifique et invérifiable au moment du témoignage est ultérieurement confirmé par la science, cela augmente statistiquement la crédibilité des autres éléments du témoignage. Ce n'est pas une preuve absolue, mais c'est un critère de crédibilité reconnu en jurisprudence et en épistémologie.*

---

**D005**
**SCÉNARIO :** Analyse comparative de 3 vidéos militaires déclassifiées (FLIR1/Tic-Tac 2004, Gimbal 2015, Go Fast 2015). Chacune montre des objets détectés par radar et confirmés visuellement. Dans aucune des 3 vidéos : pas d'ailes visibles, pas de propulsion thermique (signature IR normale sur les côtés), mouvements qui ne correspondent pas à des ballons (résistance au vent, changements de direction).

**Q :** Quelle conclusion peut être tirée de l'analyse conjointe de ces 3 cas, selon la méthode scientifique ?
- A) Il s'agit dans les 3 cas de drones militaires non déclarés
- B) L'absence de propulsion thermique indique un phénomène atmosphérique naturel
- C) Les caméras FLIR sont défectueuses dans les 3 cas
- D) **Les 3 objets partagent des caractéristiques physiques inexplicables par les technologies aériennes connues en 2004–2015, ce qui exclut une explication banale commune** ✓

*Explication : L'analyse conjointe (pattern recognition) de plusieurs cas indépendants est une méthode scientifique valide. L'absence de signature thermique de propulsion (les réacteurs conventionnels et les moteurs thermiques sont clairement visibles en FLIR), combinée aux trajectoires anomales, indique une catégorie de phénomène distincte des aéronefs connus.*

---

**D006**
**SCÉNARIO :** À l'école d'Ariel, Zimbabwe (1994), 62 enfants âgés de 5 à 12 ans décrivent le même événement. Séparés pour les interrogatoires, leurs dessins présentent les mêmes 3 caractéristiques : grande tête, yeux noirs en amande très larges, combinaison sombre. Aucun accès à la télévision montrant des images d'aliens dans cette école rurale en 1994.

**Q :** Selon la méthode scientifique d'évaluation des témoignages multiples, quel est le point le plus significatif de cette observation ?
- A) La jeunesse des témoins les rend automatiquement peu fiables
- B) La convergence iconographique sans source commune identifiable d'images alien préalables ✓
- C) Le nombre total de 62 témoins dépasse le seuil statistique de fiabilité
- D) La présence du Dr Mack garantit la valeur scientifique des témoignages

*Explication : En 1994, le stéréotype de "l'alien aux grands yeux noirs" était présent dans la culture américaine (couverture du livre "Communion" de Whitley Strieber, 1987) mais très peu diffusé en Afrique rurale. La convergence iconographique indépendante des enfants sur des détails spécifiques (pas d'oreilles, pas de nez) sans source d'images commune est le point analytiquement le plus solide.*

---

## 14. ÉQUILIBRE & GAME FEEL

### 14.1 Courbe de Difficulté

```
DÉBUT DE PARTIE
  ├── Questions de niveau Débutant prioritaires
  ├── Obstacles moins fréquents (1 Skeptic pour 4 questions)
  └── La toupie a légèrement plus de chance de tomber sur une Autorité

MILIEU DE PARTIE
  ├── Mix Débutant/Intermédiaire
  ├── Obstacles normaux (1 Skeptic pour 3 questions)
  └── Début des Debunkers et MIB

FIN DE PARTIE
  ├── Questions Intermédiaire/Avancé
  ├── Obstacles fréquents (compétitif : adversaires jouent leurs Debunkers)
  └── Tension maximale — un joueur peut être proche de la victoire
```

### 14.2 Risques de Déséquilibre & Contre-mesures

| Risque | Problème | Solution de Design |
|---|---|---|
| Snowball effect | Le joueur en tête est trop difficile à rattraper | Les MIB ciblent préférentiellement le leader |
| Frustration toupie | Le joueur ne tombe jamais sur la bonne Autorité | Règle "Consolation" : après 3 mauvais résultats consécutifs, +1 case bonus |
| Déséquilibre personnages | L'Investigateur UFO est trop fort en Trivia | Sa mobilité limitée et l'absence de bonus Gouvernement/Militaire compensent |
| Fin de partie trop longue | Personne ne parvient à finir la 3e Autorité | Timer optionnel : 90 min max, victoire au joueur avec le plus de tokens |
| Mode Coopératif trop facile | Les joueurs partagent toutes les réponses | Règle "Silence Radio" : communication limitée à 10s avant chaque question |

### 14.3 Paramètres de Difficulté

| Paramètre | Facile | Normal | Expert |
|---|---|---|---|
| Timer par question | 45 secondes | 30 secondes | 15 secondes |
| Indices disponibles | Oui (2 réponses éliminées) | Non | Non |
| Skeptic Cards | Moins fréquentes | Normales | Plus fréquentes |
| MIB | Rare | Normal | Fréquent |
| Tokens requis par Autorité | 2 | 3 | 3 + question bonus |

---

## 15. ADAPTATION JEU VIDÉO — ARCHITECTURE COMPLÈTE

### 15.1 Choix de Plateforme & Genre

**Genre :** Jeu de plateau numérique + Enquête narrative éducative  
**Plateformes recommandées :** PC/Mac (prioritaire), iOS/Android (adaptation), Nintendo Switch  
**Résolution cible :** 1920×1080 (PC), 2732×2048 (iPad Pro)

### 15.2 Structure des Écrans

```
ÉCRAN TITRE
│   Animation : OVNI traversant le ciel nocturne
│
├── 🆕 NOUVELLE PARTIE
│       ├── Solo (Quick Play)
│       ├── Campagne Solo (5 actes)
│       ├── Multijoueur Local (2–6 joueurs sur même écran)
│       ├── Multijoueur en Ligne (matchmaking + lobbies)
│       └── Mode Personnalisé (tous paramètres manuels)
│
├── ▶ CONTINUER (sauvegarde locale / cloud)
│
├── 📁 DOSSIERS (Encyclopédie des cas débloqués)
│
├── 🏆 ACHIEVEMENTS & STATISTIQUES
│
├── ⚙️ OPTIONS
│       ├── Audio (musique / SFX / voix)
│       ├── Graphismes
│       ├── Langue (FR / EN / ES / DE / IT)
│       └── Accessibilité (taille texte, daltonisme)
│
└── ℹ️ CRÉDITS
```

### 15.3 Flow de Lobby (Multijoueur)

```
LOBBY
│
├── Créer une partie
│       ├── Choisir mode (Compétitif / Coopératif)
│       ├── Choisir deck (Trivia / Déduction / Mixte)
│       ├── Choisir difficulté (Facile / Normal / Expert)
│       ├── Activer/Désactiver Asymétrique
│       └── Code de lobby à partager
│
├── Rejoindre une partie (via code ou liste publique)
│
└── SÉLECTION DES PERSONNAGES
        ├── 12 personnages affichés avec stats visibles
        ├── Aperçu audio du monologue du personnage
        ├── Hover : affiche les capacités spéciales détaillées
        └── Confirmation → Placement des pions sur continent de départ
```

### 15.4 Boucle de Jeu Numérique

```
BOUCLE PRINCIPALE (par tour)
        │
        ▼
[Animation du plateau 3D — caméra zoome sur le joueur actif]
        │
        ▼
[HUD : "C'est votre tour, [NOM] — [PERSONNAGE]"]
[Affichage : Event Cards actives + Disclosure Path du joueur]
        │
        ▼
[Interface de déplacement]
  Option A : Cliquer sur un continent pour s'y déplacer
  Option B : Lancer le dé animé (dé 3D qui roule)
  Option C (si capacité spéciale) : Utiliser Skill Token
        │
        ▼
[Animation du pion se déplaçant sur le plateau 3D]
        │
        ▼
[Vérification Event Card automatique]
  Match → [Animation toupie 3D qui tourne]
  No Match → [Fin de tour / Pioche Event Card]
        │
        ▼
[Résultat toupie avec animation lumineuse]
  Bonne Autorité → [Ouverture du Disclosure Path]
  Obstacle → [Pioche Skeptic / Debunker]
  Spécial → [Animation d'événement Mass Sighting / MIB]
        │
        ▼
[Interface de question plein écran — voir section 15.5]
        │
        ▼
[Retour plateau — mise à jour des tokens, passage au joueur suivant]
```

### 15.5 Interface de Question (Détail)

```
╔══════════════════════════════════════════════════════════════╗
║  📚 TRIVIA — Niveau : ★★ Intermédiaire                      ║
║  Autorité : ⚔️ MILITAIRE      [████████░░] Timer : 22s      ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  QUESTION :                                                  ║
║  Lors de l'incident Nimitz en 2004, quel radar a            ║
║  détecté les UAP pendant plusieurs semaines avant           ║
║  l'interception des pilotes de F/A-18 ?                     ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ┌───────────────────────┐  ┌───────────────────────┐       ║
║  │  A) APG-73 du F/A-18  │  │  B) AN/SPY-1 de       │       ║
║  │                       │  │     l'USS Princeton   │       ║
║  └───────────────────────┘  └───────────────────────┘       ║
║  ┌───────────────────────┐  ┌───────────────────────┐       ║
║  │  C) NORAD BMEWS       │  │  D) AN/TPS-75         │       ║
║  └───────────────────────┘  └───────────────────────┘       ║
║                                                              ║
║  💡 [INDICE — Mode Facile uniquement]                        ║
╚══════════════════════════════════════════════════════════════╝
```

**Écran après réponse correcte :**
```
╔══════════════════════════════════════════════════════════════╗
║  ✅ BONNE RÉPONSE !  +1 Token MILITAIRE                     ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  La réponse correcte est : B) AN/SPY-1 de l'USS Princeton   ║
║                                                              ║
║  📖 CONTEXTE :                                               ║
║  L'opérateur radar Kevin Day trackait ces objets depuis      ║
║  plusieurs semaines depuis le croiseur USS Princeton.        ║
║  Ils apparaissaient à haute altitude (~80 000 pieds)         ║
║  avant de descendre à basse altitude en quelques            ║
║  secondes — comportement sans équivalent connu.             ║
║                                                              ║
║  [Continuer →]   [Voir le cas complet dans les Dossiers]    ║
╚══════════════════════════════════════════════════════════════╝
```

**Écran après mauvaise réponse :**
```
╔══════════════════════════════════════════════════════════════╗
║  ❌ MAUVAISE RÉPONSE — Sortie du Disclosure Path            ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  La réponse correcte était : B) AN/SPY-1 de l'USS Princeton ║
║                                                              ║
║  📖 CONTEXTE : [même que ci-dessus]                          ║
║                                                              ║
║  Votre investigation est suspendue. Tentez à nouveau         ║
║  lors de votre prochain tour sur Amérique du Nord.          ║
║                                                              ║
║  [Continuer →]                                               ║
╚══════════════════════════════════════════════════════════════╝
```

### 15.6 Écran Disclosure Path (Individuel)

```
╔═════════════════════════════════════════════════════════╗
║  DISCLOSURE PATH — [NOM DU JOUEUR]                     ║
║  Rôle : 🔍 INVESTIGATEUR UFO — Variante : MUFON        ║
╠═════════════════════════════════════════════════════════╣
║                                                         ║
║  🏛️ GOUVERNEMENT   [●] [●] [ ]   2/3 — En cours        ║
║  ⚔️ MILITAIRE      [●] [ ] [ ]   1/3 — En cours        ║
║  🔬 SCIENTIFIQUE   [ ] [ ] [ ]   0/3 — Non commencé    ║
║                                                         ║
╠═════════════════════════════════════════════════════════╣
║  PROGRESSION FULL DISCLOSURE : 3/9 (33%)               ║
║  [▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]              ║
║                                                         ║
║  EVENT CARDS ACTIVES :                                  ║
║  🛸 [AATIP 2017] → Amér. Nord → Gouvernement ★★★       ║
║  🛸 [Rendlesham] → Europe → Militaire ★★               ║
║                                                         ║
║  SKILL TOKEN : ✅ Disponible (Choix Éclairé)            ║
╚═════════════════════════════════════════════════════════╝
```

### 15.7 Plateau 3D Interactif — Spécifications Visuelles

**Style artistique :** Réalisme stylisé sombre, ambiance "dossier d'enquête top secret"

- **Carte du monde 3D** vue de haut légèrement inclinée
- **Continents cliquables** avec hover qui fait apparaître les cas actifs dans la zone
- **Effets météo** réactifs : orages lors d'obstacles MIB, lumières vertes lors de Mass Sighting
- **Pions 3D** avec modèles de personnages animés (idle animation, déplacement)
- **Animation de la toupie** : soucoupe 3D qui tourne avec traînées lumineuses
- **Lignes de connexion** entre le pion et ses Event Cards actives
- **Interface minimale** en jeu : HUD non-intrusif, info au survol uniquement

---

## 16. UI/UX — SYSTÈME COMPLET

### 16.1 Charte Graphique

**Palette de couleurs :**

| Rôle | Couleur | Hex | Usage |
|---|---|---|---|
| Fond principal | Bleu nuit profond | `#0A0A1A` | Arrière-plans |
| Accent primaire | Vert néon | `#00FFAA` | Succès, technologie |
| Accent secondaire | Violet mystère | `#7B2FBE` | Mystère, Autorité Scientifique |
| Texte principal | Blanc bleuté | `#E8E8FF` | Corps de texte |
| Danger / MIB | Rouge vif | `#FF4444` | Obstacles, alertes |
| Succès / Token | Vert clair | `#44FF88` | Confirmations |
| Spécial / Or | Doré | `#FFD700` | Récompenses, Whistleblower |
| Gouvernement | Bleu institutionnel | `#3A7FD5` | Axe Gouvernement |
| Militaire | Kaki / Vert armée | `#7DA83B` | Axe Militaire |
| Scientifique | Cyan technique | `#00D4FF` | Axe Scientifique |

**Typographie :**
- Titres / UI : **Orbitron** (Google Fonts) — Police techno géométrique
- Corps de texte / Questions : **Inter** — Police lisible, confort de lecture
- Données classifiées : **Share Tech Mono** — Police monospace pour les dossiers
- Effets spéciaux : **Russo One** — Pour les intitulés de cartes

**Effets visuels :**
- Scanlines légères en surimpression (atmosphère CRT / dossier secret)
- Transitions de page avec effet "decryptage" ou "déclassification"
- Cartes qui s'ouvrent comme des dossiers classifiés avec tampon "TOP SECRET"
- Timer représenté comme une barre de signal qui se vide

### 16.2 HUD In-Game

```
╔══════════════════════════════════════════════════════════════════╗
║ [UFO LOGO]  TOUR 4/15  🏛[●●○] ⚔[●○○] 🔬[○○○]   [⏸ PAUSE]  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║              [PLATEAU 3D INTERACTIF CENTRAL]                     ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║ 📦 Events: 32  📚 History: 86  🤨 Skeptic: 21  🚫 Debunker: 18 ║
║                                                                  ║
║ C'est votre tour, ALEX (Investigateur UFO) — 🎲 Lancer le dé   ║
╚══════════════════════════════════════════════════════════════════╝
```

### 16.3 Accessibilité

- **Mode daltonisme** : filtres de couleur alternatifs pour les 3 Autorités
- **Taille de texte** : 3 niveaux (Normal, Grand, Très Grand)
- **Sous-titres audio** : toutes les narrations sous-titrées
- **Timer accessible** : signal sonore progressif (pas seulement visuel)
- **Contrôles simplifiés** : mode "un bouton" pour les joueurs à mobilité réduite

---

## 17. SYSTÈME AUDIO & AMBIANCE

### 17.1 Structure Musicale

| Contexte | Style | BPM | Durée boucle |
|---|---|---|---|
| Menu principal | Ambient mystérieux + synthé analogique | 60 | 3 min |
| Plateau monde (normal) | Thriller atmosphérique, cordes | 85 | 4 min |
| Plateau monde (fin de partie) | Tension montante, percussions | 100 | 2 min |
| Question Trivia | Tension légère, tic-tac stylisé | 90 | 45 s |
| Question Déduction | Enquête, jazz noir, contrebasse | 70 | 60 s |
| Résolution Skeptic | Courte stinger de tension | — | 5 s |
| Victoire | Épique, révélateur, cordes + cuivres | 120 | 1 min |
| Défaite | Grave, oppressant, drones | 50 | 30 s |
| Mass Sighting | Mystérieux + grandiose, chœur | 95 | 30 s |
| MIB | Menaçant, électronique sombre | 115 | 20 s |
| Campagne Acte 1 | Années 40–50, big band mystère | 75 | 5 min |
| Campagne Acte 4–5 | Moderne, techno ambient | 90 | 5 min |

### 17.2 Effets Sonores

**Sons de jeu :**
- Rotation de la toupie (sifflement + bourdonnement magnétique)
- Résultat toupie (chime positif OU buzz négatif)
- Déplacement du pion (pas stylisés + whoosh)
- Bonne réponse (chime ascendant en 3 notes)
- Mauvaise réponse (buzz descendant en 2 notes)
- Timer (tic-tac qui s'accélère dans les 5 dernières secondes)
- Pioche de carte (froissement de papier + scan holographique)
- Token placé (clic cristallin translucide)
- MIB apparaît (son de porte qui s'ouvre + statique)
- Mass Sighting (bourdonnement de foule + modulation grave)
- Whistleblower (voix distordue + alarme de sécurité)
- Full Disclosure (fanfare + son de fréquence radio + applaudissements)

**Sons d'ambiance par continent :**
- Amérique du Nord : radio militaire grésillante, vent du désert (Nevada)
- Europe : sons de campagne anglaise, vent de forêt (Rendlesham)
- Afrique : nature africaine, bruissement d'herbe sèche (Ruwa)
- Asie : ambiance aéronautique, trafic radio
- Océanie : vagues de mer, mouettes (Kaikoura)
- Amérique du Sud : jungle tropicale

### 17.3 Audiobook des Personnages (12 monologues)

**Exemple — Investigateur UFO (Variante MUFON) :**
> *"Après 20 ans à enquêter sur des centaines de cas, j'en suis arrivé à une conclusion qui me coûte encore parfois le sommeil : les témoins les plus crédibles ne sont pas ceux qui cherchent à nous convaincre. Ce sont ceux qui, comme vous et moi, ne comprennent tout simplement pas ce qu'ils ont vu — et qui en ont assez de se taire."*

**Exemple — Officier de Police (Variante Rural) :**
> *"J'étais de permanence le soir du 24 avril 1964. Ce que j'ai vu sur cette colline de Socorro... Je l'ai décrit dans mon rapport. Je n'ai rien ajouté, rien retiré. Trente ans plus tard, quand les gens me demandent si j'y crois encore, je leur réponds : croire n'a rien à voir là-dedans. J'ai vu."*

**Exemple — Abductee (Variante Moderne) :**
> *"Les gens pensent que c'est la peur qui vous reste. Non. Ce qui reste, c'est la certitude. La certitude absolue que ce que vous considérez comme le sommet de la connaissance humaine... n'est qu'un début. Et que quelqu'un, quelque part, le sait depuis très longtemps."*

---

## 18. PROGRESSION, MÉTA & REJOUABILITÉ

### 18.1 Encyclopédie des Dossiers

Accessible depuis le menu principal. Se débloque progressivement via le gameplay.

**Contenu de chaque dossier :**
- Description factuelle complète du cas
- Chronologie détaillée des événements
- Témoins et leurs profils
- Documents déclassifiés référencés (liens vers sources officielles)
- "Ce qu'on sait / Ce qui reste inexpliqué"
- Cas liés et comparaisons

**Filtres disponibles :**
- Par continent (6 zones)
- Par décennie (1940s → 2020s)
- Par type (observation, abduction, crash, gouvernemental, etc.)
- Par Autorité concernée (Gouvernement / Militaire / Scientifique)
- Par niveau de documentation (de "anecdotique" à "officiellement déclassifié")

### 18.2 Système d'Achievements

| Achievement | Condition | Description |
|---|---|---|
| 🛸 Premier Contact | Gagner sa première partie | "Vos premiers pas vers la Disclosure" |
| 📚 Témoin Crédible | 10 questions Trivia correctes de suite | "Votre connaissance est irréfutable" |
| 🔍 Sherlock des UAP | 10 questions Déduction correctes | "Votre logique transcende le mystère" |
| 🚫 Débunké le Debunker | 5 défenses de preuves réussies | "Vous avez cloué le bec aux sceptiques" |
| 🎭 All-Star | Jouer les 12 personnages au moins une fois | "Tous les angles du mystère" |
| 🌍 Full Disclosure | Gagner en mode Expert | "La vérité est connue de tous" |
| 🤝 L'Équipe | Gagner en coopératif à 4+ joueurs | "Ensemble vous avez changé le monde" |
| 🕴️ Le Survivant | Résister aux MIB 3 fois de suite | "Ils ne peuvent pas vous arrêter" |
| 📣 Whistleblower | Activer 5 cartes Whistleblower | "Les sources protégées parlent" |
| 🇺🇸 Roswell à Phoenix | Jouer tous les cas américains | "L'Amérique cache beaucoup" |
| 🌍 Tour du Monde | Jouer un cas sur chaque continent | "Le phénomène est global" |
| ⏰ Speed Runner | Gagner en moins de 30 minutes | "La vérité ne peut pas attendre" |
| 📖 L'Encyclopédiste | Débloquer 50 dossiers dans l'encyclopédie | "La connaissance est votre bouclier" |
| 🎯 Parfait | Gagner sans aucun échec à une question | "Impeccable, de bout en bout" |

### 18.3 Statistiques Personnelles

- Taux de réussite global / par type de question / par thème
- Personnage préféré / taux de victoire par personnage
- Continent le plus visité / cas le plus souvent joué
- Temps de jeu total / nombre de parties complètes
- Classement en ligne (optionnel)

---

## 19. ARCHITECTURE TECHNIQUE

### 19.1 Stack Recommandé

```
MOTEUR DE JEU
└─ Unity 2022 LTS avec Universal Render Pipeline (URP)
   (Alternative : Godot 4.x pour réduire les coûts)

MULTIJOUEUR
└─ Photon PUN 2 (temps réel, peer-to-peer)
   OU Mirror Networking (open source)
   Backend : PlayFab pour les scores et profils

AUDIO
└─ FMOD Studio (audio adaptatif selon état de jeu)
   Fallback : Unity Audio avec AudioMixer

UI SYSTÈME
└─ Unity UI Toolkit (Flexible, CSS-like)

BASE DE DONNÉES DES CARTES
└─ Fichiers JSON chargés dynamiquement
   (permet DLC sans mise à jour moteur)

LOCALISATION
└─ Unity Localization Package
   Langues cibles : FR, EN, ES, DE, IT

SAUVEGARDE
└─ Locale : PlayerPrefs + JSON chiffré
   Cloud : PlayFab Save Data (optionnel)

ANALYTICS
└─ Unity Analytics (comportement joueur, drop-off)
```

### 19.2 Structure de Données JSON

**Event Card :**
```json
{
  "id": "E013",
  "title": "Incident Nimitz / Tic-Tac",
  "year": 2004,
  "continent": "north_america",
  "authority": "military",
  "level": 3,
  "witnesses": ["David Fravor", "Jim Slaight", "Alex Dietrich"],
  "description": "Des pilotes de F/A-18 de l'USS Nimitz interceptent...",
  "image": "nimitz_tic_tac.png",
  "ambient_audio": "ambient_military_base",
  "hotspot": false,
  "linked_trivia": ["T006", "T012"],
  "linked_deduction": ["D001", "D005"],
  "source_url": "https://www.navair.navy.mil/"
}
```

**History Card — Trivia :**
```json
{
  "id": "T012",
  "type": "trivia",
  "level": 3,
  "authority": "military",
  "theme": "nimitz",
  "question": "Quel radar a détecté les UAP de l'USS Nimitz ?",
  "answers": [
    {"text": "APG-73 du F/A-18", "correct": false},
    {"text": "AN/SPY-1 de l'USS Princeton", "correct": true},
    {"text": "NORAD BMEWS", "correct": false},
    {"text": "AN/TPS-75", "correct": false}
  ],
  "context": "L'opérateur radar Kevin Day trackait les objets depuis plusieurs semaines...",
  "linked_event": "E013",
  "timer_normal": 30,
  "timer_expert": 15,
  "hint": "Pensez au croiseur qui accompagnait le groupe aéronaval"
}
```

**Skeptic Card :**
```json
{
  "id": "SK007",
  "challenge_text": "Un sceptique conteste la fiabilité des radars militaires...",
  "question": "Quel biais technique peut affecter les détections radar à haute altitude ?",
  "answers": [
    {"text": "Interférences solaires", "correct": false},
    {"text": "Lobing des ondes radar dû à la réfraction atmosphérique", "correct": true},
    {"text": "Surcharge de données du système AEGIS", "correct": false},
    {"text": "Erreur de calibration du gyroscope", "correct": false}
  ],
  "fail_effect": "skip_turn",
  "context": "La réfraction atmosphérique peut créer des échos fantômes sur radar...",
  "source": "IEEE Radar Conference Proceedings"
}
```

### 19.3 Architecture Réseau (Multijoueur)

```
ARCHITECTURE PEER-TO-PEER (Photon PUN 2)

Room Master (joueur qui héberge)
  │
  ├── État du jeu (plateau, tokens, deck positions)
  ├── File des tours (ordre des joueurs)
  └── Historique des actions (replay possible)

Clients (autres joueurs)
  ├── Envoient leurs actions au Master
  ├── Reçoivent le nouvel état de jeu
  └── Appliquent les animations localement

Synchronisation :
  ├── Lancer de dé → seed partagée (même résultat tous)
  ├── Lancer de toupie → seed partagée
  ├── Pioche de carte → index partagé
  └── Réponses → soumises avant dévoilement (anti-triche)
```

### 19.4 Système de DLC & Extensions

```
DLC_STRUCTURE/
├── base_game/
│   ├── events/ (70 cartes)
│   ├── trivia/ (50 cartes)
│   ├── deduction/ (50 cartes)
│   ├── skeptic/ (40 cartes)
│   └── debunker/ (40 cartes)
│
├── dlc_stretch_trivia/
│   └── trivia_bonus/ (50 cartes supplémentaires)
│
├── dlc_crashes_landings/
│   └── (40 cartes History — cas de crashs et atterrissages)
│
├── dlc_uso_hidden_depths/
│   └── (Cas sous-marins — USO, phénomènes navals)
│
├── dlc_close_encounters/
│   └── (20 Trivia + 20 Déduction — Contacts rapprochés 3e et 4e type)
│
├── dlc_event_expansion_1/
│   └── (40 Event Cards supplémentaires + nouvelles mécaniques)
│
└── dlc_casebook/
    └── (100 dossiers complets + audiobook narrateur)
```

---

## 20. ROADMAP & CONTENU POST-LANCEMENT

### 20.1 Phases de Développement

| Phase | Contenu | Durée estimée |
|---|---|---|
| **Alpha** | Core gameplay compétitif, 50 cartes Trivia, 25 Event Cards | 4 mois |
| **Beta** | Mode coopératif, 50 cartes Déduction, tous les personnages | 3 mois |
| **Launch v1.0** | Jeu complet (toutes cartes base), multijoueur en ligne | 2 mois |
| **Post-launch** | DLC contenu, mode Campagne, Encyclopédie | 6 mois |
| **v2.0** | Nouvelles expansions, cas internationaux, multilangue étendu | 1 an |

### 20.2 Contenu Post-Lancement

- **Mise à jour "2024–2025"** : Nouveaux cas réels intégrés au fil de l'actualité UAP
- **Pack "Cas Internationaux"** : Focus Europe, Asie, Amérique Latine
- **Mode "Archiviste"** : Créer ses propres questions à partir des dossiers
- **Tournois en ligne** : Saisons compétitives avec classement mondial
- **Partenariat pédagogique** : Version "classroom" pour établissements scolaires

---

## 21. ANNEXES

### Annexe A — Glossaire Complet

| Terme | Définition |
|---|---|
| UAP | Unidentified Aerial Phenomenon — terme officiel américain depuis 2020 |
| OVNI | Objet Volant Non Identifié — terme classique, toujours utilisé hors USA |
| Disclosure | Divulgation officielle de l'existence des phénomènes non-humains |
| MIB | Men in Black — agents supposément chargés d'intimider les témoins |
| Abductee | Personne ayant vécu une expérience d'enlèvement extraterrestre |
| Experiencer | Terme plus neutre désignant toute personne ayant vécu un contact |
| AATIP | Advanced Aerospace Threat Identification Program (2007–2012) |
| AARO | All-domain Anomaly Resolution Office (bureau UAP Pentagon actuel) |
| ODNI | Office of the Director of National Intelligence |
| MUFON | Mutual UFO Network — plus grand réseau d'enquêteurs civils |
| USO | Unidentified Submerged Object — version sous-marine des UAP |
| Project Blue Book | Programme d'enquête US Air Force 1952–1969 (12 618 cas) |
| Confirmation Token | Jeton représentant la validation d'une Autorité |
| Disclosure Path | Mini-plateau individuel mesurant la progression |
| Skill Token | Jeton activant les capacités spéciales d'un personnage |
| Full Disclosure | Condition de victoire : 3 Autorités confirmées = 9 tokens |
| Landing Trace | Trace physique au sol laissée par un atterrissage d'OVNI |
| FLIR | Forward-Looking InfraRed — caméra thermique militaire |
| G-force | Force d'accélération exprimée en multiples de la gravité terrestre |
| Technosignature | Signal ou artefact indiquant une technologie non-naturelle |

### Annexe B — Références Officielles

- Rapport UAP ODNI 2021 : [dni.gov](https://www.dni.gov)
- Auditions Congrès US 2023 (Grusch, Fravor, Graves) : [congress.gov](https://www.congress.gov)
- Archives Project Blue Book : [fold3.com](https://www.fold3.com/title/project-blue-book)
- National Archives (Roswell) : [archives.gov](https://www.archives.gov)
- NASA UAP Independent Study (2023) : [science.nasa.gov/uap](https://science.nasa.gov/uap)
- AARO (Bureau officiel Pentagon) : [aaro.mil](https://www.aaro.mil)
- Vidéos FLIR déclassifiées : [navair.navy.mil](https://www.navair.navy.mil/)

### Annexe C — Différences entre GDD v1.0 et v2.0

| Section | Ajout / Modification |
|---|---|
| Vision | Tableau de références inspirantes ajouté |
| Personnages | 5 attributs au lieu de 4, fiches complètes avec contre-mesures |
| Tour de jeu | 5 phases codifiées, arbre décisionnel complet |
| Event Cards | Liste complète 25 cartes, anatomie d'une carte, bonus hotspot |
| Questions | Banques enrichies avec niveaux, sources, contexte pédagogique |
| Équilibre | Section dédiée : risques de déséquilibre et contre-mesures |
| UI | Charte graphique complète, HUD détaillé, accessibilité |
| Audio | BPM, durées de boucle, monologues des personnages |
| Technique | Architecture réseau détaillée, DLC structure, JSON enrichi |
| Roadmap | Phases de développement et contenu post-lancement |

---

*Document GDD v2.0 — The UFO Disclosure Game — Adaptation Jeu Vidéo*  
*Basé sur le jeu de plateau original de Kenneth Media LTD (Londres, UK, 2025)*  
*Campagne Kickstarter : 4 445 € / 9 147 € — 58 contributeurs — Annulée le 2 juin 2025*  
*GDD enrichi et précisé à partir des sources officielles de la campagne*

---
*"We Are Not Alone."*
