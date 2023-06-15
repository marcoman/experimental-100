import turtle
import random


class CarManager():
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    STARTING_MOVE_DISTANCE = 5
    MOVE_INCREMENT = 2

    def __init__(self):
        self.all_cars = []
        self.car_speed = self.STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # print('Create car')
            new_car = turtle.Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(self.COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < -300:
                # print ('remove car')
                car.hideturtle()
                self.all_cars.remove(car)   

    def level_up(self):
        self.car_speed += self.MOVE_INCREMENT

    def collision(self, player):
        for car in self.all_cars:
            # We COULD modify this conditional to also include if the y-coordinates are close
            if car.distance(player) < 20:
                return True
        return False
