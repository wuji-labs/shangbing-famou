# 上兵伐谋 ShangBing FaMou — Winning Without War (Vaincre sans guerre)

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/shangbing-famou"><img src="https://www.skills.sh/b/wuji-labs/shangbing-famou" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 中文](README.zh-CN.md)** | **[🇺🇸 English](README.md)** | **[🇯🇵 日本語](README.ja.md)** | **[🇰🇷 한국어](README.ko.md)** | **[🇪🇸 Español](README.es.md)** | **[🇧🇷 Português](README.pt.md)** | **🇫🇷 Français**

> Ceci est l'un des dix présents que le courant de sagesse chinois offre à la communauté mondiale de l'open source (叩兩端·無極樞紐).
> Nous ne dressons aucun centrisme chinois et ne prétendons pas qu'une civilisation soit supérieure à une autre ; nous partons simplement du courant que nous connaissons le mieux,
> nous le façonnons en un outil utilisable, et nous le posons sur l'étagère à outils open source commune à l'humanité. Viendront ensuite,
> tour à tour, les présents des courants grec, de Nâlandâ, hébraïque et perse, formant ensemble une matrice de capacités open source en dialogue avec douze civilisations.

---

> **上兵伐谋，其次伐交，其次伐兵，其下攻城。** — La stratégie suprême est de déjouer les plans de l'ennemi ; vient ensuite briser ses alliances ; puis défaire ses forces en rase campagne ; le pire est d'assaillir des murailles fortifiées.
> — *Sunzi · « L'attaque par stratagème »* (孙子·谋攻), Sunzi Bingfa, *The Art of War*

**Votre IA joue chaque partie comme un combat à mort. Apprenez-lui à vaincre sans combat.**

La plupart des entraînements stratégiques d'IA recourent au même réflexe : surpasser, manœuvrer, faire pression. Gagner l'échange. Mais le plus ancien traité de stratégie jamais écrit dit que la plus haute victoire est celle où aucune bataille n'est livrée — là où l'on change la structure du jeu pour que le conflit se dissolve.

**上兵伐谋** (ShangBing FaMou) infuse la doctrine de **vaincre sans guerre** de *L'art de la guerre* dans le raisonnement stratégique de l'IA. Non comme agression, mais comme un cadre complet d'évaluation, de levier et de jeu collaboratif qui vise la **全胜 — victoire totale qui préserve tous les camps**.

## Le problème

```
Vous : « Aide-moi à obtenir ce que je veux de cette négociation. »
IA sans ShangBing : Voici comment les mettre sous pression, créer
                    l'urgence, exploiter leur point faible et les
                    acculer.
                    (Vous « gagnez » — et vous carbonisez la relation.)
IA avec ShangBing : D'abord, de quoi ont-ils vraiment besoin sous leur
                    position ? Peut-on restructurer cela pour qu'obtenir
                    ce que vous voulez les laisse eux aussi mieux lotis ?
                    Gagnez la partie en changeant la partie, non en
                    battant la personne.
```

## Ce qu'elle enseigne à l'IA

### Les quatre niveaux de la stratégie (谋攻四级, d'après *Sunzi · « L'attaque par stratagème »*)

Cherchez toujours du haut vers le bas — le niveau le plus haut est le moins coûteux :

| Niveau | Chinois | Ce que cela signifie | Correspondance en IA |
|--------|---------|----------------------|----------------------|
| Déjouer le plan | 伐谋 | Défaire l'*intention*, non l'armée | Restructurer le jeu pour que le conflit ne puisse naître |
| Briser les alliances | 伐交 | Dissoudre leur soutien | Réaligner le réseau ; gagner des collaborateurs |
| Défaire les forces | 伐兵 | Affrontement ouvert | Concurrence directe — le coût grimpe déjà |
| Assaillir les murailles | 攻城 | Prendre d'assaut le point le plus fort | Le dernier recours, le plus coûteux ; évitez-le |

### La doctrine du 全胜 — victoire totale (d'après *Sunzi · « L'attaque par stratagème »*)

> **百战百胜，非善之善者也；不战而屈人之兵，善之善者也。**
> Vaincre cent batailles n'est pas le sommet de l'art. Soumettre l'ennemi sans combattre — voilà le sommet de l'art.

| 全胜 Victoire totale | 破胜 Victoire brisée |
|----------------------|----------------------|
| Le but est atteint ET la relation, la confiance, la coopération future sont préservées | Vous « gagnez » mais brûlez le pont |
| Objectif par défaut de cette skill | De second ordre ; évité sauf nécessité |

### Connaître les deux camps avant d'agir (知己知彼, d'après *Sunzi · « L'attaque par stratagème »*)

> **知彼知己，百战不殆。** Connais l'autre et connais-toi toi-même, et jamais tu ne seras en péril.

La skill impose une évaluation bidirectionnelle — vos besoins et limites essentiels, les préoccupations *réelles* de l'autre camp sous sa position affichée, et l'environnement — **avant** de produire la moindre stratégie. Là où l'information manque, l'IA marque l'incertitude au lieu d'inventer l'esprit de l'autre.

### L'ancre éthique — 以道驭术 (partagée avec NoPUA)

| Manipulation (interdite) | Stratagème (enseigné) |
|--------------------------|------------------------|
| Changer sa *perception* en le trompant | Changer la *structure* pour que le conflit se dissolve |
| Peur, fausse urgence, gaslighting, exploitation de la faiblesse | Meilleure conception, évaluation plus fine, un gagnant-gagnant plus large |
| Ils se soumettent parce qu'ils ont peur | Ils acceptent parce que c'est vraiment meilleur pour eux aussi |

**La ligne rouge, en une phrase :** ShangBing vainc en remodelant le jeu pour que le conflit disparaisse — jamais en remodelant l'esprit d'une personne pour la duper.

## Avant / Après

| Déclencheur | IA sans ShangBing | IA avec ShangBing |
|-------------|-------------------|-------------------|
| « Aide-moi à gagner cette négociation » | Tactiques de pression, urgence artificielle, exploiter le point faible | Faire émerger leur préoccupation réelle → restructurer en gagnant-gagnant (全胜) |
| « Fais-les signer aujourd'hui » (rareté factice) | Écrit le script manipulateur | Refuse, nomme la ligne rouge, redirige vers une urgence légitime |
| « On ne peut pas battre le leader de front » | Guerre de fonctionnalités/prix/publicité sur les forces du leader | 避实击虚 — un coin acéré sur sa faiblesse négligée |
| « Donne-moi une stratégie pour l'emporter » (sans données) | Invente les motifs de l'autre, plan en un seul coup | Évaluation bidirectionnelle, marque les inconnues, demande avant de stratégiser |

Voir les cas travaillés entrée→sortie dans [examples/](examples/).

## Installation

### Plugin en un clic (Claude Code)

```bash
# ajoutez ce dépôt comme marketplace de plugins, puis installez
/plugin marketplace add wuji-labs/shangbing-famou
/plugin install shangbing-famou
```

Ensuite, déclenchement automatique (Claude apparie la `description` du SKILL.md) ou manuel avec `/shangbing-famou`.

### Clone direct (toute plateforme)

```bash
git clone https://github.com/wuji-labs/shangbing-famou
cp -r shangbing-famou ~/.claude/skills/
```

### Miroirs par plateforme

| Plateforme | Guide | Déclenchement manuel |
|------------|-------|----------------------|
| Claude Code | [platforms/claude-code.md](platforms/claude-code.md) | `/shangbing-famou` |
| Codex | [platforms/codex.md](platforms/codex.md) | auto via description |
| Cursor | [platforms/cursor.md](platforms/cursor.md) | basé sur des règles |

## Crédibilité

- **Citations véridiques, vérifiables** — chaque citation indique son chapitre dans le *Sunzi Bingfa* (p. ex. 谋攻/始计/虚实/军形/军争/用间/火攻). Liste des sources avec étiquettes de chapitre dans [reference/sunzi-bingfa.md](reference/sunzi-bingfa.md).
- **Benchmark reproductible, sans chiffres fabriqués** — 7 scénarios de stratégie/ligne rouge avec vérité de référence, conception baseline-contre-skill et une grille de notation dans [benchmark/](benchmark/). Les résultats sont **délibérément** laissés vides ; ils attendent une exécution réelle. Règle d'intégrité de la recherche : pas de valeurs p / scores inventés.
- **Ancre éthique partagée avec NoPUA** — 以道驭术 : refuse de générer manipulation/tromperie/coercition. La ligne rouge est appliquée, non décorative.

## Du même courant

- **NoPUA** — Skill anti-PUA qui meut l'IA par la confiance plutôt que par la peur. ShangBing partage son ancre éthique : 以道驭术 — manier la technique par la Voie.

## Informations de base

| Champ | Valeur |
|-------|--------|
| Rattachement | WUJI Labs |
| Répertoire | `labs/skills/shangbing-famou/` |
| Licence | MIT |
| Amont | github.com/wuji-labs/shangbing-famou |
| Version | v1.0.0 · 2026-06-02 |
| README en chinois | [README.zh-CN.md](README.zh-CN.md) |

---

*上兵伐谋 ShangBing FaMou — 乾元無極實驗室 · WUJI Labs*
*Soumettre sans combattre ; voilà le sommet de l'art.*
