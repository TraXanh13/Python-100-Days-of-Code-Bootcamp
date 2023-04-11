from turtle import Turtle
MOVE_DISTANCE = 20


class Snek:
    def __init__(self):
        self.snek = []
        for i in range(3):
            self.createSnek(i * -20, 0)

    def createSnek(self, x, y):
        temp = Turtle("square")
        temp.color("white")
        temp.penup()
        temp.goto(x, y)
        self.snek.append(temp)

    def move(self):
        for seg in range(len(self.snek)-1, 0, -1):
            self.snek[seg].goto(self.snek[seg - 1].pos())

        self.snek[0].forward(MOVE_DISTANCE)
