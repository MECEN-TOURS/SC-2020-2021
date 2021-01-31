#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Tests de la bibliothèque auxiliaire.
"""
import pytest
from auxiliaire import (
    Grille,
    insere_valeur,
    recupere_premier_x,
    genere_voisins,
    genere_solutions,
)


class Test_Grille:
    """Test de la classe Grille."""

    def test_init(self):
        """Test l'instanciation normale."""
        creation = Grille(
            [
                1,
                2,
                "x",
                "x",
                "x",
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        assert isinstance(creation, Grille)

    def test_init_mauvaise_valeur(self):
        """Test la détection d'une mauvaise valeur en entrée."""
        with pytest.raises(ValueError):
            creation = Grille(cases=[i for i in range(16)])

    def test_init_mauvaise_taille(self):
        """Test la détection du mauvais nombre de cases."""
        with pytest.raises(ValueError):
            creation = Grille([1, 2, 3, 4])

    def test_repr(self):
        """Test de l'affichage repr."""
        essai = Grille(
            [
                1,
                2,
                "x",
                "x",
                "x",
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        assert (
            repr(essai)
            == "Grille(cases=[1, 2, 'x', 'x', 'x', 'x', 1, 2, 2, 'x', 'x', 3, 'x', 3, 2, 'x'])"
        )

    def test_str(self):
        """Test de l'affichage str."""
        essai = Grille(
            [
                1,
                2,
                "x",
                "x",
                "x",
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        assert (
            str(essai)
            == """
-----------------
| 1 | 2 | x | x |
-----------------
| x | x | 1 | 2 |
-----------------
| 2 | x | x | 3 |
-----------------
| x | 3 | 2 | x |
-----------------
"""
        )

    def test_eq(self):
        """Vérifie qu'on teste l'égalité et pas l'identité."""
        cases = [
            1,
            2,
            "x",
            "x",
            "x",
            "x",
            1,
            2,
            2,
            "x",
            "x",
            3,
            "x",
            3,
            2,
            "x",
        ]
        assert Grille(cases) == Grille(cases)

    def test_par_ligne(self):
        """Test le constructeur par table."""
        generee = Grille.par_lignes(
            [
                [1, 2, 3, 4],
                [3, 4, 1, 2],
                [2, 1, 4, 3],
                [4, 3, 2, 1],
            ]
        )
        attendue = Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
        assert attendue == generee

    def test_par_ligne_x(self):
        """Test le constructeur par table avec des cases vides."""
        generee = Grille.par_lignes(
            [
                ["x", 2, 3, 4],
                [3, "x", 1, 2],
                [2, 1, "x", 3],
                [4, 3, 2, "x"],
            ]
        )
        attendue = Grille(["x", 2, 3, 4, 3, "x", 1, 2, 2, 1, "x", 3, 4, 3, 2, "x"])
        assert attendue == generee

    def test_par_str(self):
        """Test le constructeur par str."""
        generee = Grille.par_str("""
1234
3412
2143
4321
""")
        attendue = Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
        assert attendue == generee
        
    def test_par_str_x(self):
        """Test le constructeur par str avec cases vides."""
        generee = Grille.par_str("""
x234
3x12
21x3
432x
""")
        attendue = Grille(["x", 2, 3, 4, 3, "x", 1, 2, 2, 1, "x", 3, 4, 3, 2, "x"])
        assert attendue == generee

    def test_iter(self):
        """Vérifie qu'on itère bien sur les cases."""
        essai = Grille(
            [
                1,
                2,
                "x",
                "x",
                "x",
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        assert list(essai) == [
            1,
            2,
            "x",
            "x",
            "x",
            "x",
            1,
            2,
            2,
            "x",
            "x",
            3,
            "x",
            3,
            2,
            "x",
        ]

    def test_getitem(self):
        """Teste l'accès par indice."""
        essai = Grille(
            [
                1,
                2,
                "x",
                "x",
                "x",
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        assert essai[0] == 1
        assert essai[-1] == "x"
        assert essai[1:5] == [2, "x", "x", "x"]

    def test_setitem(self):
        """Teste l'insertion par indice."""
        essai = Grille(
            [
                1,
                2,
                "x",
                "x",
                "x",
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        essai[0] = "x"
        assert essai[0] == "x"

    def test_verifie_ligne(self):
        essai = Grille(
            [
                1,
                2,
                "x",
                "x",
                "x",
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        assert essai.verifie_lignes()
        essai = Grille(
            [
                1,
                2,
                "x",
                1,
                "x",
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        assert not essai.verifie_lignes()

    def test_verifie_colonnes(self):
        essai = Grille(
            [
                1,
                2,
                "x",
                "x",
                "x",
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        assert essai.verifie_colonnes()
        essai = Grille(
            [
                1,
                2,
                "x",
                "x",
                1,
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        assert not essai.verifie_lignes()

    def test_verifie_carres(self):
        essai = Grille(
            [
                1,
                2,
                "x",
                "x",
                "x",
                "x",
                1,
                2,
                2,
                "x",
                "x",
                3,
                "x",
                3,
                2,
                "x",
            ]
        )
        assert essai.verifie_carres()
        essai = Grille([1, 2, 3, 4, 2, 1, 4, 3, 3, 4, 1, 2, 4, 3, 2, 1])
        assert not essai.verifie_carres()

    def test_est_valide(self):
        essai = Grille([1, 2, 3, 4, 2, 1, 4, 3, 3, 4, 1, 2, 4, 3, 2, 1])
        assert not essai.est_valide()
        essai = Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
        assert essai.est_valide()


def test_insere_valeur():
    """Vérifie qu'on a bien une nouvelle grille et la bonne valeur."""
    essai = Grille(
        [
            1,
            2,
            "x",
            "x",
            "x",
            "x",
            1,
            2,
            2,
            "x",
            "x",
            3,
            "x",
            3,
            2,
            "x",
        ]
    )
    identification = id(essai)
    nouvelle = insere_valeur(grille=essai, indice=0, valeur=4)
    assert identification != id(nouvelle)
    assert nouvelle[0] == 4


def test_recupere_premier_x():
    """Test un cas standard."""
    entree = Grille(
        [
            1,
            2,
            "x",
            "x",
            "x",
            "x",
            1,
            2,
            2,
            "x",
            "x",
            3,
            "x",
            3,
            2,
            "x",
        ]
    )
    sortie = recupere_premier_x(entree)
    attendu = 2
    assert attendu == sortie


def test_recupere_premier_x_vide():
    """Test génération exception avec absence de x."""
    entree = Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    with pytest.raises(ValueError):
        _ = recupere_premier_x(entree)


def test_genere_voisins():
    """Test standard."""
    entree = Grille([1, 2, "x", "x", "x", "x", 1, 2, 2, "x", "x", 3, "x", 3, 2, "x"])
    attendu = [
        Grille([1, 2, 1, "x", "x", "x", 1, 2, 2, "x", "x", 3, "x", 3, 2, "x"]),
        Grille([1, 2, 2, "x", "x", "x", 1, 2, 2, "x", "x", 3, "x", 3, 2, "x"]),
        Grille([1, 2, 3, "x", "x", "x", 1, 2, 2, "x", "x", 3, "x", 3, 2, "x"]),
        Grille([1, 2, 4, "x", "x", "x", 1, 2, 2, "x", "x", 3, "x", 3, 2, "x"]),
    ]
    sortie = genere_voisins(entree)
    assert attendu == sortie


def test_genere_voisins_vide():
    """Teste une grille complète."""
    entree = Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    sortie = genere_voisins(entree)
    attendu = list()
    assert sortie == attendu


def test_genere_solutions():
    """Regarde les solutions."""
    essai = Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, "x"])
    assert list(genere_solutions(essai)) == [
        Grille([1, 2, 3, 4, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 2, 1])
    ]
