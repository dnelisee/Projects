"""
Le but est de creer des figures ressemblant à des algues et ce à partir de 
constructions aléatoires 
"""
from tkinter import *
import random 


class Bloc() : 
    def __init__(self, i, j, size, type, color, border_color, line_orientation=NONE):

        self.x = (2*i+1) * size/2 # The x-coordinate of the center of the bloc
        self.y = (2*j+1) * size/2 #  The y-coordinate of the center of the bloc
        self.type = type          # 'circle', 'square', ...
        self.size = size          # The size of the bloc
        self.color = color        # His color
        self.border_color = border_color 
        self.line_orientation = line_orientation 

    def draw(self, canvas) : 
        x0, y0 = self.size/2, self.size/2
        if self.type == 'circle' : 
            canvas.create_oval(self.x - x0, self.y - y0, self.x + x0, self.y + y0,
                                fill=self.color, outline=self.border_color)
        if self.type == 'square' : 
            canvas.create_rectangle(self.x - x0, self.y - y0, self.x + x0, self.y + y0,
                                fill=self.color, outline=self.border_color) 
        if self.type == 'line' : 
            if self.line_orientation == 'top-bottom' : 
                canvas.create_line(self.x - x0, self.y - y0, self.x + x0, self.y + y0,
                                    fill=self.color, width=10)
            if self.line_orientation == 'bottom-top' : 
                canvas.create_line(self.x - x0, self.y + y0, self.x + x0, self.y - y0,
                                    fill=self.color, width=10)
            
class Random_construction() : 
    def __init__(self, nb_lines, nb_columns):
        """ Propriétés non graphiques """
        self.tab = [[0 for j in range(nb_columns)] for i in range(nb_lines)]
        self.nb_lines = nb_lines 
        self.nb_columns = nb_columns 

        """ Propriétés graphiques """
        # création de la fenêtre principale
        self.window = Tk() 
        self.window.title('Algues Marines')

        # création du canvas
        self.canvas = Canvas(self.window, height=400, width=400, bg='skyblue')
        self.canvas.grid(row=1, columnspan=4)
        self.canvas.create_text(200,200,text=" CHOISISSEZ UN TYPE D'AFFICHAGE ",
                                           justify=CENTER, fill='green')
        # Titre du jeu 
        Label(self.window, text='CONSTRUCTIONS ALEATOIRES'
              ).grid(row=0, column=0, columnspan=4)
        
        # Boutons 
        Button(self.window, width=20, text='Affichage statique',
                command=self.static_display).grid(row=2, column=1)
        Button(self.window, width=20, text='Affichage dynamique',
                command=self.dynamic_display).grid(row=2, column=3)
        Button(self.window, width=20, text='Quitter',
                command=self.window.destroy).grid(row=3, column=2)
        
    """ Méthodes non graphiques """
    def can_fall(self, i, j) :
        """
        cette fonction verifie si le bloc en position (i,j) peut tomber d'une case ou pas
        """
        if (i == self.nb_lines-1)  or (self.tab[i+1][j] == 1 ) or (
            (j == 0 and self.tab[i][1] == 1) ) or (j == self.nb_columns-1 and self.tab[i][j-1] == 1) or (
                (0<j<self.nb_columns-1) and (self.tab[i][j-1] == 1 or self.tab[i][j+1] == 1)) : 
            
            return False 
        else : 
            return True  
    
    def bring_down_a_block(self, j) : 
        """
        Cette fonction fait tomber un bloc dans la colonne j jusqu'à ce 
        qu'il ne puisse plus descendre.
        """
        if self.tab[0][j] == 1 : 
            return 

        i = 0 
        while True: 
            if self.can_fall(i,j) : 
                i += 1 
            else : 
                break 
        # Donc le bloc doit être sur la ligne i de la colonne j 
        self.tab[i][j] = 1 

    def bring_down_many_blocks(self, k) : 
        """
        Cette fonction lance k blocs un par un en choisissant à chaque fois
        une colonne au hasard.
        """  
        for b in range(k) : 
            j = random.randrange(self.nb_columns) 
            self.bring_down_a_block(j) 
        
    """ Méthodes graphiques """
    
    def static_display(self) : 
        self.canvas.delete(ALL)
        nb_blocks = 100

        # On fait tomber les blocs
        self.bring_down_many_blocks(nb_blocks)

        # On dessine le tableau à l'écran 
        for i in range(self.nb_lines) : 
            for j in range(self.nb_columns) :
                if self.tab[i][j] != 0 : 
                    
                    block = Bloc(j, i, size=400/self.nb_columns, type='circle',
                                  color='green', border_color='black')
                     
                    block.draw(self.canvas)



    def dynamic_display(self) :
        self.canvas.delete(ALL)

game = Random_construction(100, 100)
game.window.mainloop()