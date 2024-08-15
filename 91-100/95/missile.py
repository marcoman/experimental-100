import turtle
import random

class Missile(turtle.Turtle):
    MISSILE_WIDTH = 0.5
    def __init__(self, x, y, dy, r, color, screen_width, screen_height, heading=90):
        turtle.Turtle.__init__(self)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.setheading(heading)
        self.shapesize(stretch_wid=self.MISSILE_WIDTH, stretch_len=1)
        self.speed(1)
        self.penup()
        self.dy = dy
        self.shape("arrow")
        self.color(color)
        self.goto(x, y)

    def move(self):
        current_y = self.ycor()
        new_y = current_y + self.dy
        self.goto(self.xcor(), new_y)

    def check_wall_collision(self):
        if (self.ycor() > int (self.screen_height/2)):
            print(f"wall-Top {self.ycor()} at {self.screen_height/2}")
            return True
        else:
            return False

    def check_floor_collision(self):
        if (self.ycor() < int (-self.screen_height/2)):
            print(f"wall-Bottom {self.ycor()} at {self.screen_height/2}")
            return True
        else:
            return False

    def check_alien_collision(self, alien:turtle.Turtle)->bool:
        if alien.alive and self.distance(alien) < 30:
            return True
        else:
            return False

    def check_base_collision(self, base:turtle.Turtle)->bool:
        if self.distance(base) < 30:
            return True
        else:
            return False

