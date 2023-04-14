from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEED = randint(5, 20)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLORS[randint(0, len(COLORS)-1)])
        self.penup()
        self.setheading(180)
        self.goto(randint(300, 700), randint(-230, 230))
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move(self):
        self.forward(SPEED)

    def reset(self):
        self.goto(randint(300, 700), randint(-230, 230))
        self.color(COLORS[randint(0, len(COLORS)-1)])
