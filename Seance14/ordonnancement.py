#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Classes pour résoudre des problèmes d'ordonnancement.

TODO:
    - Tester complètement y compris mutations?
    - Refactor de la fonction de résolution?
    - Refactor _est_valide pour avoir des exception directement dans __init__
    - Documenter l'interface publique?
    - La vérifiction de la durée de l'activité par rapport aux tâches est plutôt du ressort de Activite que de celui de EDT?
"""
import networkx as nx
from typing import Any, Dict, List, Union, Generator
from dataclasses import dataclass
from rich.table import Table

Duree = Union[int, float]
Instant = Union[int, float]
Nom = str


@dataclass
class Tache:
    """Représente une tâche."""

    nom: Nom
    duree: Duree
    prerequis: List[Nom]


class Probleme:
    """Représente un problème d'ordonnancement.

    Exemple:
    >>> probleme = Probleme(
    ...     taches=[
    ...             Tache(nom="A", duree=1, prerequis=[]),
    ...             Tache(nom="B", duree=2, prerequis=["A"]),
    ...             Tache(nom="C", duree=3, prerequis=["A", "B"]),
    ...             Tache(nom="D", duree=4, prerequis=["A"]),
    ...     ]
    ... )
    >>> probleme
    Probleme(taches=[Tache(nom='A', duree=1, prerequis=[]), Tache(nom='B', duree=2, prerequis=['A']), Tache(nom='C', duree=3, prerequis=['A', 'B']), Tache(nom='D', duree=4, prerequis=['A'])])
    >>> print(probleme)
    Tache(nom='A', duree=1, prerequis=[])
    Tache(nom='B', duree=2, prerequis=['A'])
    Tache(nom='C', duree=3, prerequis=['A', 'B'])
    Tache(nom='D', duree=4, prerequis=['A'])
    >>> for tache in probleme.taches:
    ...     print(tache)
    ...
    Tache(nom='A', duree=1, prerequis=[])
    Tache(nom='B', duree=2, prerequis=['A'])
    Tache(nom='C', duree=3, prerequis=['A', 'B'])
    Tache(nom='D', duree=4, prerequis=['A'])
    >>> for nom in probleme.noms:
    ...     print(nom)
    ...
    A
    B
    C
    D
    >>> probleme["A"]
    Tache(nom='A', duree=1, prerequis=[])
    >>> probleme_bis = Probleme.par_str('''
    ... A / 1 /
    ... B / 2 / A
    ... C / 3 / A B
    ... D / 4 / A
    ... '''
    ... )
    >>> probleme_bis
    Probleme(taches=[Tache(nom='A', duree=1, prerequis=[]), Tache(nom='B', duree=2, prerequis=['A']), Tache(nom='C', duree=3, prerequis=['A', 'B']), Tache(nom='D', duree=4, prerequis=['A'])])
    >>> probleme == probleme_bis
    True
    >>> from rich import print
    >>> print(probleme_bis.affiche())
    ┏━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
    ┃ Tache ┃ Durée ┃ Prérequis ┃
    ┡━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
    │ A     │ 1     │           │
    │ B     │ 2     │ A         │
    │ C     │ 3     │ A, B      │
    │ D     │ 4     │ A         │
    └───────┴───────┴───────────┘
    """

    def __init__(self, taches: List[Tache]):
        """Stocke la liste des tâches sous forme de dictionnaire."""
        self._taches: Dict[Nom, Tache] = dict()
        for tache in taches:
            if tache.nom in self._taches:
                raise ValueError(f"{tache.nom} est présente deux fois!")
            self._taches[tache.nom] = tache

        self._est_valide()

    @staticmethod
    def _encode(ligne) -> Tache:
        """Encode une ligne en tache."""
        nom, duree, prerequis = ligne.split("/")
        nom_valide = nom.strip()
        try:
            duree_valide: Duree = int(duree.strip())
        except ValueError:
            duree_valide = float(duree.strip())
        prerequis_valide = prerequis.split()
        return Tache(
            nom=nom_valide, duree=duree_valide, prerequis=prerequis_valide
        )

    @classmethod
    def par_str(cls, message: str) -> "Probleme":
        """Constructeur alternatif."""
        taches = list()
        for ligne in message.strip().splitlines():
            taches.append(cls._encode(ligne))

        return cls(taches)

    @property
    def taches(self) -> Generator[Tache, None, None]:
        """Itére sur les tâches."""
        yield from self._taches.values()

    @property
    def noms(self) -> Generator[Nom, None, None]:
        """Itère sur les noms des tâches."""
        yield from self._taches.keys()

    def _est_valide(self):
        """Vérifie que toutes les tâches dans les prérequis existent."""
        for tache in self.taches:
            for nom in tache.prerequis:
                if nom not in self._taches:
                    raise ValueError(f"{nom} n'est pas une tâche existante.")

    def __eq__(self, autre: Any) -> bool:
        """Egalite."""
        if type(autre) != type(self):
            return False
        return self._taches == autre._taches

    def __repr__(self) -> str:
        """Renvoie la liste de construction."""
        return f"Probleme(taches={list(self.taches) !r})"

    def __str__(self) -> str:
        """Affiche les tâches par ligne."""
        return "\n".join(repr(tache) for tache in self.taches)

    def __getitem__(self, nom: Nom) -> Tache:
        """Accès aux tâches par leurs noms."""
        return self._taches[nom]

    def affiche(self) -> Table:
        """Renvoie une table rich."""
        resultat = Table()
        resultat.add_column("Tache")
        resultat.add_column("Durée")
        resultat.add_column("Prérequis")
        for tache in self.taches:
            resultat.add_row(
                tache.nom, str(tache.duree), str(", ".join(tache.prerequis))
            )

        return resultat


@dataclass
class Activite:
    """Tache plannifiée."""

    tache: Tache
    debut: Instant
    fin: Instant


class EDT:
    """Emploi du temps."""

    def __init__(self, activites: List[Activite]):
        """Instancie à partir de la liste d'activites."""
        self._activites: List[Activite] = []
        for activite in activites:
            self.ajoute(activite)

    def __eq__(self, autre: Any) -> bool:
        """Pour ne pas tester l'identité."""
        if type(autre) != type(self):
            return False
        return self._activites == autre._activites

    def __repr__(self) -> str:
        """Repr."""
        return f"EDT(activites={self._activites})"

    @property
    def activites(self) -> Generator[Activite, None, None]:
        """ITérateur."""
        yield from self._activites

    def __getitem__(self, nom: Nom) -> Activite:
        """Accède aux activités par leur nom de tâche."""
        for activite in self._activites:
            if activite.tache.nom == nom:
                return activite

        raise ValueError("Pas d'activité avec ce nom de tâche.")

    def ajoute(self, activite: Activite):
        """Rajoute une nouvelle activité."""
        if activite.tache.duree > activite.fin - activite.debut:
            raise ValueError(
                "Le début et la fin ne sont pas compatibles avec la"
                f" durée de l'activité f{activite}"
            )
        if any(
            activite.tache.nom == autre.tache.nom for autre in self.activites
        ):
            raise ValueError(
                f"La tache {activite.tache.nom} est déjà présente "
                "dans l'emploi du temps."
            )
        self._activites.append(activite)

    def est_valide(self) -> bool:
        """Vérifie si l'emploi du temps respecte les contraintes."""
        for activite in self.activites:
            for prerequis in activite.tache.prerequis:
                if activite.debut < self[prerequis].fin:
                    return False
        return True

    def affiche(self) -> Table:
        """Retourn une table rich."""
        resultat = Table()
        resultat.add_column("Tache")
        resultat.add_column("Début")
        resultat.add_column("Fin")
        for activite in self._activites:
            resultat.add_row(
                activite.tache.nom, str(activite.debut), str(activite.fin)
            )

        return resultat


def _genere_graphe(probleme: Probleme) -> nx.DiGraph:
    """Crée le graphe associé au problème."""
    resultat = nx.DiGraph()
    for tache in probleme.taches:
        for prerequis in tache.prerequis:
            resultat.add_edge(tache.nom, prerequis)
    return resultat


def resous(probleme: Probleme) -> EDT:
    """Résout un problème d'ordonnancement."""
    graphe = _genere_graphe(probleme)
    if not nx.is_directed_acyclic_graph(G=graphe):
        raise ValueError("Le problème n'a pas de solution.")
    bon_ordre = [probleme[nom] for nom in nx.topological_sort(G=graphe)]
    resultat = EDT(activites=[])
    for tache_courante in bon_ordre:
        demarrage = max(
            resultat[prerequis].fin for prerequis in tache_courante.prerequis
        )
        arrivee = demarrage + tache_courante.duree
        resultat.ajoute(
            Activite(
                tache=tache_courante,
                debut=demarrage,
                fin=arrivee,
            )
        )

    return resultat
