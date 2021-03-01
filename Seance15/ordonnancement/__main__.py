#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Démonstration du module.
"""

from .probleme import Probleme
from .algorithme import resous

mon_probleme = Probleme.par_str(
    """
A / 1.5 / F
B / 3 / I
C / 4 / F I
D / 1 / A G F
E / 6 / A B
F / 2 /
G / 4.5 / B C F
H / 0.5 / A I J
I / 3 /
J / 4 / D G
"""
)
mon_probleme.affiche()

solution = resous(mon_probleme)
solution.affiche()
