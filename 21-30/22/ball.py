import turtle

class Ball(turtle.Turtle):
    PADDLE_BUFFER = 25
    def __init__(self, x, y, dx, dy, r, color, screen_width, screen_height):
        turtle.Turtle.__init__(self)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed(0)
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
        # check collision with top or bottom wall
        if self.top_side_ball > int (self.screen_height/2) or self.bottom_side_ball < -int(self.screen_height/2):
            self.dy *= -1

    def check_right_collision(self):
        if self.right_side_ball > int(self.screen_width/2):
            print("Right side collision")
            return True
        else:
            return False
        
    def check_left_collision(self):
        if self.left_side_ball < -int(self.screen_width/2):
            print("Left side collision")
            return True
        else:
            return False
        
    def reset_ball(self):
        self.goto(0,0)
        self.dx *= -1
        self.dy *= -1
        self.move(self.screen_width, self.screen_height)
        print("Reset")

    def check_paddle_collision(self, paddle_left, paddle_right):
        # check left side
        if self.distance(paddle_left) < 40 and self.xcor() < -320:
            self.dx *= -1
            print("Left paddle collision")
        elif self.distance(paddle_right) < 40 and self.xcor() > 320:
            self.dx *= -1 
            print("Right paddle collision")
        else:
            pass
