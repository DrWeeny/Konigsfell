# Journal de Conception ⚠️

*Les décisions de design du système D10, dans l'ordre chronologique : ce qui a été tranché, pourquoi, et ce qui reste ouvert. Les règles elles-mêmes sont dans `regles/`.*

---

## 2026-10-15 — Compétences, objets, piste pour la magie

### Point de départ

- Idée : les joueurs **inventent leurs propres compétences**, dans la même logique que les autres récompenses (planque, PNJ loyal…).
- Antécédent : le **Système Metal**, utilisé pour une campagne Warhammer 40k / Dark Heresy. Compétences-métiers de 1 à 5, aspects libres de 1 à 5, failles, motivations.
- Problèmes constatés dans Metal :
  - **Compétences trop larges.** « Expert martial » s'applique à chaque combat, c'est un bonus permanent.
  - **Doublons.** L'aspect répète la compétence : *Bretteur 4 + Fine lame 3 + Sur la défensive 4*, *Tireur 4 + As de la gâchette 4*. Trois bonus pour le même geste.
  - Les meilleurs aspects décrivaient une **situation** : *Les mensonges ont une odeur*, *Mettre quelqu'un en porte-à-faux*, *Le visage de l'innocence*, *Expert en trafic de livres*.

### Décisions → [Compétences](../regles/competences.md)

| Sujet | Décision | Pourquoi |
|---|---|---|
| Caractéristiques | **Supprimées** | Les pools séparent déjà corps, esprit et magie. Une carac s'appliquerait à tous les jets, comme « expert martial ». Et un PJ n'est plus empêché de formuler une idée à cause de sa valeur d'« intellect ». |
| Compétences majeures | Domaines larges, **tirés de la liste de l'archétype**, +1 dé | La largeur est rationnée par l'archétype, pas par le joueur. On retrouve l'ancien « +1 DC si compétence liée ». Négociable avec le MJ. |
| Compétences mineures | Libres, grammaire **geste + circonstance**, rangs +1 / +2 / +2 et relance, rang 3 maximum | La grammaire se vérifie à la table, empêche les doublons et pousse à jouer la scène. |
| Cumul | **Une seule compétence par jet** | Évite d'empiler les bonus. Une mineure dans un domaine majeur devient inutile, ce qui décourage les doublons. |
| Relance | **Après l'assignation**, sur un dé de l'action ; jamais un 1 | Plus lisible. Le fumble reste protégé. |
| Bonus et doubles | Les doubles se lisent sur les **faces naturelles**, les bonus viennent après | Un bonus ne crée ni ne casse un double. |
| Économie d'XP | Les mineures de rang 1 s'obtiennent **en jouant**, gratuitement. L'XP paie les rangs, les dés, les PV. | La survie et l'utilitaire ne se paient plus avec la même monnaie. *Féru d'histoire* ou *danseur émérite* ne rivalisent plus avec les PV. |
| « Au total » | Le bonus s'ajoute au **total d'une action** (un groupe de dés assignés), pas du jet entier | Épée +2 : 4/6/8/4 → mouvement 6, attaque 8 ou 4/4, et le +2 va sur l'une des deux. |

### Décisions → [Échelle de puissance](../regles/echelle-de-puissance.md)

- Une **unité commune** : 1 point = +1 en moyenne sur une action, avec 3 dés de référence. Cinq paliers, de Mineur à Relique.
- **Objets :** l'équipement de base reste simple et hors échelle (arme +1 dé, armure réduit les dommages, bouclier +1 dé de défense, tenue +1 dé de mouvement). La facture, de *bonne facture* à *légendaire*, se lit sur l'échelle.
- **Tous les types d'effets peuvent coexister** (au total, par dé, relance, effets magiques), du moment que c'est explicite. Les effets par dé grandissent avec le pool : c'est permis, mais le MJ le sait.
- **Objets avec bonus et malus :** on calcule le **solde**. Le déséquilibre est un choix assumé, pas un accident.

### Piste : la magie (rien n'est tranché)

**Le besoin :** une grammaire qui permette au MJ d'arbitrer le coût d'un pouvoir inventé par un joueur, sans écrire un manuel de sorts à la D&D.

**Références :**
- **Ars Magica** (à relire, le livre est quelque part). Chaque sort est un verbe et un domaine (Créer / Percevoir / Transformer / Détruire / Contrôler × Feu, Eau, Corps, Esprit, Image…). Le niveau se calcule selon la portée, la durée et la cible.
- **Hunter x Hunter (Nen) :** restrictions et serments. Plus la condition est contraignante, plus le pouvoir est fort. Limite : la série n'est pas cohérente sur l'échelle de puissance, et une grande partie vient de l'inné.
- **Game of Roles :** un deck de cartes dont les couleurs symbolisent un domaine (élémentaire, nécromancie, télékinésie, manipulation mentale) et montrent la puissance du sort.
- JdR du théâtre de l'esprit (*Fruits et Légumes*, Tales of Pi, OGaming TV) : le joueur propose, le MJ donne un modificateur au jugé. C'est souple, mais il n'y a aucun repère.

**Formule à tester** : elle donne un seuil, puisque les sorts en ont déjà (*Lien de serment* 10+).

```
Seuil = verbe (Percevoir 3 · Altérer 5 · Contrôler/Créer 10)
      + portée (contact 0 · vue +5)
      + durée (instant 0 · scène +5 · permanent +10)
      + cibles (une 0 · groupe +5)
      − restrictions (circonstance −5 · prix réel −10)
```

**Idées de lore et de mécanique :**
- **L'inné existe déjà** : tout le monde a 1 DP permanent. La magie est partout, comme le Nen.
- **Le guerrier redoutable est fort par la magie, sans que personne l'appelle magie.** Ses DP servent des aspects martiaux. Dans un monde où tout est régulé, la loi ne reconnaît que certaines formes (sorts déclarés, guildes, permis). Ça crée une zone grise pour l'Inquisition : qu'est-ce que la loi appelle magie, et qui en décide ?
- **Les restrictions façon Nen s'intègrent à la formule** : la précision achète la puissance, comme pour les compétences.
- **Il faudra un inventaire** pour donner la tonalité de Königsfell : une grille verbe × domaine avec 2 ou 3 exemples par case. Ranger une arme dans son ombre, faire de la lumière du bout du doigt, cracher des flammes… C'est l'esprit des classes de prestige de D&D 3.5 : la saveur avant la liste.
- Les interdits doctrinaux (Eau Calme : ni soin, ni contrôle mental) fonctionnent déjà comme des affinités.

### Piste : les failles (rien n'est tranché)

- Reprises de Metal (*Peur d'être un mutant*, *Paranoïa*) et à adapter au dark fantasy. Elles s'écrivent avec la même grammaire : *« je perds mes moyens devant un prêtre »*.
- Modèle à étudier : les **contraintes de Fate** (*compels*). Le MJ propose une complication liée à la faille. Le joueur accepte et gagne quelque chose (de l'XP ?), ou refuse et paie. Le joueur peut aussi la déclencher lui-même. Fate Condensé est gratuit et court.
- L'idée : le joueur écrit à la fois ce qui le rend fort et ce qui le rend vulnérable.

### Questions ouvertes

1. Nombre de compétences majeures à la création : 2 pour l'instant (1 si l'archétype a un bonus de pool). Faut-il plutôt 3 ou 4 ?
2. Nombre de compétences mineures à la création : 2 pour l'instant.
3. Coûts en XP des rangs (2 / 4) et d'une nouvelle majeure (4) : à tester.
4. Une majeure et une mineure peuvent-elles se cumuler sur un même jet ? Pour l'instant, non.
5. Listes de compétences majeures de Théurge, Landsknecht, Akkadien, Eau Calme et Ritualiste : ce sont des **propositions** à valider.
6. Valeur de l'armure (réduction des dommages) : à fixer avec les règles de combat.
7. **Initiative** (règle hors de ce repo) : le +1 par dé vaut plus qu'une compétence de rang 3. Passer à +2 au total, ou plafonner à 3 dés. Le cran légendaire (« 1 relance ») doit monter : deux relances ou un verrouillage.
8. Magie : relire Ars Magica, tester la formule, commencer l'inventaire.
9. Failles : déclenchement, contrepartie, nombre maximum.

---

[← Notes MJ](notes.md) · [Compétences](../regles/competences.md) · [Échelle de puissance](../regles/echelle-de-puissance.md)
