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
        self.update_scoreboard(newscore=0)

    def update_scoreboard(self, newscore):
        self.clear()
        self.goto(0, 250)
        self.color(self.TEXT_COLOR)
        self.score += newscore
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(f"Score:{self.score} High:{self.high_score}",  align=self.TEXT_ALIGN, font=self.TEXT_FONT)
        print (f'Score is {self.score}')

    def reset_scoreboard(self):
        self.score = 0
        self.update_scoreboard(self.score)
