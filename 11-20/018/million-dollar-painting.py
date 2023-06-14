import turtle
import random


myscreen = turtle.Screen()

###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 10)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(rgb_colors)

class MillionDollarPainting():
    gapsize = 40
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
        # self.turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.turtle.color(random.choice(rgb_colors))

    def change_speed(self, speed):
        self.turtle.speed(speed)

    def change_color(self):
        self.turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def draw_dotted_line(self, length):
        self.turtle.pensize(10)
        self.turn_east()

        for i in range(0, length):
            self.change_color()
            self.turtle.pendown()
            self.turtle.dot()
            self.turtle.penup()
            self.turtle.forward(self.gapsize)
 
    def turn_north(self):
        self.turtle.setheading(90)
    def turn_east(self):
        self.turtle.setheading(0)
    def turn_south(self):
        self.turtle.setheading(270)
    def turn_west(self):
        self.turtle.setheading(180)

    def draw_painting(self):

        for _ in range(10):
            self.turtle.setx(0)
            self.turtle.sety(_ * self.gapsize)
            self.draw_dotted_line(10)
            self.turtle.penup()

myturtle = MillionDollarPainting()
myturtle.change_speed(0)
myturtle.draw_painting()

myscreen.exitonclick()
