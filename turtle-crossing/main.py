import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()

scoreboard = Scoreboard()

scoreboard.show_level()

screen.onkey(player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing.
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increment_level()
        car_manager.increase_speed()

screen.exitonclick()
