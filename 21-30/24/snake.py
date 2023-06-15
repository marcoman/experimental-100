'''
This is the snake class, that defines how the snake moves and behaves.
'''
import turtle
import time

# Local files
import food
import scoreboard

class Snake:
    SIZE_X = 700
    SIZE_Y = 700
    GAPSIZE = 20
    STEPSIZE = 20
    DIR_UP = 90
    DIR_DOWN = 270
    DIR_LEFT = 180
    DIR_RIGHT = 0

    snake_body = {'length': 1,
                  'direction': "right",
                  'x_coordinate': 0,
                  'y_coordinate': 0,
                  }

    def __init__(self):
        self.snake = []
        self.myscreen = turtle.Screen()
        self.addListeners()
        self.score = 0

        self.setup_scoreboard()
        self.reset_snake()
        self.setupscreen()

        self.food = food.Food()
        self.food.set_random_position(self.SIZE_X, self.SIZE_Y, self.STEPSIZE)

    def setup_scoreboard(self):
        self.scoreboard = scoreboard.ScoreBoard(self.SIZE_X, self.SIZE_Y)

    def setupscreen(self):
        self.myscreen = turtle.Screen()
        self.myscreen.tracer(0)
        self.myscreen.setup(width=self.SIZE_X, height=self.SIZE_Y)
        self.myscreen.bgcolor("darkblue")
        self.myscreen.title("Snake Game")
        self.myscreen.update()

    def addListeners(self):
        self.myscreen.listen()
        self.myscreen.onkey(key="w", fun=self.moveup)
        self.myscreen.onkey(key="s", fun=self.movedown)
        self.myscreen.onkey(key="a", fun=self.moveleft)
        self.myscreen.onkey(key="d", fun=self.moveright)

    def moveup(self):
        if self.snake[0].heading() != self.DIR_DOWN:    
            self.snake[0].setheading(self.DIR_UP)

    def movedown(self):
        if self.snake[0].heading() != self.DIR_UP:    
            self.snake[0].setheading(self.DIR_DOWN)

    def moveleft(self):
        if self.snake[0].heading() != self.DIR_RIGHT:    
            self.snake[0].setheading(self.DIR_LEFT)

    def moveright(self):
        if self.snake[0].heading() != self.DIR_LEFT:    
            self.snake[0].setheading(self.DIR_RIGHT)

    def addsegment(self):
        newpart = turtle.Turtle()
        newpart.shape("square")
        newpart.color("white")
        newpart.penup()
        newpart.shapesize(stretch_wid=1, stretch_len=1, outline=1)
        newpart.goto(self.snake[self.snake.index(self.snake[-1])-1].xcor(), 
                    self.snake[self.snake.index(self.snake[-1])-1].ycor())
        self.snake.append(newpart)
        self.myscreen.update()

    def reset_snake(self):
        for part in self.snake:
            part.goto(1000,1000)
            part.hideturtle()
        self.snake.clear()
        for i in range(3):
            newpart = turtle.Turtle()
            newpart.shape("square")
            newpart.color("white")
            newpart.penup()
            newpart.shapesize(stretch_wid=1, stretch_len=1, outline=1)
            newpart.goto(self.snake_body['x_coordinate'], self.snake_body['y_coordinate'])
            self.snake_body['x_coordinate'] -= self.STEPSIZE
            self.snake.append(newpart)

    def crash_into_self(self):
        for part in self.snake[1:]:
            if self.snake[0].distance(part) < 10:
                return True
        return False

    def crash_into_wall(self):
        # if we crash with a wall
        if (self.snake[0].xcor() > self.SIZE_X/2 or 
            self.snake[0].xcor() < -self.SIZE_X/2 or
            self.snake[0].ycor() > self.SIZE_Y/2 or 
            self.snake[0].ycor() < -self.SIZE_Y/2):
            return True
        else:
            return False

    def playgame(self):
        gameon = True
        limit = 10000
        while gameon and limit > 0:
            limit -= 1
            # if we crash
            if (self.crash_into_wall() or self.crash_into_self()):
                print(f'crash!')
                self.reset_snake()
                self.scoreboard.reset_scoreboard()
            else:
                self.myscreen.tracer(0)
                for part in reversed(self.snake):
                    if self.snake.index(part) == 0:
                        part.forward(self.STEPSIZE)
                    else:
                        part.goto(self.snake[self.snake.index(part)-1].xcor(), 
                                self.snake[self.snake.index(part)-1].ycor())

                time.sleep(0.1)
                if self.snake[0].distance(self.food) < 15:
                    self.scoreboard.update_scoreboard(self.scoreboard.score + 1)
                    self.food.set_random_position(self.SIZE_X, self.SIZE_Y, self.STEPSIZE)
                    self.addsegment()
                self.myscreen.update()
        
        self.myscreen.exitonclick()

