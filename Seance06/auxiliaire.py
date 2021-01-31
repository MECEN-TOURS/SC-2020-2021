"""Description.

Bibliothèque pour la résolution de Sudoku de type 2.
"""
from typing import List
from copy import deepcopy


class Grille:
    """Implémente une grille de Sudoku 4x4."""

    valeurs = set([1, 2, 3, 4, "x"])

    def __init__(self, cases):
        """Initialise via une liste."""
        if not all(case in self.valeurs for case in cases):
            raise ValueError("Les seuls valeurs possibles sont 1 2 3 4 ou x")
        if len(cases) != 16:
            raise ValueError("Il faut fournir 16 valeurs.")
        self.cases = cases
    
    @classmethod
    def par_lignes(cls, lignes):
        """Initialise en passant une liste de listes."""
        return cls([element for ligne in lignes for element in ligne])
    
    @classmethod
    def par_str(cls, chaine: str):
        """Initialise en passant une chaine multiligne."""
        cases = [
            cls.__transforme_car(caractere) 
            for ligne in chaine.strip().splitlines() 
            for caractere in ligne
        ]
        return cls(cases)
    
    @staticmethod
    def __transforme_car(car):
        try:
            return int(car)
        except ValueError:
            return car
    
    def __repr__(self):
        """Pour deboggage."""
        return f"Grille(cases={self.cases})"

    def __str__(self):
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
            *self.cases
        )

    def __eq__(self, autre):
        """Egalité si memes cases."""
        return self.cases == autre.cases

    def __iter__(self):
        """On itère sur de gauche à droite de haut en bas."""
        return iter(self.cases)

    def __getitem__(self, indice):
        """On accède à la case voulue.
        
        Permet de faire self[indice] 
            -> self.__getitem__(indice) 
            -> Grille.__getitem__(self, indice)
        """
        return self.cases[indice]

    def __setitem__(self, indice, valeur):
        """On insère à la case voulue.
        
        Permet de faire self[indice] = valeur
            -> self.__setitem__(indice, valeur)
            -> Grille.__setitem__(self, indice, valeur)
        """
        self.cases[indice] = valeur

    def verifie_lignes(self):
        """Vérifie que les valeurs ne sont présentes qu'au plus une fois par ligne."""
        for valeur in (1, 2, 3, 4):
            for i3 in (0, 1):
                for i2 in (0, 1):
                    if sum(
                        1 
                        for i1 in (0, 1)
                        for i0 in (0, 1)
                        if self[i3 * 2**3 + i2 * 2 ** 2 + i1 * 2**1 + i0 * 2 ** 0] == valeur
                    ) >= 2:
                        return False
            return True

    def verifie_colonnes(self):
        """Vérifie que les valeurs ne sont présentes qu'au plus une fois par ligne."""
        for valeur in (1, 2, 3, 4):
            for i1 in (0, 1):
                for i0 in (0, 1):
                    if sum(
                        1 
                        for i3 in (0, 1)
                        for i2 in (0, 1)
                        if self[i3 * 2**3 + i2 * 2 ** 2 + i1 * 2**1 + i0 * 2 ** 0] == valeur
                    ) >= 2:
                        return False
            return True

    def verifie_carres(self):
        """Vérifie que les valeurs ne sont présentes qu'au plus une fois par ligne."""
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

    def est_valide(self):
        """Vérifie si la grille respecte les règles."""
        if not self.verifie_lignes():
            return False
        if not self.verifie_colonnes():
            return False
        if not self.verifie_carres():
            return False
        return True
        # equivalent à 
        # return self.verifie_lignes() and self.verifie_colonnes() and self.verifie_carres()
    
    def est_finale(self):
        return not any(valeur == "x" for valeur in self)


def insere_valeur(grille: Grille, indice: int, valeur: int) -> Grille:
    """Rajoute la valeur à la position donnée par l'indice dans la grille.

    Renvoie une nouvelle grille.
    """
    nouvelle_grille = deepcopy(grille)
    nouvelle_grille[indice] = valeur
    return nouvelle_grille


def recupere_premier_x(grille: Grille) -> int:
    """Renvoie l'indice de la première case valant x."""
    for indice, valeur in enumerate(grille):
        if valeur == "x":
            return indice
    raise ValueError("Pas de x dans la grille")


def genere_voisins(grille: Grille) -> List[Grille]:
    """Genere les sommets voisins de la grille.

    On remplit la première case vide avec 1, 2, 3 ou 4.
    """
    try:
        indice = recupere_premier_x(grille)
    except ValueError:
        return []
    resultat = list()
    for valeur in (1, 2, 3, 4):
        resultat.append(insere_valeur(grille=grille, indice=indice, valeur=valeur))
    return resultat


def genere_solutions(grille: Grille):
    """Renvoie un itérateur sur les solutions."""
    if grille.est_valide():
        if grille.est_finale():
            yield grille
        else:
            for voisin in genere_voisins(grille):
                yield from genere_solutions(voisin)

