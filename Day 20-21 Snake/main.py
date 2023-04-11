from turtle import Screen, Turtle
import time
from snek import Snek
from food import Food
from score import Score

snek = Snek()
food = Food()
score = Score()

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
        score.updateScore()
        snek.createSnekSeg(snek.head.xcor(), snek.head.ycor())

    if (snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280):
        isRunning = False
        score.gameOver()

sc.exitonclick()
