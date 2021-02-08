"""Description.

Graphes pondérés avec
    - des chaines de caractères pour noeuds
    - des poids entiers ou flottants.
"""
import re
from typing import Any, Dict, Iterator, List, Tuple, Union

Sommet = str
Poids = Union[int, float]
Arrete = Tuple[Tuple[Sommet, Sommet], Poids]


class GrapheP:
    """Graphe pondérée.

        Exemple:
    >>> graphe = GrapheP(
    ...     voisinage={
    ...         "A": {"B": 1},
    ...         "B": {},
    ...         "C": {},
    ...     }
    ... )
    >>> graphe
    GrapheP(voisinage={'A': {'B': 1}, 'B': {}, 'C': {}})
    >>> graphe_bis = GrapheP.par_sommets_arretes(
    ...     sommets=["A", "B", "C"],
    ...     arretes=[(("A", "B"), 1)],
    ... )
    >>> graphe == graphe_bis
    True
    >>> graphe is graphe_bis
    False
    >>> for sommet in graphe.sommets:
    ...     print(sommet)
    ...
    A
    B
    C
    >>> graphe.sommets = ["A", "B", "C", "D"]
    AttributeError:
    can't set attribute
    >>> for arrete in graphe.arretes:
    ...     print(arrete)
    ...
    (('A', 'B'), 1)
    >>> graphe.arretes.append((("A", "C"), 2))
    AttributeError:
    'generator' object has no attribute 'append'
    >>> graphe["A"]
    {'B': 1}
    >>> nouveau = GrapheP.par_str_non_ordonne(
    ... '''
    ... A B 1
    ... A C 2
    ... A D 3
    ... A E 4.5
    ... B C 5
    ... B F 6
    ... C G 7
    ... D H 8
    ... '''
    ... )
    >>> nouveau
    GrapheP(voisinage={'A': {'B': 1, 'C': 2, 'D': 3, 'E': 4.5}, 'B': {'A': 1, 'C': 5, 'F': 6}, 'C': {'A': 2, 'B': 5, 'G': 7}, 'D': {'A': 3, 'H': 8}, 'E': {'A': 4.5}, 'F': {'B': 6}, 'G': {'C': 7}, 'H': {'D': 8}})
    >>> print(nouveau.adjacence)
    [
        [0, 1, 2, 3, 4.5, 0, 0, 0],
        [1, 0, 5, 0, 0, 6, 0, 0],
        [2, 5, 0, 0, 0, 0, 7, 0],
        [3, 0, 0, 0, 0, 0, 0, 8],
        [4.5, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0]
    ]
    >>> import numpy as np
    >>> np.array(nouveau.adjacence)
    array([[0. , 1. , 2. , 3. , 4.5, 0. , 0. , 0. ],
           [1. , 0. , 5. , 0. , 0. , 6. , 0. , 0. ],
           [2. , 5. , 0. , 0. , 0. , 0. , 7. , 0. ],
           [3. , 0. , 0. , 0. , 0. , 0. , 0. , 8. ],
           [4.5, 0. , 0. , 0. , 0. , 0. , 0. , 0. ],
           [0. , 6. , 0. , 0. , 0. , 0. , 0. , 0. ],
           [0. , 0. , 7. , 0. , 0. , 0. , 0. , 0. ],
           [0. , 0. , 0. , 8. , 0. , 0. , 0. , 0. ]])

    >>> nouveau.est_non_ordonne()
    True
    """

    _motif = re.compile(r"^\s?(\w+)\s(\w+)\s(\d+|\d+.\d+)\s?$")

    def __init__(self, voisinage=Dict[Sommet, Dict[Sommet, Poids]]):
        """Initialise par dictionnaire de voisinage."""
        self._voisinage = voisinage

    def __eq__(self, autre: Any) -> bool:
        """Egalite parfaite pas isomorphisme."""
        if type(self) != type(autre):
            return False
        return self._voisinage == autre._voisinage

    def __repr__(self):
        """Repr pour débug."""
        return f"GrapheP(voisinage={self._voisinage})"

    @classmethod
    def par_sommets_arretes(cls, sommets: List[Sommet], arretes: List[Arrete]):
        """Constructeur alternatif par sommets et arretes."""
        voisinage: Dict[Sommet, Dict[Sommet, Poids]] = dict()
        for ((depart, arrivee), poids) in arretes:
            if depart not in voisinage:
                voisinage[depart] = {arrivee: poids}
            else:
                if arrivee not in voisinage[depart]:
                    voisinage[depart][arrivee] = poids
                else:
                    raise ValueError(
                        f"L'arrête {depart} {arrivee} est présente deux fois."
                    )

        for sommet in sommets:
            if sommet not in voisinage:
                voisinage[sommet] = dict()

        return cls(voisinage=voisinage)

    @property
    def sommets(self) -> Iterator[Sommet]:
        """Itérateur des sommets."""
        return iter(self._voisinage.keys())

    @property
    def arretes(self) -> Iterator[Arrete]:
        """Itère sur les arrêtes."""
        for sommet, voisins in self._voisinage.items():
            for voisin, poids in voisins.items():
                yield ((sommet, voisin), poids)

    @property
    def adjacence(self) -> List[List[Poids]]:
        """Renvoie une matrice d'adjacence."""
        resultat = list()
        for depart in self.sommets:
            ligne = list()
            for arrivee in self.sommets:
                if arrivee in self._voisinage[depart]:
                    ligne.append(self._voisinage[depart][arrivee])
                else:
                    ligne.append(0)
            resultat.append(ligne)
        return resultat

    def __getitem__(self, sommet: Sommet) -> Dict[Sommet, Poids]:
        """Renvoit le voisinage du sommet."""
        return self._voisinage[sommet]

    @classmethod
    def par_str_non_ordonne(cls, graphe: str) -> "GrapheP":
        """Permet de construire par chaine de caractère."""
        arretes = list()
        for ligne in graphe.strip().splitlines():
            if (resultat := cls._motif.match(ligne)) is not None:
                depart, arrivee, poids = resultat.groups()
            else:
                raise ValueError(
                    f"Il y a un problème sur cette ligne>>\n{ligne}"
                )
            try:
                poids_numerique: Poids = int(poids)
            except ValueError:
                poids_numerique = float(poids)
            arretes.append(((depart, arrivee), poids_numerique))
            arretes.append(((arrivee, depart), poids_numerique))
        sommets = list(set([depart for ((depart, _), _) in arretes]))
        return cls.par_sommets_arretes(sommets=sommets, arretes=arretes)

    def est_non_ordonne(self) -> bool:
        """Détermine si la matrice d'adjacence est symétrique."""
        matrice = self.adjacence
        return matrice == [
            [matrice[j][i] for j, _ in enumerate(ligne)]
            for i, ligne in enumerate(matrice)
        ]
    
    def genere_dot(self, nom_fichier="temp"):
        """Ecrit un fichier au format dot."""
        with open(nom_fichier + ".dot", "w") as fichier:
            fichier.write(f"digraph {nom_fichier} {{\n")
            for ((depart, arrivee), poids) in self.arretes:
                fichier.write(f"{depart} -> {arrivee} [label={poids}];\n")
            fichier.write(f"}}")
            
