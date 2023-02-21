from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(1)
timmy.speed("fastest")


def setRandColor():
    """Set a random color for the turtle"""
    timmy.pencolor(random.random(), random.random(), random.random())


def drawSquare(size):
    """Challenge 1: Draw a square

    Arguments:
        size {int} -- Size of the square
    """
    for x in range(4):
        timmy.forward(size)
        timmy.right(90)


def dashedLine(size):
    """Challenge 2: Draw a dashed line

    Arguments:
        size {int} -- Length of the line
    """
    for x in range(int(size/10)):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def drawShape(sides, size):
    """Challenge 3: Draw a shape with n sides

    Arguments:
        sides {int} -- Number of sides
        size {int} -- Size of the shape
    """

    for x in range(sides):
        timmy.forward(size)
        timmy.right(360/sides)


def randomWalk(steps):
    """Challenge 4: Draw a random walk

    Arguments:
        steps {int} -- Number of steps
    """
    for x in range(steps):
        setRandColor()
        timmy.forward(30)
        timmy.right(random.randrange(0, 360, 90))


def drawSpirograph(steps):
    """Challenge 5: Draw a spirograph

    Arguments:
        steps {int} -- Number of steps
    """
    for x in range(steps):
        setRandColor()
        timmy.circle(100)
        timmy.right(360/steps)

# drawSquare(300)

# dashedLine(100)

# creating shapes with n sides
# for sides in range(3, 11):
#     setRandColor()
#     drawShape(sides, 100)


# randomWalk(200)
drawSpirograph(100)


screen = Screen()
screen.exitonclick()
