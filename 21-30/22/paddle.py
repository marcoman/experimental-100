import turtle

class Paddle(turtle.Turtle):
    myscreen = turtle.Screen()
    WIDTH = 20
    HEIGHT = 100
    def __init__(self, position, height, width):
        self.max_y = int (height/2) - 50
        self.min_y = -self.max_y + 30
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        # default is 20x20, so we strech the width
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=position, y=0)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y > self.max_y:
            new_y = self.max_y
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y < self.min_y:
            new_y = self.min_y
        self.goto(self.xcor(), new_y)

    def add_listeners(self, function, key):
        self.myscreen.listen()
        self.myscreen.onkey(function, key)

    def quit(self):
        self.myscreen.bye()
