from tkinter import *
from random import randint
from time import sleep

#  La grille de jeu fait 600 sur 600
#  et les boules ont un diamètres de 20

speed = 100  # en ms
highscore = 0
score = 0


with open('highscore.txt', 'w+') as file:
    try:
        highscore = int(file.readline().removesuffix("\n"))
    except:
        file.write('0')


class Ball:
    def __init__(self):
        self.x = randint(0, 30) * 20
        self.y = randint(0, 30) * 20

    def draw(self, canvas):
        canvas.create_oval(self.x-10, self.y-10, self.x+10,
                           self.y+10, fill='red', outline='red')


class Snake:
    def __init__(self):
        # ce sont les centres de ses parties,
        self.centers = [(300, 300), (320, 300), (340, 300), (360, 300)]
        # le premier élément est la tête du serpent
        self.direction = 'Left'  # c'est la direction dans laquelle le serpent se déplace

    def draw(self, canvas):
        for i in range(len(self.centers)):
            x, y = self.centers[i]
            if i == 0:
                color = 'yellow'
            else:
                color = 'green'
            canvas.create_oval(x-10, y-10, x+10, y+10,
                               fill=color, outline=color)

    def gameover(self):
        x, y = self.centers[0]
        if 0 <= x <= 590 and 0 <= y - 10 <= 590 and (x, y) not in self.centers[1:]:
            return False
        else:
            return True

    def move(self):
        x, y = self.centers[0]
        # Rappellons que l'axe des ordonnées en tkinter est descendante !
        if self.direction == 'Up':
            y -= 20
        if self.direction == 'Down':
            y += 20
        if self.direction == 'Left':
            x -= 20
        if self.direction == 'Right':
            x += 20
        # on insère les nouvelles coordonnées de la tête
        self.centers.insert(0, (x, y))
        self.centers.pop(-1)


class Game:
    def __init__(self):
        self.window = Tk()
        # création du canvas
        self.canvas = Canvas(self.window, height=600, width=600, bg='black')
        self.canvas.grid(row=1, columnspan=4)
        # Boutons de deplacements, c'est pour que l'on puisse également jouer sur téléphone
        Button(self.window, width=20, text='Up',
               command=self.Up).grid(row=2, column=2)
        Button(self.window, width=20, text='Down',
               command=self.Down).grid(row=4, column=2)
        Button(self.window, width=20, text='Left',
               command=self.Left).grid(row=3, column=1)
        Button(self.window, width=20, text='Right',
               command=self.Right).grid(row=3, column=3)
        Button(self.window, width=20, text='Exit',
               command=self.window.destroy).grid(row=3, column=0)

        # paramétrage du clavier
        self.window.bind_all('<KeyPress-Up>', self.Up)
        self.window.bind_all('<KeyPress-Down>', self.Down)
        self.window.bind_all('<KeyPress-Left>', self.Left)
        self.window.bind_all('<KeyPress-Right>', self.Right)

        # definition de la balle et du serpent
        self.ball = Ball()

        self.snake = Snake()

        # debut du jeu
        self.jouer()

    def jouer(self):
        global highscore, score
        # affichage des scores
        global hightscore, score
        Label(self.window, text="Score: " + str(score) + ' '*10 +
              "Highscore: " + str(highscore)).grid(row=0, column=0, columnspan=4)
        # gérons la collision entre le serpent et la balle
        if self.collision():
            score += 1
            if score > highscore:
                highscore = score
                update_hightscore()
                self.congratulation()
            self.ball = Ball()
        self.canvas.delete(ALL)
        self.snake.move()
        self.ball.draw(self.canvas)
        self.snake.draw(self.canvas)
        if self.snake.gameover():
            Label(self.canvas, text="GAME OVER").place(
                relx=0.5, rely=0.5, anchor='center')
            return
        # gérons mainenant la colision du serpent avec la balle
        if self.collision() :
            x,y = self.snake.centers[-1]
            if self.snake.direction == 'Up' :
                y += 20
            elif self.snake.direction == 'Down' :
                y-=20
            elif self.snake.direction =='Left' :
                x+=20
            elif self.snake.direction == 'Right':
                x-=20

            self.snake.centers.append((x,y))

        # On anime via la récursivité
        
        self.window.after(speed, self.jouer)

     # on supprime la queue pour garder la même taille et faire avancer le serpent

    def Up(self, event):
        self.snake.direction = 'Up'

    def Down(self, event):
        self.snake.direction = 'Down'

    def Left(self, event):
        self.snake.direction = 'Left'

    def Right(self, event):
        self.snake.direction = 'Right'

    def collision(self):
        if self.snake.centers[0] == (self.ball.x, self.ball.y):
            return True
        else:
            return False

    def congratulation(self):
        message = self.canvas.create_text(300, 300, text="!!! NEW SCORE !!!")
        self.window.update()
        self.window.after(1000)
        self.canvas.delete(message)


def update_hightscore():
    global highscore
    with open('highscore.txt', 'w') as file:
        file.write(str(highscore))


# programme principal
def start():
    game = Game()
    game.window.mainloop()


window = Tk()
Button(window, text='Start', command=start).grid(
    row=0, column=1, padx=10, pady=10, columnspan=3)
Button(window, text='Exit', command=window.destroy).grid(
    row=1, column=1, padx=10, pady=10, columnspan=3)
window.mainloop()