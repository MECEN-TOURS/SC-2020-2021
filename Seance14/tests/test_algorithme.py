#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Teste la fonction de résolution.
"""
import pytest
from ordonnancement import Activite, EDT, Probleme, resous


def test_sans_solution():
    """Doit planter."""
    probleme = Probleme.par_str(
        """
A / 1 / B
B / 2 / A
"""
    )
    with pytest.raises(ValueError):
        resous(probleme)


def test_solution():
    """Attention à l'ordre sinon il faut modifier l'égalité entre deux EDT!"""
    probleme = Probleme.par_str(
        """
A / 1 / 
B / 2 / A
C / 3 / A B
D / 4 / A
"""
    )
    solution = resous(probleme)
    a, b, c, d = probleme.taches
    edt = EDT(
        activites=[
            Activite(a, debut=0, fin=1),
            Activite(d, debut=1, fin=5),
            Activite(b, debut=1, fin=3),
            Activite(c, debut=3, fin=6),
        ]
    )
    assert solution == edt
