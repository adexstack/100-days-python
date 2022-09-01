# Mine is more optimised than tutor-main
import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=800, height=400)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()
no_of_states = len(state_list)
score = 0
trials = 0
game_is_on = True
while game_is_on:
    if trials == 49:
        game_is_on = False
    answer_state = screen.textinput(title=f"{score}/{trials}", prompt="What's another state's name").title()
    trials += 1
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_df = data[data.state == answer_state]
        t.goto(int(state_df.x), int(state_df.y))
        t.write(answer_state)
        state_list.remove(answer_state)
        score += 1
to_learn = pd.DataFrame(state_list)
to_learn.to_csv("states_to_learn.csv")
