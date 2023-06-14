import turtle
import random
import time

import paddle
import scoreboard
import ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
X_LEFT = -350
X_RIGHT = 350

myscreen = turtle.Screen()
myscreen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
myscreen.bgcolor("black")
myscreen.title("Pong")

paddle_left = paddle.Paddle(X_LEFT, SCREEN_HEIGHT, SCREEN_WIDTH)
paddle_right = paddle.Paddle(X_RIGHT, SCREEN_HEIGHT, SCREEN_WIDTH)
score = scoreboard.Scoreboard()
ball = ball.Ball(0, 0, random.randint(1, 10), random.randint(1, 10), 10, "red", SCREEN_WIDTH, SCREEN_HEIGHT)

paddle_left.add_listeners(paddle_left.go_up, 'w')
paddle_left.add_listeners(paddle_left.go_down, 's')
paddle_right.add_listeners(paddle_right.go_up, 'Up')
paddle_right.add_listeners(paddle_right.go_down, 'Down')
paddle_right.add_listeners(paddle_right.quit, 'q')

# while True:
#     for i in range (0, int (SCREEN_HEIGHT/10)):
#         if i % 20 < 10:
#             paddle_left.go_up()
#             paddle_right.go_down()
#         else:
#             paddle_left.go_down()
#             paddle_right.go_up()

#     myscreen.update()
#     break

game_is_on = True
score.update_scoreboard()

while game_is_on:
    ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    ball.check_wall_collision()
    if ball.check_right_collision():
        score.l_point()
        ball.reset_ball()

    if ball.check_left_collision():
        score.r_point()
        ball.reset_ball()

    ball.check_paddle_collision(paddle_left, paddle_right)
    time.sleep(0.02)
    
    myscreen.update()

myscreen.exitonclick()
