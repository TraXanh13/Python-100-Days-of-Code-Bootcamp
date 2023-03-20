from turtle import Turtle, Screen

tim = Turtle()
sc = Screen()

def move_forward():
    tim.forward(10)

sc.listen()
sc.onkey(key="space", fun=move_forward)


sc.exitonclick()