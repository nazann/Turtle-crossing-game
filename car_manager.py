from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars =[]
        self.add_car()
        self.speed_cars=0.1

    def increase_car_speed(self):
        self.speed_cars += MOVE_INCREMENT

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance==1:
            randy=random.randint(-250,250)
            randx=random.randint(250,300)
            car=Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(randx,randy)
            self.cars.append(car)



    def move_cars(self):
        for car in range(len(self.cars)-1):
            self.cars[car].setheading(180)
            self.cars[car].forward(STARTING_MOVE_DISTANCE)

