"""Description.

Tests de la bibliothèque auxiliaire.
"""
from auxiliaire import (
    enleve_sauts_de_ligne,
    convertit_majuscules,
    remplace_caracteres_speciaux,
    reduit_espaces,
    genere_liste_mots,
)


def test_enleve_sauts_de_ligne():
    """Test."""
    entree = """
Phrase1.

Ligne2.
"""
    attendue = "Phrase1.  Ligne2."
    calculee = enleve_sauts_de_ligne(entree)
    assert calculee == attendue
    
def test_convertit_majuscules():
    """Test."""
    entree = "ABcdEfGh,. "
    attendue = "abcdefgh,. "
    calculee = convertit_majuscules(entree)
    assert calculee == attendue
    
def test_remplace_caracteres_speciaux():
    """Test."""
    entree = """une,Phrase de.TEST\tpour'verification."""
    attendue = """une  hrase de      pour verification """
    calculee = remplace_caracteres_speciaux(entree)
    assert calculee == attendue
    
def test_reduit_espaces():
    """Test."""
    entree = "  test  test test   test"
    attendue = " test test test test"
    calculee = reduit_espaces(entree)
    assert calculee == attendue
    
def test_genere_liste_mots():
    """Test."""
    entree = """
Motun, motdeux. 
Mottrois;\tmotquatre.
    """
    attendue = ["motun", "motdeux", "mottrois", "motquatre"]
    calculee = genere_liste_mots(entree)
    assert attendue == calculee