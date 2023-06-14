import turtle

class ScoreBoard (turtle.Turtle):
    TEXT_ALIGNMENT = 'center'
    TEXT_FONT = ('Courier', 24, 'normal')
    TEXT_COLOR = 'white'
    
    def __init__(self, sizex, sizey) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,int(sizey/2 - 50))
        self.write(f"Score : {self.score}", align="center", font=("Courier", 24, "normal"))

    def update_score(self, score) :
        self.score = score
        self.clear()
        self.write(f"Score : {score}", align=self.TEXT_ALIGNMENT, font=self.TEXT_FONT)

    def game_over(self, message) :
        self.goto(0,0)
        self.write(message, align=self.TEXT_ALIGNMENT, font=self.TEXT_FONT)
