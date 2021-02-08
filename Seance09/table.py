#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Table pour faire tourner l'algorithme de Dijkstra.
"""
import pandas as pd
from typing import Any, Dict, List, Optional
from graphe_p import GrapheP, Sommet, Poids
from collections import deque


class Table:
    """Structure pour Dijkstra.

            Exemples:
    >>> mon_graphe = GrapheP(voisinage={'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}})
    >>> mon_graphe
    GrapheP(voisinage={'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}})
    >>> ma_table = Table(graphe=mon_graphe, depart='A')
    >>> ma_table
    Table(graphe=GrapheP(voisinage={'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}}), depart='A')
    >>> print(ma_table)
       NaN
    A  0.0
    B  inf
    C  inf
    >>> ma_table.lance_dijkstra()
    >>> print(ma_table)
       NaN    A    B    C
    A  0.0  0.0  0.0  0.0
    B  inf  1.0  1.0  1.0
    C  inf  4.0  3.0  3.0
    """

    def __init__(self, graphe: GrapheP, depart: Sommet):
        """Initialise à partir du graphe et du sommet."""
        self._depart = depart
        self._visites: List[Optional[Sommet]] = [None]
        self._graphe = graphe
        self._colonnes: List[Dict[Sommet, Poids]] = list()
        premiere = {sommet: float("inf") for sommet in graphe.sommets}
        premiere[depart] = 0
        self._colonnes.append(premiere)
        self._complete = False

    def __repr__(self) -> str:
        """Pour déboggage."""
        return f"Table(graphe={self._graphe!r}, depart={self._depart!r})"

    def __eq__(self, autre: Any) -> bool:
        """Egalite par les attributs."""
        if type(self) != type(autre):
            return False
        return (
            self._graphe == autre._graphe
            and self._visites == autre._visites
            and self._colonnes == autre._colonnes
        )

    def __str__(self) -> str:
        """Affiche la table."""
        df = pd.DataFrame(data=self._colonnes, index=self._visites)
        return str(df.T)

    def _trouve_prochain(self) -> Sommet:
        """Trouve le sommet non visite de plus petit poids."""
        resultat: Optional[Sommet] = None
        poids_min: Poids = float("inf")
        for sommet, poids in self._colonnes[-1].items():
            if poids < poids_min and sommet not in self._visites:
                resultat = sommet
                poids_min = poids

        if resultat is None:
            raise ValueError("Tous les sommets on été parcourus.")
        else:
            return resultat

    def _genere_nouvelle_colonne(self, sommet_courant: Sommet):
        """Rajoute une nouvelle colonne à partir du sommet."""
        nouvelle_colonne: Dict[Sommet, Poids] = dict()
        self._visites.append(sommet_courant)
        for voisin, poids in self._graphe[sommet_courant].items():
            nouvelle_colonne[voisin] = min(
                self._colonnes[-1][voisin],
                self._colonnes[-1][sommet_courant] + poids,
            )
        for sommet in self._graphe.sommets:
            if sommet not in nouvelle_colonne:
                nouvelle_colonne[sommet] = self._colonnes[-1][sommet]
        self._colonnes.append(nouvelle_colonne)

    def lance_dijkstra(self):
        """Fait tourner l'algorithme de Dijkstra."""
        while True:
            try:
                prochain = self._trouve_prochain()
            except ValueError:
                break
            self._genere_nouvelle_colonne(sommet_courant=prochain)
        self._complete = True

    def calcule_chemin(self, arrivee: Sommet):
        """Calcule le chemin minimale."""
        if not self._complete:
            self.lance_dijkstra()
        chemin = deque()
        courant = arrivee
        while courant != self._depart:
            chemin.appendleft(courant)
            for indice, colonne in enumerate(self._colonnes):
                if colonne[courant] == self._colonnes[-1][courant]:
                    break
            courant = self._visites[indice]
        chemin.appendleft(self._depart)
        return chemin
        
        