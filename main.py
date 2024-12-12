import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.tracer(0)
player=Player()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.move,'Up')
cars = CarManager()
game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.add_car()
    cars.move_cars()

    for car in cars.cars:
        if player.distance(car)<15:
            scoreboard.game_over()
            game_is_on=False
    if player.distance(0,FINISH_LINE_Y)<20:
        player.reset_pos_turtle()
        scoreboard.update_level()
        cars.increase_car_speed()

screen.exitonclick()