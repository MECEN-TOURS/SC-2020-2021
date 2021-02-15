"""Description.

Librairie de fonctions pour le preprocessing du discours de Kennedy.
"""

def enleve_sauts_de_ligne(texte: str) -> str:
    """Enleve les \n"""
    return texte.strip().replace("\n", " ")

def convertit_majuscules(texte: str) -> str:
    """Transforme les majuscules en minuscules."""
    ...