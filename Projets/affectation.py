#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Script effectuant la répartition des sujets au élèves.
"""
import random as rd
from rich.console import Console

ELEVES = (
    "Cornet Hugo",
    "Diot Pierre-Emmanuel",
    "Le Halper Guillaume",
    "Mancer Djawed",
    "Fuchez Thibault",
    "Chaveneau Lucas",
    "Lefafta Rémi",
    "Feteira Jeremy",
    "Corre Guillaume",
    "Lenoir Yoan",
    "Cardoso Jeremy",
    "Boudou Manon",
    "Billon Melissa",
    "Guichard Allan",
    "Vickos Gloria",
    "Li Marine",
    "Meyer Marie",
    "Gendron Marine",
    "Ducamp Axel",
)

SUJETS = [f"{numero+1:02}" for numero, _ in enumerate(ELEVES)]
rd.seed(123456789)
rd.shuffle(SUJETS)

CS = Console()

AFFECTATION = {eleve: sujet for eleve, sujet in zip(ELEVES, SUJETS)}
CS.print(AFFECTATION)
