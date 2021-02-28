#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Tests pour la classe Probleme du module ordonnancement.
"""
import pytest
from ordonnancement import Probleme, Tache


@pytest.fixture
def taches():
    """4 taches pour les tests suivants."""
    a = Tache(nom="A", duree=1, prerequis=[])
    b = Tache(nom="B", duree=2, prerequis=["A"])
    c = Tache(nom="C", duree=3, prerequis=["A", "B"])
    d = Tache(nom="D", duree=4, prerequis=["A"])
    return [a, b, c, d]


def test_instanciation(taches):
    """Création."""
    probleme = Probleme(taches=taches)
    assert isinstance(probleme, Probleme)
    assert probleme._taches == {tache.nom: tache for tache in taches}


def test_egalite(taches):
    """Doit être différent de l'identité."""
    probleme1 = Probleme(taches)
    probleme2 = Probleme(taches)
    assert probleme1 == probleme2


def test_validation_doublon(taches):
    """Vérifie la détection de deux tâches avec le même nom."""
    a, b, c, d = taches
    e = Tache(nom="A", duree=1, prerequis=["B"])
    with pytest.raises(ValueError):
        Probleme([a, b, c, d, e])


def test_validation_taches(taches):
    """Vérifie la détection de prérequis phantome."""
    a, b, c, d = taches
    e = Tache(nom="E", duree=1, prerequis=["F"])
    with pytest.raises(ValueError):
        Probleme([a, b, c, d, e])


def test_taches(taches):
    """Teste la propriété taches."""
    probleme = Probleme(taches)
    assert "taches" not in vars(probleme)
    assert taches == list(probleme.taches)


def test_noms(taches):
    """Teste la propriété noms."""
    probleme = Probleme(taches)
    assert "noms" not in vars(probleme)
    assert list("ABCD") == list(probleme.noms)


def test_acces(taches):
    """Utilisation de []."""
    probleme = Probleme(taches)
    assert probleme["A"] == taches[0]


def test_repr():
    """Teste le repr."""
    probleme = Probleme(taches=[Tache(nom="A", duree=1, prerequis=[])])
    assert (
        repr(probleme)
        == "Probleme(taches=[Tache(nom='A', duree=1, prerequis=[])])"
    )


def test_encode():
    """Teste l'encodage d'une ligne."""
    correspondance = {
        "B / 1 / A": Tache(nom="B", duree=1, prerequis=["A"]),
        "A / 2 / ": Tache(nom="A", duree=2, prerequis=[]),
    }
    for entree, attendu in correspondance.items():
        assert attendu == Probleme._encode(entree)


def test_constructeur(taches):
    """Constructeur alternatif."""
    entree = """
A / 1 /
B / 2 / A
C / 3 / A B
D / 4 / A
"""
    probleme = Probleme.par_str(entree)
    assert probleme == Probleme(taches)
