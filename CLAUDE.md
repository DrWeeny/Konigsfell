# CLAUDE.md — Königsfell

Contexte de travail pour Claude + **journal de conception** (garder la trace des décisions et de leur raison).
Les conventions générales du projet sont dans [.github/copilot-instructions.md](.github/copilot-instructions.md) — ce fichier ne les répète pas.

---

## Cap éditorial

- **Deux livres cibles** : Manuel du joueur (lore, création, règles) et Manuel du maître (superset : joueur + secrets, direction de jeu). Un manuel de lore séparé reste possible.
- **Modèle « livre en boutique »** : le dépôt est public par choix. Un joueur peut lire le manuel du maître comme il le ferait en magasin — on ne cache pas, on sépare.
- **Le HTML n'est pas prioritaire** tant que le système est en développement. Le Markdown est la source.
- **Une seule source, deux sorties** (cible) : balises Pandoc dans le Markdown.
  - `::: mj` … `:::` → réservé au Manuel du maître
  - `::: dev` … `:::` → note de conception, retirée des deux manuels

## Canon à ne pas « corriger »

- **11 Comtes de la Croisade**, dont **Kette (= Überlieben)**, considéré comme mort → **10 Comtes** gouvernent aujourd'hui. Les deux chiffres sont justes selon le contexte.
- L'utilisateur tape ses **prompts** sans accents (clavier US) : **tous les documents** du dépôt s'écrivent avec accents et graphies canoniques — `Königsfell`, `Göre`, `Überlieben`, `Erlöser`. Seuls les noms de fichiers restent en ASCII.

## Règles : principe directeur

*On lance d'abord, on décide ensuite.* Toute règle ajoutée doit nourrir la décision d'assignation, jamais la contourner.
Référence des seuils : `regles/jets-de-des.md` (les autres fichiers y renvoient).

---

## Journal de conception

Format : date — sujet — décision / statut — pourquoi. Statuts : **acté**, **en test**, **ouvert**.

### 2026-10 — Refonte combat (session claude.ai, cf. [dev/handoff-equilibrage.md](dev/handoff-equilibrage.md))

- **acté** — Plancher d'action : total minimum 3. *Pourquoi :* un 1 ou 2 isolé n'apporte pas de choix.
- **acté** — Round : initiative, gardes posées à découvert dans l'ordre inverse, actions, résolution immédiate. Dés cachés écartés (triche, contraire au « lancer puis adapter »).
- **acté** — Dégâts = somme brute attaque − somme brute défense engagée − armure. Dés de garde engagés dépensés.
- **acté** — Grammaire des dés (6 verbes) et ordre d'application ; doubles lus sur faces naturelles.
- **acté** — PV sans progression par niveau, soins lents (1d6/jour), soins magiques = tabou. ⚠ `creation-de-personnage.md` dit 8 PV, le handoff évoque 20–22 : à calibrer en playtest.

### 2026-10-10 — Harmonisation des règles (Claude Code)

- **en test** — **Doubles** : V × 3 *pour réussir uniquement*, dégâts sur somme brute ; double 10 = critique narratif ignorant l'armure ; pas de triple. *Pourquoi :* l'ancienne règle « effets doublés » rendait les dégâts trop violents. Pas complètement tranché.
- **en test** — **Dés éphémères consommés** dès qu'ils sont engagés, retour à la scène suivante. *Pourquoi :* limiter le nombre de sorts puissants ; ce sont un levier de réglage de la violence (combien on en donne, quel pouvoir ils ouvrent). Remplace « ne se consomment pas sur les sorts d'archétype » et la recharge « nuit de repos ».
- **en test** — **Épuisement** : engager tous ses éphémères dans une scène → un dé épuisé jusqu'à la nuit. *Pourquoi :* freiner le « tout ou rien » sans compter les sorts.
- **acté** — Seuils 3/5/10/15/25, table unique dans `jets-de-des.md`. Exemple du mage corrigé (seuil 20+ inexistant → 15+).
- **acté** — Les dés se combinent pour former des actions ; un bonus de compétence s'ajoute une fois au total de l'action.
- **acté** — Tréma : Uberlieben → Überlieben dans tout le dépôt.
- **acté** — **Ewald** : nom du faux dieu du Pape-Dragon (progrès, civilisation, justice). Remplace Abadar (Pathfinder) : Palais de Justice d'Ewald, prêtres d'Ewald, symbole pyramide-clef conservé. *Pourquoi :* la justice de la cité est placée sous un dieu mensonger.
- **acté** — **Pool de départ : 2 dés** (1 DA de base + 1 dé de mouvement). Équipement, dons, archétype en ajoutent.
- **en test** — **Blessure grave : −1 dé** au pool.
- **acté** — Brainstorm ChatGPT ([dev/brainstorm-chatgpt.md](dev/brainstorm-chatgpt.md)) : sa version de la vampiresse, des Pilliers et ses dates sont **écartées**, le dépôt fait foi. Aucun système de magie n'existait avant ce jour.
- **acté** — **Lore collaboratif** : planque (devantures), PNJ loyal, casse avec flashbacks vrais — tout sert à faire écrire la ville par les joueurs.
- **en test** — **Flashback vrai** (`resolution-et-combat.md`) : en mission, un joueur déclare une préparation passée, jet selon la plausibilité ; réussite = fait du monde, échec = fait avec un prix. Outil de jeu, hors des 5–6 types de récompenses.

- **acté** — Accents rétablis dans `archetypes.md`, `pitch.md`, `01-meurtre-compagnon.md` (seuls les prompts sont sans accents).
- **acté** — Nouveau dossier **`univers/contes/`** : lore sous forme de contes. Premier conte : *Journée en Akkadie* (relu : accents et orthographe seulement, questions de l'auteur en bloc `::: dev`). Termes akkadiens (Waldu, Shanu, Incorporation, Belshanu) ajoutés au glossaire.

### 2026-10-10 — Première passe magie (`regles/magie.md`, brouillon)

- **en test** — 1 DP permanent pour tous = volonté / résistance de l'esprit ; on devient pratiquant par une **tradition** (sorts, statut légal, interdits).
- **en test** — 5 traditions : Eau Calme, Théurgie du Silence, funéraire akkadienne, Runistes, Alchimie. Arts proscrits : nécromancie, soin, peausserie, contrôle mental.
- **en test** — **Paliers de sort = table des seuils** (3/5/10/15/25). *Pourquoi :* une seule échelle pour tout ; répond à la question « magie et compétences ont-elles les mêmes seuils ».
- **en test** — Résistance : sort physique → garde ; sort sur l'esprit → DP de la cible.
- **en test** — Double 1 = **contrecoup** ; sort Majeur/Prodige ou contrecoup = **trace** que le Silence peut remarquer. *Pourquoi :* frein politique plutôt que mécanique.
- **en test** — **Mage en combat** : option A, les sorts de protection permettent de poser des DP en garde. Risque noté : les non-mages ont aussi 1 DP.
- **acté** — **Garde magique ouverte à tous** : un sort peut « guerrifier » un mage, et un guerrier peut apprendre un sort de protection. *Pourquoi :* l'avantage reste mince (flammes, encombrement) et avec 1 DP on risque toujours 1 ou 2.
- **acté** — **Contre-sort** du Théurge : DP posés en garde contre la magie, total ≥ sort = annulé, dés dépensés. Remplace « 2 DC pour annuler » (mélange de pools).
- **acté** — **Nouveau sort : 4 XP.**
- **en test** — **Runiste du Registre** (`archetypes.md`) : magie préparée — graver = action DP au calme, la rune garde son palier jusqu'au déclenchement, chaque rune active retient un dé éphémère. Poinçon déposé au Registre : la rune est une preuve. Interdit : runes sur le vivant. *Pourquoi :* niche distincte (préparation, casse, flashback) et frein par la ressource plutôt que par une liste.

---

## Questions ouvertes

1. **Archétypes de mages** : Eau Calme, Ritualiste akkadien, Runiste existent. Théurge et Physicus (`creation-de-personnage.md`) à développer au même gabarit ; Alchimie sans archétype complet.
2. **Combat du mage** : proposition dans `regles/magie.md` — valider en playtest.
3. Sorts physiques : les dégâts magiques ignorent-ils certaines armures (la plaque contre l'eau ?) — pour l'instant non.
4. **Dés éphémères à la table** : comment les distinguer (couleur) quand ils sont lancés avec le DP permanent — et le joueur choisit-il lesquels engager ?
5. Bonus plats (+2 Navigation dans `archetypes.md`) vs dés bonus (+1 DC ailleurs) : garder les deux ?
6. Équilibrage restant (handoff §2) : +1 d'initiative qui grandit avec le pool, inflation des doubles à gros pool, duels qui s'enlisent, boss contre 5–7 PJ, égalité d'initiative, compétences en combat.

## Chantiers à venir

- Résumé session par session de la campagne (fourni par l'utilisateur) → rationaliser les scénarios.
- Devantures de la planque (12 idées dans `dev/brainstorm-chatgpt.md`) → recalibrer en D10 et rédiger une section « Planque ».
- Bestiaire : extraire des notes MJ (Erlösers, vampires, créatures d'Überlieben) avec profils de combat.
- Baliser `resolution-et-combat.md` en `::: mj` / `::: dev`, puis script de génération des deux manuels.
