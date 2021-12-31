from tkinter import *
import time
import random

class Ball:
    def __init__(self,canvas,color):
        self.x=0
        self.y=-1
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id, 245,100)

    def ran(self):
        return random.randint(-3,3)
    def stop(self):
      return random.randint(0,0)

    def draw(self,game):
        self.canvas.move(self.id, self.x,self.y)
        pos = self.canvas.coords(self.id)
        l=game.level
        if pos[1] <=0: #top
            self.change(self.ran(),l)
            game.addScore()
        if pos[3] >= 400: #bottom
            self.change(self.ran(),-l)
            game.uselive()

        if pos[0] <=0: #left
            self.change(l,self.ran())
            game.addScore()
        if pos[2] >=500: #right
            self.change(-l,self.ran())
            game.addScore()



    def change(self,x,y):
        self.x=x
        self.y=y



        

class Game:
    def __init__(self,canvas):
        self.canvas=canvas
        self.level=1
        self.score=0
        self.lives = 3
        self.idlevel=canvas.create_text(125,375, text= 'level='+str(self.level), fill='red',font=('Trebuchet '))
        self.idscore=canvas.create_text(350,375, text= 'score='+str(self.score), fill='red',font=('Trebuchet '))
        self.curlives=canvas.create_text(240,375, text= 'lives='+str(self.lives), fill='red',font=('Trebuchet '))

    def addScore(self):
        if self.level<= 10:
            self.score+=1
        if self.score % 3 == 0 and self.level<=10:
            self.nextLevel()
        self.canvas.itemconfig(self.idscore, text='score='+str(self.score))
       

    def gameover(self):
        if self.level>= 10:
            canvas.create_text(250,200, text = "YOU WON", fill="blue", font=('Times',70))
            return True
        if self.lives<= 0:
            canvas.create_text(250,200, text = "YOU LOST", fill="blue", font=('Times',70))
            return True
        return False
    def uselive(self):
        self.lives=self.lives-1
        self.canvas.itemconfig(self.curlives, text='lives='+str(self.lives))
            
    
    def nextLevel(self):

        self.level+=1
        self.canvas.itemconfig(self.idlevel, text='level='+str(self.level))
        
tk=Tk()
tk.title("GazumpaBall")

canvas = Canvas(tk, width=500, height = 400)
canvas.pack()

ball = Ball(canvas,'lime')
game = Game(canvas)

while game.gameover() == False:
    ball.draw(game)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
input("Do you like GazumpaBall?")
