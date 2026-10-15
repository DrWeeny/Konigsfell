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
- Les **dégâts** se calculent sur la somme brute (7,7 → 14). Même règle en défense.
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

**Pool de départ : 2 dés** — 1 DA de base + 1 dé de Mouvement. L'équipement, les dons et l'archétype en ajoutent (une épée donne 1 DA **attaque uniquement**).

::: dev
**En test — blessure grave :** un personnage gravement blessé perd 1 dé de son pool. Voir `CLAUDE.md`.
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

**Exemple — Enquêteur avec 2 DC et un bonus de métier +2 :**
Résultats 7 et 3.
- Une seule action : 7 + 3 + 2 = **12** → Difficile réussi
- Ou deux actions : (7 + 2 = 9) et (3), par exemple fouiller une pièce et repérer une sortie
**Exemple — Juriste avec 1 DC, compétence majeure *Droit impérial* :**
Il cherche une faille dans un contrat de guilde (seuil 10). *Droit impérial* lui donne un 2e dé : 7 et 3 → **10**, réussite.
S'il avait plutôt utilisé sa compétence mineure *Je débusque les clauses piégées des contrats de guilde* (rang 2), il n'aurait lancé que son dé de base : 7 + 2 = 9, échec. Une seule compétence par jet.

---

## Dés de Pouvoir — Détail

**Pool de départ :** 1 DP permanent (minimum pour tous).

Des dés **éphémères** peuvent être achetés avec de l'XP. Ils se distinguent à la table par une couleur différente.

### Dés permanents vs Éphémères

| Type | Comportement |
|---|---|
| **Permanents** | Toujours disponibles, ne se consomment jamais |
| **Éphémères** | **Consommés** dès qu'ils sont engagés dans une action — ils ne reviennent qu'à la scène suivante |

> Les dés éphémères sont le carburant des sorts puissants : un mage peut frapper fort, mais pas à chaque tour.

::: dev
**En test — épuisement.** Si un personnage engage **tous** ses dés éphémères dans une même scène, l'un d'eux reste épuisé jusqu'à une nuit de repos complet. Objectif : limiter les scènes « tout ou rien » sans compter les sorts. Voir `CLAUDE.md`.
:::

**Exemple — Mage avec 3 DP (1 permanent + 2 éphémères) :**
- Lance *Prison de Glace* avec les 3 DP → résultats : 8, 8, 5
- **Double 8** → 8 × 3 = 24 pour réussir. Seuil Très difficile (15+) dépassé → la prison tient
- Les 2 dés éphémères sont consommés pour la scène ; il ne lui reste que son DP permanent

---

## Recharge des Pools

Les pools se rechargent **entre chaque scène**.

| Pool | Recharge |
|---|---|
| Dés d'Action (DA) | ✅ Complet entre les scènes |
| Dés de Compétence (DC) | ✅ Complet entre les scènes |
| Dés de Pouvoir permanents | ✅ Complet entre les scènes |
| Dés éphémères | Entre les scènes — sauf dé épuisé (nuit de repos) |

> Une scène correspond à une unité narrative distincte (lieu, temps ou enjeu différent). Le MJ tranche en cas de doute.

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
5. Relances (compétence de rang 3, objet…) sur les dés de l'action concernée
   — jamais sur un 1
6. Lire les doubles sur les faces naturelles (bonus = valeur du double)
7. Ajouter les bonus par dé, puis les bonus au total
   (une seule compétence par jet)
8. Résoudre contre seuil ou opposition
9. Narrer
```

---

[← Retour à l'accueil](../index.html) · [Création de personnage](creation-de-personnage.md) · [Compétences](competences.md) · [Échelle de puissance](echelle-de-puissance.md)
