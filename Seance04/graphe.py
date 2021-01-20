"""Description.

Librairie implémentant un graphe "abstrait" et les algorithmes de recherches de chemin.
"""
from typing import List
from collections import deque

class Graphe:
    def __init__(self, sommets, arretes):
        self.sommets = sommets
        self.arretes = arretes
        
    def __repr__(self):
        return f"Graphe(sommets={self.sommets}, arretes={self.arretes})"
    
    def __str__(self):
        return f"""
Sommets:
    {self.sommets}
    
Arretes:
    {self.arretes}
"""
        

def sont_relies(depart: "Sommet", arrivee: "Sommet", graphe: Graphe) -> bool:
    """Décide si un chemin du graphe relie les deux états."""
    deja_visites = set()
    a_visites = [depart]
    while a_visites:
        sommet_courant = a_visites.pop()
        if sommet_courant == arrivee:
            return True
        if sommet_courant in deja_visites:
            continue
        else:
            deja_visites.add(sommet_courant)
        print(sommet_courant)
        for sommet_1, sommet_2 in graphe.arretes:
            if sommet_1 == sommet_courant:
                a_visites.append(sommet_2)
    return False

def sont_relies_v2(depart: "Sommet", arrivee: "Sommet", graphe: Graphe) -> bool:
    """Décide si un chemin du graphe relie les deux états."""
    deja_visites = set()
    a_visites = deque([depart])
    while a_visites:
        sommet_courant = a_visites.popleft()
        if sommet_courant == arrivee:
            return True
        if sommet_courant in deja_visites:
            continue
        else:
            deja_visites.add(sommet_courant)
        print(sommet_courant)
        for sommet_1, sommet_2 in graphe.arretes:
            if sommet_1 == sommet_courant:
                a_visites.append(sommet_2)
    return False

def __est_absent(sommet_cherche: "Sommet", arretes: List["Arrete"]) -> bool:
    """Décide si le sommet apparaît comme origine d'une des arrêtes."""
    for sommet_1, sommet_2 in arretes:
        if sommet_1 == sommet_cherche:
            return False
    return True

def __remonte_arbre(depart: "Sommet", arrivee: "Sommet", arbre: List["Arrete"]) -> "Chemin":
    """Génère un chemin entre depart et arrivee utilisant les arrêtes de l'arbre.
    """
    sommets = list()
    noeud_courant = arrivee
    while noeud_courant != depart:
        for sommet1, sommet2 in arbre:
            if sommet1 == noeud_courant:
                sommets.append(noeud_courant)
                noeud_courant = sommet2

    sommets.append(noeud_courant)
    return list(reversed(sommets))

def trouve_chemin(depart: "Sommet", arrivee: "Sommet", graphe: Graphe) -> "Chemin":
    """Renvoie un chemin reliant depart et arrivee à travers le graphe.

    Renvoie la liste vide si il n'existe pas de tel chemin.
    """
    deja_visites = list()
    a_visites = [depart]
    vu_en_premier_par = [(depart, None)]
    while a_visites:
        sommet_courant = a_visites.pop()
        if sommet_courant == arrivee:
            return __remonte_arbre(depart, arrivee, vu_en_premier_par)
        if sommet_courant in deja_visites:
            continue
        else:
            deja_visites.append(sommet_courant)
        for sommet_1, sommet_2 in graphe.arretes:
            if sommet_1 == sommet_courant:
                a_visites.append(sommet_2)
                if __est_absent(sommet_2, vu_en_premier_par):
                    vu_en_premier_par.append((sommet_2, sommet_courant))

    return []

