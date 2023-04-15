from turtle import Screen, Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center",
                   font=("Arial", 24, "normal"))

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {self.highScore}", align="center",
                   font=("Courier", 24, "normal"))

    def increaseScore(self):
        self.score += 1

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center",
                   font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score

        self.score = 0
        self.updateScore()
