import colorgram
import random
from turtle import Turtle, Screen

colors = colorgram.extract('paintingReference.jpg', 30)

screen = Screen()
screen.colormode(255)
screen.setup(width=550, height=550)

timmy = Turtle()
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()
timmy.goto(-250, -250)


def setRandColor():
    """Set a random color for the turtle"""
    timmy.pencolor(random.choice(colors).rgb)


def drawLineOfCircles():
    """Draw a circle with random color"""
    for x in range(10):
        setRandColor()
        timmy.dot(20)
        timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.right(180)


for x in range(10):
    drawLineOfCircles()

screen.exitonclick()
