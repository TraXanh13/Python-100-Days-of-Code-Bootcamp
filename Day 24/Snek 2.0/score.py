from turtle import Screen, Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt") as f:
            score = f.read()
            if score == "":
                self.highScore = 0
            else:
                self.highScore = int(score)
        self.score = 0
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
            
            with open("highscore.txt", "w") as f:
                f.write(str(self.highScore))

        self.score = 0
        self.updateScore()
