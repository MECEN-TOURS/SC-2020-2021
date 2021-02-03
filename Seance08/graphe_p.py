"""Description.

Bibliothèque avec une classe pour les graphes pondérés et des fonctions pour faire tourner l'algorithme de Dijkstra.
"""
from typing import Dict, Generator, List, Set, Tuple 

Sommet = str
Arrete = Tuple[Tuple[Sommet, Sommet], int]

class GrapheP:
    """Graphe pondérée."""
    def __init__(self, sommets: List[Sommet], arretes: List[Arrete]):
        self._sommets = sommets
        self._arretes = arretes
        
    def __repr__(self):
        return f"GrapheP(sommets={self._sommets}, arretes={self._arretes})"
        
    def __getitem__(self, sommet: Sommet) -> Generator[Tuple[Sommet, int], None, None]:
        """Itérateur de voisinage."""
        for ((depart, arrivee), poids) in self._arretes:
            if depart == sommet:
                yield (arrivee, poids)
    
    @classmethod
    def par_str_non_ordonne(cls, graphe: str) -> "GrapheP":
        ...
      

        
exemple = GrapheP.par_str_non_ordonne(
"""
AB1
AE7
BC2
BD4
CD1
CF1
CG5
DF2
DH1
EG2
EI4
FH1
GH2
GI1
"""
)
assert sorted(exemple._sommets) == list("ABCDEFGHI")
        
def calcule_distance(depart, graphe):
    ...
    
def calcule_chemin(depart, graphe):
    ...
