import turtle

class Scoreboard(turtle.Turtle):

    TEXT_FONT = ("Courier", 40, "normal")
    TEXT_COLOR = "white"
    TEXT_ALIGN = "center"
    TEXT_SHADOW = True

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.color(self.TEXT_COLOR)
        self.write(self.score, align=self.TEXT_ALIGN, font=self.TEXT_FONT)

    def add_point(self):
        self.score += 1

