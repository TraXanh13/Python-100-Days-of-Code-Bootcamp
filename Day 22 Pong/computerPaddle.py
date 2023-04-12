from paddle import Paddle
COMP_SPEED = 10


class ComputerPaddle(Paddle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = COMP_SPEED

    def computerMove(self, ball):
        if (self.ycor() < ball.ycor()):
            self.up()
        if (self.ycor() > ball.ycor()):
            self.down()
