import turtle

class Brick(turtle.Turtle):
    PADDLE_BUFFER = 25
    def __init__(self, x, y, color, screen_width, screen_height):
        turtle.Turtle.__init__(self)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.penup()
        self.x = x
        self.y = y
        self.shape("square")
        self.shapesize(2)
        self.color(color)
        self.goto(x, y)

    def set_color(self, color):
        self.color(color)
