"""Description.

Bibliothèque pour la résolution de Sudoku.
"""
from typing import List
from copy import copy

class Grille:
    """Implémente une grille de Sudoku 4x4."""
    valeurs = set([1, 2, 3, 4, 'x'])
    def __init__(self, cases):
        if not all(case in self.valeurs for case in cases):
            raise ValueError("Les seuls valeurs possibles sont 1 2 3 4 ou x")
        self.cases = cases
        
    def __repr__(self):
        return f"Grille(cases={self.cases})"
    
    def __str__(self):
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
        """.format(*self.cases)
    
    def __eq__(self, autre):
        return self.cases == autre.cases
    
    def __iter__(self):
        return iter(self.cases)
    
    def insere_valeur(self, indice, valeur):
        nouvelles_cases = copy(self.cases)
        nouvelles_cases[indice] = valeur
        return Grille(cases=nouvelles_cases)
    
def recupere_premier_x(grille: Grille) -> int:
    """Renvoie l'indice de la première case valant x."""
    for indice, valeur in enumerate(grille):
        if valeur == "x":
            return indice
    raise ValueError("Pas de x dans la grille")
    
def test_recupere_premier_x():
    entree = Grille([1, 2, 'x', 'x', 'x', 'x', 1, 2, 2, 'x', 'x', 3, 'x', 3, 2, ])
    sortie = recupere_premier_x(entree)
    attendu = 2
    return attendu == sortie

assert test_recupere_premier_x()

def test_recupere_premier_x_vide():
    entree = Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    try:
        sortie = recupere_premier_x(entree)
    except ValueError:
        return True
    return False

assert test_recupere_premier_x_vide()

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
        resultat.append(grille.insere_valeur(indice=indice, valeur=valeur))
    return resultat
    
def test_genere_voisins():
    entree = Grille([1, 2, 'x', 'x', 'x', 'x', 1, 2, 2, 'x', 'x', 3, 'x', 3, 2, 'x'])
    attendu = [
        Grille([1, 2, 1, 'x', 'x', 'x', 1, 2, 2, 'x', 'x', 3, 'x', 3, 2, 'x']),
        Grille([1, 2, 2, 'x', 'x', 'x', 1, 2, 2, 'x', 'x', 3, 'x', 3, 2, 'x']),
        Grille([1, 2, 3, 'x', 'x', 'x', 1, 2, 2, 'x', 'x', 3, 'x', 3, 2, 'x']),
        Grille([1, 2, 4, 'x', 'x', 'x', 1, 2, 2, 'x', 'x', 3, 'x', 3, 2, 'x']),
    ]
    sortie = genere_voisins(entree)
    return   attendu == sortie

assert test_genere_voisins()

def test_genere_voisins_vide():
    entree = Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    sortie = genere_voisins(entree)
    attendu = list()
    return sortie == attendu

assert test_genere_voisins_vide()

class Graphe:
    ...
