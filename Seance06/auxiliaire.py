"""Description.

Bibliothèque pour la résolution de Sudoku de type 2.
"""
from typing import Any, Generator, Iterator, List, Set, Union
from copy import deepcopy

Valeur = Union[int, str]


class Grille:
    """Implémente une grille de Sudoku 4x4.

        Exemples:
    >>> Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    Grille(cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    >>> Grille.par_lignes(
    ...     [
    ...             [1, 2, 3, 4],
    ...             [3, 4, 1, 2],
    ...             [2, 1, 4, 3],
    ...             [4, 3, 2, 1],
    ...     ]
    ... )
    Grille(cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    >>> Grille.par_str(
    ... '''
    ... 1234
    ... 3412
    ... 2143
    ... 4321
    ... '''
    ... )
    Grille(cases=[1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    >>> print(Grille.par_str(
    ...     "x234"
    ...     "3x12"
    ...     "21x3"
    ...     "432x"
    ... )
    ... )

    -----------------
    | x | 2 | 3 | 4 |
    -----------------
    | 3 | x | 1 | 2 |
    -----------------
    | 2 | 1 | x | 3 |
    -----------------
    | 4 | 3 | 2 | x |
    -----------------
    >>> g = Grille.par_str(
    ... '''
    ... 1234
    ... 3412
    ... 2143
    ... 4321
    ... '''
    ... )
    >>> g.est_finale()
    True
    >>> g.est_valide()
    True
    >>> h = Grille.par_str(
    ... '''
    ... 1234
    ... 2143
    ... xxxx
    ... xxxx
    ... '''
    ... )
    >>> h.est_finale()
    False
    >>> h.est_valide()
    False
    """

    _valeurs: Set[Valeur] = set([1, 2, 3, 4, "x"])

    def __init__(self, cases: List[Valeur]):
        """Initialise via une liste."""
        if not all(case in self._valeurs for case in cases):
            raise ValueError("Les seuls valeurs possibles sont 1 2 3 4 ou x")
        if len(cases) != 16:
            raise ValueError("Il faut fournir 16 valeurs.")
        self._cases = cases

    @classmethod
    def par_lignes(cls, lignes: List[List[Valeur]]) -> "Grille":
        """Initialise en passant une liste de listes."""
        return cls([element for ligne in lignes for element in ligne])

    @classmethod
    def par_str(cls, chaine: str) -> "Grille":
        """Initialise en passant une chaine multiligne."""
        cases = [
            cls._transforme_car(caractere)
            for ligne in chaine.strip().splitlines()
            for caractere in ligne
        ]
        return cls(cases)

    @staticmethod
    def _transforme_car(car: str) -> Valeur:
        try:
            return int(car)
        except ValueError:
            return car

    def __repr__(self) -> str:
        """Pour deboggage."""
        return f"Grille(cases={self._cases})"

    def __str__(self) -> str:
        """Pour inspection visuelle."""
        return """
-----------------
| {} | {} | {} | {} |
-----------------
| {} | {} | {} | {} |
-----------------
| {} | {} | {} | {} |
-----------------
| {} | {} | {} | {} |
-----------------
""".format(
            *self._cases
        )

    def __eq__(self, autre: Any) -> bool:
        """Egalité si memes cases."""
        if type(autre) != type(self):
            return False
        return self._cases == autre._cases

    def __iter__(self) -> Iterator[Valeur]:
        """On itère sur de gauche à droite de haut en bas."""
        return iter(self._cases)

    def __getitem__(self, indice: int) -> Valeur:
        """On accède à la case voulue.

        Permet de faire self[indice]
            -> self.__getitem__(indice)
            -> Grille.__getitem__(self, indice)
        """
        return self._cases[indice]

    def __setitem__(self, indice: int, valeur: Valeur):
        """On insère à la case voulue.

        Permet de faire self[indice] = valeur
            -> self.__setitem__(indice, valeur)
            -> Grille.__setitem__(self, indice, valeur)
        """
        self._cases[indice] = valeur

    def _verifie_lignes(self) -> bool:
        """Vérifie que les valeurs ne sont présentes qu'au plus une fois par ligne."""
        for valeur in (1, 2, 3, 4):
            for i3 in (0, 1):
                for i2 in (0, 1):
                    if (
                        sum(
                            1
                            for i1 in (0, 1)
                            for i0 in (0, 1)
                            if self[
                                i3 * 2 ** 3 + i2 * 2 ** 2 + i1 * 2 ** 1 + i0 * 2 ** 0
                            ]
                            == valeur
                        )
                        >= 2
                    ):
                        return False
        return True

    def _verifie_colonnes(self) -> bool:
        """Vérifie que les valeurs ne sont présentes qu'au plus une fois par colonne."""
        for valeur in (1, 2, 3, 4):
            for i1 in (0, 1):
                for i0 in (0, 1):
                    if (
                        sum(
                            1
                            for i3 in (0, 1)
                            for i2 in (0, 1)
                            if self[
                                i3 * 2 ** 3 + i2 * 2 ** 2 + i1 * 2 ** 1 + i0 * 2 ** 0
                            ]
                            == valeur
                        )
                        >= 2
                    ):
                        return False
        return True

    def _verifie_carres(self) -> bool:
        """Vérifie que les valeurs ne sont présentes qu'au plus une fois par carré."""
        for cible in (1, 2, 3, 4):
            for p3 in range(2):
                for p1 in range(2):
                    if (
                        sum(
                            1
                            for p2 in range(2)
                            for p0 in range(2)
                            if self[p0 + p1 * 2 + p2 * 2 ** 2 + p3 * 2 ** 3] == cible
                        )
                        >= 2
                    ):
                        return False
        return True

    def est_valide(self) -> bool:
        """Vérifie si la grille respecte les règles."""
        return (
            self._verifie_lignes()
            and self._verifie_colonnes()
            and self._verifie_carres()
        )

    def est_finale(self) -> bool:
        """Vérifie si toutes les cases sont bien remplies."""
        return not any(valeur == "x" for valeur in self)


def __insere_valeur(grille: Grille, indice: int, valeur: int) -> Grille:
    """Rajoute la valeur à la position donnée par l'indice dans la grille.

    Renvoie une nouvelle grille.
    """
    nouvelle_grille = deepcopy(grille)
    nouvelle_grille[indice] = valeur
    return nouvelle_grille


def __recupere_premier_x(grille: Grille) -> int:
    """Renvoie l'indice de la première case valant x."""
    for indice, valeur in enumerate(grille):
        if valeur == "x":
            return indice
    raise ValueError("Pas de x dans la grille")


def __genere_voisins(grille: Grille) -> List[Grille]:
    """Genere les sommets voisins de la grille.

    On remplit la première case vide avec 1, 2, 3 ou 4.
    """
    try:
        indice = __recupere_premier_x(grille)
    except ValueError:
        return []
    resultat = list()
    for valeur in (1, 2, 3, 4):
        resultat.append(__insere_valeur(grille=grille, indice=indice, valeur=valeur))
    return resultat


def genere_solutions(grille: Grille) -> Generator[Grille, None, None]:
    """Renvoie un itérateur sur les solutions.

        Exemple:
    >>> g = Grille.par_str(
    ... '''
    ... 123x
    ... 3412
    ... x143
    ... 4321
    ... '''
    ... )
    >>> print(g)

    -----------------
    | 1 | 2 | 3 | x |
    -----------------
    | 3 | 4 | 1 | 2 |
    -----------------
    | x | 1 | 4 | 3 |
    -----------------
    | 4 | 3 | 2 | 1 |
    -----------------

    >>> for sol in genere_solutions(g):
    ...     print(sol)
    ...

    -----------------
    | 1 | 2 | 3 | 4 |
    -----------------
    | 3 | 4 | 1 | 2 |
    -----------------
    | 2 | 1 | 4 | 3 |
    -----------------
    | 4 | 3 | 2 | 1 |
    -----------------
    """
    if grille.est_valide():
        if grille.est_finale():
            yield grille
        else:
            for voisin in __genere_voisins(grille):
                yield from genere_solutions(voisin)
