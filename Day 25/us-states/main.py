import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "C:/Users/minia/Documents/Projects/Python-100-Days-of-Code-Bootcamp/Day 25/us-states/blank_states_img.gif"



screen.addshape(image)

turtle.shape(image)

answer = screen.textinput(title="Guess the State", prompt="Guess a state's name?")

turtle.mainloop()