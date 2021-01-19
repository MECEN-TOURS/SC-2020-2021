"""Description.

Module auxiliaire pour la résolution du problème de traversée.
"""
import copy
from typing import Callable, Dict, List, Literal, Tuple, NewType

Cote = Literal["Gauche", "Droite"]
Personnage = Literal["Berger", "Loup", "Mouton", "Choux"]
Etat = NewType("Etat", Dict[Personnage, Cote])
Chemin = NewType("Chemin", List[Etat])
Arrete = NewType("Arrete", Tuple[Etat, Etat])
Graphe = NewType("Graphe", Tuple[List[Etat], List[Arrete]])

COTES: List[Cote] = ["Gauche", "Droite"]
PERSONNAGES: List[Personnage] = ["Berger", "Loup", "Mouton", "Choux"]

DEPART = Etat(
    {"Berger": "Gauche", "Loup": "Gauche", "Mouton": "Gauche", "Choux": "Gauche"}
)
ARRIVEE = Etat(
    {"Berger": "Droite", "Loup": "Droite", "Mouton": "Droite", "Choux": "Droite"}
)


def est_valide(etat: Etat) -> bool:
    """Fonction implémentant la règle Loup/Mouton Mouton/Chou.

    Exemples:
    >>> est_valide({"Berger": "Gauche", "Loup": "Gauche", "Mouton": "Gauche", "Choux": "Gauche"})
    True
    >>> est_valide({"Berger": "Gauche", "Loup": "Droite", "Mouton": "Droite", "Choux": "Gauche"})
    False"""
    if etat["Loup"] == etat["Mouton"] and etat["Loup"] != etat["Berger"]:
        return False
    if etat["Mouton"] == etat["Choux"] and etat["Mouton"] != etat["Berger"]:
        return False
    return True


assert est_valide(DEPART)
assert not est_valide(
    Etat({"Berger": "Gauche", "Loup": "Droite", "Mouton": "Droite", "Choux": "Gauche"})
)
assert not est_valide(
    Etat({"Berger": "Gauche", "Loup": "Gauche", "Mouton": "Droite", "Choux": "Droite"})
)


def sont_connectes(etat_depart: Etat, etat_arrivee: Etat) -> bool:
    """Décide si deux états forment une arrête.

    Exemples:
    >>> sont_connectes(
    ...     etat_depart={
    ...         "Berger": "Gauche",
    ...         "Loup": "Gauche",
    ...         "Mouton": "Droite",
    ...         "Choux": "Droite"
    ...     },
    ...     etat_arrivee={
    ...         "Berger": "Droite",
    ...         "Loup": "Gauche",
    ...         "Mouton": "Droite",
    ...         "Choux": "Droite"
    ...     }
        ... )
    True
    >>> sont_connectes(
    ...     etat_depart={
    ...         "Berger": "Gauche",
    ...         "Loup": "Gauche",
    ...         "Mouton": "Droite",
    ...         "Choux": "Droite"
    ...     },
    ...     etat_arrivee={
    ...         "Berger": "Droite",
    ...         "Loup": "Droite",
    ...         "Mouton": "Droite",
    ...         "Choux": "Droite"
    ...     }
    ... )
    True
    >>> sont_connectes(
    ...     etat_depart={
    ...         "Berger": "Gauche",
    ...         "Loup": "Gauche",
    ...         "Mouton": "Droite",
    ...         "Choux": "Droite"
    ...     },
    ...     etat_arrivee={
    ...         "Berger": "Droite",
    ...         "Loup": "Gauche",
    ...         "Mouton": "Gauche",
    ...         "Choux": "Droite"
    ...     }
    ... )
    False"""
    if etat_depart["Berger"] == etat_arrivee["Berger"]:
        return False
    nombre_de_changements = 0
    for personnage in PERSONNAGES:
        if etat_depart[personnage] != etat_arrivee[personnage]:
            nombre_de_changements = nombre_de_changements + 1
            personnage_changeant_de_cote = personnage
    if nombre_de_changements == 1:
        return True
    elif nombre_de_changements == 2:
        return etat_depart["Berger"] == etat_depart[personnage_changeant_de_cote]
    else:
        return False


assert sont_connectes(
    etat_depart=Etat(
        {
            "Berger": "Gauche",
            "Loup": "Gauche",
            "Mouton": "Droite",
            "Choux": "Droite",
        }
    ),
    etat_arrivee=Etat(
        {
            "Berger": "Droite",
            "Loup": "Gauche",
            "Mouton": "Droite",
            "Choux": "Droite",
        }
    ),
)
assert sont_connectes(
    etat_depart=Etat(
        {
            "Berger": "Gauche",
            "Loup": "Gauche",
            "Mouton": "Droite",
            "Choux": "Droite",
        }
    ),
    etat_arrivee=Etat(
        {
            "Berger": "Droite",
            "Loup": "Droite",
            "Mouton": "Droite",
            "Choux": "Droite",
        }
    ),
)
assert not sont_connectes(
    etat_depart=Etat(
        {
            "Berger": "Gauche",
            "Loup": "Gauche",
            "Mouton": "Droite",
            "Choux": "Droite",
        }
    ),
    etat_arrivee=Etat(
        {
            "Berger": "Droite",
            "Loup": "Gauche",
            "Mouton": "Gauche",
            "Choux": "Droite",
        }
    ),
)


def genere_etats(clefs: List[Personnage], valeurs: List[Cote]) -> List[Etat]:
    """Genere les etats correspondant au problème de la traversée.

Exemples:
>>> genere_etats(clefs=["Berger", "Loup"], valeurs=["Gauche", "Droite"])
[
    {'Berger': 'Gauche', 'Loup': 'Gauche'},
    {'Berger': 'Gauche', 'Loup': 'Droite'},
    {'Berger': 'Droite', 'Loup': 'Gauche'},
    {'Berger': 'Droite', 'Loup': 'Droite'}
]
"""
    if not clefs:
        vide: Etat = Etat({})
        return [vide]
    else:
        intermediaire = genere_etats(clefs=clefs[:-1], valeurs=valeurs)
        resultat = list()
        for etat in intermediaire:
            for valeur in valeurs:
                nouveau = copy.deepcopy(etat)
                nouveau[clefs[-1]] = valeur
                resultat.append(nouveau)
        return resultat




assert genere_etats(clefs=["Berger", "Loup"], valeurs=["Gauche", "Droite"]) == [
    {"Berger": "Gauche", "Loup": "Gauche"},
    {"Berger": "Gauche", "Loup": "Droite"},
    {"Berger": "Droite", "Loup": "Gauche"},
    {"Berger": "Droite", "Loup": "Droite"},
]

SOMMETS = [ etat for etat in genere_etats(clefs=PERSONNAGES, valeurs=COTES) if est_valide(etat)]


def genere_graphe(sommets: List[Etat], contraintes=List[Callable]) -> Graphe:
    """Renvoie le graphe associé au problème.

Exemple:
>>> genere_graphe(sommets=[DEPART, ARRIVEE], contraintes=[lambda e1, e2: e1 != e2])
(
    [
        {'Berger': 'Gauche', 'Loup': 'Gauche', 'Mouton': 'Gauche', 'Choux': 'Gauche'},
        {'Berger': 'Droite', 'Loup': 'Droite', 'Mouton': 'Droite', 'Choux': 'Droite'}
    ],
    [
        (
            {'Berger': 'Gauche', 'Loup': 'Gauche', 'Mouton': 'Gauche', 'Choux': 'Gauche'},
            {'Berger': 'Droite', 'Loup': 'Droite', 'Mouton': 'Droite', 'Choux': 'Droite'},
        ),
        (
            {'Berger': 'Droite', 'Loup': 'Droite', 'Mouton': 'Droite', 'Choux': 'Droite'},
            {'Berger': 'Gauche', 'Loup': 'Gauche', 'Mouton': 'Gauche', 'Choux': 'Gauche'},
        )
    ]
)
    """
    fleches = [
        Arrete((etat1, etat2))
        for etat1 in sommets
        for etat2 in sommets
        if all(contrainte(etat1, etat2) for contrainte in contraintes)
    ]
    return Graphe((sommets, fleches))

assert (genere_graphe(sommets=[DEPART, ARRIVEE], contraintes=[lambda e1, e2: e1 != e2])
        ==
(
    [
        {'Berger': 'Gauche', 'Loup': 'Gauche', 'Mouton': 'Gauche', 'Choux': 'Gauche'},
        {'Berger': 'Droite', 'Loup': 'Droite', 'Mouton': 'Droite', 'Choux': 'Droite'}
    ],
    [
        (
            {'Berger': 'Gauche', 'Loup': 'Gauche', 'Mouton': 'Gauche', 'Choux': 'Gauche'},
            {'Berger': 'Droite', 'Loup': 'Droite', 'Mouton': 'Droite', 'Choux': 'Droite'},
        ),
        (
            {'Berger': 'Droite', 'Loup': 'Droite', 'Mouton': 'Droite', 'Choux': 'Droite'},
            {'Berger': 'Gauche', 'Loup': 'Gauche', 'Mouton': 'Gauche', 'Choux': 'Gauche'}
        )
    ]
)
)


GRAPHE = genere_graphe(sommets=SOMMETS, contraintes=[sont_connectes])


def sont_relies(depart: Etat, arrivee: Etat, graphe: Graphe) -> bool:
    """Décide si un chemin du graphe relie les deux états.

    Exemples:
    >>> sont_relies(
    ...     depart="A",
    ...     arrivee="D",
    ...     graphe=(
    ...         ["A", "B", "C", "D"],
    ...         [("A", "B"), ("A", "C"), ("C", "D")]
    ...     )
    ... )
    True
    >>> sont_relies(
    ...     depart="A",
    ...     arrivee="D",
    ...     graphe=(
    ...         ["A", "B", "C", "D"],
    ...         [("A", "B"), ("C", "D")]
    ...     )
    ... )
    False"""
    _, arretes = graphe
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


def test_sont_relies():
    """Test sur deux cas particuliers la fonction."""
    a, b, c, d = GRAPHE[0][:4]
    resultat1 = sont_relies(
        depart=a,
        arrivee=d,
        graphe=Graphe(
            (
                [a, b, c, d],
                [Arrete((a, b)), Arrete((a, c)), Arrete((c, d))],
            )
        ),
    )

    resultat2 = not sont_relies(
        depart=a,
        arrivee=d,
        graphe=Graphe(([a, b, c, d], [Arrete((a, b)), Arrete((c, d))])),
    )
    return resultat1 and resultat2


assert test_sont_relies()


def est_absent(sommet_cherche: Etat, arretes: List[Arrete]) -> bool:
    """Décide si le sommet apparaît comme origine d'une des arrêtes.

    Exemples:
    >>> est_absent(
    ...     sommet_cherche="A",
    ...     arretes=[("A", "B"), ("B", "C"), ("C", "D")]
    ... )
    False
    >>> est_absent(
    ...     sommet_cherche="A",
    ...     arretes=[("B", "C"), ("C", "D"), ("A", "B")]
    ... )
    False
    >>> est_absent(
    ...     sommet_cherche="D",
    ...     arretes=[("B", "C"), ("C", "D"), ("A", "B")]
    ... )
    True"""
    for sommet_1, sommet_2 in arretes:
        if sommet_1 == sommet_cherche:
            return False
    return True


def test_est_absent():
    """Test sur trois cas particuliers la fonction."""
    a, b, c, d = GRAPHE[0][:4]
    resultat1 = not est_absent(
        sommet_cherche=a, arretes=[Arrete((a, b)), Arrete((b, c)), Arrete((c, d))]
    )

    resultat2 = not est_absent(
        sommet_cherche=a, arretes=[Arrete((b, c)), Arrete((c, d)), Arrete((a, b))]
    )

    resultat3 = est_absent(
        sommet_cherche=d, arretes=[Arrete((a, b)), Arrete((b, c)), Arrete((c, d))]
    )
    return resultat1 and resultat2 and resultat3


assert test_est_absent()


def remonte_arbre(depart: Etat, arrivee: Etat, arbre: List[Arrete]) -> Chemin:
    """Génère un chemin entre depart et arrivee utilisant les arrêtes de l'arbre.

    Exemple:
    >>> remonte_arbre(
    ...     depart="D",
    ...     arrivee="A",
    ...     arbre=[("A", "B"), ("B", "C"), ("C", "D")]
    ... )
    ['D', 'C', 'B', 'A']
    """
    sommets = list()
    noeud_courant = arrivee
    while noeud_courant != depart:
        for sommet1, sommet2 in arbre:
            if sommet1 == noeud_courant:
                sommets.append(noeud_courant)
                noeud_courant = sommet2

    sommets.append(noeud_courant)
    return Chemin(list(reversed(sommets)))


def test_remonte_arbre():
    """Test sur trois cas particuliers la fonction."""
    a, b, c, d = GRAPHE[0][:4]
    resultat = remonte_arbre(
        depart=d, arrivee=a, arbre=[Arrete((a, b)), Arrete((b, c)), Arrete((c, d))]
    )
    return resultat == Chemin([d, c, b, a])


assert test_remonte_arbre()


def trouve_chemin(depart: Etat, arrivee: Etat, graphe: Graphe) -> Chemin:
    """Renvoie un chemin reliant depart et arrivee à travers le graphe.

    Renvoie la liste vide si il n'existe pas de tel chemin.

    Exemples:
    >>> trouve_chemin(
    ...     depart="A",
    ...     arrivee="D",
    ...     graphe=(
    ...         ["A", "B", "C", "D"],
    ...         [("A", "B"), ("A", "C"), ("C", "D")]
    ...     )
    ... )
    ['A', 'C', 'D']
    >>> trouve_chemin(
    ...     depart="A",
    ...     arrivee="D",
    ...     graphe=(
    ...         ["A", "B", "C", "D"],
    ...         [("A", "B"), ("C", "D")]
    ...     )
    ... )
    []
    """
    sommets, arretes = graphe
    deja_visites = list()
    a_visites = [depart]
    vu_en_premier_par = [Arrete((depart, None))]
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
                    vu_en_premier_par.append(Arrete((sommet_2, sommet_courant)))

    return Chemin([])


def test_trouve_chemin():
    """Test sur deux cas particuliers la fonction."""
    a, b, c, d = GRAPHE[0][:4]
    resultat1 = trouve_chemin(depart=a, arrivee=d, graphe=Graphe(([a,b,c,d], [Arrete((a,b)), Arrete((a, c)), Arrete((c, d))]))) == Chemin([a, c, d])
    resultat2 = trouve_chemin(depart=a, arrivee=d, graphe=Graphe(([a,b,c,d], [Arrete((a,b)), Arrete((c, d))]))) == Chemin([])
    return resultat1 and resultat2

assert test_trouve_chemin()
