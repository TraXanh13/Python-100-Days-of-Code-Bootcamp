from turtle import Screen
from paddle import Paddle
from playerPaddle import PlayerPaddle

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("🏓 Pong 🏓")
sc.tracer(0)

player1 = PlayerPaddle()
player2 = Paddle()


sc.listen()
sc.onkey(player1.up, "Up")
sc.onkey(player1.down, "Down")

gameIsOn = True
while gameIsOn:
    sc.update()

sc.exitonclick()
