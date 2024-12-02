import turtle
import pandas
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read data and prepare variables
data = pandas.read_csv("day-25-us-states-game-start/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Timer start
start_time = time.time()

# Create a turtle for drawing
def create_turtle():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    return t

# Animated turtle for correct guesses
def animated_turtle(x, y):
    anim_turtle = create_turtle()
    anim_turtle.goto(x, y)
    anim_turtle.color("green")
    for _ in range(10):
        anim_turtle.write("✔", align="center", font=("Arial", 12, "bold"))
        anim_turtle.hideturtle()
        time.sleep(0.1)
        anim_turtle.showturtle()
        time.sleep(0.1)
    anim_turtle.clear()

# Display progress message
def display_message(message):
    msg_turtle = create_turtle()
    msg_turtle.goto(0, -270)
    msg_turtle.color("blue")
    msg_turtle.write(message, align="center", font=("Arial", 16, "italic"))
    time.sleep(2)
    msg_turtle.clear()

# Game loop
while len(guessed_states) < 50:
    # Input from user
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", 
        prompt="What's another state's name?"
    )
    
    if not answer_state:  # Exit on Cancel or empty input
        break
    
    answer_state = answer_state.title()

    if answer_state == "Exit":
        # Create a list of states to learn
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        
        # Update the map with the state name
        t = create_turtle()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.color(random.choice(["red", "green", "blue", "purple", "orange", "pink"]))
        t.write(answer_state, align="center", font=("Arial", 10, "bold"))
        
        # Add animation for correct guess
        animated_turtle(state_data.x.item(), state_data.y.item())
    else:
        # Encouragement feedback
        display_message("Try again or type 'Exit' to finish!")

# End game and show results
end_time = time.time()
elapsed_time = round(end_time - start_time)
display_message(f"Game Over! You guessed {len(guessed_states)} states in {elapsed_time} seconds.")
screen.exitonclick()
