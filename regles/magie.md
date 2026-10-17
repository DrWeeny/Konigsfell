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

### La magie préparée

Les runistes **gravent** leurs sorts, les alchimistes les **préparent** en fioles : voir [Runiste du Registre](archetypes.md#runiste-du-registre) et [Physicus](archetypes.md#physicus--docteur-chirurgien). Leur avantage, c'est le temps : au calme, ils ne lancent pas les dés.

- **Pas de jet.** Le palier vaut **5 par DP engagé** : 1 dé → 5+, 2 → 10+, 3 → 15+. Ni double, ni contrecoup. **Seul, un préparateur ne dépasse pas 15+**, quel que soit le nombre de ses dés.
- **Le 25+ est une œuvre collective.** Il faut un cercle (toute une guilde, un atelier du Registre, les moines d'un Taufbecken), un lieu qui s'y prête et une semaine de travail ; le MJ fixe la condition, et chaque participant y retient un éphémère. C'est ainsi qu'on grave les runes du Palais de Justice ou les bassins de transit.
- **Le temps.** Quelques minutes jusqu'à 5+, une heure à 10+, une nuit à 15+. Sous la pression d'une scène, on lance comme pour un sort ordinaire.
- **Le prix.** Chaque effet en réserve **retient un dé éphémère**, quel que soit son palier, jusqu'à ce qu'il se déclenche ou soit effacé. Le DP permanent ne se retient pas : le nombre d'éphémères fixe le nombre de runes ou de fioles actives. Les autres dés puisés reviennent après une nuit, comme toujours.
- **La durée ne compte pas** dans la formule : l'effet tient jusqu'à son déclenchement, et c'est le dé retenu qui le paie : il ne revient pas avec la nuit tant que l'effet existe.
- **Déclencher n'est pas lancer.** Briser une fiole, toucher une rune ou dire son mot de déclenchement est une action de DA (un tir pour une fiole lancée), pas le sort du round. Le runiste et le Physicus ont payé d'avance : en combat, ils peuvent déclencher une préparation et lancer un sort.

::: dev
**En test (2026-10-16).** « 5 par dé » est un peu sous la moyenne d'un d10 (5,5) : prendre son temps garantit le résultat moyen, sans la chance des doubles. Le runiste et le Physicus perdent la surprise mais gagnent la fiabilité.

**Plafond 15+ (2026-10-17).** Sans jet, il n'y a pas de double 1 : cinq éphémères auraient donné une rune 25+ sans aucun risque. Le lanceur, lui, est freiné par le contrecoup (avec 6 dés, environ une chance sur neuf) ; le préparateur l'est par le plafond.
:::

::: mj
Les arts proscrits sont des **ressources de scénario**, pas des options de création. Un PJ peut les approcher (un grimoire, un prêtre véreux, un rituel akkadien), mais chaque usage est une prise que quelqu'un pourra exercer sur lui.
:::

---

## Lancer un sort

Un sort est une **action** formée avec des dés de Pouvoir. Il suit la mécanique de base : on lance, on regarde, on assigne, et si besoin on **puise** dans sa réserve.

1. Le joueur annonce le sort et sa cible.
2. Il lance ses **DP de base** (le DP permanent, un focus de bonne facture, les DP gagnés en jeu) et forme une action avec un ou plusieurs d'entre eux (plancher : total 3).
3. Avant la résolution, il peut **puiser** dans sa réserve de dés éphémères (voir *La réserve*).
4. Le total détermine le **palier** atteint.
5. Si le sort vise une créature, elle s'y oppose (voir *Résister*).

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

### Un sort par round

En combat, un personnage lance **un seul sort par round**. Avec 5, 10, 8 et 7 sur ses DP de base, un mage ne fait pas trois petits sorts : il en lance un, avec les dés qu'il veut, et les autres ne servent pas ce round, sauf s'il les a posés en garde au début (voir *Le mage en combat*).

- **Les dés de base** servent aux sorts faciles, round après round : ils ne s'usent pas.
- **La réserve** sert aux gros sorts : atteindre 10+ ou 15+, passer un contre-sort ou une rune de dissipation.

::: dev
**En test (2026-10-16).** Poser des DP en garde (sort de protection, contre-sort) ne compte pas comme le sort du round.
:::

### L'écho

**Une fois par scène**, quand un sort réussit, le mage peut le **faire résonner** : il [paie comptant](jets-de-des.md#payer-un-dé) autant de dés éphémères que l'action comptait de dés, base et réserve confondues. Le même sort, **au même total**, touche une seconde cible ou se reproduit ailleurs à sa portée.

- **Pas de nouveau jet** : ni double, ni contrecoup. La cible de l'écho résiste comme la première.
- L'écho ne compte pas comme un second sort. Il ne s'applique ni au contre-sort ni à la magie préparée.
- Il vide vite la réserve : c'est le grand moment du mage, pas sa routine.

**Exemple.** Schön lance *Bourrasque* à 15+ avec ses trois DP de base pour désarçonner un chevalier en vol. Le sort passe. Elle paie trois éphémères : la même rafale, au même total, frappe la wyverne du second chevalier. Sa réserve est vide jusqu'à la nuit.

::: dev
**En test (2026-10-17).** Idée du MJ (« valider le sort et, si succès, utiliser le même nombre de dés éphémères pour un burst »). Le test de progression montrait un guerrier chevronné qui engage 6 dés par round contre un seul sort pour le mage. L'écho double le sort sans rouvrir les sorts multiples : un seul jet, un seul risque de double 1, et un prix en fatigue. « Un sort de plus tous les 5 dés » a été écarté : le pool de base d'un mage n'y arrive jamais, et cela rouvrait les petits sorts en rafale.
:::

### La réserve : les dés éphémères

Les dés éphémères ne se lancent pas avec le pool. Ils forment une **réserve** où le mage puise : c'est sa fatigue. Elle se remplit avec la **tradition** (+1), le **focus** ordinaire (+1) et l'XP.

Les **DP de base**, eux, reviennent à chaque scène, comme les DA d'un guerrier : le DP permanent, un focus de bonne facture, et les DP achetés à l'XP (4 / 8 / 12… XP, comme les DA). C'est avec eux qu'un mage chevronné lance un sort **et** pose une garde magique dans le même round.

- **À tout moment**, quand il lance un sort ou engage un contre-sort, le mage peut **puiser** : il lance un ou plusieurs éphémères et les ajoute à l'action, après avoir vu ses dés de base. Les doubles se lisent sur tous les dés de l'action, double 1 compris.
- Les dés puisés sont **épuisés** jusqu'à une nuit de repos complet.
- Le DP permanent ne s'épuise jamais.

C'est la règle qui limite les sorts puissants. Un mage débutant a 2 éphémères : deux coups de pouce par jour, ou un seul gros sort.

**Exemple.** Une mage de l'Eau Calme veut renverser un groupe d'une vague (*Déplacement de l'eau*, 15+). Son DP permanent donne 6 : trop peu. Elle puise un éphémère : 6. Double 6 → 18, la vague passe. Il lui reste un éphémère pour la journée.

### Les focus

Un **focus** (bâton, pyramide-clef, encensoir, poinçon, mortier) canalise la magie. Il faut le tenir en main, et on n'en utilise qu'un à la fois.

| Focus | Effet | Où le trouver |
|---|---|---|
| **Ordinaire** | +1 dé éphémère dans la réserve | dans l'équipement de départ de chaque tradition ([Armurerie](armurerie.md#les-packs-de-départ)) |
| **De bonne facture** et au-delà | +1 DP **de base**, réservé aux sorts, comme le dé d'attaque d'une épée ; la facture suivante s'ajoute ensuite ([Échelle de puissance](echelle-de-puissance.md#facture--ce-qui-sajoute-à-la-base)) | en jeu : récompense, maître, commande à un artisan |

::: dev
**En test (2026-10-16).** La réserve remplace l'ancien modèle (éphémères lancés avec le pool, consommés pour la scène) et la règle d'épuisement, devenue inutile : la recharge à la nuit suffit à freiner le « tout ou rien ». Elle répond aussi à la question n° 4 de `CLAUDE.md` : les éphémères ne se distinguent plus à la table, ils se lancent à part.
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
- Là où une **Sirène** est postée, tout sort se remarque (voir ci-dessous).

::: dev
La trace est le principal frein à la magie, et il est **politique** plutôt que mécanique : conforme au ton de la campagne. À tester : est-ce que ça suffit à empêcher le mage de tout résoudre hors combat ?
:::

### Les sens du Silence

Le Silence entretient des ordres qui ont sacrifié un sens ou un membre pour gagner un pouvoir. Ce pouvoir ne se lance pas : **sans jet**, ce n'est pas un sort, c'est ce qu'ils sont devenus. Seul ce qu'ils imposent à autrui demande des dés.

| Ordre | Privé de | Pouvoir |
|---|---|---|
| **Les Sirènes** | l'odorat | sentent toute magie lancée dans leur périmètre (un quai, une place, un bâtiment), même discrète et sous 15, et sa tradition |
| *(à nommer)* | l'ouïe | sentent tout mouvement autour d'eux, même dans le noir ou derrière un mur |
| *(à nommer)* | la vue | sentent les esprits présents et parlent par télépathie ; sonder les pensées : la cible oppose ses DP, comme à un sort d'esprit |
| *(à nommer)* | les mains | télékinésie : saisir, porter, ouvrir à distance comme avec des mains ; contre une personne (désarmer, saisir, projeter), action en DP, la cible oppose sa garde, comme à un sort physique |
| *(à nommer)* | les jambes | volent comme on marche ; leurs dés de mouvement servent dans les airs |

**Le cri des Sirènes.** Une Sirène pose des DP en garde, comme pour un [contre-sort](#le-contre-sort), et crie au premier sort lancé dans son périmètre.
- **Interrompre** : tout sort lancé dans le périmètre pendant ce round, et dont le total ne dépasse pas celui du cri, est annulé. Un seul cri touche tous les lanceurs.
- **Ébranler** : chacun de ceux qui l'entendent oppose ses DP. En dessous du total du cri, il est ébranlé : au round suivant, il retire son dé le plus haut avant d'assigner.
- Un sourd n'entend pas le cri.

::: mj
**Le palladium.** Chaque ordre porte une greffe de palladium, souvent à même la chair, à la place de ce qu'il a perdu. La greffe est forte : c'est le métal qui sent, saisit ou porte, et c'est pourquoi ses porteurs n'ont pas besoin de dés. Le Silence l'exploite dans la mine des Monts Spectraux et convoite la veine sous le Gouffre (voir `mj/timeline.md`, *Le Palladium et le Silence*). Proteo, qui sniffe la poudre, sent à son tour les membres du Silence : il emprunte, sans le savoir, le sens des Sirènes.
:::

::: dev
**En test (2026-10-16), à revérifier par le MJ dans ses notes** : les cinq ordres, leurs privations et leurs noms. À la table, les noms étaient *Méduse*, *Basilic* et *Sirènes* ; le MJ trouve qu'ils ne collent pas au lore (créatures grecques dans une cité germanique). Piste : des noms allemands ironiques, comme le reste du vocabulaire de la ville (*Taufbecken*, *Sturmbrecher*) — chaque ordre nommé d'après ce qu'il a perdu et retrouvé par le métal : *Lauscher* (les sourds qui écoutent le mouvement), *Seher* (les aveugles qui voient les esprits), *Greifer* (les sans-mains qui saisissent), *Läufer* (les sans-jambes qui courent dans les airs). *Sirènes* peut rester le surnom populaire de l'ordre qui crie. La privation rejoint la piste « magie par privation » de `CLAUDE.md` : un interdit réel achète un pouvoir. Le cri reprend le contre-sort et le verbe miroir « dé le plus haut retiré avant assignation » ([Grammaire des dés](resolution-et-combat.md)).
:::

---

## Le mage en combat

Les pools ne se mélangent pas : une action est faite **soit** de DA, **soit** de DP. Dans un round, un personnage dispose des deux pools.

- **Gardes** : on garde avec des DA. Un pratiquant peut aussi poser des **DP en garde**, comme un guerrier garde ses dés : contre la magie (le *contre-sort*, ci-dessous), ou contre les coups s'il connaît un **sort de protection** (*Bouclier aqueux*…). Il peut puiser dans sa réserve au moment de les engager.
- **Actions** : les DP restants servent au sort du round (un seul, voir [Un sort par round](#un-sort-par-round)).

Un mage sans sort de protection est fragile face aux lames : il compte sur sa garde en DA (2 dés au départ), sa distance et ses alliés.

::: dev
**Problème n° 3 de `CLAUDE.md`.** Proposition retenue ici : *sorts défensifs qui dépensent du DP* (option A du handoff). Elle donne un vrai choix d'assignation — protéger ou frapper — et s'appuie sur des sorts qui existent déjà (*Bouclier aqueux*).

**Tranché :** la garde magique est ouverte à tous. Un guerrier qui apprend *Bouclier aqueux* gagne peu — se protéger des flammes, se passer d'un bouclier encombrant — et avec un seul DP, il risque toujours un 1 ou un 2 (sous le plancher).
:::

### Le contre-sort

Tout **pratiquant** (un personnage qui a une tradition) peut poser des DP en garde **contre la magie** pendant la phase des gardes.

- Quand un sort le vise, ou vise un allié qu'il voit, il engage tout ou partie de ces dés, et peut puiser dans sa réserve.
- Si leur total (doubles compris) **égale ou dépasse** celui du sort, le sort est annulé. L'égalité va au contre-sort, comme à tout défenseur.
- Les dés de garde engagés sont dépensés, réussite ou non. Les éphémères puisés sont épuisés jusqu'à la nuit.

Le contre-sort ne pare pas les coups : des DP posés contre la magie ne servent à rien contre une lame. C'est le choix d'assignation du mage.

---

## Apprendre des sorts

| Source | Effet |
|---|---|
| Archétype de tradition | 3 sorts d'archétype dès la création |
| Entrer dans une tradition en jeu | **4 XP** (compétence majeure de tradition) : le dé éphémère de réserve et 1 sort d'archétype |
| XP | 1 nouveau sort de sa tradition : **4 XP** |
| XP | +1 DP de base : **4 / 8 / 12… XP**, comme les DA |
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
**En test.** Formule tirée du journal de conception (`mj/journal-de-conception.md`, d'après Ars Magica et les restrictions du Nen). Ajouts : la portée vaut aussi dans le temps (pour les morts et les souvenirs), et l'effet sur les dés se chiffre avec l'échelle de puissance. La restriction par interdit personnel rejoint la piste « magie par privation » de `CLAUDE.md`. L'**inventaire** verbe × domaine est plus bas (proposition du 2026-10-16, à relire).
:::

### Improviser

Un pratiquant peut tenter un effet qu'il n'a pas appris, **dans le domaine de sa tradition** :

- on calcule le seuil avec la formule, puis on monte d'**un seuil** (5 → 10, 10 → 15…) ;
- l'improvisation laisse **toujours une trace**, même sous 15 ;
- hors du domaine de sa tradition, on n'improvise pas : c'est le territoire des arts proscrits.

Un sort appris, c'est une improvisation devenue routine : les 4 XP achètent la fiabilité et la discrétion.

### Inventaire : verbe × domaine

Ce que chaque tradition sait faire, verbe par verbe, avec le seuil calculé. Ce ne sont pas des sorts appris : ce sont des repères pour **improviser** (un seuil de plus, et une trace) ou pour écrire un nouveau sort. Les traditions préparées (runes, fioles) ne comptent pas la durée.

**Eau Calme** — *l'eau, la glace, le vent, les bassins*

| Verbe | Exemples |
|---|---|
| **Percevoir** | lire le courant d'un canal et savoir où il mène (3+) · sentir qu'on s'est noyé ici, dans l'eau à vue (3 + vue 5 → **10+**) · prévoir la prochaine grosse vague du mois (3 + un mois 5 → **10+**) |
| **Altérer** | faire frissonner l'eau d'un bassin pour y écrire un mot (5+) · pousser une bourrasque dans une voile à vue (5 + vue 5 → **10+**) · geler les pavés sous un groupe à vue pour la scène (5 + vue 5 + scène 5 + groupe 5 → **25+**) |
| **Créer / Contrôler** | remplir une gourde d'eau douce (10+) · lever un brouillard sur une place pour la scène (10 + scène 5 → **15+**) · faire remonter une gondole à contre-courant, à vue (10 + vue 5 → **15+**) |

**Théurgie du Silence** — *les serments, le sacrilège, la purification*

| Verbe | Exemples |
|---|---|
| **Percevoir** | savoir si quelqu'un a juré sur la tête de l'Empereur aujourd'hui (3+) · sentir un sacrilège commis dans ce lieu depuis moins d'un mois (3 + un mois 5 → **10+**) |
| **Altérer** | purifier une eau ou une plaie souillée (5+, sans soigner) · affaiblir la rune d'un autre : son palier baisse d'un seuil (5 + effet Notable 5 → **10+**) |
| **Créer / Contrôler** | sceller une porte au nom d'Ewald, pour toujours, en y engageant son propre serment (10 + permanent 10 − prix réel 10 → **10+**) · imposer le silence à une foule à vue pour la scène, après sommation (10 + vue 5 + scène 5 + groupe 5 − circonstance 5 → **25+** : on en parlera en ville) |

**Tradition funéraire akkadienne** — *les morts, les souvenirs, la préservation*

| Verbe | Exemples |
|---|---|
| **Percevoir** | savoir depuis combien de temps ce corps est mort (3+) · voir le dernier souvenir d'un mort de moins d'un mois (3 + un mois 5 → **10+**) |
| **Altérer** | apaiser un mort qui s'agite avant l'Incorporation (5+) · effacer l'odeur de la mort d'une pièce pour la scène (5 + scène 5 → **10+**) |
| **Créer / Contrôler** | faire parler un crâne pour la scène, avec l'accord de sa famille (10 + scène 5 − consentement 5 → **10+**) · ⚠ au-delà, on lève les morts : c'est la nécromancie, un art proscrit |

**Runistes** — *magie préparée : alarme, dissipation, scellement, transit*

| Verbe | Exemples |
|---|---|
| **Percevoir** | une rune-témoin qui retient le visage du dernier qui l'a touchée (3+) · lire si un coffre a été ouvert depuis moins d'un mois (3 + un mois 5 → **10+**) |
| **Altérer** | une rune qui chauffe un poêle ou refroidit un tonneau (5+) · une rune qui alourdit une serrure : −1 dé à qui veut la crocheter (5 + effet Notable 5 → **10+**) |
| **Créer / Contrôler** | sceller une porte (10+) · une rune de transit vers un Taufbecken hors de vue (10 + hors de vue 10 → **25+**) |

**Alchimie** — *la matière, les poisons, les fioles*

| Verbe | Exemples |
|---|---|
| **Percevoir** | reconnaître un poison au goût ou à l'odeur (3+) · dater une tache de sang de moins d'un mois (3 + un mois 5 → **10+**) |
| **Altérer** | une encre qui disparaît au soleil (5+) · une poudre qui fait rouiller une serrure en une nuit (5+) · un somnifère : la cible perd un dé de son prochain jet (5 + effet Notable 5 → **10+**) |
| **Créer / Contrôler** | une fiole de fumée qui couvre un groupe (10 + groupe 5 → **15+**) · ⚠ le feu grégeois : 15+ et une trace, car le Silence en surveille chaque ingrédient |

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
