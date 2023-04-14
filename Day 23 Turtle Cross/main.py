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

sc.listen()
sc.onkey(player.up, "Up")
sc.onkey(player.down, "Down")


def nextLevel():
    level.nextLevel()
    player.reset()
    addCars(2)
    for car in cars:
        car.reset()
        car.increaseSpeed()


def addCars(numOfCars):
    for _ in range(numOfCars):
        car = Car()
        cars.append(car)


addCars(5)

isAlive = True

while isAlive:
    if (player.ycor() > 230):
        nextLevel()

    for car in cars:
        if player.collision(car):
            isAlive = False
            level.gameOver()
            break
        car.move()
        if car.xcor() < -300:
            car.reset()
    sc.update()
    time.sleep(0.05)


sc.exitonclick()
