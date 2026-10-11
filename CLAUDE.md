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

## Dossiers

- `prive/` — **ignoré par git** : ressources de travail non publiables (notes Google Drive converties dans `prive/notes-drive/`, fiches écrites par les joueurs). On s'en sert comme source ; ce qui devient contenu de manuel est réécrit dans le dépôt.
- `dev/sessions/` — résumés des sessions jouées (2020–2021, D&D 5e), noms des personnages uniquement, jamais ceux des joueurs. `dev/sessions/noms.md` = orthographe de référence.
- Transcripts et audio : hors dépôt, `D:\dw_workspace\Konigsfell_Episodes\` (`outils/transcrire.py`).

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

### 2026-10-10 — Théurge et Physicus

- **en test** — **Théurge du Silence** complet : contre-sort, sorts de progression (Silence, Aveu, Lecture du serment, Lumière d'Ewald, Sceau de proscription, Exorcisme). Note MJ : le Silence s'autorise ce qu'il interdit ; Lumière d'Ewald peut démasquer un doppelgänger (secret de Göre).
- **en test** — **Physicus** = tradition Alchimie. Préparations ordinaires (DC, sans trace) vs alchimiques (DP, palier, **chaque préparation en réserve retient un dé éphémère**). *Pourquoi :* même famille que les runes — la « magie préparée » se paie en dés retenus. Chirurgie : 5+ stabilise, 10+ = +1 PV au repos. Plus d'1 PV rendu = magie de soin.

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

### 2026-10-11 — Lore tranché d'après les résumés de session (`dev/sessions/`)

- **acté** — **Hahn, Göre et Kette, pupilles de l'Empereur** : otages par leur nature et leur statut, élevés par l'administration du palais, puis liés à l'Empereur lui-même. Après la guerre, Hahn, traumatisé lui aussi, dit à Göre qu'elle peut faire ce qu'elle veut. *Pourquoi :* concilie « l'Empereur m'a élevée » (Le Sucret, épisode 19) et « Hahn était très gentil » (épisode 20).
- **acté** — **Calendrier impérial** : l'Empereur à J+30, le Jubilé à J+45 (version CGI), avec un report possible par intempéries. `mj/timeline.md` est corrigé (au lieu de J+14). *Pourquoi :* deux semaines, c'était trop serré pour une table qui voulait faire toutes les quêtes secondaires.
- **acté** — **Lucie (Gouffre)** : enfant Iggigi élue par les créatures défuntes du Rêve. Elle est un peu le cauchemar : elle erre dans son sommeil et protège sa famille de Kette. Son pouvoir donne des animaux totems (le guépard de Ketnis).
- **acté** — **Origine des peuples** : à l'origine, des Elfes et des Humains. Pendant la guerre contre les dragons, une partie des Elfes devient les **Primordiaux** (vie infinie demandée aux dragons, car leurs livres théologiques les disaient éternels), une partie des Humains devient les **Akkadiens**. Les autres se sont mêlés au fil des générations : **elfe et demi-elfe d'aujourd'hui, c'est la même chose**, et rien à voir avec les Elfes anciens. Les Primordiaux tiennent à leur pureté. `mj/timeline.md` est harmonisé.
- **acté** — **Siège vacant et Hydre** : Kette étant mort dans l'esprit des gens, une place de Comte reste libre. L'Hydre (guilde des meilleurs profils, chambre de 11 représentants) doit en faire élire un. Jamais joué : ce peut être l'enjeu d'une campagne.
- **acté** — **Hahn** : elfe ; veuf de Francine la Grosse (Suéloise humaine, mariage d'alliance), jamais remarié. Ce mariage signale une politique neutre. Johan est un antagoniste facile, en contraste. Katarina von Hahn, dite sa nièce, est son arrière-petite-fille (confirmé).
- **acté** — **Willensein Sieben** (fils d'Arhedell, Empereur non élu) : opposant de Königsfell, **populaire**. C'est le camp de **Rodolphe Vauburg**, autre dynastie moins influente, qui fait traîner le vote pour déstabiliser l'autorité du fils et le rendre illégitime avec le temps. *Pourquoi :* le MJ s'était d'abord inversé, puis a corrigé sa relecture ; la version d'origine de `mj/timeline.md` était juste, elle est rétablie et précisée.
- **acté** — **Serment impérial réservé aux mages puissants** : Willensein et beaucoup de nobles n'y sont pas soumis. Un mage dans la famille, c'est comme un fils envoyé dans les ordres (un noble mage perd son titre).
- **acté** — **Le Maître des Voleurs** (distinct du Maître des rêves) peint des tableaux du Rêve et y enferme les gens ; sa quête mène vers Kette.
- **acté** — **Terry (CGI) devenu agent du Rêve** : un agent du chaos qui envoie les gens dans le Rêve. *Pourquoi :* un joueur débutant tuait trop ; on a transformé son personnage au lieu de le pénaliser. Modèle réutilisable pour le Manuel du maître.
- **ouvert** — Nowitzki (contexte perdu, piste libre) ; apprentis rivaux de l'épisode 21 (futurs Comtes ?) 
- **acté (leçon)** — **Points de karma** : ils devaient compenser une progression lente, mais, restés hors système, les joueurs les ont traités comme du butin et ils ont dérivé en dés du destin. *Pourquoi :* le système pèse plus que prévu sur le comportement. **Toute ressource du D10 doit être écrite dans les règles**, sinon elle sera lue comme un bonus.
- **en test** — **Scénario 02, *Le Bal des Armes*** (`campagnes/trames-du-onzieme/scenarios/02-bal-des-armes.md`) : réécrit à partir des notes du MJ et des épisodes 9 à 14. Échéance annoncée (minuit), règle des trois indices par conclusion, horloge par heure, PNJ secondaires passés dans une table de rencontres d10, Monzonite peut se rendre, magie au bal = trace. *Pourquoi :* autocritique du MJ (épisode 14) : prévu pour deux séances, joué en quatre ; les joueurs ne savaient pas pourquoi ils y allaient, et six PNJ n'ont jamais servi.
- **acté** — **« Le duc » = Hans d'Aragon** : frère de Jeanne la Folle, déchu en Alamania, jaloux des Comtes (son titre est plus prestigieux, leur pouvoir plus grand), tombé dans la sédition. En public, il réclame un vrai vote ; en secret, il finance le meurtre de l'Empereur (le feu grégeois, que Monzonite détourne contre sa mère) pour obtenir ensuite un vote favorable. Absent du rallye, que tient sa doublure Stefano ; présent au bal. *Pourquoi :* c'est l'intention du MJ, et cela relie l'arc des vampires, le rallye, le bal et l'exécution de Hans « pour complot contre l'Empereur » (épisode 16). Le carnet manuscrit pourra préciser.
- **acté (méthode)** — **Rattacher les historiques des PJ aux fils existants** : la mère d'Althaïr, abusée par un noble, devient une victime des Enfants de la Lune (Hans est son père) ; Docteur Schön, qui officiait dans un orphelinat, y rencontre Lucie, personnage déjà défini que la joueuse voulait d'abord inventer. *Pourquoi :* la cohérence prime sur la consistance de l'improvisation ; le Manuel du maître doit l'enseigner (session zéro : chaque historique reçoit un crochet vers un fil de campagne). **Garde-fou :** on propose, on n'impose pas. Le MJ offre au joueur d'intégrer son historique au lore, **avec son accord**, et le prévient des enjeux possibles (« ton passé touchera à une confrérie dangereuse ») sans dévoiler le secret.
- **acté** — **Auge, le funambule** : il aide les complots et finance les opposants, mais son serment lui interdit de s'impliquer dans un meurtre, même s'il sait que l'argent peut y mener. *Pourquoi :* le Serment repose en partie sur la perception ; Auge ne tient pas Willensein pour le véritable Empereur. Le Serment devient un levier de jeu : prouver qu'un financement a tué fait vaciller un Comte. Ses fonds peuvent se retrouver dans les caisses du camp Vauburg.
- **acté** — Les Imondi sont introduits, de façon facultative, pendant la quête des vampires (un village), pour créer des connexions avant le bal.
- **acté** — Scénario 01 et compagnon alignés sur le calendrier J+30 / J+45.
- **en test** — **Scénario 01 refondu** d'après les deux tables (Le Sucret 2–3, CGI 1–3) : vrai enjeu annoncé (étouffer ce qui remonte à Göre), crochets personnels **avec l'accord des joueurs**, Dévoterie, carnet d'Eichel (pont vers le scénario 02), **acte 6** (l'étable, l'ossuaire, le temple sous l'horloge des Promeneurs) et **horloge du rituel** : fusion ratée ou réussie selon le temps perdu. *Pourquoi :* le même scénario a donné Giorgio tué d'un côté, fusionné de l'autre ; le repaire, improvisé deux fois de la même façon, n'était pas écrit. Bureaucratie tranchée par un jet ou un flashback.
- **acté** — **Victimes du tueur** : Jonas Härig est vivant (prochaine cible), comme aux deux tables ; la deuxième victime, aux Fortecombles, s'appelle Konrad Weidlinger, greffier (nom arbitraire, rôle mineur). Le « démon » des notes devient la fusion avec le serpent de la ménagerie ; le « fils du juge » devient le juge Stäbler. `mj/timeline.md` aligné.
- **en test** — Piste **magie par privation** (Oyuun, d'après le wu jen de *Complete Arcane*, D&D 3.5, une mécanique très roleplay appréciée du MJ) : un interdit choisi renforce le sort. À rapprocher des interdits de tradition dans `regles/magie.md`.

---

## Questions ouvertes

1. **Archétypes** : Eau Calme, Ritualiste akkadien, Runiste, Théurge, Physicus complets dans `archetypes.md`. Les cinq autres de `creation-de-personnage.md` (Regrattier, Landsknecht, Juriste, Artisan, Émissaire) restent au format court.
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
