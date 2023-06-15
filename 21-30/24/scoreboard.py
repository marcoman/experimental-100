import turtle
import os

class ScoreBoard (turtle.Turtle):
    TEXT_ALIGNMENT = 'center'
    TEXT_FONT = ('Courier', 24, 'normal')
    TEXT_COLOR = 'white'
    
    def __init__(self, sizex, sizey) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.sizex = sizex
        self.sizey = sizey
        self.setup_scoreboard()
        self.update_scoreboard(self.score)

    def setup_scoreboard(self):
        self.clear()
        self.load_highscore()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,int(self.sizey/2 - 50))
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=self.TEXT_ALIGNMENT, font=self.TEXT_FONT)

    def reset_scoreboard(self):
        self.save_highscore()
        self.clear()
        self.goto(0,int(self.sizey/2 - 50))
        self.load_highscore()
        self.score = 0
        self.update_scoreboard(self.score)

    def update_scoreboard(self, score) :
        self.clear()
        self.score = score
        if self.score > self.high_score :
            self.high_score = self.score
        self.write(f"Score : {score} High Score: {self.high_score}",  align=self.TEXT_ALIGNMENT, font=self.TEXT_FONT)

    def game_over(self, message) :
        self.goto(0,0)
        self.score = 0
        self.write(message, align=self.TEXT_ALIGNMENT, font=self.TEXT_FONT)
        self.save_highscore()

    def save_highscore(self):
        myfile = open("high_score.txt", "w")
        myfile.write(str(self.high_score))
        myfile.close()

    def load_highscore(self):
        path="high_score.txt"
        isExist = os.path.exists(path)
        if isExist:
            print('loading high score')
            myfile = open(path, "r")
            score = myfile.read()
            print (f'score is {int(score)}')
            self.high_score = int(score)
        else:
            self.high_score = 0
        myfile.close()
