from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snek:
    def __init__(self):
        self.snek = []
        for i in range(3):
            self.addSnekSegment(i * -20, 0)

        self.head = self.snek[0]

    def addSnekSegment(self, x, y):
        temp = Turtle("square")
        temp.color("white")
        temp.penup()
        temp.goto(x, y)
        self.snek.append(temp)

    def extendSnek(self):
        self.addSnekSegment(self.snek[-1].xcor(), self.snek[-1].ycor())

    def move(self):
        for seg in range(len(self.snek)-1, 0, -1):
            self.snek[seg].goto(self.snek[seg - 1].pos())

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.snek:
            seg.goto(1000, 1000)
        self.snek.clear()
        self.__init__()
