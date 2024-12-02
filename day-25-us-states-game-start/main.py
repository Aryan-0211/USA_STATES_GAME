import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("States Game")
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Uncomment the following lines to get coordinates of the states by clicking on the map
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()  # Similar to screen.exitonclick()

# Read data and prepare variables
data = pandas.read_csv("day-25-us-states-game-start/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", 
        prompt="What's another state's name?"
    ).title()

    if answer_state == "Exit":
        # Create a list of states to learn
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        # Create a turtle to display the state name on the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))

screen.exitonclick()
