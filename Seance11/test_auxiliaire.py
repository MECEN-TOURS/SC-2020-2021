"""Description.

Tests de la bibliothèque auxiliaire.
"""
from auxiliaire import (
    enleve_sauts_de_ligne,
    convertit_majuscules,
)


def test_enleve_sauts_de_ligne():
    """Test."""
    entree = """
Phrase1.

Ligne2.
"""
    sortie = "Phrase1.  Ligne2."
    calculee = enleve_sauts_de_ligne(entree)
    assert calculee == sortie
    
def test_convertit_majuscules():
    """Test."""
    entree = "ABcdEfGh,. "
    sortie = "abcdefgh,. "
    calculee = convertit_majuscules(entree)
    assert calculee == sortie
    
def test_supprime_caracteres_speciaux():
    """Test."""
    entree = ...
    sortie = ...
    calculee = ...
    assert calculee == sortie