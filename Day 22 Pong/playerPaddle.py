from paddle import Paddle


class PlayerPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(-350, 0)
