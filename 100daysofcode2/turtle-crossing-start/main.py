import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_car()

    for veh in car_manager.all_cars:
        if veh.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_the_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
