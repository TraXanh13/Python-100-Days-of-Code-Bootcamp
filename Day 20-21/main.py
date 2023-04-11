from turtle import Screen, Turtle
import time


sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("🐍 Snek 🐍")
sc.tracer(0)

snek = []


def buildSeg(x, y, dir="right"):
    temp = Turtle("square")
    temp.color("white")
    temp.penup()
    temp.goto(x, y)
    snek.append(temp)


for i in range(3):
    buildSeg(i * -20, 0)

isRunning = True

while isRunning:
    sc.update()
    time.sleep(0.1)

    # Move snek
    for seg in range(len(snek)-1, 0, -1):
        snek[seg].goto(snek[seg - 1].pos())

    snek[0].forward(20)

sc.exitonclick()
