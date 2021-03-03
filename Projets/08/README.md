# Sujet 08 : Réseau routier

On désire étudier la capacité du réseau routier reliant les villes **E** à **S**.

Le graphe ci-dessous représente le réseaux ainsi qu'une évaluation du nombres véhicule pouvant parcourir un tronçon par heure (par centaines).

![reseau](reseau.svg)

1. Quel est le débit horaire maximal de véhicules reliant **E** à **S**?
2. En fait chaque ville admet également un flux maximal de véhicule pouvant la traverser

| villes | a | b | c | d | e | f | g |
|--------|---|---|---|---|---|---|---|
| débits | 6 | 7 | 8 | 6 | 6 | 5 | 9 |

Proposer un modèle permettant de ramener ce problème à une question de flot comme pour la question 1., puis résoudre ce nouveau modèle.

3. En vue de créer une bretelle de contournement on demande d'analyser la variation du flux maximal traversant **d** dans la table précédente sur le flot total.
