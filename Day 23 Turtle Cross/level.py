from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-260, 240)
        self.hideturtle()
        self.level = 1
        self.updateLevel()

    def updateLevel(self):
        self.clear()
        self.goto(-260, 240)
        self.write(f"Level {self.level}",
                   font=("Courier", 15, "normal"))

    def nextLevel(self):
        self.level += 1
        self.updateLevel()

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center",
                   font=("Courier", 15, "normal"))
