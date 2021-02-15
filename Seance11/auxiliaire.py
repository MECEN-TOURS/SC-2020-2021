"""Description.

Librairie de fonctions pour le preprocessing du discours de Kennedy.

>>> Texte = '''
... Motun, motdeux
... mottrois, motQuatre; 
... 'motcinq'
... '''
>>> genere_liste_mots(Texte)
['motun', 'motdeux', 'mottrois', 'motquatre', 'motcinq']
"""
from typing import List

def enleve_sauts_de_ligne(texte: str) -> str:
    """Enleve les \n.
    
    TODO: EXEMPLE
    """
    return texte.strip().replace("\n", " ")

def convertit_majuscules(texte: str) -> str:
    """Transforme les majuscules en minuscules.
        
    TODO: EXEMPLE
    """
    return texte.lower()

def remplace_caracteres_speciaux(texte: str) -> str:
    """Remplace les non minuscules par des espaces.
    
        
    TODO: EXEMPLE
    """
    autorises = set("abcdefghijklmnopqrstuvwxyz")
    resultat = list()
    for caractere in texte:
        if caractere in autorises:
            resultat.append(caractere)
        else:
            resultat.append(" ")
    return "".join(resultat)
    
def reduit_espaces(texte: str) -> str:
    """Remplace les suites d'espaces par un seul espace.
    
        
    TODO: EXEMPLE
    """
    resultat = list()
    for caractere in texte:
        if caractere != " ":
            resultat.append(caractere)
        else:
            try:
                if resultat[-1] != " ":
                    resultat.append(caractere)
            except IndexError:
                resultat.append(caractere)
    return "".join(resultat)
    
def genere_liste_mots(texte: str) -> List[str]:
    """Génère la liste des mots.
    
        
    TODO: EXEMPLE
    """
    sur_une_ligne = enleve_sauts_de_ligne(texte)
    en_minuscule = convertit_majuscules(sur_une_ligne)
    sans_speciaux = remplace_caracteres_speciaux(en_minuscule)
    un_seul_espace = reduit_espaces(sans_speciaux)
    return un_seul_espace.strip().split(" ")