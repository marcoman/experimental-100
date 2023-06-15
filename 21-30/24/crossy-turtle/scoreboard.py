'''
Created on Oct 19, 2020
Our running score for our turtle crossing game
'''
import turtle

class Scoreboard (turtle.Turtle):
    FONT = ("Courier", 24, "normal")
    ALIGN = 'center'
    SCORE_X = 0
    SCORE_Y = 250
    high_score = 0

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(self.SCORE_X, self.SCORE_Y)
        if self.level > self.high_score:
            self.high_score = self.level
        self.write(f"Level: {self.level}, High Score: {self.high_score}", align=self.ALIGN, font=self.FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=self.ALIGN, font=self.FONT)

