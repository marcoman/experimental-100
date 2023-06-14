import turtle
import random
import math

class Food (turtle.Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)


    def set_random_position(self, xsize, ysize, stepsize):
        half_x = int(stepsize * math.ceil(((xsize-stepsize)/2)/stepsize))
        half_y = int(stepsize * math.ceil(((ysize-stepsize)/2)/stepsize))
        x = random.randint(-half_x, half_x)
        y = random.randint(-half_y, half_y)
        print (f'setting food to location ({x}, {y}) ')
        self.goto(x, y)
        self.showturtle()
