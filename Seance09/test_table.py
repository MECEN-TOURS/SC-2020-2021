#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Tests de la table de Dijsktra.
"""
import pytest
from table import Table
from graphe_p import GrapheP


@pytest.fixture
def graphe_bateau():
    """Pour les tests."""
    return GrapheP.par_sommets_arretes(
        sommets=["A", "B", "C"],
        arretes=[(("A", "B"), 1), (("A", "C"), 4), (("B", "C"), 2)],
    )


def test_init(graphe_bateau):
    """Initialisation."""
    table = Table(graphe=graphe_bateau, depart="A")
    assert isinstance(table, Table)
    assert table.visites == set()
    assert table.graphe == graphe_bateau
    assert table.colonnes == [{"A": 0, "B": float("inf"), "C": float("inf")}]


def test_repr(graphe_bateau):
    """Dunder __repr__ ."""
    table = Table(graphe=graphe_bateau, depart="A")
    assert (
        repr(table)
        == "Table(graphe=GrapheP(voisinage={'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}}), depart='A')"
    )


def test_str(graphe_bateau):
    """Représentation."""
    table = Table(graphe=graphe_bateau, depart="A")
    assert str(table) == "[{'A': 0, 'B': inf, 'C': inf}]"


def test_eq(graphe_bateau):
    """Dunder __eq__ ."""
    table1 = Table(graphe=graphe_bateau, depart="A")
    table2 = Table(graphe=graphe_bateau, depart="A")
    assert table1 == table2


def test_prochain(graphe_bateau):
    """Test trouve_prochain."""
    table = Table(graphe=graphe_bateau, depart="A")
    assert table.trouve_prochain() == "A"


def test_nouvelle_colonne(graphe_bateau):
    """Test genere_nouvelle_colonne."""
    table = Table(graphe=graphe_bateau, depart="A")
    suivant = table.trouve_prochain()
    table.genere_nouvelle_colonne(sommet_courant=suivant)
    assert table.visites == {"A"}
    assert table.colonnes[-1] == {"A": 0, "B": 1, "C": 4}


def test_lance_dijkstra(graphe_bateau):
    """Test l'algorithme de Dijkstra."""
    table = Table(graphe=graphe_bateau, depart="A")
    table.lance()
    assert table.visites == set("ABC")
    assert table.colonnes == [
        {"A": 0, "B": float("inf"), "C": float("inf")},
        {"A": 0, "B": 1, "C": 4},
        {"A": 0, "B": 1, "C": 3},
        {"A": 0, "B": 1, "C": 3},
    ]
