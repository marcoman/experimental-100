'''
This is the beginning of the snake game
'''
import turtle
import time
snake = []

SIZE_X = 600
SIZE_Y = 600
GAPSIZE = 20

snake_body = {'length': 1,
              'direction': "right",
              'x_coordinate': 0,
              'y_coordinate': 0,
              'body' : snake,
              }


for i in range(3):
    newpart = turtle.Turtle()
    newpart.shape("square")
    newpart.color("white")
    newpart.penup()
    newpart.shapesize(stretch_wid=1, stretch_len=1, outline=1)
    newpart.goto(snake_body['x_coordinate'], snake_body['y_coordinate'])
    snake_body['x_coordinate'] -= 20
    snake.append(newpart)
        

myscreen = turtle.Screen()
myscreen.tracer(0)
myscreen.setup(width=SIZE_X, height=SIZE_Y)
myscreen.bgcolor("darkblue")
myscreen.title("Snake Game")
myscreen.update()

gameon = True
limit = 100
while gameon and limit > 0:
    limit -= 1
   
    myscreen.tracer(0)
    for part in reversed(snake):
        if snake.index(part) == 0:
            if part.xcor() + GAPSIZE > int(SIZE_X/2):
                part.left(90)
            if part.ycor() + GAPSIZE > int(SIZE_Y/2):
                part.left(90)
            if part.xcor() - GAPSIZE < -int(SIZE_X/2):
                part.left(90)
            if part.ycor() - GAPSIZE < -int(SIZE_Y/2):
                part.left(90)
            part.forward(20)
        else:
            part.goto(snake[snake.index(part)-1].xcor(), snake[snake.index(part)-1].ycor())

    time.sleep(0.1)
    myscreen.update()


myscreen.exitonclick()
