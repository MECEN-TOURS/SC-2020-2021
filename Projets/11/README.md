# Sujet 11

Une usine fabrique sept produits (`PROD1` à `PROD7`) sur les machines suivantes:
- 4 broyeuses
- 2 perceuses verticales
- 3 perceuses horizontales
- 1 foreuse
- 1 raboteuse

Chaque produit a une certaine contribution au profit (défini par euros par unité de produit moins le cout des matériaux bruts)
Ces quantités ainsi que le temps nécessaire par machine sont dans la table suivante

|                     | PROD1 | PROD2 | PROD3 | PROD4 | PROD5 | PROD6 | PROD7 |
| ------------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Contribution profit |    10 |     6 |     8 |     4 |    11 |     9 |     3 |
| broyage             |   0.5 |   0.7 |     _ |     _ |   0.3 |   0.2 |   0.5 |
| Percée verticale    |   0.1 |   0.2 |     _ |   0.3 |     _ |   0.6 |     _ |
| Percée horizontale  |   0.2 |     _ |   0.8 |     _ |     _ |     _ |   0.6 |
| Forage              |  0.05 |  0.03 |     _ |  0.07 |   0.1 |     _ |  0.08 |
| Rabotage            |     _ |     _ |  0.01 |     _ |  0.05 |     _ |  0.05 |


Lors des prochains mois les machines suivantes seront à l'arrêt pour maintenance

- Janvier : 1 broyeuse
- Février : 2 perceuses horizontales
- Mars : 1 Foreuse
- Avril : 1 broyeuse et 1 perceuse verticale
- Mai : 1 raboteuse et 1 perceuse horizontale

On limite la production pour les différents produits et mois pour des raisons marketing:

- Janvier  500 1000 300 300 800 200 100
- Février 600 500 200 0 400 300 150
- Mars 300 600 0 0 500 400 100
- Avril 200 300 400 500 200 0 100
- Mai 0 100 500 100 1000 300 0
- Juin 500 500 100 300 110 500 60

On peut stocker jusqu'à 100 unités de chaque produit par mois à un cout de 0.5 euros par unité.
On commence l'année avec un stock vide, mais on veut un stock de 50 unités par produit fin juin.
L'usine travaile 6 jours par semaine avec 2 tranches de 8h.
Comment doit-on optimiser la production?
