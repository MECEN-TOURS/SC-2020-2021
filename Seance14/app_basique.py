#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Application permettant la résolution de problème d'ordonnancement.
"""
import typer
from pathlib import Path
from rich.console import Console
from ordonnancement import Probleme, resous


def main(fichier: str):
    """Résout le problème d'ordonnancement décrit dans FICHIER."""
    cs = Console()
    entree = Path(fichier).read_text()
    probleme = Probleme.par_str(entree)
    cs.print(probleme.genere_table())
    cs.print(resous(probleme).genere_table())


if __name__ == "__main__":
    typer.run(main)
