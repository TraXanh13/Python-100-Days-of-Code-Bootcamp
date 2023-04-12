from turtle import Turtle

BALL_SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED

    def move(self):
        if (self.ycor() > 280 or self.ycor() < -280):
            self.y_move *= -1

        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
