#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Démonstration du module.
"""

from rich import print
from .probleme import Probleme
from .algorithme import resous

mon_probleme = Probleme.par_str(
    """
A / 1 / 
B / 2 / A
C / 3 / A B
D / 4 / A
"""
)
print("Problème à résoudre:\n")
print(mon_probleme.affiche())

solution = resous(mon_probleme)
print("Et la solution.\n")
print(solution.affiche())
