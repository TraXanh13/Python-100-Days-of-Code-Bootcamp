from turtle import Turtle, Screen

tim = Turtle()
sc = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def left():
    tim.left(10)


def right():
    tim.right(10)


sc.listen()
sc.onkey(key="w", fun=forward)
sc.onkey(key="s", fun=backward)
sc.onkey(key="a", fun=left)
sc.onkey(key="d", fun=right)


sc.exitonclick()
