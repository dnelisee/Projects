from turtle import *
speed(0)

def polygone(length : int, nb_cotes = 3) : 
    """
    Cette fonction trace un polygone régulier à nb_cotes côtés de longueur length 
    chacun et remet la trotue dans le même sens qu'au départ
    """
    
    for i in range(nb_cotes) : 
        forward(length)
        left(360//nb_cotes)

def draw_grille(nb_lines : int, nb_columns: int, square_length : int) : 
    """
    Cette fonction dessine une grille (nb_lines × nb_columns)
    """
    up()
    #goto(-nb_lines*square_length, -nb_columns*square_length)
    goto(0,0)
    down()

    for i in range(1, nb_lines + 1) : 
        # sur la ligne i 
        for j in range(1, nb_columns) : 
            # sur la colonne j 

            # on dessine le carré en position (i, j) 
            polygone(square_length, 4)
            left(180)
            forward(square_length)
            left(180)
        # le dernier carré 
        polygone(square_length, 4)
        # on se positionne pour dessiner la prochaine ligne
        forward((nb_columns-1)*square_length)
        left(90)
        forward(square_length)
        left(-90)

def draw_colored_grille(nb_lines : int, nb_columns : int, square_length : int) : 
    """
    Cette fonction dessine une grille avec certaines cases diagonales avec une couleur
    """
    up()
    #goto(-nb_lines*square_length, -nb_columns*square_length)
    goto(0,0)
    down()

    for i in range(nb_lines) : 
        # sur la ligne i 
        for j in range(nb_columns-1) : 
            # sur la colonne j 
            if (j % nb_lines) == nb_lines -1 -i : 
                couleur = "black"
            else : 
                couleur = "blue"
            
            # on dessine le carré en position (i, j) 
            color(couleur)
            begin_fill()
            polygone(square_length, 4)
            end_fill()
            left(180)
            forward(square_length)
            left(180)
        # le dernier carré 
        if ( (nb_columns-1) % nb_lines) == nb_lines -1 -i : 
            couleur = "black"
        else : 
            couleur = "blue"
        begin_fill()
        polygone(square_length, 4)
        end_fill()
        # on se positionne pour dessiner la prochaine ligne
        forward((nb_columns-1)*square_length)
        left(90)
        forward(square_length)
        left(-90)
# Test 
draw_grille(3,3,30)       
exitonclick()