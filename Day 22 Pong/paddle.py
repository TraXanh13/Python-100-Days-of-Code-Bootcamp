from turtle import Turtle

PADDLE_SPEED = 20


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)
        self.speed = PADDLE_SPEED

    def up(self):
        self.goto(self.xcor(), self.ycor() + self.speed)

    def down(self):
        self.goto(self.xcor(), self.ycor() - self.speed)
