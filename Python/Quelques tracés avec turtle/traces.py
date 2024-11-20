from turtle import * 
speed(0)

def polygone(length : int, nb_cotes = 3) : 
    """Cette fonction trace en carré de côté length 
    et remet la trotue dans le même sens qu'au départ"""
    
    for i in range(nb_cotes) : 
        forward(length)
        left(360//nb_cotes)

def moulin_a_vent(nb_palles : int) -> None : 
    "Cette fonction permet de dessiner un moulin ayant nb_palles"

    #Paramètres du moulin
    angle = 360 // nb_palles # degres
    length_square = 50 # pixels
    length_palles = 100 

    #Traçage du moulin
    
    up()
    goto(0,0)
    down()
    for i in range(nb_palles) : 
        left(angle)
        forward(length_palles)
        polygone(length_square, 4)
        up()
        goto(0,0)
        down()
   
def rosace(type : str, nb_motifs : int) -> None : 
    "Cette fonction trace une rosacre de forme 'type' avec nb_motifs motifs" 

    angle = 360 // nb_motifs

    for i in range(nb_motifs) :
        up()
        goto(0,0)
        down()
        left(angle)
        if type == 'cercle' : 
            circle(100)
        elif type == 'carre' : 
            polygone(nb_cotes=8, length=50) 
        
        

def symetrie_circulaire(nb_grpes : int, taille_grpe : int) : 
    """Cette fonction trace plusieurs groupes de figures dont les uns s'obtiennent
    par rotation des autres et un groupe est formé de 'taille_grpe' cercles partant
    tous d'un même point (origine)"""   

    rayon_max = 10
    angle = 360 // nb_grpes 
    up()
    goto(0,0)
    down()

    for i in range(nb_grpes) : 
        rayon_i = (i+1)* rayon_max // taille_grpe
        for j in range(taille_grpe) : 
            rayon_j = (j+1)* rayon_i // taille_grpe

            circle(rayon_j) 
        left(angle)


# Test 
#moulin_a_vent(10)
# rosace(type='carre', nb_motifs=20)
# symetrie_circulaire(50, 3)
# exitonclick()