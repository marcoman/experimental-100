from turtle import Turtle, Screen
import time
import random

import paddle
import scoreboard
import ball


class Breakout:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    X_LEFT = -350
    X_RIGHT = 350

    GAPSIZE = 20
    STEPSIZE = 20
    DIR_UP = 90
    DIR_DOWN = 270
    DIR_LEFT = 180
    DIR_RIGHT = 0
    PADDLE_SIZE = 7

    def __init__(self):
        self.gameon = False
        self.limit = 0
        self.score = 0

        self.setupscreen()

        self.paddle = paddle.Paddle(position=-self.X_LEFT, height=self.SCREEN_HEIGHT, width=self.SCREEN_WIDTH, )
        self.paddle.add_listeners(self.paddle.go_left, key='Left')
        self.paddle.add_listeners(self.paddle.go_right, key='Right')

        self.score = scoreboard.Scoreboard()
        self.ball = ball.Ball(0, 0, random.randint(1, 10), 
                              random.randint(1, 10), 
                              10, "red", 
                              self.SCREEN_WIDTH, 
                              self.SCREEN_HEIGHT)

    def setupscreen(self):
        self.myscreen = Screen()
        self.myscreen.tracer(0)
        self.myscreen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self.myscreen.bgcolor("darkblue")
        self.myscreen.title("Breakout Game")
        self.myscreen.update()

    def playgame(self):
        self.gameon = True
        self.limit = 500
        while self.gameon and self.limit > 0:
            self.ball.move(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
            self.ball.check_wall_collision()

            self.ball.check_paddle_collision(self.paddle)
            time.sleep(0.05)

            self.myscreen.update()
        self.myscreen.exitonclick()




    def resetPaddle(self):
        self.paddle.goto(1000, 1000)
        self.paddle.hideturtle()
        self.paddle.clear() 
        self.paddle.shape("square")
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=self.PADDLE_SIZE, stretch_len=1, outline=1)
        self.paddle.goto(self.paddle.xcor(), 0)

