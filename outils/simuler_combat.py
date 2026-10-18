"""Simulation Monte-Carlo du combat D10 (calibrage des rencontres).

Modélise le round de `regles/resolution-et-combat.md` : initiative (+1 par dé
au plus haut, rien en cas d'égalité), gardes posées à découvert, actions,
doubles V × 3 pour réussir, double 1 = échec, plancher 3, double 10 qui
ignore l'armure, dégâts = attaque brute − garde engagée − armure.

Choix des camps :
  - l'attaquant essaie toutes les façons de grouper ses dés et de les
    répartir sur les cibles, et garde la plus meurtrière ;
  - le défenseur pare avec le plus petit groupe de dés qui suffit, sinon
    engage toute sa garde pour réduire les dégâts ;
  - le nombre de dés gardés est fixe par combattant ; pour le PJ, on essaie
    toutes les valeurs et on affiche la meilleure.

Exemples :
  python outils/simuler_combat.py
  python outils/simuler_combat.py -n 5000 --pv 12
"""

import argparse
import itertools
import random


def partitions(lst):
    if not lst:
        yield []
        return
    first, rest = lst[0], lst[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p


PARTS = {n: list(partitions(list(range(n)))) for n in range(8)}


def lire(faces, bonus):
    """(réussite, brut, critique) d'une action, ou None si elle échoue."""
    brut = sum(faces) + bonus * len(faces)
    if faces.count(1) >= 2:
        return None
    paire = max((v for v in set(faces) if faces.count(v) >= 2), default=0)
    reussite = brut + paire  # V × 3 au lieu de 2V
    if reussite < 3:
        return None
    return reussite, brut, paire == 10


class Combattant:
    def __init__(self, nom, libres, arme=1, bouclier=0, armure=0, pv=8,
                 duel=0, garde=1, pj=False, fuit=False):
        self.nom, self.libres, self.arme, self.bouclier = nom, libres, arme, bouclier
        self.armure, self.pv, self.pv_max = armure, pv, pv
        self.duel, self.garde, self.pj, self.fuit = duel, garde, pj, fuit
        self.hors = False


def parade(garde, reussite):
    """Plus petit groupe de dés de garde qui pare, ou None."""
    meilleur = None
    for r in range(1, len(garde) + 1):
        for sub in itertools.combinations(range(len(garde)), r):
            faces = [garde[i][0] for i in sub]
            lu = lire(faces, garde[sub[0]][1])
            if lu and lu[0] >= reussite and (meilleur is None or lu[1] < meilleur[0]):
                meilleur = (lu[1], sub)
    return meilleur


def encaisser(attaque, cible, garde):
    reussite, brut, critique = attaque
    p = parade(garde, reussite)
    if p:
        for i in sorted(p[1], reverse=True):
            garde.pop(i)
        return 0
    armure = 0 if critique else cible.armure
    if brut - armure <= 0:
        return 0
    engage = sum(f + b for f, b in garde)
    garde.clear()
    return max(0, brut - engage - armure)


def planifier(att, faces, bonus, cibles, gardes):
    meilleur = (-1, None)
    for p in PARTS[len(faces)]:
        blocs = [lu for lu in (lire([faces[i] for i in b], bonus) for b in p) if lu]
        if not blocs:
            continue
        for repartition in itertools.product(range(len(cibles)), repeat=len(blocs)):
            for sens in (1, -1):
                g = [list(gardes[id(c)]) for c in cibles]
                pv = [c.pv for c in cibles]
                score = 0
                seq = sorted(zip(blocs, repartition), key=lambda x: -sens * x[0][0])
                for (r, b, cr), ti in seq:
                    if pv[ti] <= 0:
                        continue
                    duel = att.duel if len(cibles) == 1 else 0
                    d = min(encaisser((r + duel, b, cr), cibles[ti], g[ti]), pv[ti])
                    pv[ti] -= d
                    score += d + (20 if pv[ti] <= 0 else 0)
                if score > meilleur[0]:
                    meilleur = (score, seq)
    return meilleur[1]


def combat(pj, ennemis, rounds_max=10):
    """(victoire : True / False / None si enlisé, rounds, PV restants, KO d'un coup)."""
    un_coup = False
    for n in range(1, rounds_max + 1):
        vivants = [c for c in [pj] + ennemis if not c.hors]
        init = {id(c): random.randint(1, 10) for c in vivants}
        haut = max(init.values())
        premiers = [c for c in vivants if init[id(c)] == haut]
        bonus = {id(c): int(len(premiers) == 1 and c is premiers[0]) for c in vivants}
        gardes = {}
        for c in vivants:
            g = min(c.garde, c.libres)
            gardes[id(c)] = [(random.randint(1, 10), bonus[id(c)]) for _ in range(g + c.bouclier)]
            c.actions = c.libres - g + c.arme
        for c in sorted(vivants, key=lambda c: -init[id(c)]):
            if c.hors:
                continue
            cibles = [e for e in (ennemis if c.pj else [pj]) if not e.hors]
            if not cibles:
                break
            faces = [random.randint(1, 10) for _ in range(c.actions)]
            plan = planifier(c, faces, bonus[id(c)], cibles, gardes) or []
            for (r, b, cr), ti in plan:
                t = cibles[ti]
                if t.hors:
                    continue
                duel = c.duel if len(cibles) == 1 else 0
                d = encaisser((r + duel, b, cr), t, gardes[id(t)])
                if t.pj and t.pv == t.pv_max and d >= t.pv_max:
                    un_coup = True
                t.pv -= d
                if t.pv <= 0:
                    t.hors = True
                    if not t.pj:  # moral : les sbires fuient à la première mort
                        for e in ennemis:
                            if e.fuit:
                                e.hors = True
            if pj.hors:
                return False, n, 0, un_coup
        if all(e.hors for e in ennemis):
            return True, n, pj.pv, un_coup
    return None, rounds_max, pj.pv, un_coup


PJ = {
    "Landsknecht, épée et bouclier, mailles": dict(libres=3, arme=1, bouclier=1, armure=2, pv=11),
    "Landsknecht, épée à deux mains, mailles": dict(libres=3, arme=1, armure=2, pv=11),
    "Regrattier, dague": dict(libres=2, arme=1, armure=0, pv=8),
    "Artisan, marteau, cuir": dict(libres=2, arme=1, armure=1, pv=8),
    "Mage sans arme ni sort": dict(libres=2, arme=0, armure=0, pv=8),
}


def mercenaire(garde):
    return Combattant("mercenaire", 1, 1, armure=1, pv=4, garde=garde, fuit=True)


RENCONTRES = {
    "1 mercenaire offensif": lambda: [mercenaire(0)],
    "2 mercenaires (offensif + prudent)": lambda: [mercenaire(0), mercenaire(1)],
    "Ugo, vétéran": lambda: [Combattant("Ugo", 3, 1, armure=1, pv=12, duel=1)],
    "Ugo + 2 mercenaires": lambda: [Combattant("Ugo", 3, 1, armure=1, pv=12, duel=1),
                                   mercenaire(0), mercenaire(0)],
}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("-n", type=int, default=2000, help="combats par cas")
    ap.add_argument("--pv", type=int, default=8, help="PV de départ (Endurci : +3)")
    ap.add_argument("--graine", type=int, default=1)
    args = ap.parse_args()
    random.seed(args.graine)
    for nom_r, rencontre in RENCONTRES.items():
        print(f"== {nom_r}")
        for nom_pj, profil in PJ.items():
            profil = dict(profil, pv=profil["pv"] - 8 + args.pv)
            res = {}
            for g in range(profil["libres"] + 1):
                defaites = 0
                rounds = []
                for _ in range(args.n):
                    pj = Combattant("PJ", pj=True, garde=g, **profil)
                    v, r, _, _ = combat(pj, rencontre())
                    defaites += v is False
                    rounds.append(r)
                res[g] = (defaites / args.n, sum(rounds) / args.n)
            g = min(res, key=lambda k: res[k][0])
            print(f"  {nom_pj:42s} {profil['pv']:2d} PV  tombe {res[g][0]:4.0%}"
                  f"  (garde {g}, {res[g][1]:.1f} round)")


if __name__ == "__main__":
    main()
