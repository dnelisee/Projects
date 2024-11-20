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

def rectangle(dimension : tuple) : 
    length, width = dimension[0], dimension[1]
    begin_fill()
    forward(length)
    left(90)
    forward(width)
    left(90)
    forward(length)
    left(90)
    forward(width)
    left(90)
    end_fill()
"""
def rectangle_avec_traits_internes(dimension : tuple, nb_traits : int) : 
    length, width = dimension[0]/(nb_traits+1), dimension[1]
    for i in range(nb_traits) : 
        rectangle((length, width))
        forward(length) 

    left(180)
    forward(nb_traits*length)
    left(180)
"""

# code principal 

def draw_toupie() : 

    dimensions_array = [10, (20, 40), (5*20, 20), (7*20, 5), (6*20, 20), (7*20, 30)]

    colors = ["red", "orange", "yellow", "blue", "red", "blue"]

    # niveau 0
    color(colors[0])
    left(180)
    up()
    goto(0,-100)
    down()
    begin_fill()
    polygone(dimensions_array[0], 3)
    end_fill()
    forward(dimensions_array[0] + (dimensions_array[1][0] - dimensions_array[0]) // 2)
    left(180)
     
    for i in range(1, 5) : 
        # on dessine le niveau i 
        color(colors[i])
        rectangle(dimensions_array[i])
        left(90)
        forward(dimensions_array[i][1])
        left(90)
        forward((dimensions_array[i+1][0] - dimensions_array[i][0]) // 2)
        left(180)
    #niveau 5 

    color(colors[5])
    rectangle(dimensions_array[5])
    left(90)
    forward(dimensions_array[5][1])

    up()
    left(180)
    forward(100)
    left(-90)
    forward(100)
    left(-90)
    write("Toupie d'Emma", font=("Arial", 12, "normal"))
    left(-90)
    down()
    forward(120)
    exitonclick()

draw_toupie()