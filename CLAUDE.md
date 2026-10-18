# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Königsfell

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

## Dossiers

- `prive/` — **ignoré par git** : ressources de travail non publiables (notes Google Drive converties dans `prive/notes-drive/`, fiches écrites par les joueurs). On s'en sert comme source ; ce qui devient contenu de manuel est réécrit dans le dépôt.
- `dev/sessions/` — **ignoré par git** : résumés des sessions jouées (2020–2021, D&D 5e), noms des personnages uniquement, jamais ceux des joueurs. `dev/sessions/noms.md` = orthographe de référence. Tout ce qui vient des joueurs ou sert seulement de référence pour écrire les livres reste local ; les manuels peuvent en tirer des **exemples de jeu** réécrits (« à la table, un groupe a… »).
- Transcripts et audio : hors dépôt, `D:\dw_workspace\Konigsfell_Episodes\` (`outils/transcrire.py`).
- **Documents de référence, pas canon** : `mj/timeline-claude-sync.md` sert à fusionner peu à peu dans `mj/timeline.md`, qui fait foi. `scenarios/01-meurtre-compagnon.md` propose des variantes optionnelles de `01-meurtre.md` sans en changer le canon.

## Publication et outils

- **Pas de build, de lint ni de tests** : le dépôt n'est que du Markdown. GitHub Pages (`.nojekyll`) sert `index.html` et `univers/index.html` tels quels ; ils renvoient vers les `.md` bruts. Le script Pandoc qui doit générer les deux manuels n'existe pas encore (voir Chantiers).
- `outils/transcrire.py` (WhisperX ; le mode `mix` demande `HF_TOKEN` pour pyannote) :
  `python outils/transcrire.py pistes "<dossier Craig>" -o <sortie>` (une piste par joueur) ou
  `python outils/transcrire.py mix "<fichier>" -o <sortie> --arc purge` (voix mélangées).
  Les noms soufflés à Whisper suivent `dev/sessions/noms.md`. Les sorties restent hors du dépôt.
- `README.md` et la structure de `.github/copilot-instructions.md` sont en retard (pas de `blocs/`, ni de `competences.md`, `armurerie.md`…) : se fier à l'arborescence réelle.

## Canon à ne pas « corriger »

- **11 Comtes de la Croisade**, dont **Kette (= Überlieben)**, considéré comme mort → **10 Comtes** gouvernent aujourd'hui. Les deux chiffres sont justes selon le contexte.
- L'utilisateur tape ses **prompts** sans accents (clavier US) : **tous les documents** du dépôt s'écrivent avec accents et graphies canoniques — `Königsfell`, `Göre`, `Überlieben`, `Erlöser`. Seuls les noms de fichiers restent en ASCII. Cette règle prime sur `copilot-instructions.md`, qui tolère les brouillons sans accents.

## Règles : principe directeur

*On lance d'abord, on décide ensuite.* Toute règle ajoutée doit nourrir la décision d'assignation, jamais la contourner.
Référence des seuils : `regles/jets-de-des.md` (les autres fichiers y renvoient).

---

## Journal de conception

**L'historique complet** (chronologique, avec le *pourquoi* de chaque décision) est dans [dev/journal.md](dev/journal.md) ; le chantier des compétences est détaillé dans [mj/journal-de-conception.md](mj/journal-de-conception.md). Ci-dessous : **l'état actuel**, une ligne par décision. Statuts : **acté**, **en test**, **ouvert**.
Quand une décision change : ajouter une entrée datée dans `dev/journal.md`, puis mettre à jour la ligne ici.

### Système D10

- **acté** — Seuils **3/5/10/15/25** (table unique : `regles/jets-de-des.md`). Plancher d'action : total minimum 3.
- **acté** — Round : initiative, gardes posées à découvert dans l'ordre inverse, actions, résolution immédiate. Pas de dés cachés.
- **acté** — Dégâts = somme brute de l'attaque − somme brute de la défense engagée − armure. Les dés de garde engagés sont **dépensés**.
- **acté** — Les dés se combinent en actions. Ordre : on assigne, on relance, on lit les doubles sur les **faces naturelles**, puis on ajoute les bonus (une fois par action). Grammaire des dés : 6 verbes (`resolution-et-combat.md`).
- **en test** — **Doubles** : V × 3 *pour réussir uniquement* ; dégâts = somme brute + bonus d'objet et de compétence ; double 10 = critique narratif qui ignore l'armure ; pas de triple.
- **acté** — **Pool de départ** : 2 DA **libres** (attaque, garde ou mouvement) ; seuls les dés d'équipement sont spécialisés.
- **en test** — **PV** : 8 au départ, +3 avec *Endurci*, pas de progression par niveau ; soins lents (1d6/jour) ; soin magique tabou. Si la table tombe en un coup, monter les PV à 10–12 ou l'armure.
- **acté** — **À 0 PV, hors de combat** ; celui qui porte le coup décisif choisit l'issue : capture, **blessure grave** (séquelle durable, un membre perdu : −1 dé dans le pool touché) ou mort. Plus de seuil de mort à −4.
- **acté** — **Les armes sont des « skins »** : toutes donnent +1 dé d'attaque, les mots-clés et le port légal font la différence. **Tirs** : un tir s'esquive (DA libres, dés de mouvement ; bouclier si l'on fait face) ; au contact, une arme à distance ne donne pas son dé ; les armes à feu divisent l'armure par deux.
- **en test** — **Pas de caractéristiques.** Compétences **majeures** (liste d'archétype, +1 dé) et **mineures** (*geste + circonstance*, rangs +1 / +2 / +2 et relance ; rang 1 gagné en jouant) ; une seule par jet (`competences.md`).
- **en test** — **Échelle de puissance** : Léger, Notable, Fort, Exceptionnel, Relique (`echelle-de-puissance.md`). *Majeure / mineure* est réservé aux compétences.
- **en test** — **Payer un dé** : comptant (épuisé jusqu'à une nuit) ou à crédit (posé sur 1 au prochain jet). Payer ≠ dépenser.
- **en test** — **Dix archétypes**, chacun avec deux avantages de départ ; la **Tradition** est une compétence majeure (+1 éphémère, 3 sorts ; 4 XP en jeu) (`archetypes.md`). Armurerie : un pack de départ et un objet personnel (`armurerie.md`).
- **acté** — Création en 8 étapes (`creation-de-personnage.md`, `fiche-de-personnage.md`). Nouveau sort : 4 XP. Pas de relance ponctuelle à 2 XP.
- **en test** — **Progression étalonnée** : ~2 XP par session ; après deux douzaines de sessions, un PJ est à mi-chemin d'un Comte (repères par niveau dans `mj/bestiaire.md`). PV par tranches de 4 (1 XP, puis 2, puis 3…).
- **en test** — **Flashback vrai** : une préparation passée déclarée en mission ; réussite = fait du monde, échec = fait avec un prix.
- **en test** — **Premier playtest préparé** : aide de jeu d'une page (`regles/aide-de-jeu.md`), scène de test avec grille d'observation (`mj/scene-de-test.md`).
- **en test** — **Bestiaire** (`mj/bestiaire.md`) : barème sbire / soldat / vétéran / monstre / fléau / **légende** (les Comtes), moral, capacités de fléau ; profils tirés des combats joués, **Hahn** et **Göre**, et les cinq PJ du Sucret (48 XP) avec Jacques la Savate (vétéran, ≈ 32 XP) comme étalons.
- **en test** — **Sceaux officiels** des Comtes (cuivre → météorite) dans `armurerie.md`, avec leurs règles : sans permis, forgés par l'Empereur, un seul porteur, ils engagent qui les a confiés, se reprennent, le faux est un crime. Le **cuivre** est administratif : celui des hauts administrateurs (juge, haut commissaire, capitaine), un vrai pouvoir borné au ressort de leur charge ; le plus falsifié. Tout noble de l'Empire (baron, duc, prince, Comte) confie des sceaux selon son rang : le métal dit le rang de la mission, le blason dit qui en répond.
- **en test** — **Objets magiques** (`objets-magiques.md`) : un objet, un verbe, un palier ; runes utilitaires déclenchées par tous, gravées par les runistes, chaque rune donnée retient un éphémère du graveur ; le palladium tient lieu de cercle pour une Relique. Profil de Kette à venir : sa version rêvée.
- **en test** — **Dons de la Nuit** (`mj/dons-de-la-nuit.md`) : pouvoirs donnés par un Iggigi, sans XP ni permis ni identification, toujours avec un prix ; détectables comme un art akkadien. Dons de Lucie : guides-esprits, *Armure angélique* (Ketnis), *Enfant funeste* (Schön). Table de trente dons et marques.
- **acté (leçon)** — **Toute ressource doit être écrite dans les règles**, sinon les joueurs la lisent comme un bonus (les points de karma ont fini en dés du destin).

### Magie (`regles/magie.md`)

- **en test** — 1 DP permanent pour tous ; on devient pratiquant par une **tradition** (Eau Calme, Théurgie du Silence, funéraire akkadienne, Runistes, Alchimie). Arts proscrits : nécromancie, soin, peausserie, contrôle mental.
- **en test** — **La formule écrit, les paliers lancent** : verbe + portée (espace ou temps) + durée + cibles + effet − restrictions, arrondi au seuil supérieur. Improviser = un seuil de plus et toujours une trace.
- **acté** — **Un sort par round**, avec les DP de base qu'on veut ; les dés restants ne font pas un second sort. Poser des DP en garde ne compte pas comme le sort du round (en test).
- **acté** — **Les éphémères sont une réserve** (la fatigue du mage), pas lancés avec le pool : à tout moment, après avoir vu ses dés de base, on y puise pour renforcer un sort ou un contre-sort ; les dés puisés sont épuisés jusqu'à une **nuit** de repos. Plus de règle d'épuisement.
- **en test** — **Focus** : ordinaire = +1 éphémère dans la réserve, dans l'équipement de départ de chaque tradition ; de bonne facture (gagné en jeu) = +1 DP de base réservé aux sorts, comme le dé d'une épée. Un mage débutant : 1 DP permanent + 2 éphémères.
- **en test** — **Magie préparée** (runes, fioles du Physicus) : au calme, sans jet, palier = 5 par DP engagé, contre du temps (minutes → nuit) ; chaque effet actif retient un éphémère. L'avantage du runiste, c'est la fiabilité. **15+ au plus en solitaire** ; le 25+ demande un cercle (toute une guilde) et une condition.
- **en test** — **Économie d'action du mage** : DP de base achetable (4 / 8 / 12 XP, comme les DA) ; **écho** une fois par scène (un sort réussi touche une seconde cible au même total, contre autant d'éphémères payés comptant, sans jet) ; déclencher une préparation est une action de DA, pas le sort du round.
- **en test** — Les 15 sorts et préparations de départ ont leurs paliers chiffrés par la formule (`archetypes.md`).
- **en test** — Résistance : sort physique → garde ; sort sur l'esprit → DP. Double 1 = contrecoup. **Trace** (sort à 15+, improvisation, contrecoup) : un frein politique.
- **acté** — **Garde magique ouverte à tous.** **Contre-sort ouvert à tout pratiquant**, à égalité : DP en garde contre la magie, total ≥ sort → sort annulé. Le Théurge reçoit à la place *Arrestation*, un sort d'immobilisation borné par la sommation (en test). **Les sens du Silence** (en test) : ordres greffés de palladium, pouvoirs sans jet ; hiérarchie dans `univers/empire.md`. **Basilique** (pieux dans les yeux : sent tout, repousse le métal), **Sirène** dite inquisiteur (télépathie), **Témoin** (assassin, traque des mages), **Criquet** (sent la magie, son cri interrompt les sorts). Noms de Basilique, Sirène et Criquet à remplacer (**ouvert**) ; *Témoin* reste.
- **en test** — **Inventaire verbe × domaine** des cinq traditions, seuils calculés (`magie.md`).
- **en test** — Théurge du Silence, Physicus, Runiste du Registre écrits (`archetypes.md`). Piste **magie par privation** (interdit personnel = prix réel).

### Canon tranché (détail et sources : `dev/journal.md`, `mj/timeline.md`)

- **Ewald** : faux dieu du Pape-Dragon (progrès, justice), remplace Abadar. **Erlöser** : parasites stellaires qui mangent l'énergie et le chaos, pas l'eau.
- **Origine des peuples** : Elfes + Humains → Primordiaux et Akkadiens ; elfe et demi-elfe d'aujourd'hui, c'est la même chose.
- **Hahn, Göre, Kette** : pupilles de l'Empereur. **Kette = Überlieben = Maître des rêves**, réfugié dans le **Rêve** créé par **Zeichen** (Comte Présage). Siège de Comte vacant, élection par l'Hydre (jamais joué).
- **Willensein Sieben** (« Willen ») : fils d'Arhedell, Empereur non élu, populaire ; le camp **Vauburg** fait traîner le vote. Le Serment impérial ne lie que les mages puissants.
- **Hans d'Aragon** = « le duc » : il finance en secret le meurtre de l'Empereur. **Auge** finance les opposants, jamais un meurtre.
- **Calendrier** : l'Empereur à J+30, le Jubilé à J+45.
- **Orques** fongiques (reine *Physarum*) ; leur noyade = le tsunami de la Croisade ; l'orque « apaiseur » de la cathédrale est un prédateur. **Suifs** (Pic des Empalés) ; **End Station** (onzième étage = néant, portail vers le Rêve).
- **Tuer Kette** demande l'**arme de l'Arbre de Métal** (l'Autre Épée : cinq branches de fer, chacune arrachée change un destin) ; l'épée-arbre du rêve de Ketnis en était l'indice.
- **La Nuit** : née du pouvoir des dragons morts qui pèse sur le territoire et du Roi de la Nuit ; ses créatures sont des korrigans, cruels ou bienfaisants, dans le gris ; l'Empire y voit une corruption et la déteste. S'en faire une alliée est un choix (Lucie).
- **Lucie** : maîtresse du cauchemar, l'Iggigi du Rêve ; ses pouvoirs et ses dons disparaissent avec le Rêve. **Göre** : ses doubles sont sa chair accumulée et modelée ; elle est la somme de tous.
- Orthographe fixée : **Assur Sandergul**, **Comte Morgenwelle** (fondateur de l'Eau Calme). **Godwelle** : le tsunami de la Croisade, qui a changé le cours de la guerre. Brainstorm ChatGPT écarté : le dépôt fait foi.
- **ouvert** — Nowitzki ; apprentis rivaux de l'épisode 21.

### Campagne et méthode

- **acté** — **Les scénarios sont des blocs**, jouables dans n'importe quel ordre, avec une ou deux connexions ; la structure reste invisible pour les joueurs. Chaque scénario finit par une section **Connexions**. Carte : `campagnes/trames-du-onzieme/blocs.md` (six portes d'entrée) ; fiches dans `blocs/`.
- **en test** — Scénarios **01** (horloge du rituel, acte 6) et **02** (*Bal des Armes* : échéance à minuit, règle des trois indices, table de rencontres) refondus d'après les parties jouées.
- **acté (méthode)** — Rattacher l'historique des PJ aux fils existants, **avec l'accord du joueur** (on propose, on n'impose pas). Un PJ qui dérape se transforme plutôt qu'il n'est pénalisé (Terry, devenu agent du Rêve).
- **acté** — **Lore collaboratif** : la planque, le PNJ loyal, le casse en flashbacks font écrire la ville par les joueurs. Contes de lore dans `univers/contes/`.


---

## Questions ouvertes

1. ~~Archétypes au format court~~ → les dix sont au même format dans `archetypes.md` (2026-10-15). Dé de Mouvement et « payer un dé » tranchés le 2026-10-15.
2. **Combat du mage** : proposition dans `regles/magie.md` — valider en playtest. Économie d'action : DP de base achetable, écho et déclenchement des préparations en test depuis le 2026-10-17.
3. Sorts physiques : les dégâts magiques ignorent-ils certaines armures (la plaque contre l'eau ?) — pour l'instant non.
4. ~~Dés éphémères à la table~~ → tranché : ils forment une réserve lancée à part (2026-10-16).
5. ~~Bonus plats vs dés bonus~~ → tranché par les compétences : majeure = +1 dé, mineure = bonus plat (2026-10-15).
6. Équilibrage restant (handoff §2) : +1 d'initiative qui grandit avec le pool, inflation des doubles à gros pool, duels qui s'enlisent, boss contre 5–7 PJ, égalité d'initiative, compétences en combat.
7. ~~Eau Calme, Émissaire, armes à distance, capacité du Théurge~~ → tranchés le 2026-10-16.

## Chantiers à venir

- ~~Résumé session par session de la campagne~~ → fait (`dev/sessions/`, local). Scénarios 01 et 02 refondus.
- ~~Carte des blocs~~ → `campagnes/trames-du-onzieme/blocs.md` (sommaire). Suite : une fiche d'une page par bloc (enjeu, entrées, horloge, connexions).
- Devantures de la planque (12 idées dans `dev/brainstorm-chatgpt.md`) → recalibrer en D10 et rédiger une section « Planque ».
- ~~Bestiaire~~ → `mj/bestiaire.md`. Suite : vampires, ange d'Ewald, Chimères, Nagas, créatures du pays de la Nuit, la Mousse.
- Baliser `resolution-et-combat.md` en `::: mj` / `::: dev`, puis script de génération des deux manuels.
