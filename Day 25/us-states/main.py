import turtle, pandas

statesGuessed = [];
answer = ""

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "C:/Users/minia/Documents/Projects/Python-100-Days-of-Code-Bootcamp/Day 25/us-states/blank_states_img.gif"

data = pandas.read_csv("C:/Users/minia/Documents/Projects/Python-100-Days-of-Code-Bootcamp/Day 25/us-states/50_states.csv")

screen.addshape(image)
turtle.shape(image)

stateTurtle = turtle.Turtle()
stateTurtle.penup()
stateTurtle.hideturtle()

while answer != "Exit" and len(statesGuessed) < 50:
    answer = screen.textinput(title=f"{len(statesGuessed)}/50 Guess the State", prompt="Guess a state's name?").title()

    if answer in data.state.values:
        stateTurtle.goto(int(data[data.state == answer].x), int(data[data.state == answer].y))
        stateTurtle.write(answer)
        statesGuessed.append(data[data.state == answer])