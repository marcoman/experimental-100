'''
Crossy Turtle.  A riff on the classic.

'''
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    scoreboard.update_scoreboard()
    time.sleep(0.1)
    car_manager.create_car()
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    else:
        car_manager.move_cars()
    screen.update()
    if car_manager.collision(player):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
