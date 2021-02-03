# Graphes pondérés

## Définitions

- Un graphe $(S, A)$ est dit pondéré lorsqu'on a une fonction $\pi:A \to \mathbb{R}$.
- On dit qu'il est pondéré positivement si la fonction $\pi$ est à valeurs positives.
- Si on a un graphe pondéré positivement on introduit la distance $d$ sur $S^2$ par
$$
\forall (S_1, S_2)\in S^2,\quad d(S_1, S_2):= \underset{(x_0,x_1,...,x_n)\in S^{n+1}}{\min}\sum_{i=1}^n \pi((x_{i-1}, x_i)) \quad \text{ avec } 
\begin{cases}
x_0=S_1\\
x_n=S_2\\
\forall i \in \{1,...,n\},\quad (x_{i-1}, x_i) \in A
\end{cases}
$$
**REMARQUE** si il n'y a pas de chemin reliant les deux sommets, la distance est $+\infty$
- Un graphe pondéré sera dit non orienté si les arrêtes symétriques ont même poids.
## Calcul

**QUESTION** comment calculer efficacement la distance entre deux sommets. Et si possible trouver un chemin de longueur minimale?

**EXERCICE** 10min -> 10h45\
Trouver la distance entre $A$ et $I$ dans le graphe ci-dessous.
<img src="./graphe_base.svg"/>