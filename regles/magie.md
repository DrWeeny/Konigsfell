# La Magie

*À Königsfell, la magie est un talent, un métier et un délit. On la pratique avec un permis, sous l'œil du Silence, et chaque sort laisse une trace.*

> Ce chapitre est un **brouillon de conception**. Les blocs `::: dev` signalent ce qui reste à trancher. Il s'appuie sur les [Dés de Pouvoir](jets-de-des.md#dés-de-pouvoir--détail), la [Grammaire des dés](resolution-et-combat.md#grammaire-des-dés) et le [round de combat](resolution-et-combat.md#le-round).

---

## Qui pratique la magie

Tout le monde possède **1 DP permanent**. Ce n'est pas encore de la magie : c'est la volonté, la foi, la résistance de l'esprit. Il sert à **résister** aux sorts qui visent l'âme ou l'esprit, et à alimenter les capacités spéciales qui n'appartiennent à aucune école.

On devient **pratiquant** en appartenant à une **tradition**. La tradition donne :

- des **sorts d'archétype** (gratuits, connus dès le départ) ;
- un **statut légal** (permis, visa, tolérance, clandestinité) ;
- des **interdits** — ce que la tradition refuse, ou ce que la loi lui refuse.

On entre dans une tradition par sa **compétence majeure de tradition** (*Tradition de l'Eau Calme*, *Théurgie du Silence*…). Elle donne **+1 dé éphémère** au pool DP et les trois sorts d'archétype. Les archétypes de tradition l'ont dès la création. Un autre personnage peut l'acheter en jeu (4 XP), auprès d'un maître ou d'une guilde : il reçoit le dé éphémère et **un** sort d'archétype, les autres s'apprennent ensuite.

---

## Les traditions

| Tradition | Domaine | Statut à Königsfell | Interdits |
|---|---|---|---|
| **Eau Calme** (Sturmbrecher, Seekmeister, Windrufer, Unterhalt) | eau, glace, vent, climat, transit runique | légale — permis de la guilde | soin, contrôle mental, invocation de créatures aquatiques |
| **Théurgie du Silence** | serments, détection du sacrilège, purification, contre-magie | légale — la loi elle-même | tout ce qui prolonge la vie ; magie akkadienne |
| **Tradition funéraire akkadienne** | lecture des morts, préservation, souvenirs | tolérée — visa spécial, surveillance | animation combative des morts, contrôle d'esprit, soin |
| **Runistes** | magie **préparée** : runes d'alarme, de dissipation, de scellement, Taufbecken | légale — poinçon déposé au Registre | runes sur le vivant |
| **Alchimie** (Physicus, verriers) | préparations, poisons, analyses, fioles | grise — la matière n'est pas la magie… tant qu'on ne soigne pas | élixirs de jouvence, remèdes « trop » efficaces |

### Les arts proscrits

Aucune tradition légale ne les enseigne. Ils existent dans les archives du Silence, dans les cales de contrebandiers, dans les légendes.

- **Nécromancie** — lever les morts, les commander. Le cœur de la guerre contre l'Akkadie.
- **Magie de soin** — assimilée à la nécromancie : *repousser la mort est un blasphème*.
- **Peausserie** — l'échange de peaux, art dissous par le Roi Peausserie (voir [La Cité du Roi Peausserie](../univers/contes/la-cite-du-roi-peausserie.md)).
- **Contrôle mental** — interdit par toutes les traditions, pratiqué par certaines.

Les runistes ne lancent pas leurs sorts, ils les **gravent** à l'avance : voir l'archétype [Runiste du Registre](archetypes.md#runiste-du-registre). Les alchimistes font de même avec leurs **préparations** : voir [Physicus](archetypes.md#physicus--docteur-chirurgien). Dans les deux cas, chaque effet en réserve retient un dé éphémère.

::: mj
Les arts proscrits sont des **ressources de scénario**, pas des options de création. Un PJ peut les approcher (un grimoire, un prêtre véreux, un rituel akkadien), mais chaque usage est une prise que quelqu'un pourra exercer sur lui.
:::

---

## Lancer un sort

Un sort est une **action** formée avec des dés de Pouvoir. Il suit la mécanique de base : on lance tout le pool DP, on regarde, puis on assigne.

1. Le joueur annonce le sort et sa cible.
2. Il forme une action avec un ou plusieurs DP (plancher : total 3).
3. Le total détermine le **palier** atteint.
4. Si le sort vise une créature, elle s'y oppose (voir *Résister*).

### Les paliers

Les paliers sont les [seuils de difficulté](jets-de-des.md#seuils-de-difficulté), avec leurs noms : la magie n'a ni échelle ni vocabulaire à part. On dit « un sort à 10+ ».

| Total | Seuil | Ordre de grandeur |
|---|---|---|
| 3+ | **Facile** | un effet utile et bref : éteindre une lanterne, sentir une rune |
| 5+ | **Moyen** | l'effet de base du sort |
| 10+ | **Difficile** | plus grand, plus loin, plusieurs cibles |
| 15+ | **Très difficile** | un effet qui change la scène |
| 25+ | **Quasi impossible** | un effet dont on parlera en ville |

Un sort précise ce qu'il fait à chaque palier ; ce seuil se calcule avec la [formule](#écrire-un-sort--la-formule). Un sort qui n'a pas d'effet à 3+ ne peut pas être lancé sous 5.

### Dés éphémères

Les dés éphémères engagés dans un sort sont **consommés** pour la scène. Le DP permanent ne l'est jamais. C'est la règle qui limite les sorts puissants : un mage peut atteindre 15+ une fois, rarement deux, dans la même scène.

::: dev
Question ouverte (n° 4 de `CLAUDE.md`) : les éphémères se lancent-ils avec le pool, de couleur différente, et le joueur choisit ensuite lesquels engager ? Proposition : oui. Le joueur sait ce qu'il dépense, et la décision reste dans l'assignation.
:::

### Résister

| Type de sort | La cible oppose |
|---|---|
| Physique (jet d'eau, glace, flamme) | sa **garde**, comme une attaque ([Attaque et défense](resolution-et-combat.md#attaque-et-défense)) |
| Esprit ou âme (serment, peur, lecture) | ses **DP** — chacun en a au moins un |
| Sur un objet, un lieu, l'eau | pas d'opposition, seulement le palier |

Les dégâts d'un sort physique suivent la règle des attaques : somme brute − défense engagée − armure.

### Doubles et contrecoup

- Les doubles comptent comme partout : **V × 3 pour atteindre le palier**, somme brute pour les dégâts.
- **Double 1 = contrecoup.** Le sort échoue et se retourne : le mage subit l'effet, perd un dé éphémère jusqu'à la nuit, ou la magie déborde dans le décor. Le MJ choisit.

### La trace

Chaque sort laisse une trace que les runistes et les théurges savent lire.

- Un sort à **15+**, un sort **improvisé**, ou un **contrecoup**, se remarque : le Silence ou le Registre peut en entendre parler.
- Dans un lieu protégé par des runes de dissipation (Palais de Justice d'Ewald, temples, bureaux du Registre), aucun sort ne prend en dessous de 15.

::: dev
La trace est le principal frein à la magie, et il est **politique** plutôt que mécanique : conforme au ton de la campagne. À tester : est-ce que ça suffit à empêcher le mage de tout résoudre hors combat ?
:::

---

## Le mage en combat

Les pools ne se mélangent pas : une action est faite **soit** de DA, **soit** de DP. Dans un round, un personnage dispose des deux pools.

- **Gardes** : on garde avec des DA. Un mage qui connaît un **sort de protection** (*Bouclier aqueux*, *Lien de serment*…) peut aussi poser des **DP en garde**. Ils parent comme des dés de garde, et les éphémères posés ainsi sont consommés.
- **Actions** : les DP restants servent à lancer des sorts.

Un mage sans sort de protection est fragile : il compte sur sa garde en DA (2 dés au départ), sa distance et ses alliés.

::: dev
**Problème n° 3 de `CLAUDE.md`.** Proposition retenue ici : *sorts défensifs qui dépensent du DP* (option A du handoff). Elle donne un vrai choix d'assignation — protéger ou frapper — et s'appuie sur des sorts qui existent déjà (*Bouclier aqueux*).

**Tranché :** la garde magique est ouverte à tous. Un guerrier qui apprend *Bouclier aqueux* gagne peu — se protéger des flammes, se passer d'un bouclier encombrant — et avec un seul DP, il risque toujours un 1 ou un 2 (sous le plancher).
:::

### Le contre-sort

Un pratiquant qui connaît le **contre-sort** (sort d'archétype du Théurge du Silence) peut poser des DP en garde **contre la magie** pendant la phase des gardes.

- Quand un sort vise le théurge ou un allié qu'il voit, il engage tout ou partie de ces dés.
- Si leur total (doubles compris) **égale ou dépasse** celui du sort, le sort est annulé. L'égalité va au contre-sort, comme à tout défenseur.
- Les dés engagés sont dépensés, réussite ou non. Les éphémères sont consommés.

Le contre-sort ne pare pas les coups : des DP posés contre la magie ne servent à rien contre une lame. C'est le choix d'assignation du théurge.

---

## Apprendre des sorts

| Source | Effet |
|---|---|
| Archétype de tradition | 3 sorts d'archétype dès la création |
| Entrer dans une tradition en jeu | **4 XP** (compétence majeure de tradition) : le dé éphémère et 1 sort d'archétype |
| XP | 1 nouveau sort de sa tradition : **4 XP** |
| Grimoire trouvé | +1 DP permanent, et souvent un sort |
| Parchemin | lancer un sort une fois, sans le connaître |
| Maître | un sort hors de sa tradition, contre un service ou une dette |

Un sort coûte 4 XP, comme un dé permanent : il ouvre une action nouvelle.

---

## Écrire un sort : la formule

Le seuil d'un effet se **calcule**. On additionne les composantes, puis on **arrondit au seuil supérieur** (3, 5, 10, 15, 25). Le MJ s'en sert pour écrire un sort, pour chiffrer un sort inventé par un joueur, et pour arbitrer une improvisation.

| Composante | Valeur |
|---|---|
| **Verbe** | Percevoir 3 · Altérer 5 · Créer ou Contrôler 10 |
| **Portée** (dans l'espace ou dans le temps) | contact, ou moins d'un jour : 0 · à vue, ou moins d'un mois : +5 · hors de vue, ou moins d'un an : +10 |
| **Durée** | instant : 0 · la scène : +5 · permanent : +10 |
| **Cibles** | une : 0 · un groupe : +5 |
| **Effet sur les dés** ([Échelle de puissance](echelle-de-puissance.md)) | aucun ou Léger : 0 · Notable ou Fort : +5 · Exceptionnel : +10 · Relique : réservé aux artefacts |
| **Restrictions** | une circonstance (consentement, eau présente, de nuit) : −5 · un prix réel (PV, serment, interdit personnel) : −10 |

- **Minimum 3.** Le domaine (l'eau, les morts, les serments) n'entre pas dans le calcul : c'est la tradition qui le fixe.
- **La précision achète la puissance**, comme pour les compétences mineures. Un interdit personnel choisi en apprenant le sort (ne jamais le lancer à jeun, jamais contre un enfant, jamais sans avoir prié) compte comme un prix réel.
- Un sort écrit, c'est la formule déjà calculée pour chacun de ses paliers.

::: dev
**En test.** Formule tirée du journal de conception (`mj/journal-de-conception.md`, d'après Ars Magica et les restrictions du Nen). Ajouts : la portée vaut aussi dans le temps (pour les morts et les souvenirs), et l'effet sur les dés se chiffre avec l'échelle de puissance. La restriction par interdit personnel rejoint la piste « magie par privation » de `CLAUDE.md`. Il faudra un **inventaire** verbe × domaine, 2 ou 3 exemples par case, pour donner la tonalité de Königsfell.
:::

### Improviser

Un pratiquant peut tenter un effet qu'il n'a pas appris, **dans le domaine de sa tradition** :

- on calcule le seuil avec la formule, puis on monte d'**un seuil** (5 → 10, 10 → 15…) ;
- l'improvisation laisse **toujours une trace**, même sous 15 ;
- hors du domaine de sa tradition, on n'improvise pas : c'est le territoire des arts proscrits.

Un sort appris, c'est une improvisation devenue routine : les 4 XP achètent la fiabilité et la discrétion.

### La fiche d'un sort

| Champ | Contenu |
|---|---|
| **Nom** | |
| **Tradition** | et statut légal |
| **Type** | physique / esprit / objet-lieu |
| **Paliers** | ce que fait le sort à 3+, 5+, 10+, 15+, 25+ (au moins deux paliers), avec le calcul |
| **Grammaire** | le verbe utilisé s'il modifie des dés (relance, transfert, verrouillage…) |
| **Trace** | discret / visible / signé |

### Exemples

**Bouclier aqueux** — *Eau Calme, protection, physique*
- **Spécial** : permet de poser des DP en garde pendant le round.
- **5+** : une lame d'eau protège le mage. *(Altérer 5)*
- **10+** : le bouclier couvre aussi un allié au contact. *(Altérer 5 + groupe 5)*
- **15+** : le bouclier tient jusqu'à la fin de la scène pour une seule garde de 1 dé, sans la dépenser. *(Altérer 5 + scène 5 + effet Fort 5)*

**Jet d'eau pressurisé** — *Eau Calme, attaque, physique*
- **5+** : au contact, projette, renverse, éteint un feu. *(Altérer 5)*
- **10+** : à vue ; mêmes effets, ou inflige les dégâts de l'action, comme une attaque à distance. *(Altérer 5 + vue 5)*
- **15+** : traverse une garde — la cible ne peut engager qu'un seul dé de garde pour parer. *(Altérer 5 + vue 5 + effet Fort 5)*

**Murmure des défunts** — *funéraire akkadienne, esprit, discret*
- **3+** : une question à un mort de moins d'un jour. *(Percevoir 3)*
- **10+** : trois questions, ou un mort de moins d'un mois. *(Percevoir 3 + scène 5, ou + un mois 5 → 8, arrondi à 10)*
- **15+** : un mort de moins d'un an répond avec sa voix, et se souvient de ce qu'il a vu. *(Percevoir 3 + un an 10 → 13, arrondi à 15)*

**Lien de serment** — *Théurgie du Silence, esprit, signé*
- **10+** : deux personnes consentantes sont liées par une promesse ; celui qui la rompt le sait, et le théurge aussi. *(Contrôler 10 + permanent 10 + groupe 5 − consentement 5 − prix réel 10 : le théurge porte le serment)*
- **15+** : la rupture fait souffrir. Un PJ lié ne peut pas engager de DP contre l'autre partie. *(+ effet Fort 5)*
- **Interdit** : sans Empereur couronné, l'ancre du serment est incertaine. Le MJ peut décider qu'un lien ne tient pas.

**Improvisation — geler une serrure** — *Eau Calme*
Une mage veut geler l'intérieur d'une serrure à vue pour bloquer une porte jusqu'à la fin de la scène : Altérer 5 + vue 5 + scène 5 = 15. Elle ne connaît pas ce sort : elle improvise, donc **25+**. Elle préfère s'approcher : au contact, 10, improvisé **15+**, et une trace.
---

[← Retour à l'accueil](../index.html) · [Jets de dés](jets-de-des.md) · [Résolution & Combat](resolution-et-combat.md) · [Archétypes](archetypes.md)
