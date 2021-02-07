#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Table pour faire tourner l'algorithme de Dijkstra.
"""
from typing import Any, Dict, List, Optional, Set
from graphe_p import GrapheP, Sommet, Poids


class Table:
    """Structure pour Dijkstra.

        Exemples:
    >>> mon_graphe = GrapheP(voisinage={'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}})
    >>> mon_graphe
    GrapheP(voisinage={'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}})
    >>> ma_table = Table(graphe=mon_graphe, depart="A")
    >>> ma_table
    Table(graphe=GrapheP(voisinage={'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}}), depart='A')
    >>> print(ma_table)
    [{'A': 0, 'B': inf, 'C': inf}]
    >>> from rich import print
    >>> print(ma_table)
    [{'A': 0, 'B': inf, 'C': inf}]
    >>> ma_table.lance_dijkstra()
    >>> print(ma_table)
    [
        {'A': 0, 'B': inf, 'C': inf},
        {'B': 1, 'C': 4, 'A': 0},
        {'C': 3, 'A': 0, 'B': 1},
        {'A': 0, 'B': 1, 'C': 3}
    ]
    """

    def __init__(self, graphe: GrapheP, depart: Sommet):
        """Initialise à partir du graphe et du sommet."""
        self.depart = depart
        self.visites: Set[Sommet] = set()
        self.graphe = graphe
        self.colonnes: List[Dict[Sommet, Poids]] = list()
        premiere = {sommet: float("inf") for sommet in graphe.sommets}
        premiere[depart] = 0
        self.colonnes.append(premiere)

    def __repr__(self) -> str:
        """Pour déboggage."""
        return f"Table(graphe={self.graphe!r}, depart={self.depart!r})"

    def __eq__(self, autre: Any) -> bool:
        """Egalite par les attributs."""
        if type(self) != type(autre):
            return False
        return (
            self.graphe == autre.graphe
            and self.visites == autre.visites
            and self.colonnes == autre.colonnes
        )

    def __str__(self) -> str:
        """Affiche la table."""
        return str(self.colonnes)

    def trouve_prochain(self) -> Sommet:
        """Trouve le sommet non visite de plus petit poids."""
        resultat: Optional[Sommet] = None
        poids_min: Poids = float("inf")
        for sommet, poids in self.colonnes[-1].items():
            if poids < poids_min and sommet not in self.visites:
                resultat = sommet
                poids_min = poids

        if resultat is None:
            raise ValueError("Tous les sommets on été parcourus.")
        else:
            return resultat

    def genere_nouvelle_colonne(self, sommet_courant: Sommet):
        """Rajoute une nouvelle colonne à partir du sommet."""
        nouvelle_colonne: Dict[Sommet, Poids] = dict()
        self.visites.add(sommet_courant)
        for voisin, poids in self.graphe[sommet_courant].items():
            nouvelle_colonne[voisin] = min(
                self.colonnes[-1][voisin],
                self.colonnes[-1][sommet_courant] + poids,
            )
        for sommet in self.graphe.sommets:
            if sommet not in nouvelle_colonne:
                nouvelle_colonne[sommet] = self.colonnes[-1][sommet]
        self.colonnes.append(nouvelle_colonne)

    def lance(self):
        """Fait tourner l'algorithme de Dijkstra."""
        while True:
            try:
                prochain = self.trouve_prochain()
            except ValueError:
                break
            self.genere_nouvelle_colonne(sommet_courant=prochain)
