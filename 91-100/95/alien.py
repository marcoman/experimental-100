import turtle
import missile

class Alien(turtle.Turtle):
    myscreen = turtle.Screen()

    def __init__(self, x, y, color, screen_width, screen_height, alive:bool):
        turtle.Turtle.__init__(self)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.alive = alive
        self.penup()
        self.x = x
        self.y = y
        self.shape("turtle")
        self.setheading(85)
        self.shapesize(1)
        self.color(color)
        self.goto(x, y)

    def set_color(self, color):
        self.color(color)
    
    def move(self, x, y):
        new_x = self.xcor() + x
        new_y = self.ycor() + y
        if new_x < -self.screen_width / 2:
            new_x = -self.screen_width / 2
        elif new_x > self.screen_width / 2:
            new_x = self.screen_width / 2
        if new_y < -self.screen_height / 2:
            new_y = -self.screen_height / 2
        elif new_y > self.screen_height / 2:
            new_y = self.screen_height / 2
        self.goto(new_x, new_y)
    
