#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Contient les classes Activite et EDT.
TODO:
    - Tester complètement y compris mutations?
    - Documenter l'interface publique?
    - La vérifiction de la durée de l'activité par rapport aux tâches est plutôt du ressort de Activite que de celui de EDT?
"""
from typing import Any, List, Union, Generator
from dataclasses import dataclass
from rich.table import Table
from .probleme import Nom, Tache

Instant = Union[int, float]


@dataclass
class Activite:
    """Tache plannifiée."""

    tache: Tache
    debut: Instant
    fin: Instant

    def __post_init__(self):
        """Vérifie que la durée est respectée."""
        if self.fin - self.debut < self.tache.duree:
            raise ValueError(
                "L'activité correspondant à la tache {self.tache} ne respecte pas la durée."
            )


class EDT:
    """Emploi du temps.

        Exemple:
    >>> edt = EDT(
    ...     activites=[
    ...         Activite(tache=Tache(nom="A", duree=1, prerequis=[]), debut=0, fin=1),
    ...         Activite(tache=Tache(nom="B", duree=2, prerequis=["A"]), debut=1, fin=3),
    ...         Activite(tache=Tache(nom="C", duree=3, prerequis=["A", "B"]), debut=3, fin=6),
    ...         Activite(tache=Tache(nom="D", duree=4, prerequis=["A"]), debut=1, fin=5),
    ...     ]
    ... )
    >>> edt
    EDT(activites=[Activite(tache=Tache(nom='A', duree=1, prerequis=[]), debut=0, fin=1), Activ
    ite(tache=Tache(nom='B', duree=2, prerequis=['A']), debut=1, fin=3), Activite(tache=Tache(n
    om='C', duree=3, prerequis=['A', 'B']), debut=3, fin=6), Activite(tache=Tache(nom='D', dure
    e=4, prerequis=['A']), debut=1, fin=5)])
    >>> for activite in edt.activites:
    ...     print(activite)
    ...
    ...
    Activite(tache=Tache(nom='A', duree=1, prerequis=[]), debut=0, fin=1)
    Activite(tache=Tache(nom='B', duree=2, prerequis=['A']), debut=1, fin=3)
    Activite(tache=Tache(nom='C', duree=3, prerequis=['A', 'B']), debut=3, fin=6)
    Activite(tache=Tache(nom='D', duree=4, prerequis=['A']), debut=1, fin=5)
    >>> edt["A"]
    Activite(tache=Tache(nom='A', duree=1, prerequis=[]), debut=0, fin=1)
    >>> edt_bis = EDT([])
    >>> edt_bis.ajoute(Activite(tache=Tache(nom="A", duree=1, prerequis=[]), debut=0, fin=1))
    >>> edt_bis.ajoute(Activite(tache=Tache(nom="B", duree=2, prerequis=["A"]), debut=1, fin=3)
    )
    >>> edt_bis.ajoute(Activite(tache=Tache(nom="C", duree=3, prerequis=["A", "B"]), debut=3, f
    in=6))
    >>> edt_bis.ajoute(Activite(tache=Tache(nom="D", duree=4, prerequis=["A"]), debut=1, fin=5)
    )
    >>> edt_bis
    EDT(activites=[Activite(tache=Tache(nom='A', duree=1, prerequis=[]), debut=0, fin=1), Activ
    ite(tache=Tache(nom='B', duree=2, prerequis=['A']), debut=1, fin=3), Activite(tache=Tache(n
    om='C', duree=3, prerequis=['A', 'B']), debut=3, fin=6), Activite(tache=Tache(nom='D', dure
    e=4, prerequis=['A']), debut=1, fin=5)])
    >>> edt == edt_bis
    True
    >>> edt.affiche()
    ┏━━━━━━━┳━━━━━━━┳━━━━━┓
    ┃ Tache ┃ Début ┃ Fin ┃
    ┡━━━━━━━╇━━━━━━━╇━━━━━┩
    │ A     │ 0     │ 1   │
    │ B     │ 1     │ 3   │
    │ C     │ 3     │ 6   │
    │ D     │ 1     │ 5   │
    └───────┴───────┴─────┘
    >>> edt_bis.ajoute(Activite(tache=Tache(nom="A", duree=5, prerequis=[]), debut=6, fin=11)
    ... )
    ValueError: La tache A est déjà présente dans l'emploi du temps.
    >>> edt.ajoute(Activite(tache=Tache("E", duree=4, prerequis=["D"]), debut=5, fin=8))
    ValueError: Le début et la fin ne sont pas compatibles avec la durée de l'activité Activite(tache=Tache(nom='E', duree=4, prerequis=['D']), debut=5, fin=8)
    >>> from rich import print
    >>> print(edt_bis.genere_table())
    ┏━━━━━━━┳━━━━━━━┳━━━━━┓
    ┃ Tache ┃ Début ┃ Fin ┃
    ┡━━━━━━━╇━━━━━━━╇━━━━━┩
    │ A     │ 0     │ 1   │
    │ B     │ 1     │ 3   │
    │ C     │ 3     │ 6   │
    │ D     │ 1     │ 5   │
    └───────┴───────┴─────┘
    >>> edt_bis.est_valide()
    True
    >>> edt_bis.ajoute(Activite(tache=Tache(nom="E", duree=5, prerequis=["D"]), debut=4, fin=9)
    )
    >>> edt_bis.affiche()
    ┏━━━━━━━┳━━━━━━━┳━━━━━┓
    ┃ Tache ┃ Début ┃ Fin ┃
    ┡━━━━━━━╇━━━━━━━╇━━━━━┩
    │ A     │ 0     │ 1   │
    │ B     │ 1     │ 3   │
    │ C     │ 3     │ 6   │
    │ D     │ 1     │ 5   │
    │ E     │ 4     │ 9   │
    └───────┴───────┴─────┘
    >>> edt_bis.est_valide()
    False
    """

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

    def genere_table(self) -> Table:
        """Retourn une table rich."""
        resultat = Table(title="Solution du problème")
        resultat.add_column("Tache")
        resultat.add_column("Début")
        resultat.add_column("Fin")
        for activite in self._activites:
            resultat.add_row(
                activite.tache.nom, str(activite.debut), str(activite.fin)
            )

        return resultat

    def affiche(self):
        """Affiche la table."""
        from rich import print

        print(self.genere_table())
