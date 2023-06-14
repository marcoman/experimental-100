import turtle
import random

myscreen = turtle.Screen()

class Turtle1():
    def __init__(self):
        self.turtle = turtle.Turtle()
        turtle.colormode(255)
        self.turtle.shape('square')
    
    def turn_north(self):
        self.turtle.setheading(90)
    def turn_east(self):
        self.turtle.setheading(0)
    def turn_south(self):
        self.turtle.setheading(270)
    def turn_west(self):
        self.turtle.setheading(180)
    def draw_square(self, size):
        for _ in range (4):
            self.turtle.forward(size)
            self.turtle.right(90)
    def draw_line(self, length):
        self.turtle.forward(length)
    def draw_dashed_line(self, length):
        for _ in range(int(length/10)):
            self.turtle.forward(10)
            self.turtle.penup()
            self.turtle.forward(10)
            self.turtle.pendown()
    def draw_square_dashed(self, size):
        for _ in range (4):
            self.draw_dashed_line(size)
            self.turtle.right(90)
    def turn_right(self, degrees):
        self.turtle.right(degrees)

    def draw_polygon(self, sides, size):
        angle = 360/sides
        self.turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

        for _ in range(sides):
            self.turtle.forward(size)
            self.turtle.right(angle)
    
myTurtle = Turtle1()
# myTurtle.draw_square(100)

# myTurtle.turn_right(3)
# myTurtle.draw_square_dashed(200)


for _ in range (3,11):
    myTurtle.draw_polygon(_, 100)

myscreen.exitonclick()
