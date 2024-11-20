# importation des modules à utiliser
from tkinter import *
from math import *

# nous créons un graphe de 5 personnes 
n = 5

# c'est une matrice n*n
graphe = [[0 for j in range(n)] for i in range(n)]

# on met en scène une petite situation
test = [(1,2), (1,4), (0,2), (0,3), (4,3)]

for (i, j) in test :
    graphe[i][j] = 1
    graphe[j][i] = 1


 
def voir_graphe(graphe : list[list]) -> None :
    """ fonction permettant de voir le graphe en console"""

    for i in range(n) : # i c'est la ligne 
        for j in range(n) : # j c'est la colonne 
            print('{:>3d}'.format(graphe[i][j]), end='')
        print()

#voir_graphe(graphe)

def contient_3_amis_fixes(graphe : list[list], i : int, j : int, k : int) -> bool :
    """
    on fixe 3 amis fixes i, j et k. 
    La fonction suivante teste si ils sont bien amis entre eux.
    elle renvoie vrai si c'est le cas et faux dans le cas contraire
    """
    if (graphe[i][j]==1 and graphe[j][i]==1) and (
        graphe[i][k]==1 and graphe[k][i]==1) and (
        graphe[j][k]==1 and graphe[k][j]==1) :

        return True
    
    else :
        return False


def contient_3_etrangers_fixes(graphe : list[list], i : int, j : int, k : int) -> bool :
    """
    on fixe 3 etrangers fixes i, j et k. 
    La fonction suivante teste si ils sont bien etrangers entre eux.
    elle renvoie vrai si c'est le cas et faux dans le cas contraire
    """
    if (graphe[i][j]==0 and graphe[j][i]==0) and (
        graphe[i][k]==0 and graphe[k][i]==0) and (
        graphe[j][k]==0 and graphe[k][j]==0) :

        return True
    
    else :
        return False


"""
nous créons un graphe de 5 personnes 
n = 5

c'est une matrice n*n
graphe = [[0 for j in range(n)] for i in range(n)]

on met en scène une petite situation
test = [(1,2), (1,4), (0,2), (0,3), (4,3)]

for (i, j) in test :
    graphe[i][j] = 1
    graphe[j][i] = 1

On teste les fonctions précédentes sur le graphe défini ci-dessus 

print(contient_3_amis_fixes(graphe, 1, 2, 4)) ajouter pour cela (2,4)
print(contient_3_etrangers_fixes(graphe, 1, 2, 3)) enlever pour cela (1,2)
"""


def afficher_graphe(graphe : list[list]) -> None :
    """
    Cette fonction permet de dessiner le graphe en tkinter 
    """

    # rayon du cercle sur lequel est dessiné le graphe
    R = 200 

    # rayon des cercles représentants les sommets
    r=15
    # calcul des coordonnées des sommets du graphe 
    # dans le cercle. on ajoute R pour avoir les
    # coordonnées dans le canvas (marge de 10)
    coords = []
    for i in range(n) :
        xi = R + 20 + R*cos(2 * i * pi / n)
        yi = R + 20 + R*sin(2 * i * pi / n)
        coords.append((xi, yi))

    # creation de la fenêtre d'affichage
    window = Tk()

    # creation de la zone de dessin
    
    canvas = Canvas(window, width=3*R, height=3*R, bg='white')
    canvas.pack(side=BOTTOM)


    # dessin des lignes de relation entre les personnes
    # i.e les sommets 
    for i in range(n) :
        for j in range(i, n) : # à partir de i car la matrice représentant 
                               # le graphe est symétrique

            x0, y0 = coords[i]
            x1, y1 = coords[j]

            if graphe[i][j] == 1 :
                canvas.create_line(x0, y0, x1, y1, fill='green', width=3)
            else :
                canvas.create_line(x0, y0, x1, y1, fill='red', width=3)


    # dessin des sommets du graphe 
    for i in range(n) :
        (x, y) = coords[i]

        canvas.create_oval(x-r, y-r, x+r, y+r, fill='black')

        # le texte aura un taille égale au diametre du sommet : (2*r)
        canvas.create_text(x, y, text=i, fill='white', justify=CENTER, width=(4*r))
       
   

    # affichage de la fenêtre 
    window.mainloop()


afficher_graphe(graphe)