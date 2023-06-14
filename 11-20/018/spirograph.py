import turtle
import random

myscreen = turtle.Screen()

class Spirograph():
    def __init__(self):
        self.turtle = turtle.Turtle()
        turtle.colormode(255)
        self.turtle.shape('square')
    
    def draw_circle(self, radius):
        self.turtle.circle(radius)
    
    def turn_right(self, degrees):
        self.turtle.right(degrees)
    def turn_left(self, degrees):
        self.turtle.left(degrees)
    def turn_random(self):
        self.turtle.right(random.randint(0,360))
    def change_color(self):
        self.turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def change_speed(self, speed):
        self.turtle.speed(speed)

    def draw_circles(self, radius, n):
        heading_step = 360/n
        for i in range(n):
            self.draw_circle(radius)
            self.turn_left(heading_step)
            self.change_color()
    
myturtle = Spirograph()
myturtle.change_speed(0)
myturtle.draw_circles(100, 50)

myscreen.exitonclick()
