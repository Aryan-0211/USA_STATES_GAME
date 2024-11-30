import turtle

screen = turtle.Screen()
screen.title("States Game")
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # similar to screen.exitonclick() -- To Get the Coordinates of States

answer_state = screen.textinput(title="Guess the State", prompt= "What's another state's name?" )
print(answer_state)
screen.exitonclick()
