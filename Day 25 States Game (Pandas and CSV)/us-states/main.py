import turtle, pandas

PATH = "C:/Users/minia/Documents/Projects/Python-100-Days-of-Code-Bootcamp/Day 25/us-states/"
statesGuessed = [];
missingStates = []
answer = ""

screen = turtle.Screen()
screen.title("U.S. States Game")

image = f"{PATH}blank_states_img.gif"

data = pandas.read_csv(f"{PATH}50_states.csv")
allStates = data.state.to_list()

screen.addshape(image)
turtle.shape(image)

stateTurtle = turtle.Turtle()
stateTurtle.penup()
stateTurtle.hideturtle()

while len(statesGuessed) < 50:
    answer = screen.textinput(title=f"{len(statesGuessed)}/50 Guess the State", prompt="Guess a state's name?").title()

    if answer == "Exit":
        for state in allStates:
            if state not in statesGuessed:
                missingStates.append(state)
        newData = pandas.DataFrame(missingStates)
        newData.to_csv(f"{PATH}missingStates.csv")
        break

    if answer in data.state.values:
        stateData = data[data.state == answer]
        stateTurtle.goto(int(stateData.x), int(stateData.y))
        stateTurtle.write(answer)
        statesGuessed.append(answer)