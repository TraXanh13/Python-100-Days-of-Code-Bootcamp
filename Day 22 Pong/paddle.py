from turtle import Turtle

PADDLE_SPEED = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def up(self):
        self.goto(0, self.ycor() + PADDLE_SPEED)

    def down(self):
        self.goto(0, self.ycor() - PADDLE_SPEED)
