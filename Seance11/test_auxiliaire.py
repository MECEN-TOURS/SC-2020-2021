"""Description.

Tests de la bibliothèque auxiliaire.
"""
from auxiliaire import (enleve_sauts_de_ligne,)


def test_enleve_sauts_de_ligne():
    """Test."""
    entree = """
Phrase1.

Ligne2.
"""
    sortie = "Phrase1.  Ligne2."
    calculee = enleve_sauts_de_ligne(entree)
    assert calculee == sortie