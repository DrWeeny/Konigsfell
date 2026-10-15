# Jets de Dés

*Le système de Königsfell repose sur trois pools de dés distincts et une mécanique d'assignation tactique : on lance d'abord, on décide ensuite.*

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
Le joueur distribue librement ses dés entre les actions disponibles :
- Attaques
- Défenses (dés en réserve)
- Mouvements
- Sorts multiples
- Actions tactiques

**4. Résoudre contre les seuils ou l'opposition**

---

## Seuils de Difficulté

Le MJ fixe un seuil avant le jet selon la difficulté de l'action :

| Difficulté | Seuil |
|---|---|
| Automatique | Pas de jet |
| Facile | 3+ |
| Moyen | 5+ |
| Difficile | 10+ |
| Très difficile | 15+ |
| Quasi-impossible | 25+ |

Pour les jets opposés, le seuil est le résultat du défenseur.

---

## Combiner des Dés

Plusieurs dés peuvent être **combinés sur une même action** en additionnant leurs valeurs.

**Exemple :**
Attaque avec 2 dés — résultats 5 et 3 → total 8. Utile pour surpasser une défense ennemie élevée.

---

## La Règle des Doubles

Quand deux dés (ou plus) affichent **la même valeur**, des règles spéciales s'appliquent.

### Doubles positifs

| Double | Effet |
|---|---|
| Double 10 | Critique absolu — réussite automatique spectaculaire |
| Double quelconque (ex: 7, 7) | Valeur combinée (7+7 = 14) + bonus égal à la valeur (+7) → **total 21**, effets doublés |

### Double 1 — Échec Critique

Si le pool contient **deux ou plusieurs 1**, le joueur **doit** effectuer une action avec ces 1 en premier.

| Résultats | Obligation |
|---|---|
| 1, 1, 6 | Action principale avec (1,1) = échec critique. Peut utiliser 6 séparément. |
| 1, 1, 1, 6 | Action avec (1,1) = échec critique. Puis (1,6) ou deux actions séparées. |

> ⚠️ Le double 1 annule toute réussite de cette action-là — les autres dés ne compensent pas.

---

## Dés d'Action — Détail

**Pool de départ :** 1 DA de base + 1 dé de Mouvement.

Le joueur lance tous ses DA simultanément et les assigne librement :

**Exemple — Guerrier avec 3 DA (résultats : 7, 5, 2) :**
- Option A : Attaque avec (7), défense en réserve (5), mouvement (2)
- Option B : Attaque combinée (7+5 = 12), rien en réserve — risqué
- Option C : Attaque massive (7+5+2 = 14 combinés) — tout investir

---

## Dés de Compétence — Détail

**Pool de départ :** 1 DC de base, +1 DC quand le jet relève d'une [compétence majeure](competences.md).

Utilisé hors combat pour toute action de connaissance, sociale ou artisanale. Le pool est séparé des DA — les deux ne se mélangent pas. Comme pour les autres pools, les dés assignés à une même action **s'additionnent**.

**Exemple — Juriste avec 1 DC, compétence majeure *Droit impérial* :**
Il cherche une faille dans un contrat de guilde (seuil 10). *Droit impérial* lui donne un 2e dé : 7 et 3 → **10**, réussite.
S'il avait plutôt utilisé sa compétence mineure *Je débusque les clauses piégées des contrats de guilde* (rang 2), il n'aurait lancé que son dé de base : 7 + 2 = 9, échec. Une seule compétence par jet.

---

## Dés de Pouvoir — Détail

**Pool de départ :** 1 DP permanent (minimum pour tous).

Des dés **éphémères** peuvent être achetés avec de l'XP.

### Dés permanents vs Éphémères

| Type | Comportement |
|---|---|
| **Permanents** | Toujours disponibles, ne se consomment jamais |
| **Éphémères** | Ne se consomment PAS sur les sorts d'archétype ou sorts appris |

> Les dés éphémères représentent de la puissance supplémentaire disponible — ils ne disparaissent pas à l'usage normal.

**Exemple — Mage avec 3 DP (1 permanent + 2 éphémères) :**
- Lance *Bouclier Aqueux* (sort d'archétype) avec 2 DP → aucun dé consommé
- Lance *Prison de Glace* (sort appris) avec 3 DP → aucun dé consommé
- Résultats : 8, 8, 5 → **Double 8 !** → 8+8 = 16, bonus +8 = **total 24**. Seuil 20+ dépassé → effet spectaculaire

---

## Recharge des Pools

Les pools se rechargent **entre chaque scène**.

| Pool | Recharge |
|---|---|
| Dés d'Action (DA) | ✅ Complet entre les scènes |
| Dés de Compétence (DC) | ✅ Complet entre les scènes |
| Dés de Pouvoir (DP) | ✅ Complet entre les scènes |

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
