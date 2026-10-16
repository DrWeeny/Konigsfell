# Jets de Dés

*Le système de Königsfell repose sur trois pools de dés distincts et une mécanique d'assignation tactique : on lance d'abord, on décide ensuite.*

> Pour le round de combat détaillé (initiative, gardes, attaque/défense, armure, mouvement) et le cadre de conception des objets magiques, voir [Résolution & Combat](resolution-et-combat.md).

---

## Les Trois Pools

Chaque personnage possède trois pools indépendants de **dés à 10 faces (D10)** :

| Pool | Usage |
|---|---|
| **Dés d'Action (DA)** | Combat, mouvement physique, actions corporelles |
| **Dés de Compétence (DC)** | Diplomatie, investigation, connaissances, artisanat |
| **Dés de Pouvoir (DP)** | Magie, rituels, capacités spéciales |

Chaque pool est utilisé séparément selon la nature de la situation.

---

## Mécanique de Base — Lancer puis Assigner

**1. Rassembler le pool**
Déterminer combien de dés sont disponibles selon le pool concerné.

**2. Lancer tous les dés en même temps**
On ne lance pas en plusieurs fois — tout sort ensemble.

**3. Regarder les résultats, puis assigner**
Le joueur répartit ses dés en **actions**. Une action est formée d'un dé seul ou de plusieurs dés combinés :
- Attaques
- Défenses (dés en réserve)
- Mouvements
- Sorts
- Actions tactiques

**4. Résoudre contre les seuils ou l'opposition**

### Plancher d'action

**Une action demande un total minimum de 3.** Un 1 ou un 2 isolé ne peut rien tenter : il doit être combiné à un autre dé, placé en garde, ou laissé de côté.

---

## Seuils de Difficulté

*Table de référence unique — les autres chapitres y renvoient.*

Le MJ fixe un seuil avant le jet selon la difficulté de l'action :

| Difficulté | Seuil |
|---|---|
| Automatique | Pas de jet |
| Facile | 3+ |
| Moyen | 5+ |
| Difficile | 10+ |
| Très difficile | 15+ |
| Quasi-impossible | 25+ |

Les paliers 15+ et 25+ ne sont pas atteignables avec un pool de départ : ils passent par la magie, la progression, les objets et les doubles.

Pour les jets opposés, le seuil est le résultat de l'adversaire. **L'égalité va au défenseur.**

---

## Combiner des Dés

Plusieurs dés peuvent être **combinés sur une même action** en additionnant leurs valeurs.

**Exemple :**
Attaque avec 2 dés — résultats 5 et 3 → total 8. Utile pour surpasser une défense ennemie élevée.

Un **bonus de compétence** (+1, +2…) s'ajoute **une fois au total de l'action**, pas à chaque dé.

---

## La Règle des Doubles

Quand deux dés de même valeur sont **combinés sur une même action**, des règles spéciales s'appliquent. Les doubles se lisent sur les faces naturelles, avant tout bonus.

### Doubles positifs

| Double | Effet |
|---|---|
| Double quelconque (ex : 7, 7) | Vaut **V × 3** pour réussir (7,7 → 21) |
| Double 10 | **Critique** — effet narratif décisif, ignore l'armure |

- Le bonus du double ne compte que pour **réussir** (passer un seuil, battre une opposition).
- Les **dégâts** se calculent sur la somme brute (7,7 → 14), plus les bonus d'objet ou de compétence : seul le bonus du double est réservé à la réussite. Même règle en défense.
- **Trois dés identiques** : on en choisit deux pour la paire, le troisième reste un dé normal. Pas de triple.

::: dev
Les doubles restent en test : la règle « effets doublés » de la première version rendait les dégâts trop violents. Voir `CLAUDE.md`, journal de conception.
:::

### Double 1 — Échec Critique

Si le pool contient **deux ou plusieurs 1**, le joueur **doit** former une action avec deux de ces 1, résolue en premier.

| Résultats | Obligation |
|---|---|
| 1, 1, 6 | Action avec (1,1) = échec critique. Le 6 peut agir séparément. |
| 1, 1, 1, 6 | Action avec (1,1) = échec critique. Le troisième 1 ne peut agir seul (plancher) : il se combine au 6 (total 7) ou reste de côté. |

> ⚠️ Le double 1 annule toute réussite de cette action-là — les autres dés ne compensent pas.

---

## Dés d'Action — Détail

**Pool de départ : 2 DA libres.** Chacun peut servir à attaquer, à parer ou à se déplacer : un personnage qui n'a pas besoin de bouger met ses deux dés ailleurs. L'équipement, les dons et l'archétype en ajoutent, mais les dés d'équipement sont **spécialisés** (une épée donne 1 DA **attaque uniquement**, un bouclier 1 dé de garde, une tenue légère 1 dé de mouvement).

::: dev
**En test — blessure grave :** une issue possible de la mise hors de combat (un membre perdu, un œil crevé) : 1 dé de moins dans le pool touché. Voir [Points de vie et soins](resolution-et-combat.md#points-de-vie-et-soins).
:::

Le joueur lance tous ses DA simultanément et les assigne librement. En combat, les dés de garde sont posés avant les actions — voir [Le round](resolution-et-combat.md#le-round).

**Exemple — Escalade sous pression, 3 DA (2 de base + 1 de don) — résultats : 7, 5, 2 :**
- Option A : grimper avec (7+5 = 12, Difficile réussi), le 2 reste de côté
- Option B : grimper avec (5+2 = 7, Moyen réussi) et garder le 7 pour une autre action
- Le 2 seul ne peut rien tenter (plancher d'action)

---

## Dés de Compétence — Détail

**Pool de départ :** 1 DC de base, +1 DC quand le jet relève d'une [compétence majeure](competences.md).

Utilisé hors combat pour toute action de connaissance, sociale ou artisanale. Le pool est séparé des DA — les deux ne se mélangent pas. Comme pour les autres pools, les dés assignés à une même action **s'additionnent**.

**Exemple — Enquêteur avec 2 DC et une compétence mineure de rang 2 (*Je fouille les bureaux en désordre*) :**
Résultats 7 et 3.
- Une seule action : 7 + 3 + 2 = **12** → Difficile réussi
- Ou deux actions : fouiller le bureau (7 + 2 = 9) et repérer une sortie (3) ; le +2 ne va qu'à l'action que décrit la compétence

**Exemple — Juriste avec 1 DC, compétence majeure *Droit impérial* :**
Il cherche une faille dans un contrat de guilde (seuil 10). *Droit impérial* lui donne un 2e dé : 7 et 3 → **10**, réussite.
S'il avait plutôt utilisé sa compétence mineure *Je débusque les clauses piégées des contrats de guilde* (rang 2), il n'aurait lancé que son dé de base : 7 + 2 = 9, échec. Une seule compétence par jet.

---

## Dés de Pouvoir — Détail

**Pool de départ :** 1 DP permanent (minimum pour tous).

Les dés **éphémères** viennent d'une tradition, d'un [focus](magie.md#les-focus) ou de l'XP. Ils ne se lancent pas avec le pool : ils forment une **réserve**, la fatigue du mage, où il puise pour renforcer un sort ([Magie](magie.md#la-réserve--les-dés-éphémères)).

### Dés permanents vs Éphémères

| Type | Comportement |
|---|---|
| **Permanents** | Toujours disponibles, ne se consomment jamais |
| **Éphémères** | **Puisés** à la demande, après avoir vu ses dés de base — épuisés jusqu'à une nuit de repos complet |

> Les dés éphémères sont le carburant des sorts puissants : un mage peut frapper fort, mais pas à chaque tour.

**Exemple — Mage avec 1 DP permanent et 2 éphémères en réserve :**
- Lance *Prison de Glace* (15+) avec son DP permanent → 8. Trop peu
- Il puise ses deux éphémères → 8 et 5
- **Double 8** → 8 × 3 = 24 pour réussir. Seuil Très difficile (15+) dépassé → la prison tient
- Sa réserve est vide jusqu'à la nuit : le reste de la journée, il lance avec son seul DP permanent

---

## Recharge des Pools

Les pools se rechargent **entre chaque scène**.

| Pool | Recharge |
|---|---|
| Dés d'Action (DA) | ✅ Complet entre les scènes |
| Dés de Compétence (DC) | ✅ Complet entre les scènes |
| Dés de Pouvoir permanents | ✅ Complet entre les scènes |
| Dés éphémères (réserve) | Après une nuit de repos complet |
| Dé **épuisé** (quel que soit le pool) | Après une nuit de repos complet |

> Une scène correspond à une unité narrative distincte (lieu, temps ou enjeu différent). Le MJ tranche en cas de doute.

---

## Payer un Dé

Certaines capacités **coûtent un dé** (« payer 1 DC », « payer 1 DA »). Elles se déclarent **à tout moment**, sans lancer : c'est le personnage qui tire sur la corde. Le joueur choisit comment il paie.

| Paiement | Effet |
|---|---|
| **Comptant** | un dé du pool est **épuisé** jusqu'à une nuit de repos complet |
| **À crédit** | au **prochain jet** de ce pool, un des dés est posé sur **1** d'office, avant de lancer les autres |

- Le 1 posé à crédit ne sert à rien, sauf à **former un double 1** avec un 1 naturel : plus le pool est gros, plus le risque monte (environ 10 % avec 1 autre dé, 19 % avec 2, 27 % avec 3).
- Un pool ne descend jamais sous 1 dé : **le dernier dé ne se paie qu'à crédit**.
- On peut payer plusieurs fois, mais pas deux fois à crédit sur le même jet : la seconde dette se paie comptant.

**Exemple — le Regrattier, 1 DC :** dans une taverne du Dédale, il déclare *« Je connais quelqu'un ici »*. Son pool ne compte qu'un dé : il paie à crédit. Au prochain jet de DC, il pose un 1 et lance son dé normalement (et le dé de sa compétence majeure s'il en a une) : si un autre 1 tombe, c'est un double 1.

::: dev
**En test.** Comptant = coût lourd et sûr ; à crédit = coût léger et risqué, qui grandit avec le pool. Le verbe « payer » est réservé à ces coûts : « dépenser » reste celui des dés de garde engagés.
:::

---

## Ordre de Résolution

Les bonus ne s'appliquent qu'**après** la lecture des doubles, qui se fait **sur les faces naturelles**. Un bonus ne crée jamais de double et n'en casse jamais un.

**Exemple — 4/4 assignés à une attaque, épée +1 par dé :**
4+4 = 8, bonus de double +4 → 12, puis +1 par dé → **14** (et non 5+5+5 = 15).

---

## Résumé du Tour

```
1. Choisir le pool (Action / Compétence / Pouvoir)
   + 1 dé si une compétence majeure s'applique
2. Lancer TOUS les dés du pool simultanément
3. Double 1 → obligation d'action échouée en premier
4. Assigner les dés aux actions (attaque / défense / sort / mouvement)
   — total minimum 3 par action
5. Relances (compétence de rang 3, objet…) sur les dés de l'action concernée
   — jamais sur un 1
6. Lire les doubles sur les faces naturelles (bonus = valeur du double,
   pour réussir seulement : les dégâts restent sur la somme brute)
7. Ajouter les bonus par dé, puis les bonus au total
   (une seule compétence par jet)
8. Résoudre contre seuil ou opposition
9. Narrer
```

---

[← Retour à l'accueil](../index.html) · [Création de personnage](creation-de-personnage.md) · [Compétences](competences.md) · [Échelle de puissance](echelle-de-puissance.md)
