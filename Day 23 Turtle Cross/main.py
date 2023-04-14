from turtle import Screen
from car import Car
from player import Player
from level import Level
import time

sc = Screen()
sc.setup(width=550, height=550)
sc.bgcolor("black")
sc.title("Turtle Cross")
sc.tracer(0)

level = Level()
player = Player()
cars = []

for _ in range(10):
    car = Car()
    cars.append(car)

sc.listen()
sc.onkey(player.up, "Up")
sc.onkey(player.down, "Down")

isAlive = True

while isAlive:
    if (player.ycor() > 230):
        isAlive = False
        level.nextLevel()

    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.reset()
    time.sleep(0.05)
    sc.update()


sc.exitonclick()
