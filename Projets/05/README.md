# Sujet 05 : Montage d'un film


Un producteur de cinéma est confronté au problème du planning de son prochain film et vous soumet les tâches qui doivent être effectuées :

|Tâche | Nature                    | Durée (Jours)| Prérequis (au plus tôt)|
|------|---------------------------|--------------|------------------------|
|  A   | Ecriture du scénario      | 30           | -                      |
|  B   | Casting                   | 12           | fin A + 15j            |
|  C   | Choix du lieu de tournage | 8            | fin A + 20j            |
|  D   | Découpage technique       | 4            | A et C finies          |
|  E   | Décors                    | 7            | C et D finies          |
|  F   | Tournages extérieurs      | 10           | A,B,C et D finies      |
|  G   | Tournages intérieurs      | 12           | D, E et F finies       |
|  H   | Synchronisation           | 3            | F et G finies          |
|  I   | Montage                   | 14           | H finie                |
|  J   | Son                       | 7            | debut I + 3j et fin H  |
|  K   | Mixage                    | 6            | I et J finies          |
|  L   | Tirage                    | 1            | fin K + 2j             |

Proposer un planning optimal au  producteur.
