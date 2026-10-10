# Königsfell — Passation : refonte du système de combat

*Synthèse d'une session de conception (octobre 2026). À lire avec `resolution-et-combat.md`, qui contient la version rédigée des règles décidées.*

**Objectif de la refonte :** faire tourner le système en **théâtre de l'esprit**, sans grille ni distances, en gardant l'identité du jeu : *on lance d'abord, on décide ensuite*.

**Principe directeur pour toute règle ajoutée :** elle doit nourrir la décision d'assignation des dés, jamais la contourner. Un effet qui ne crée aucun choix (« +1 partout ») est suspect.

---

## 1. Décisions prises

### Base

- **Plancher d'action : total minimum de 3.** Un 1 ou un 2 isolé ne peut rien tenter ; il doit être combiné, mis en garde ou abandonné. S'applique partout (combat, compétence, pouvoir, mouvement). La partie opposée n'a qu'à dépasser un 3.
- **Seuils inchangés** : 3 / 5 / 10 / 15 / 25. Les paliers 15+ et 25+ sont volontairement hors de portée au niveau 1 — magie, niveaux, objets, doublons.
- **Pool de départ : 1 DA de base + 1 dé de mouvement**, plus les dés d'équipement. Une épée donne **1 DA spécialisé attaque** (ne peut pas aller en garde). Un bouclier en serait le miroir : 1 dé garde uniquement.
- **Dés éphémères** : se régénèrent par **nuit de repos**, pas entre les scènes. Les autres pools se rechargent entre les scènes.

### Doubles

- Deux dés identiques combinés = **V × 3**, mais **uniquement pour réussir**. Les dégâts se calculent sur la **somme brute**. Même règle en défense.
- **Critique = double 10 uniquement.** Effet narratif fixe, ignore l'armure — pas un gros nombre.
- **Pas de triple.** Trois dés identiques : on en choisit deux pour la paire, le troisième reste normal.
- Double 1 = échec critique, résolu en premier.
- Les doubles se lisent sur les **faces naturelles** (après relance/verrouillage, avant tout +N).

### Le round

1. **Initiative** : 1d10 chacun.
2. **Gardes** posées dans l'**ordre inverse** de l'initiative, jetées, **à découvert**, valeurs fixes pour le round.
3. **Actions** dans l'ordre d'initiative.
4. Résolution immédiate de chaque action.

Les dés cachés et les déclarations à l'aveugle ont été **écartés** : risque de triche à la table, et contraire au « lancer puis adapter ».

**Récompense d'initiative, en échelle :**
- initiative simple : **+1 sur chaque dé** (ne crée ni ne détruit de doublon) ;
- formation/équipement : 1 dé générique ;
- garde d'élite / légendaire : 1 relance.

### Attaque, défense, dégâts

- Défense ≥ attaque (totaux avec bonus de doublon) → paré. **Égalité au défenseur.**
- Sinon : **dégâts = somme brute attaque − somme brute défense engagée − armure.** Le défenseur peut engager partiellement (« bankrupt ») pour réduire.
- **Les dés de garde engagés sont dépensés**, parés ou non. La garde s'use de ce qu'elle dépense, pas du nombre de coups reçus. Le défenseur peut choisir d'encaisser pour garder ses dés.
- But : le focus et le nombre percent une garde ; cinq paysans à 3 épuisent un boss sans qu'il soit invulnérable *ni* fragile.

### Armure, PV, soins

- Armure : cuir/gambison −1, mailles −2, plaque −4 (sociale, cérémonielle). Sans effet sur critique et poison.
- **PV ≈ 20–22**, **pas de progression** avec les niveaux — la puissance passe par les dés, une lame reste mortelle.
- Soins : **1d6 par journée de repos complet**, plantes ponctuelles. Soins magiques = nécromancie, rares et compromettants (le prêtre véreux = ressource politique).
- **Hors de combat ≠ mort** : celui qui porte le coup décisif choisit l'issue ; capturer est souvent plus utile.

### Mouvement et fuite

- Pas de distances : au contact ou à distance. Le dé de mouvement ne sort que pour une action contestée.
- **Désengagement (tour 0)** :
  - initiative, adversaire n'a rien engagé → libre ;
  - une attaque est passée → la battre ;
  - attaques toutes parées ou aucune → 3+ ;
  - **sous la moitié des PV → jamais libre.**
- Échec : dés perdus, reste au contact, **pas d'attaque gratuite** (sauf magie/objet).
- Réussite : +1 à l'initiative suivante pour les métiers de type roublard.
- **Course (round suivant)** : les deux camps convertissent ce qu'ils veulent en mouvement (dés de garde dépensés possibles), résolution à l'initiative.

### Grammaire des dés (objets, sorts, malédictions)

Six verbes : **ajustement, relance, transfert, dé supplémentaire, multiplicateur, verrouillage**. Ordre d'application fixé (voir `resolution-et-combat.md`). Malédictions = miroirs des verbes. **Réaction hors tour** = verbe le plus fort, reliques uniquement, limite par scène. Charges d'objets par scène ; hausses permanentes de pool réservées à l'XP.

### Progression en co-écriture

Planque (+ fonctions), PNJ loyal (ne trahit jamais, peut mourir), secret sur un PNJ, passé partagé avec une institution, rumeur qui devient vraie, objet à histoire. **Le joueur décrit, le MJ chiffre** ; veto brumeux ; cinq ou six types maximum.

---

## 2. Problèmes d'équilibrage ouverts

Classés par urgence.

1. **Défense des lanceurs de sorts.** Le DP ne pare pas. Un mage niveau 1 a autant de dés qu'un bretteur mais une garde plus pauvre. Trancher : sorts défensifs qui dépensent du DP, ou mage fragile assumé à distance.

2. **Le niveau 1 est étriqué.** Avec ~3 dés, il n'existe que trois configurations, aucune confortable. Constat du playtest : garde à 2 dés = presque intouchable mais inoffensif. Soit monter le pool de départ, soit assumer que le jeu respire à partir du niveau 2–3.

3. **Le +1 d'initiative grandit avec le pool.** +1 par dé vaut +3 à 3 dés, +7 à 7 dés. Ce qui est « juste » au niveau 1 devient fort plus tard. Envisager un plafond (+1 sur N dés max) ou basculer vers l'échelle à mesure que les pools montent.

4. **Inflation des doublons avec la taille des pools.** ~70 % de chances d'avoir une paire à 5 dés ; une paire de 8 vaut 24. Le critique (double 10, ~8 % à 5 dés, ~15 % à 7) est sain, mais les paires ordinaires saturent les seuils. Piste : plafonner le nombre de dés assignables à une même action (ex. 3).

5. **Duels qui s'enlisent.** Deux pools comparables donnent des marges proches de zéro. Piste : plafonner la garde à la moitié du pool, ce qui ne change rien à la mêlée à plusieurs.

6. **Boss contre 5–7 joueurs.** Six pools contre une garde unique = perdu d'avance ; l'armure ne peut pas le compenser. Leviers retenus : escorte systématique, **limite d'engagement à 3** au contact d'une cible, garde renouvelable en cours de round pour les boss d'exception. À tester.

7. **Calibrage dégâts / PV.** 20–22 PV est provisoire, dépendant des dégâts moyens réels après soustraction (estimés 5–10 par coup qui passe). À valider en playtest, en tenant compte de soins très lents.

8. **Dés éphémères** : qu'est-ce qui les consomme exactement ? Le livret dit seulement ce qui ne les consomme pas.

9. **Égalité d'initiative** non tranchée.

10. **Compétences en combat** (feinte, intimidation) : les pools ne se mélangent jamais, mais les joueurs le tenteront. Prévoir le cas (transfert ? action de compétence qui modifie une garde ?).

---

## 3. Incohérences dans `regles/jets-de-des.md` à corriger

- Pool de départ (1 DA + 1 mvt) vs exemple du guerrier à 3 DA ; l'arme n'apparaît nulle part.
- Statut du dé de mouvement ambigu (dé séparé ou usage d'un DA ?).
- Exemple de compétence en « meilleur résultat retenu + 2 », contraire à « additionner et assigner » ; bonus d'archétype = +2 plat ici, +1 dé ailleurs.
- « Effets doublés » sur doublon : non défini, et contraire à la décision (bonus pour réussir seulement).
- Exemple du mage citant un seuil 20+ absent de la table.
- Tableau de recharge : « complet entre les scènes » pour tous les pools, alors que les éphémères se rechargent par nuit.
- Exemple 1,1,1,6 qui fait agir un 1 seul — interdit par le plancher à 3.
- Moment de pose des défenses non défini (réglé par la règle des gardes inversées).
- Double 10 : réussite automatique, mais rien sur les dégâts.

---

## 4. Structure et publication

- Dépôt **public par choix**, sur le modèle commercial : **Manuel joueur** (version light) et **Manuel du maître** (superset : joueur + détails MJ).
- Risque principal : **dérive entre les deux versions.** Recommandation : **une seule source, deux sorties.** Passages MJ balisés en blocs Pandoc, retirés par un filtre Lua ou un script Python à la génération :

  ```markdown
  ::: mj
  Détail réservé au maître.
  :::

  ::: dev
  Note de conception, retirée des deux manuels.
  :::
  ```

- Rendu MJ en **encarts** : même structure que le manuel joueur, le MJ voit d'un coup d'œil ce que les joueurs savent.
- Généraliser le schéma `vue-joueurs` / `vue-mj` déjà utilisé pour les PNJ : bestiaire, lieux.
- `resolution-et-combat.md` mélange actuellement contenu joueur et MJ — à baliser :
  - **MJ** : veto brumeux, limite de types de récompenses, section « Lisibilité à la table », garde renouvelable des boss, catalogue de malédictions, éventuellement la limite d'engagement ;
  - **dev** : « Points encore ouverts ».
- Impression : manuel joueur gratuit (web/PDF), seul le manuel du maître imprimé ; éventuellement la campagne en volume séparé.

---

## 5. Prochaines étapes suggérées

1. Mettre en place le balisage `::: mj` / `::: dev` et le script de génération des deux manuels.
2. Corriger `jets-de-des.md` (section 3) et y intégrer `resolution-et-combat.md`, balisé.
3. Trancher la défense des mages et le pool de départ (problèmes 1 et 2).
4. Playtester un 1v1 et un 3v1 boss pour calibrer dégâts, PV, duel et focus.
