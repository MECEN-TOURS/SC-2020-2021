"""Description.

Module auxiliaire pour la résolution du problème de traversée.
"""

def genere_etats():
    """Genere les etats correspondant au problème de la traversée."""
    resultat = list()
    for choix_berger in COTES:
        for choix_loup in COTES:
            for choix_mouton in COTES:
                for choix_chou in COTES:
                    etat = {
                        "Berger": choix_berger,
                        "Loup": choix_loup,
                        "Mouton": choix_mouton,
                        "Chou": choix_chou
                    }
                    resultat.append(etat)
    return resultat

def est_interdit(etat):
    if etat["Loup"] == etat["Mouton"] and etat["Loup"] != etat["Berger"]:
        return True
    if etat["Mouton"] == etat["Chou"] and etat["Mouton"] != etat["Berger"]:
        return True
    return False

def sont_connectes(etat_depart, etat_arrivee):
    if etat_depart["Berger"] == etat_arrivee["Berger"]:
        return False
    nombre_de_changements = 0
    for personnage in ("Loup", "Mouton", "Chou"):
        if etat_depart[personnage] != etat_arrivee[personnage]:
            nombre_de_changements = nombre_de_changements + 1
    if nombre_de_changements < 2:
        return True
    else:
        return False
    
def genere_graphe():
    sommets = [etat for etat in genere_etats() if not est_interdit(etat)]
    fleches = [
        (etat1, etat2) 
        for etat1 in sommets 
        for etat2 in sommets 
        if sont_connectes(etat1, etat2)
    ]
    return sommets, fleches

def sont_relies(depart, arrivee, graphe):
    sommets, arretes = graphe
    deja_visites = list()
    a_visites = [depart]
    while a_visites:
        sommet_courant = a_visites.pop()
        if sommet_courant == arrivee:
            return True
        if sommet_courant in deja_visites:
            continue
        else:
            deja_visites.append(sommet_courant)
        for sommet_1, sommet_2 in arretes:
            if sommet_1 == sommet_courant:
                a_visites.append(sommet_2)
    return False

assert sont_relies(
    depart="A", 
    arrivee="D", 
    graphe=(
        ["A", "B", "C", "D"], 
        [("A", "B"), ("A", "C"), ("C", "D")]
    )
)

assert not sont_relies(
    depart="A", 
    arrivee="D", 
    graphe=(
        ["A", "B", "C", "D"], 
        [("A", "B"), ("C", "D")]
    )
)

def est_absent(sommet_cherche, arretes):
    for sommet_1, sommet_2 in arretes:
        if sommet_1 == sommet_cherche:
            return False
    return True

def remonte_arbre(depart, arrivee, arbre):
    sommets = list()
    noeud_courant = arrivee
    while noeud_courant != depart:
        for sommet1, sommet2 in arbre:
            if sommet1 == noeud_courant:
                sommets.append(noeud_courant)
                noeud_courant = sommet2

            
    sommets.append(noeud_courant)
    return list(reversed(sommets))

def trouve_chemin(depart, arrivee, graphe):
    sommets, arretes = graphe
    deja_visites = list()
    a_visites = [depart]
    vu_en_premier_par = [(depart, None)]
    while a_visites:
        sommet_courant = a_visites.pop()
        if sommet_courant == arrivee:
            return remonte_arbre(depart, arrivee, vu_en_premier_par)
        if sommet_courant in deja_visites:
            continue
        else:
            deja_visites.append(sommet_courant)
        for sommet_1, sommet_2 in arretes:
            if sommet_1 == sommet_courant:
                a_visites.append(sommet_2)
                if est_absent(sommet_2, vu_en_premier_par):
                    vu_en_premier_par.append((sommet_2, sommet_courant))
                
    return []

assert ["A", "C", "D"] == trouve_chemin(
    depart="A", 
    arrivee="D", 
    graphe=(
        ["A", "B", "C", "D"], 
        [("A", "B"), ("A", "C"), ("C", "D")]
    )
)

assert [] == trouve_chemin(
    depart="A", 
    arrivee="D", 
    graphe=(
        ["A", "B", "C", "D"], 
        [("A", "B"), ("C", "D")]
    )
)

COTES = ("Gauche", "Droite")
PERSONNAGES = ("Berger", "Loup", "Mouton", "Choux")
DEPART = {
    "Berger": "Gauche", 
    "Loup": "Gauche", 
    "Mouton": "Gauche", 
    "Chou": "Gauche"
}
ARRIVEE = {
    "Berger": "Droite", 
    "Loup": "Droite", 
    "Mouton": "Droite", 
    "Chou": "Droite"
}
