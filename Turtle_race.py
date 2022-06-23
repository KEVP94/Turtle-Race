import random
import turtle

# setting racing screen
racer_length = 500
racer_width = 500

# number of turtles in race
turtles = 10

turtle.screensize(racer_length, racer_width)

class racer (object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        r = random.randrange(1, 20)
        self.pos =(self.pos[0], self.pos[1]+r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset (self):
        self.turt.penup()
        self.turt.setpos(self.pos)


def startgame():
    tList=[]
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "cyan", "black", "pink", "grey"]
    start = -(racer_length/2) + 20
    for t in range(turtles):
        newPosX = start + t*(racer_length) // turtles
        tList.append(racer(colors[t], (newPosX, -230)))
        tList[t].turt.showturtle()

    run = True
    while run:
        for t in tList:
            t.move()
        maxColor = []
        maxDis = 0
        for t in tList:
            if t.pos[1] > 230 and t.pos[1] >maxDis:
                maxDis = t.pos[1]
                maxColor = []
                maxColor.append(t.color)
            elif t.pos[1] > 230 and t.pos[1] == maxDis:
                maxDis = t.pos[1]
                maxColor.append(t.color)

        if len (maxColor) > 0:
            run = False
            print ('The winner is: ')
            for win in maxColor:
                print (win)
    end = False


def endgame():
    End = input('Game Ended')


start = input('Ready To Race?')
startgame()

while True:
    print('--------------------------------------------')
    start = input ('Ready To Race Again?')
    startgame()
else:
    endgame()
