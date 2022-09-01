# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# timmy.color("red", "green")
# timmy.color()
# timmy.backward(10)
# timmy.right(25)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# timmy.forward(20)

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["name", "address", "Age"]
table.add_row(["Ade", "Lagos", 25])
table.add_row(["Fem", "Lekki", 42])
table.add_column("Sex", ["M", "F"])
table.align = "l"
print(table)


