import turtle

class Scoreboard(turtle.Turtle):

    TEXT_FONT = ("Courier", 40, "normal")
    TEXT_COLOR = "white"
    TEXT_COLOR_WINNING = "green"
    TEXT_COLOR_LOSING = "red"
    TEXT_ALIGN = "center"
    TEXT_SHADOW = True

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        if self.left_score > self.right_score:
            self.color(self.TEXT_COLOR_WINNING)
        elif self.left_score < self.right_score:
            self.color(self.TEXT_COLOR_LOSING)
        else:
            self.color(self.TEXT_COLOR)
        self.write(self.left_score, align=self.TEXT_ALIGN, font=self.TEXT_FONT)

        self.goto(100, 200)
        if self.left_score > self.right_score:
            self.color(self.TEXT_COLOR_LOSING)
        elif self.left_score < self.right_score:
            self.color(self.TEXT_COLOR_WINNING)
        else:
            self.color(self.TEXT_COLOR)
        self.write(self.right_score, align=self.TEXT_ALIGN, font=self.TEXT_FONT)

    def l_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.right_score += 1
        self.update_scoreboard()
