import colorgram
import turtle
from random import choice


# def get_colors(image, count):
#     colors_list = []
#     colors = colorgram.extract(image, count)
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r, g, b)
#         colors_list.append(new_color)
#     return colors_list
#
#
# print(get_colors("image.jpg", 30))

color_list = [
    (229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
    (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
    (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
    (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203),
    (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)
]
turtle.colormode(255)
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()


def heist_paint(start_x_coordinate, y_dimension, x_dimension):
    turtle.backward(start_x_coordinate)
    y_coordinate = 0
    for i in range(y_dimension):
        turtle.setpos(-1 * start_x_coordinate,y_coordinate)
        print(turtle.pos())
        for k in range(x_dimension):
            color_tuple = choice(color_list)
            print(color_tuple)
            turtle.forward(50)
            turtle.dot(20, color_tuple)
        y_coordinate += 30


heist_paint(220, 10, 10)
screen = turtle.Screen()
screen.exitonclick()
