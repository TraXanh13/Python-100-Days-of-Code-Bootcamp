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
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

        if (self.ycor() > 280 or self.ycor() < -280):
            self.y_move *= -1

        if (self.xcor() > 380 or self.xcor() < -380):
            self.reset()

    def bounce(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce()
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED

    def speedUp(self):
        self.x_move *= 1.1
        self.y_move *= 1.1

    def paddleCollision(self, paddle):
        if (self.distance(paddle) < 50 and (self.xcor() > 320 or self.xcor() < -320)):
            self.bounce()
            self.speedUp()
            self.move()
