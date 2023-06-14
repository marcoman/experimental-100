import turtle
import random

myscreen = turtle.Screen()

class RandomWalk():
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
    def turn_left(self, degrees):
        self.turtle.left(degrees)
    def turn_random(self):
        self.turtle.right(random.randint(0,360))
    def change_color(self):
        self.turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def draw_polygon(self, sides, size):
        angle = 360/sides
        self.turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

        for _ in range(sides):
            self.turtle.forward(size)
            self.turtle.right(angle)
    
    def random_walk(self, steps):
        for _ in range(steps):
            self.change_color()
            self.turn_random()
            self.draw_line(20)
    
    def random_walk_square(self, steps):
        self.turtle.pensize(10)
        for _ in range(steps):
            self.change_color()
            newdirection = random.randint(0,3)
            if newdirection == 0:
                self.turn_north()
            elif newdirection == 1:
                self.turn_east()
            elif newdirection == 2:
                self.turn_south()
            else:
                self.turn_west()
            self.draw_line(25)

    def change_speed(self, speed):
        self.turtle.speed(speed)
    
myTurtle = RandomWalk()
myTurtle.change_speed(0)
myTurtle.random_walk(100)
myTurtle.random_walk_square(200)

myscreen.exitonclick()
