'''
This is the snake class, that defines how the snake moves and behaves.
'''
import turtle
import time

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

        for i in range(3):
            newpart = turtle.Turtle()
            newpart.shape("square")
            newpart.color("white")
            newpart.penup()
            newpart.shapesize(stretch_wid=1, stretch_len=1, outline=1)
            newpart.goto(self.snake_body['x_coordinate'], self.snake_body['y_coordinate'])
            self.snake_body['x_coordinate'] -= self.STEPSIZE
            self.snake.append(newpart)

        self.setupscreen()
    
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

    def playgame(self):
        gameon = True
        limit = 100
        while gameon and limit > 0:
            limit -= 1
        
            self.myscreen.tracer(0)
            for part in reversed(self.snake):
                if self.snake.index(part) == 0:
                    part.forward(self.STEPSIZE)
                else:
                    part.goto(self.snake[self.snake.index(part)-1].xcor(), 
                              self.snake[self.snake.index(part)-1].ycor())

            time.sleep(0.1)
            self.myscreen.update()
        self.myscreen.exitonclick()

