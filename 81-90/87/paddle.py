import turtle

class Paddle(turtle.Turtle):
    myscreen = turtle.Screen()
    PADDLE_WDTH = 4
    def __init__(self, position, height, width):
        self.max_x = width / 2 - self.PADDLE_WDTH
        self.min_x = -self.max_x
        super().__init__()

        self.speed(0)
        self.shape("square")
        self.color("white")
        # default is 20x20, so we strech the width
        self.shapesize(stretch_wid=1, stretch_len=self.PADDLE_WDTH)
        self.penup()
        self.goto(x=0, y=-height/2 + 20)

    def go_left(self):
        new_x = self.xcor() - 20
        print(f"go left to {new_x}, {self.ycor()}")
        if new_x < self.min_x:
            new_x = self.min_x
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        print(f"go right to {new_x}, {self.ycor()}")
        if new_x > self.max_x:
            new_x = self.max_x
        self.goto(new_x, self.ycor())

    def add_listeners(self, function, key):
        self.myscreen.listen()
        self.myscreen.onkey(function, key)

    def quit(self):
        self.myscreen.bye()
