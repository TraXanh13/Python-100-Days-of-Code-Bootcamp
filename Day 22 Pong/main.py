import time
from turtle import Screen
from paddle import Paddle
from computerPaddle import ComputerPaddle
from ball import Ball

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("🏓 Pong 🏓")
sc.tracer(0)

player1 = Paddle(-350, 0)
player2 = ComputerPaddle(350, 0)
ball = Ball()


sc.listen()
sc.onkeypress(player1.up, "Up")
sc.onkeypress(player1.down, "Down")

gameIsOn = True
while gameIsOn:
    ball.move()
    ball.paddleCollision(player1)
    ball.paddleCollision(player2)
    player2.computerMove(ball)
    sc.update()
    time.sleep(0.05)

sc.exitonclick()
