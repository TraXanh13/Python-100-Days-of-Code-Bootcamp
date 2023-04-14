from turtle import Screen, Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 24, "normal"))

    def updateScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center",
                   font=("Courier", 24, "normal"))

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center",
                   font=("Courier", 24, "normal"))
