from turtle import Screen, Turtle
import time
import snek as snek

snek = snek.Snek()

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("🐍 Snek 🐍")
sc.tracer(0)

isRunning = True

while isRunning:
    sc.update()
    time.sleep(0.1)
    snek.move()

sc.exitonclick()
