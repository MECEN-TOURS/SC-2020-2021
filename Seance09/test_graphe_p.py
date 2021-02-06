#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Tests pour la classe Graphe_P.
"""

import pytest
from graphe_p import GrapheP


def test_init():
    g = GrapheP(voisinage={})
    assert isinstance(g, GrapheP)


def test_egalite():
    g1 = GrapheP(
        voisinage={
            "A": {"B": 1},
            "B": {},
            "C": {},
        }
    )
    g2 = GrapheP(
        voisinage={
            "A": {"B": 1},
            "B": {},
            "C": {},
        }
    )
    assert g1 == g2


def test_repr():
    """Dunder __repr__ ."""
    g = GrapheP(
        voisinage={
            "A": {"B": 1},
            "B": {},
            "C": {},
        }
    )

    assert repr(g) == "GrapheP(voisinage={'A': {'B': 1}, 'B': {}, 'C': {}})"


def test_par_sommets_arretes():
    """Pour coller à la définition mathématiques."""
    alternatif = GrapheP.par_sommets_arretes(
        sommets=["A", "B", "C"], arretes=[(("A", "B"), 1)]
    )
    attendu = GrapheP(
        voisinage={
            "A": {"B": 1},
            "B": {},
            "C": {},
        }
    )
    assert alternatif == attendu


def test_arrete_rendondante():
    """Doit boguer."""
    with pytest.raises(ValueError):
        alternatif = GrapheP.par_sommets_arretes(
            sommets=["A", "B", "C"], arretes=[(("A", "B"), 1), (("A", "B"), 2)]
        )


def test_sommets():
    """Teste l'attribut sommets."""
    g = GrapheP(
        voisinage={
            "A": {"B": 1},
            "B": {},
            "C": {},
        }
    )
    assert list(g.sommets) == list("ABC")


def test_arretes():
    """Teste l'attribut arretes."""
    g = GrapheP(
        voisinage={
            "A": {"B": 1},
            "B": {},
            "C": {},
        }
    )
    assert list(g.arretes) == [(("A", "B"), 1)]


def test_voisins():
    g = GrapheP(
        voisinage={
            "A": {"B": 1},
            "B": {},
            "C": {},
        }
    )
    assert g["A"] == {"B": 1}


def test_par_str_non_ord():
    """Constructeur alternatif."""
    essai = GrapheP.par_str_non_ordonne(
        """
A B 1
"""
    )
    attendu = GrapheP(
        voisinage={
            "A": {"B": 1},
            "B": {"A": 1},
        }
    )
    assert essai == attendu


def test_adjacence():
    graphe = GrapheP(
        voisinage={
            "A": {"B": 1, "C": 2},
            "B": {"A": 3, "C": 4},
            "C": {"C": 5},
        }
    )
    attendu = [
        [0, 1, 2],
        [3, 0, 4],
        [0, 0, 5],
    ]
    assert graphe.adjacence == attendu


def test_non_ordonne():
    """Matrice symétrique?"""
    graphe = GrapheP(
        voisinage={
            "A": {"B": 1, "C": 2},
            "B": {"A": 3, "C": 4},
            "C": {"C": 5},
        }
    )
    assert not graphe.est_non_ordonne()
    graphe_s = GrapheP(
        voisinage={
            "A": {"B": 1},
            "B": {"A": 1, "C": 4},
            "C": {"B": 4},
        }
    )
    assert graphe_s.est_non_ordonne()
