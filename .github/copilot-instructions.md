# Instructions Copilot — Königsfell

## Contexte du projet

- **Type :** campagne JDR dark urban fantasy Renaissance, en cours de rédaction pour publication
- **Public :** deux publications distinctes : un livre MJ (enjeux, secrets, direction de jeu) et un livre Joueurs (lore, monde, inspiration)
- **Système de jeu :** homebrew D6 (en développement). La campagne est conçue pour être adaptable à d'autres systèmes. Les règles doivent rester simples et système-agnostiques autant que possible. Testé précédemment sur D&D 5e.
- **Format des sessions :** ~24 sessions de 3-4h par arc. Le rythme doit être fluide — éviter la surcharge d'information par session.

---

## Conventions d'écriture

- **Noms de fichiers et dossiers :** ASCII uniquement, sans accents (ex: `konigsfell-ville.md`).
- **Dans le texte (lore, pitch, scénarios) :** utiliser les graphies canoniques : `Königsfell`, `Göre`.
- **Rédaction au clavier US :** écrire sans accents est acceptable en brouillon.
- **Avant commit/PR :** normaliser les noms propres canoniques dans le contenu.
- **En cas de doute :** privilégier la cohérence de l'univers plutôt que la facilité de saisie.

---

## Style rédactionnel

- **Section MJ :** court, actionnable, structuré en listes et tableaux. Objectif : tout comprendre sans ouvrir un second document.
- **Section Joueurs :** narratif, prosélique, immersif. Avec des **inserts de lore** (textes en italique ou blocs cités) pour enrichir le monde.
- **Redondance MJ/Joueurs :** acceptable et volontaire — le livre MJ doit être autosuffisant.

---

## Structure des fichiers

- `univers/` — lore public, chronologie, géographie, glossaire
- `univers/lieux/` — descriptions de lieux + inserts de lore dédiés
- `mj/` — secrets, timeline confidentielle, notes de campagne
- `campagnes/trames-du-onzieme/` — la campagne principale
  - `pitch.md` — vue d'ensemble joueurs
  - `pnj/vue-joueurs.md` / `vue-mj.md` — fiches PNJ séparées
  - `scenarios/` — scénarios numérotés
- `regles/` — système D10 homebrew, règles simples et adaptables
- `bestiaire/` — créatures, stat-blocks légers

---

## Workflow GitHub

- **PRs par gros blocs** (ex: univers, campagne, règles) — pas par fichier
- **Assets images :** placeholders acceptables (`_assets/maps/`, `_assets/img/`)
- **Orthographe :** normaliser `Königsfell` et `Göre` avant chaque PR

---

## Géographie canonique (monde en miroir)

| Nom dans l'univers | Inspiration réelle | Notes |
|---|---|---|
| Empire d'Alammania | Saint Empire Romain Germanique (Allemagne) | Époque Charles Quint |
| Königsfell | Italie du Nord (Venise, Florence) | Cité principale de la campagne |
| Suellie | France | |
| Chimera | Est (Ukraine), cultures tribales | |
| Primordie | Danemark et Nord tempéré | Royaume elfe |
| Royaumes Perdus | Russie, région arctique | |
| Pays d'Akkadie | Mésopotamie, Empire d'Akkad | Au sud de Königsfell |
| Nouveau Monde | Petite portion des Amériques | Frontier d'exploration récente |
