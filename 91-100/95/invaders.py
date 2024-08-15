from turtle import Turtle, Screen
import time
import random

import base
import scoreboard
import missile

from alien import Alien


class Invaders:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    GAPSIZE = 30
    STEPSIZE_H = 10
    STEPSIZE_V = 20

    BASE_SIZE = 30

    MISSILES_MAX = 2
    MISSILES_X = 0
    MISSILES_Y = 15
    
    BOMBS_MAX = 2

    X_RIGHT = (SCREEN_WIDTH - 2*GAPSIZE) / 2
    X_LEFT = -X_RIGHT   

    ALIEN_SIZE = 5
    ALIEN_PULSE = 10
    ALIEN_ROWS = 5
    ALIEN_COLS = int((SCREEN_WIDTH - 4 * GAPSIZE) / ((GAPSIZE + ALIEN_SIZE)))
    
    x_adjust = 0
    y_adjust = 0
        
    def __init__(self) -> None:
        self.game_on = False
        self.missile = None
        self.missile_count = 0

        self.aliens = [[Alien for _ in range(self.ALIEN_COLS)] for _ in range(self.ALIEN_ROWS)]
        self.scoreboard = scoreboard.Scoreboard()
        self.base = base.Base(position=-self.X_LEFT, height=self.SCREEN_HEIGHT, width=self.SCREEN_WIDTH)

        self.setup_screen()
        self.setup_invaders()
        self.base.add_listeners(self.base.move_left, key="Left")
        self.base.add_listeners(self.base.move_right, key="Right")
        self.base.add_listeners(self.shoot, key="Up")

        self.base.add_listeners(self.restart, key='r')
        self.base.add_listeners(self.quit, key='q')


    def playgame(self):
        self.gameon = True
        self.limit = 2000
        while self.gameon and self.limit > 0:
            # print (f'Step {self.limit}')
            if (self.limit % 10 == 0): self.move_invaders()

            if self.missile_count > 0:
                self.move_missile()

                if self.missile.check_wall_collision():
                    self.missile_count = 0
                    self.missile.hideturtle()
                else:
                    for row in self.aliens:
                        for alien in row:
                            if (self.missile.check_alien_collision(alien)):
                                print("hit")
                                alien.hideturtle()
                                alien.goto(2000,2000)
                                alien.alive = False
                                self.missile_count = 0
                                self.scoreboard.update_scoreboard(10)
                                self.missile.hideturtle()
                                break
            
            self.myscreen.update()
            self.limit -= 1
            time.sleep(0.05)
        self.myscreen.exitonclick()
        
    def shoot(self):
        # When the player shoots, we must launch a missle.
        if self.missile_count == 0:
            self.missile_count = 1
            self.missile = missile.Missile(x = self.base.xcor(), 
                                           y = self.base.ycor() + 10,
                                           dy= self.MISSILES_Y,
                                           screen_width=self.SCREEN_WIDTH,
                                           screen_height=self.SCREEN_HEIGHT,
                                           color="purple",
                                           r = 5,
                                           )
        else:
            print ("too many missiles.")
            pass
            
    def reset_aliens(self):
        pass

    def reset_scoreboard(self):
        self.scoreboard.reset_scoreboard()

    def setup_scoreboard(self):
        pass

    def setup_screen(self):
        self.myscreen = Screen()
        self.myscreen.tracer(0)
        self.myscreen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self.myscreen.bgcolor("darkblue")
        self.myscreen.title("Space Invaders")
        self.myscreen.update()

    def setup_invaders(self):
        self.alien_direction = 1
        for row in range(0, self.ALIEN_ROWS):
            for col in range(0, self.ALIEN_COLS):
                print(f'Saving {row} {col}')
                if col % 1:
                    alien_color = "red"
                else:
                    alien_color = "orange"
                self.aliens[row][col] = Alien(x=(-self.SCREEN_WIDTH/2 + col * (self.ALIEN_SIZE + self.GAPSIZE) + 2 * self.GAPSIZE),
                                              y=( self.SCREEN_HEIGHT/2 - row * (self.ALIEN_SIZE + self.GAPSIZE) - 2 * self.GAPSIZE),
                                              color=alien_color, 
                                              screen_width=self.SCREEN_WIDTH, 
                                              screen_height=self.SCREEN_HEIGHT,
                                              alive=True)
        self.scoreboard.update_scoreboard(0)

    def move_invaders(self):
        # If we just dropped a row, don't calculcate the edge detection.
        if self.y_adjust == -1:
            self.y_adjust = 0
            self.x_adjust = self.alien_direction
        else:
            # We have to iterate over all visible aliens and check to see if they are at the left or right boundary, depending on the direction.
            for r in self.aliens:
                for a in r:
                    if a.alive:
                        if (self.alien_direction == 1 and a.xcor() > self.X_RIGHT) or (self.alien_direction == -1 and a.xcor() < self.X_LEFT):
                            self.y_adjust = -1
                            self.alien_direction *= -1
                            break
        
        # If we're dropping a row, then don't change x
        if self.y_adjust == -1:
            self.x_adjust = 0
        else:
            self.x_adjust = self.alien_direction
               
        # Move the aliens
        for row in range(0, self.ALIEN_ROWS):
            for col in range(0, self.ALIEN_COLS):
                self.aliens[row][col].move(self.x_adjust * self.STEPSIZE_H, self.y_adjust * self.STEPSIZE_V)
                self.aliens[row][col].setheading(self.aliens[row][col].heading() + self.ALIEN_PULSE)
        self.ALIEN_PULSE *= -1
        
    def move_missile(self):
        if self.missile_count > 0:
            self.missile.move()
        else:
            pass

    def reset_base(self):
        print(f"reset base x,y are {self.base.xcor()}, {self.base.ycor()}")
        self.base.hideturtle()
        self.base.clear() 
        self.base.shape("square")
        self.base.color('white')
        self.base.penup()
        self.base.shapesize(stretch_wid=self.ALIEN_SIZE, stretch_len=1, outline=1)
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