import turtle
import random

class Ball(turtle.Turtle):
    PADDLE_BUFFER = 25
    def __init__(self, x, y, dx, dy, r, color, screen_width, screen_height):
        turtle.Turtle.__init__(self)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed(1)
        self.penup()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)
        self.goto(x, y)

    def move(self, screen_width, screen_height):
        current_x = self.xcor()
        new_x = current_x + self.dx
        current_y = self.ycor()
        new_y = current_y + self.dy
        self.right_side_ball = new_x + self.r
        self.left_side_ball = new_x - self.r
        self.top_side_ball = new_y + self.r
        self.bottom_side_ball = new_y - self.r
        self.goto(new_x, new_y)
        

    def check_wall_collision(self):
        # check collision with left, Top, or Bottom Walls
        if (self.left_side_ball < -int(self.screen_width/2) or
            self.right_side_ball > int(self.screen_width/2)) :
            self.dx *= -1
            print("wall-LR")

        if (self.top_side_ball > int (self.screen_height/2)):
            self.dy *= -1
            print(f"wall-Top {self.top_side_ball} at {self.screen_height/2}")

        if (self.bottom_side_ball < -int(self.screen_height/2)):
            self.dy *= -1
            print(f"wall-Bottom {self.bottom_side_ball} at {-self.screen_height/2} and {self.ycor()}")
       
    def reset_ball(self):
        self.goto(0,0)
        self.dx *= -1
        self.dy *= -1
        self.move(self.screen_width, self.screen_height)
        print("Reset")

    def check_paddle_collision(self, paddle):
        if self.distance(paddle) < 40 and self.ycor() > (-self.screen_height/2):
            self.dy *= -1
            print("Paddle collision")
        else:
            pass

    def check_brick_collision(self, brick:turtle.Turtle)->bool:
        if brick.isvisible and self.distance(brick) < 40:
            # We are close to a brick. Now let's figure out from what side and where to bounce next

            # coming in from the bottom
            if self.top_side_ball < brick.ycor() and self.bottom_side_ball < brick.ycor():
                self.dy = -(self.dy + random.randint(-2, 2))

            # coming in from the top
            elif self.bottom_side_ball > brick.ycor() and self.top_side_ball > brick.ycor():
                self.dy = -(self.dy + random.randint(-2, 2))

            # coming in from the left
            elif self.right_side_ball < brick.xcor() and self.left_side_ball < brick.xcor():
                self.dx = -(self.dx + random.randint(-2, 2))
            
            # coming in from the right
            elif self.left_side_ball > brick.xcor() and self.right_side_ball > brick.xcor():
                self.dx = -(self.dx + random.randint(-2, 2))
            return True
        else:
            return False
