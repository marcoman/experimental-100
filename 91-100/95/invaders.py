from turtle import Turtle, Screen
import time
import random

import base
import scoreboard

from alien import Alien


class Invaders:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    GAPSIZE = 20
    STEPSIZE = 20
    BASE_SIZE = 30

    X_LEFT = -350
    X_RIGHT = 350

    ALIEN_ROWS = 5
    ALIEN_COLS = 10
        
    def __init__(self) -> None:
        self.game_on = False

        self.aliens = [[Alien for _ in range(self.ALIEN_COLS)] for _ in range(self.ALIEN_ROWS)]
        self.scoreboard = scoreboard.Scoreboard()
        self.base = base.Base(position=-self.X_LEFT, height=self.SCREEN_HEIGHT, width=self.SCREEN_WIDTH)

        self.setup_screen()
        self.base.add_listeners(self.base.move_left, key="Left")
        self.base.add_listeners(self.base.move_right, key="Right")
        self.base.add_listeners(self.base.shoot, key="Up")

        self.base.add_listeners(self.restart, key='r')
        self.base.add_listeners(self.quit, key='q')

    def reset_aliens(self):
        pass

    def reset_scoreboard(self):
        self.scoreboard.reset_scoreboard()

    def setup_scoreboard(self):
        pass

    def setup_invaders(self):
        pass

    def setup_screen(self):
        self.myscreen = Screen()
        self.myscreen.tracer(0)
        self.myscreen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self.myscreen.bgcolor("darkblue")
        self.myscreen.title("Space Invaders")
        self.myscreen.update()

    def setup_invaders(self):
        pass

    def move_invaders(self):
        pass

    def playgame(self):
        self.gameon = True
        self.limit = 500
        while self.gameon and self.limit > 0:
            time.sleep(0.01)
            self.myscreen.update()
        self.myscreen.exitonclick()

    def reset_base(self):
        print(f"reset base x,y are {self.base.xcor()}, {self.base.ycor()}")
        self.base.hideturtle()
        self.base.clear() 
        self.base.shape("square")
        self.base.color('white')
        self.base.penup()
        self.base.shapesize(stretch_wid=5, stretch_len=1, outline=1)
        # self.base.goto(self.base.xcor(), self.base.ycor())
        self.base.goto(self.base.xcor(), self.base.ycor())

    def restart(self):
        print("restart")
        self.reset_base()
        self.reset_scoreboard()
        self.reset_aliens()
        self.game_on = True

    def quit(self):
        if self.game_on:
            self.game_on = False
        else:
            self.myscreen.exitonclick()
