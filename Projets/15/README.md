# Sujet 15

Une companie veut déménager ses département de Paris.
Les départements sont notés A, B, C, D et E.

Les bénéfices des déménagement vers deux localisations sont les suivants
- A: Lyon 10, Bordeaux 10
- B: Lyon 15, Bordeaux 20
- C: Lyon 10, Bordeaux 15
- D: Lyon 20, Bordeaux 15
- E: Lyon 5, Bordeaux 15

Les couts de communications entre département suite au déménagement sont de la forme C * D où C est la quantité de communication et D le cout unitaire entre les villes.

On a la table de quantités de communication

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | _ |0.0|1.0|1.5|0.0|
| B | _ | _ |1.4|1.2|0.0|
| C | _ | _ | _ |0.0|2.0|
| D | _ | _ | _ | _ |0.7|

et les couts entre ville

|        |Lyon|Bordeaux|Paris|
|--------|----|--------|-----|
|Lyon    | 5  | 14     | 13  |
|Bordeaux| _  | 5      | 9   |
|Paris   | _  | _      | 10  |

Quelle est la meilleure répartition des différents départements?
