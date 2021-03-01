#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Exemple:

>>> from rich import print
>>> from ordonnancement import Probleme, resous
>>> mon_probleme = Probleme.par_str('''
... A / 1 /
... B / 2 / A
... C / 3 / A B
... D / 4 / A
... '''
... )
>>> print(mon_probleme.affiche())
┏━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
┃ Tache ┃ Durée ┃ Prérequis ┃
┡━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
│ A     │ 1     │           │
│ B     │ 2     │ A         │
│ C     │ 3     │ A, B      │
│ D     │ 4     │ A         │
└───────┴───────┴───────────┘
>>> solution = resous(mon_probleme)
>>> print(solution.affiche())
┏━━━━━━━┳━━━━━━━┳━━━━━┓
┃ Tache ┃ Début ┃ Fin ┃
┡━━━━━━━╇━━━━━━━╇━━━━━┩
│ A     │ 0     │ 1   │
│ D     │ 1     │ 5   │
│ B     │ 1     │ 3   │
│ C     │ 3     │ 6   │
└───────┴───────┴─────┘

Remarque:

On pourra faire python -m ordonnancement pour un exemple.
"""
from .probleme import Tache, Probleme
from .edt import Activite, EDT
from .algorithme import resous

__all__ = ["Activite", "EDT", "Tache", "Probleme", "resous"]
