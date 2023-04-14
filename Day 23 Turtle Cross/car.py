from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLORS[randint(0, len(COLORS)-1)])
        self.penup()
        self.setheading(180)
        self.goto(randint(300, 700), randint(-230, 230))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed = randint(5, 15)

    def move(self):
        self.forward(self.speed)

    def reset(self):
        self.goto(randint(300, 700), randint(-230, 230))
        self.color(COLORS[randint(0, len(COLORS)-1)])

    def increaseSpeed(self):
        self.speed += randint(1, 5)
        if (self.speed > 25):
            self.speed = randint(5, 25)
