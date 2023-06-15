from turtle import Turtle
from turtle import Screen


class Player (Turtle):
    STARTING_POSITION = (0, -280)
    MOVE_DISTANCE = 10
    FINISH_LINE_Y = 280

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.screen = Screen()
        self.screen.listen()
        self.screen.onkey(self.go_up, "Up")

    def go_up(self):
        self.forward(self.MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(self.STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > self.FINISH_LINE_Y:
            return True
        else:
            return False
