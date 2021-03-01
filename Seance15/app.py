"""Description.

Libraire pour un gui de la librairie ordonnancement.
"""
import ipywidgets as ipw
from IPython.display import display
from ordonnancement import Probleme, resous

class Application:
    def __init__(self):
        self.bouton = ipw.Button(description="Résoudre")
        self.zone_entree = ipw.Textarea(value="A / 1 / \nB / 2 / A", layout=ipw.Layout(height="200px"))
        self.zone_probleme = ipw.Output()
        self.zone_solution = ipw.Output()
        self.total = ipw.HBox(
                [
                    ipw.VBox([self.bouton, self.zone_entree]),
                    self.zone_probleme,
                    self.zone_solution
                ]
        )
        self._sur_clique(self.bouton)
        self.bouton.on_click(self._sur_clique)
        
    def affichage(self):    
        display(self.total)
    
    def _sur_clique(self, b):
        self.zone_probleme.clear_output()
        self.zone_solution.clear_output()
        probleme = Probleme.par_str(self.zone_entree.value)
        solution = resous(probleme)
        with self.zone_probleme:
            display(probleme.genere_table())
        with self.zone_solution:
            display(solution.genere_table())