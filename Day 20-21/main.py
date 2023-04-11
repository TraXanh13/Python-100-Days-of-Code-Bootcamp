from turtle import Screen, Turtle
import time
from snek import Snek
from food import Food

snek = Snek()
food = Food()

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("🐍 Snek 🐍")
sc.tracer(0)

sc.listen()
sc.onkey(snek.up, "Up")
sc.onkey(snek.down, "Down")
sc.onkey(snek.left, "Left")
sc.onkey(snek.right, "Right")

isRunning = True
while isRunning:
    sc.update()
    time.sleep(0.07)
    snek.move()

    if (snek.head.distance(food) < 15):
        food.moveFood()

sc.exitonclick()
