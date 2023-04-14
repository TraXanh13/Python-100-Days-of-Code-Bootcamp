from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

    def reset(self):
        self.goto(0, -250)
