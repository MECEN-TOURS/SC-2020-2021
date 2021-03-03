# Sujet 10

Une nourriture est fabriquée en raffinant des huiles brutes et en les mélangeant.
Ces huiles brutes sont de plusieurs types:

- Végétales: `VEG1` et `VEG2`
- Non végétales: `HUI1`, `HUI2` et `HUI3`

Chacune de ces huiles peut être obtenue pour une livraison immédiate (Janvier) ou acheter sur un marché à terme pour une livraison lors des mois suivant.
Les tarifs futurs sont fourni dans la table

| Mois    | VEG1 | VEG2 | HUI1 | HUI2 | HUI3 |
| ----    | ---- | ---- | ---- | ---- | ---- |
| Janvier | 110  | 120  | 130  | 110  | 115  |
| Février | 130  | 130  | 110  | 90   | 115  |
| Mars    | 110  | 140  | 130  | 100  | 95   |
| Avril   | 120  | 110  | 120  | 120  | 125  |
| Mai     | 100  | 120  | 150  | 110  | 105  |
| Juin    | 90   | 100  | 140  | 80   | 135  |


Le produit final se vent à 150 euros la tonne.

Les huiles végétales et non végétales utilisent des lignes de production distinctes.
Il n'est pas possible de rafiner plus de 200 tonnes d'huiles végétales par mois et 250 tonnes pour les huiles non végétales.
Il n'y a pas de deperdition de poids durant le rafinnement et le prix de celui-ci peut être négligé.

On peut stocker jusqu'à 1000 tonnes de chaque type d'huile.
Le cout de stockage est de 5 euros par tonne par mois.
Le produit final et les huiles rafinnées ne peuvent être stockées.

La dureté des huiles se mélange linéairement avec
- `VEG1` : 8.8
- `VEG2` : 6.1
- `HUI1` : 2.0
- `HUI2` : 4.2
- `HUI3` : 5.0

et le résultat final doit avoir une dureté entre 3 et 6.

Comment peut-on optimiser le bénéfice?
