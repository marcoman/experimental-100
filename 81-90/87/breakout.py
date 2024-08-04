from turtle import Turtle, Screen
import time


class Breakout:
    SIZE_X = 700
    SIZE_Y = 700
    GAPSIZE = 20
    STEPSIZE = 20
    DIR_UP = 90
    DIR_DOWN = 270
    DIR_LEFT = 180
    DIR_RIGHT = 0

    paddle = {'length': 3,
              'x': 0,
              'y': 0,
              'color': 'white'
              }
    
    ball = {'length': 1,
            'x': 0,
            'y': 0,
            'color': 'blue'
            }

    def __init__(self):
        self.gameon = False
        self.limit = 0
        self.myscreen = Screen()
        self.addListeners()
        self.score = 0

    def addListeners(self):
        self.myscreen.listen()
        self.myscreen.onkey(key="Left", fun=self.moveleft)
        self.myscreen.onkey(key="Right", fun=self.moveright)
        # self.myscreen.onkey(key='a', fun=self.moveleft)
        # self.myscreen.onkey(key='d', fun=self.moveright)

    def playgame(self):
        self.gameon = True
        self.limit = 25
        while self.gameon and self.limit > 0:
            print (self.limit)
            self.myscreen.tracer(0)
            self.limit -= 1
            time.sleep(0.1)
            self.myscreen.update()
        self.myscreen.exitonclick()


    def moveleft(self):
        print ("move left")

    def moveright(self):
        print ("move right")

    def start_game(self):
        print("start game")
        pass

    def end_game(self):
        pass

    def update_score(self):
        pass

