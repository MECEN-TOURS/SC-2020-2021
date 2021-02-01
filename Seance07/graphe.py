"""Description.

Librairie pour le parcours graphe.
"""
from collections import deque
from typing import Dict, List, Tuple

Sommet = int

class Graphe_v1:
    """Utilise la définition mathématique."""
    def __init__(self, sommets: List[Sommet], arretes: List[Tuple[Sommet, Sommet]]):
        self._sommets = sommets
        self._arretes = arretes
        
    def __getitem__(self, sommet: Sommet):
        """Itère sur les voisins du sommet."""
        for depart, arrivee in self._arretes:
            if depart == sommet:
                yield arrivee
        
class Graphe_v2:
    """Utilise un dictionnaire de voisinage sommet -> voisins"""
    def __init__(self, voisinage: Dict[Sommet, List[Sommet]]):
        self._voisinage = voisinage
        
    def __getitem__(self, sommet):
        """Itère sur les voisins du sommet."""
        for voisin in self._voisinage[sommet]:
            yield voisin

class Graphe_v3:
    """Utilise la représentation matricielle."""
    def __init__(self, adjacence=List[List[int]]):
        self._adjacence = adjacence
        
    def __getitem__(self, sommet):
        """Itère sur les voisins du sommet."""
        for indice, valeur in enumerate(self._adjacence[sommet - 1]):
            if valeur == 1:
                yield (indice + 1)
    
    
def bfs(depart, graphe):
    """Itèrateur sur les sommets du graphe en partant de depart."""
    deja_visites = set()
    a_visites = deque([depart])
    while a_visites:
        sommet_courant = a_visites.pop()
        if sommet_courant not in deja_visites:
            yield sommet_courant
            deja_visites.add(sommet_courant)
            for voisin in graphe[sommet_courant]:
                a_visites.appendleft(voisin)
            
    
def dfs(depart, graphe):
    """Itèrateur sur les sommets du graphe en partant de depart."""
    deja_visites = set()
    a_visites = deque([depart])
    while a_visites:
        sommet_courant = a_visites.pop()
        if sommet_courant not in deja_visites:
            yield sommet_courant
            deja_visites.add(sommet_courant)
            for voisin in graphe[sommet_courant]:
                a_visites.append(voisin)
