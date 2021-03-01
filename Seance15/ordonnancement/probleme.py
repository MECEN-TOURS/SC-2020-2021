#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Classes Tache et Probleme permettant de décrire le problème d'ordonnancement.
TODO:
    - Refactor _est_valide pour avoir des exceptions directement dans __init__
"""
from typing import Any, Dict, List, Union, Generator
from dataclasses import dataclass
from rich.table import Table

Duree = Union[int, float]
Nom = str


@dataclass
class Tache:
    """Représente une tâche."""

    nom: Nom
    duree: Duree
    prerequis: List[Nom]

    def __post_init__(self):
        """Vérifie que la durée est positive."""
        if self.duree < 0:
            raise ValueError("La durée doit être positive.")


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
    >>> probleme_bis.affiche()
    ┏━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
    ┃ Tache ┃ Durée ┃ Prérequis ┃
    ┡━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
    │ A     │ 1     │           │
    │ B     │ 2     │ A         │
    │ C     │ 3     │ A, B      │
    │ D     │ 4     │ A         │
    └───────┴───────┴───────────┘
    >>> from rich import print
    >>> print(probleme_bis.genere_table())
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

    def genere_table(self) -> Table:
        """Renvoie une table rich."""
        resultat = Table(title="Problème d'ordonnancement")
        resultat.add_column("Tache")
        resultat.add_column("Durée")
        resultat.add_column("Prérequis")
        for tache in self.taches:
            resultat.add_row(
                tache.nom, str(tache.duree), str(", ".join(tache.prerequis))
            )

        return resultat

    def affiche(self):
        """Affiche la table directement."""
        from rich import print

        print(self.genere_table())