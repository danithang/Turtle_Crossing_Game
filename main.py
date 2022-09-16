import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.movement, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.car_movement()

    # Detect collision of turtle and car...car is 20px height and 40px width so if player is less than 20px from the
    # center of car then it means the player has collided with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect a successful crossing
    if player.finish_line():
        player.go_to_start()
        cars.increase_speed()
        scoreboard.increase_level()
        scoreboard.update_level()


screen.exitonclick()
