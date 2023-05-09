import pandas
import turtle
import os
"""Documentation"""
"""Bringing all necessary tools by importing"""
screen = turtle.Screen()
# screen.title("blank_states_img.gif")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")


all_states_list = data.state.to_list()

"""Convert the guess to Title case"""
"""Check if the guess is among the 50 states"""

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states you need to review")
        break
    if answer_state in all_states_list:
        guessed_states.append(answer_state)
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_find_go = data[answer_state == data["state"]]
        state_location = (int(state_find_go["x"]), int(state_find_go["y"]))
        state_turtle.setposition(state_location)
        state_turtle.write(f"{answer_state}")

# Write correct guesses onto the map
# Use a loo to allow the user to keep guessing
# Record the correct guesses in a list
# Keep track of the score
turtle.mainloop()
