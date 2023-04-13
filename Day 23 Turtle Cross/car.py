from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLORS[randint(0, len(COLORS))])
        self.penup()
        self.setheading(180)
        self.goto(300, 0)

    def move(self):
        self.forward(20)
