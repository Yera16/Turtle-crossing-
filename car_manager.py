from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
initial_xcor = [300, 305, 310]


class CarManager:
    move_distance = STARTING_MOVE_DISTANCE


    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE


    def random_y(self):
        new_y = random.randint(-50, 50)
        return new_y*5

    def create(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(random.choice(initial_xcor), self.random_y())
            self.cars.append(new_car)

    def increment_speed(self):
        self.move_distance += MOVE_INCREMENT

    def move(self):
        for car in self.cars:
            new_x = car.xcor()-self.move_distance
            car.goto(new_x, car.ycor())






