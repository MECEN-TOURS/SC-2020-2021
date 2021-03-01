#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Contient la fonction de résolution du problème d'ordonnancement.
"""
from .probleme import Probleme, Tache
from .edt import Activite, EDT, Instant
import networkx as nx


def _genere_graphe(probleme: Probleme) -> nx.DiGraph:
    """Crée le graphe associé au problème."""
    resultat = nx.DiGraph()
    for tache in probleme.taches:
        for prerequis in tache.prerequis:
            resultat.add_edge(prerequis, tache.nom)
    return resultat


def _calcule_demarrage(tache: Tache, edt: EDT) -> Instant:
    """Calcule le plus petit temps ok."""
    fins_prerequis = [edt[prerequis].fin for prerequis in tache.prerequis]
    if fins_prerequis:
        return max(fins_prerequis)
    return 0


def resous(probleme: Probleme) -> EDT:
    """Résout un problème d'ordonnancement.

        Exemple:
    >>> from rich import print
    >>> probleme = Probleme.par_str('''
    ... A / 1 /
    ... B / 2 / A
    ... C / 3 / A B
    ... D / 4 / A
    ... '''
    ... )
    >>> print(probleme.genere_table())
    ┏━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
    ┃ Tache ┃ Durée ┃ Prérequis ┃
    ┡━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
    │ A     │ 1     │           │
    │ B     │ 2     │ A         │
    │ C     │ 3     │ A, B      │
    │ D     │ 4     │ A         │
    └───────┴───────┴───────────┘
    >>> solution = resous(probleme)
    >>> print(solution.genere_table())
    ┏━━━━━━━┳━━━━━━━┳━━━━━┓
    ┃ Tache ┃ Début ┃ Fin ┃
    ┡━━━━━━━╇━━━━━━━╇━━━━━┩
    │ A     │ 0     │ 1   │
    │ D     │ 1     │ 5   │
    │ B     │ 1     │ 3   │
    │ C     │ 3     │ 6   │
    └───────┴───────┴─────┘
    """
    graphe = _genere_graphe(probleme)
    if not nx.is_directed_acyclic_graph(G=graphe):
        raise ValueError("Le problème n'a pas de solution.")
    bon_ordre = [probleme[nom] for nom in nx.topological_sort(G=graphe)]
    resultat = EDT(activites=[])
    for tache_courante in bon_ordre:
        demarrage = _calcule_demarrage(tache=tache_courante, edt=resultat)
        arrivee = demarrage + tache_courante.duree
        resultat.ajoute(
            Activite(
                tache=tache_courante,
                debut=demarrage,
                fin=arrivee,
            )
        )

    return resultat
