# Sujet 09 : Labyrinthe

Crée une fonction python `resolution` prenant en entrée une chaine de caractère encodant un labyrinthe de la façon suivante :
- La première ligne est composée de "-" (case pleine) et d'un " " (l'entrée du labyrinthe).
- La dernière ligne est composée de "-" (case pleine) et d'un " " (la sortie du labyrinthe).
- Chaque ligne intermédiaire est composée de "o" (case pleine) et " " (case vide).

la fonction resolution renverra la chaine de caractère obtenue à partir de l'entrée en mettant un "x" sur les cases vides non utilisées par le chemin le plus court reliant l'entrée et la sortie en passant par des cases vides (on ne peut avancer que de haut en bas et gauche à droite).

Ainsi si l'entrée est
```
--------------- ----------------
ooooooooooooooo oooooooooooooooo
ooooooooooooooo   oooooooooooooo
ooooooooooooooooo oooooooooooooo
ooooo             oooooooooooooo
ooooo ooooooooooo     oooooooooo
ooooo ooooooooooooooo oooooooooo
ooooo oooooooo        oooooooooo
ooooo      ooo oooooo oooooooooo
oooooooooooooo oooooo     oooooo
oooooo       oooooooooooo oooooo
oo ooo ooooo oooo      oo oooooo
oo ooo ooooo oooo oooo oo oooooo
oo ooo ooooo oooo oooo oo oooooo
oo ooo ooooo       ooo    oooooo
oo     ooooooo ooo ooooooooooooo
oooooooooooooo ooo     ooooooooo
ooooooooo oooo ooooooo ooooooooo
ooooooooo oooo ooooooo ooooooooo
ooooooooo      ooooooo ooooooooo
oooooooooooooooooooooo ooooooooo
---------------------- ---------
```


la sortie sera

```
--------------- ----------------
ooooooooooooooo oooooooooooooooo
ooooooooooooooo   oooooooooooooo
ooooooooooooooooo oooooooooooooo
oooooxxxxxxxxxxxx oooooooooooooo
oooooxooooooooooo     oooooooooo
oooooxooooooooooooooo oooooooooo
oooooxooooooooxxxxxxx oooooooooo
oooooxxxxxxoooxoooooo oooooooooo
ooooooooooooooxoooooo     oooooo
ooooooxxxxxxxoooooooooooo oooooo
ooxoooxoooooxoooo      oo oooooo
ooxoooxoooooxoooo oooo oo oooooo
ooxoooxoooooxoooo oooo oo oooooo
ooxoooxoooooxxxxx  ooo    oooooo
ooxxxxxoooooooxooo ooooooooooooo
ooooooooooooooxooo     ooooooooo
oooooooooxooooxooooooo ooooooooo
oooooooooxooooxooooooo ooooooooo
oooooooooxxxxxxooooooo ooooooooo
oooooooooooooooooooooo ooooooooo
---------------------- ---------
```
