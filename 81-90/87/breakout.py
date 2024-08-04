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

    def __init__(self, x, y):
        self.myscreen = Screen()
        self.addListeners()
        self.score = 0

    def addListeners(self):
        self.myscreen.listen()
        self.myscreen.onkey(key=Turtle, "Left")
        self.myscreen.onkey(self.move_paddle_right, "Right")

    def draw_blocks(self):
        pass

    def draw_paddle(self):
        pass

    def draw_ball(self):
        pass

    def setup_score(self):
        pass

    def start_game(self):
        pass

    def end_game(self):
        pass

    def update_score(self):
        pass

