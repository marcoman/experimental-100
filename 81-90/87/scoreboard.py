import turtle

class Scoreboard(turtle.Turtle):

    TEXT_FONT = ("Courier", 10, "normal")
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
        self.high_score = 0
        self.update_scoreboard(bricks_left=0)

    def update_scoreboard(self, bricks_left):
        self.clear()
        self.goto(0, -250)
        self.color(self.TEXT_COLOR)
        self.write(f"Score:{self.score} High:{self.high_score} Bricks Left:{bricks_left}",  align=self.TEXT_ALIGN, font=self.TEXT_FONT)

    def reset_scoreboard(self):
        self.score = 0
        self.update_scoreboard()

    def add_point(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

