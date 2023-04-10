from turtle import Turtle, Screen
import random as rand

tim = Turtle()
jerry = Turtle()
bob = Turtle()
jess = Turtle()

turtles = [tim, jerry, bob, jess]
colors = ["red", "orange", "yellow", "green"]

sc = Screen()
sc.setup(width=500, height=400)
sc.listen()

choice = sc.textinput(title="Pick a color",
                      prompt="Pick a color for your turtle: ")


for turtle in turtles:
    turtle.shape("turtle")
    turtle.color(colors[turtles.index(turtle)])
    turtle.penup()
    turtle.goto(x=-230, y=-100 + (turtles.index(turtle) * 50))


def move_forward():
    for turtle in turtles:
        turtle.forward(rand.randrange(5, 20))


def hasNoWinner():
    for turtle in turtles:
        if turtle.xcor() > 230:
            if (turtle.color()[0] == choice.lower()):
                sc.title(
                    f"{turtle.color()[0].capitalize()} turtle won! You won!")
            else:
                sc.title(
                    f"{turtle.color()[0].capitalize()} turtle won! You lost!")
            return False
    return True


while hasNoWinner():
    move_forward()

sc.exitonclick()
