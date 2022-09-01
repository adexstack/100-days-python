#Minnesota to Dallas in Texas
import turtle as t
from turtle import Turtle, Screen
from random import choice, randint

t.colormode(255)

shapes = [
    {"name": "triangle", "sides": 3},
    {"name": "square", "sides": 4},
    {"name": "pentagon", "sides": 5},
    {"name": "hexagon", "sides": 6},
    {"name": "heptagon", "sides": 7},
    {"name": "octagon", "sides": 8},
    {"name": "nonagon", "sides": 9},
    {"name": "decagon", "sides": 10}
]

colors = ["red", "green", "blue", "yellow", "violet"]


def random_color():
    r= randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def move_forward_turn_right_given_names(turtle_object, distance, name):
    turtle_object.forward(distance)
    turtle_object.right(get_angle_given_name(name))


def move_forward_turn_right_given_sides(turtle_object, distance, sides):
    turtle_object.forward(distance)
    turtle_object.left(get_angle_given_side(sides))


def get_angle_given_name(name):
    for shape in shapes:
        if shape["name"] == name:
            angle = 360/(shape["sides"])
            return angle


def get_angle_given_side(sides):
            angle = 360/sides
            return angle


def move_dashed():
    for i in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


timmy = Turtle()
timmy.shape("turtle")

#timmy.color("red")
# for shape in shapes:
#     no_of_sides = shape["sides"]
#     for _ in range(no_of_sides):
#         move_forward_turn_right_given_names(timmy, 100, shape["name"])

direction = [0, 90, 180, 270]

# Drawing various shapes
# for side in range(3,11):
#     timmy.color(choice(colors))
#     for _ in range(side):
#         move_forward_turn_right_given_sides(timmy, 100, side)

# for _ in range(4):
#     move_dashed()
#     timmy.right(90)

#timmy.pensize(10)
timmy.speed("fastest")


# Drawing random walk
def random_walk(distance, leap):
    for _ in range(distance):
        timmy.pencolor(random_color())
        timmy.forward(leap)
        timmy.setheading(choice(direction))


def spirograph(tilt_size):
    for _ in range(int(360/tilt_size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + tilt_size)


random_walk(100, 30)
spirograph(10)


screen = Screen()
screen.exitonclick()

# for shape in shapes:
#     print(shape["name"])