from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # saying if random_chance = 1 every 6 times the while loop runs in main.py a new car will be generated
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            # saying it's stretching 2 times original length (20) which will be 40 and no change for width which will
            # remain at 20
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # getting random int anywhere within those coordinates
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # for loop to get car to move from all_cars which is appending a new car each time
    def car_movement(self):
        for car in self.all_cars:
            # getting each car to move backwards by 5 (STARTING_MOVE_DISTANCE) because it's moving from 300 on x-axis
            # and going down to 250, 200 and so on
            car.backward(self.car_speed)

    # increasing car speed by Move_increment(10) everytime player reaches finish line
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
