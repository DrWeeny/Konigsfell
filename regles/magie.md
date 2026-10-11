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

Les archétypes magiques commencent avec **+1 dé éphémère**.

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

Les paliers reprennent la [table des seuils](jets-de-des.md#seuils-de-difficulté) : la magie n'a pas d'échelle à part.

| Total | Palier | Ordre de grandeur |
|---|---|---|
| 3+ | **Mineur** | un effet utile et bref : éteindre une lanterne, sentir une rune |
| 5+ | **Standard** | l'effet décrit par le sort |
| 10+ | **Puissant** | plus grand, plus long, plusieurs cibles |
| 15+ | **Majeur** | un effet qui change la scène |
| 25+ | **Prodige** | un effet dont on parlera en ville |

Un sort précise ce qu'il fait à chaque palier. Un sort qui n'a pas de palier Mineur ne peut pas être lancé sous 5.

### Dés éphémères

Les dés éphémères engagés dans un sort sont **consommés** pour la scène. Le DP permanent ne l'est jamais. C'est la règle qui limite les sorts puissants : un mage peut atteindre le palier Majeur une fois, rarement deux, dans la même scène.

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

- Un sort **Majeur ou Prodige**, ou un **contrecoup**, se remarque : le Silence ou le Registre peut en entendre parler.
- Dans un lieu protégé par des runes de dissipation (Palais de Justice d'Ewald, temples, bureaux du Registre), aucun sort ne prend en dessous du palier Majeur.

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
| Archétype | 3 sorts d'archétype dès la création |
| XP | 1 nouveau sort de sa tradition : **4 XP** |
| Grimoire trouvé | +1 DP permanent, et souvent un sort |
| Parchemin | lancer un sort une fois, sans le connaître |
| Maître | un sort hors de sa tradition, contre un service ou une dette |

Un sort coûte 4 XP, comme un dé permanent : il ouvre une action nouvelle.

---

## Écrire un sort

| Champ | Contenu |
|---|---|
| **Nom** | |
| **Tradition** | et statut légal |
| **Type** | physique / esprit / objet-lieu |
| **Paliers** | ce que fait le sort à 3+, 5+, 10+, 15+, 25+ (au moins deux paliers) |
| **Grammaire** | le verbe utilisé s'il modifie des dés (relance, transfert, verrouillage…) |
| **Trace** | discret / visible / signé |

### Exemples

**Bouclier aqueux** — *Eau Calme, protection, physique*
- **Spécial** : permet de poser des DP en garde pendant le round.
- **5+** : une lame d'eau protège le mage.
- **10+** : le bouclier couvre aussi un allié au contact.
- **15+** : le bouclier tient jusqu'à la fin de la scène pour une seule garde de 1 dé, sans le dépenser.

**Jet d'eau pressurisé** — *Eau Calme, attaque, physique*
- **5+** : projette, renverse, éteint un feu.
- **10+** : inflige les dégâts de l'action, comme une attaque à distance.
- **15+** : traverse une garde — la cible ne peut engager qu'un seul dé de garde pour parer.

**Murmure des défunts** — *funéraire akkadienne, esprit, discret*
- **5+** : une question à un mort de moins d'un jour.
- **10+** : trois questions, ou un mort de moins d'un mois.
- **15+** : le mort répond avec sa voix, et se souvient de ce qu'il a vu.

**Lien de serment** — *Théurgie du Silence, esprit, signé*
- **10+** : deux personnes consentantes sont liées par une promesse ; celui qui la rompt le sait, et le théurge aussi.
- **15+** : la rupture fait souffrir. Un PJ lié ne peut pas engager de DP contre l'autre partie.
- **Interdit** : sans Empereur couronné, l'ancre du serment est incertaine. Le MJ peut décider qu'un lien ne tient pas.

---

[← Retour à l'accueil](../index.html) · [Jets de dés](jets-de-des.md) · [Résolution & Combat](resolution-et-combat.md) · [Archetypes et metiers](archetypes.md)
