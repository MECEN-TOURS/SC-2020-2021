#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Très rapide intro aux décorateurs.
"""
import time
from functools import lru_cache
from pysnooper import snoop


def decorateur(ma_fonction):
    def nouvelle(*args):
        print("Avant le calcul")
        resultat = ma_fonction(*args)
        print("Après le calcul.")

        return resultat

    return nouvelle


def mesure(ma_fonction):
    def nouvelle(*args):
        debut = time.time()
        resultat = ma_fonction(*args)
        fin = time.time()
        print(f"Temps de calcul {fin - debut}")
        return resultat

    return nouvelle


@mesure
def fibonacci(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


@snoop("./debug")
def fibo_rec(n):
    if n < 2:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)
