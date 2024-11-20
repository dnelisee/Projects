"""
On illsutre ici des mouvements aléatoires de la tortue tant qu'elle est dans 
une zone bien définie et fixée à l'avance.
"""


from turtle import * 
speed(0)
from random import randint, choice


" La zonne sera ici un disque ouvert de rayon 'radius' "

def is_in_the_circle(radius : int) : 
    "On verifie si la tortue est dans le cercle ou pas"

    return xcor()**2 + ycor()**2 < radius**2 

def change_direction() : 
    """
    On change aléatoirement la direction de la tortue
    """
    setheading(randint(1,360))

def draw_mvt(radius : int, pas : int) : 
    """
    On dessine alors la trajectoire de la tortue
    """
    # On dessine le cercle
    up()
    goto(0, -radius)
    down()
    color('red')
    circle(radius)
    color('black')
    # On se place au centre
    up()
    goto(0,0)
    down()
    # on met la tortue en mvt 
    while is_in_the_circle(radius) : 
        forward(pas)
        change_direction()


def draw_many_mvt(radius : int, pas : int, nb_mvt = 20) : 
    """
    On effectue le mvt aleatoire plusieurs fois 
    de suite avec des couleurs différentes
    """
    couleurs = ["yellow", "green", "red", "cyan", "blue"] 

    # on modifie la taille des traits
    pensize(2)

    # on dessine le cercle
    up()
    goto(0,-radius)
    down()
    
    color('red')
    circle(radius)
    color('black')
    
    # on se place au centre 
    up()
    goto(0,0)
    down()
    
    # on lance les mvts
    for i in range(nb_mvt) : 

        # on change la coouleur de dessin
        pencolor(choice(couleurs))

        # on met la tortue en mvt
        while is_in_the_circle(radius) : 
            forward(pas)
            change_direction()
        
        # on revient au centre 
        up()
        goto(0,0)
        down()

# test 
draw_many_mvt(100, 10)

exitonclick()