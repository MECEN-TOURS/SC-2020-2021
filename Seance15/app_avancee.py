#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Application permettant la résolution de problème d'ordonnancement.
"""
import typer
from sys import stdin
from pathlib import Path
from rich.console import Console
from ordonnancement import Probleme, resous

app = typer.Typer(help="Application résolvant des problèmes d'ordonnancement.")


@app.command("std")
def par_entree_standard():
    """Résout le problème d'ordonnancement à partir de l'entrée standard."""
    cs = Console()
    entree = "".join([ligne for ligne in stdin])
    probleme = Probleme.par_str(entree)
    cs.print(probleme.genere_table())
    cs.print(resous(probleme).genere_table())


@app.command("fch")
def par_fichier(
    fichier: str = typer.Argument(
        ..., help="nom du fichier décrivant le problème"
    )
):
    """Résout le problème d'ordonnancement à patir d'un fichier."""
    cs = Console()
    entree = Path(fichier).read_text()
    probleme = Probleme.par_str(entree)
    cs.print(probleme.genere_table())
    cs.print(resous(probleme).genere_table())


if __name__ == "__main__":
    app()
