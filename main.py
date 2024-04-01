import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move,"Up")
game_is_on = True
car_manager = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()

    for car in car_manager.cars:
        if car.ycor() == player.ycor() or car.ycor() - player.ycor() == 10 or car.ycor() - player.ycor() == -10:
            if car.distance(player) < 30:
                scoreboard.game_over()
                game_is_on = False
        elif car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        player.refresh()
        car_manager.increment_speed()
        scoreboard.change_level()










screen.exitonclick()