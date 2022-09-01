import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
winning_colours = []

starting_y_coordinate = -100
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=starting_y_coordinate)
    all_turtles.append(turtle)
    starting_y_coordinate += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_colours.append(turtle.pencolor())
            if user_bet not in winning_colours:
                print(f"You lose, the winning turtle is colour {winning_colours[0]} ")
            else:
                print(f"You Win, the winning turtle is colour {winning_colours[0]} ")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
