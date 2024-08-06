from turtle import Turtle, Screen
import time
import random

import paddle
import scoreboard
import ball
from brick import Brick


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
    BRICK_SIZE = 50

    NUM_ROWS = 5
    NUM_COLS = 10

    def __init__(self):
        self.gameon = False
        self.limit = 0
        self.bricks_left = 0
        self.bricks = [[Brick for _ in range(self.NUM_COLS)] for _ in range(self.NUM_ROWS)]
        self.score = scoreboard.Scoreboard()
        self.ball = ball.Ball(-3 * self.SCREEN_WIDTH/8, -3 * self.SCREEN_HEIGHT/8, 
                              random.randint(5, 10), 
                              random.randint(5, 10), 
                              10, "red", 
                              self.SCREEN_WIDTH, 
                              self.SCREEN_HEIGHT)

        self.paddle = paddle.Paddle(position=-self.X_LEFT, height=self.SCREEN_HEIGHT, width=self.SCREEN_WIDTH, )

        self.setup_screen()
        self.setup_bricks()
        self.paddle.add_listeners(self.paddle.go_left, key='Left')
        self.paddle.add_listeners(self.paddle.go_right, key='Right')
        self.paddle.add_listeners(self.restart, key='r')
        self.paddle.add_listeners(self.quit, key='q')

    def setup_screen(self):
        self.myscreen = Screen()
        self.myscreen.tracer(0)
        self.myscreen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self.myscreen.bgcolor("darkblue")
        self.myscreen.title("Breakout Game")
        self.myscreen.update()

    def setup_bricks(self):
        bricks = 0
        for row in range(0, self.NUM_ROWS):
            for col in range(0, self.NUM_COLS):
                print(f'Saving {row} {col}')
                self.bricks[row][col] = Brick(x=(-self.SCREEN_WIDTH/2 + col * (self.BRICK_SIZE + self.GAPSIZE) + 2 * self.GAPSIZE), 
                                                y=( self.SCREEN_HEIGHT/2 - row * (self.BRICK_SIZE + self.GAPSIZE) - 2 * self.GAPSIZE),
                                                color="green", 
                                                screen_width=self.SCREEN_WIDTH, 
                                                screen_height=self.SCREEN_HEIGHT)
                bricks += 1
        self.bricks_left = bricks
        self.score.update_scoreboard(self.bricks_left)

    def reset_bricks(self):
        bricks = 0
        for r in range(0, self.NUM_ROWS):
            for c in range(0, self.NUM_COLS):
                self.bricks[r][c].goto(x=(-self.SCREEN_WIDTH/2 + r * (self.BRICK_SIZE + self.GAPSIZE) + 2 * self.GAPSIZE), 
                                       y=( self.SCREEN_HEIGHT/2 - c * (self.BRICK_SIZE + self.GAPSIZE) - 2 * self.GAPSIZE))
                self.bricks[r][c].showturtle()
                bricks += 1
        self.bricks_left = bricks
        self.score.update_scoreboard(self.bricks_left)

    def playgame(self):
        self.gameon = True
        self.limit = 500
        while self.gameon and self.limit > 0:
            self.ball.move(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
            for r in self.bricks:
                for b in r:
                    if (self.ball.check_brick_collision(b)):
                        print("hit")
                        b.hideturtle()
                        b.goto(2000,2000)
                        self.bricks_left -= 1
                        self.score.add_point()
                        self.score.update_scoreboard(self.bricks_left)
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

    def restart(self):
        self.resetPaddle()
        self.ball.reset()
        self.score.reset()
        self.reset_bricks()
    
    def quit(self):
        self.gameon = False