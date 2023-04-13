from turtle import Screen

sc = Screen()
sc.setup(width=550, height=550)
sc.bgcolor("black")
sc.title("Turtle Cross")
sc.tracer(0)


isAlive = True

while isAlive:
    sc.update()


sc.exitonclick()
