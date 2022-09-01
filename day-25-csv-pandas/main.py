
# #Using just file methods
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
#
# #Using csv library
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
#
# # Using the pandas library

#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # Get Row data value
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas as pd
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_fur_count, red_fur_count, black_fur_count]
}

squirrel_data_df = pd.DataFrame(squirrel_dict)
squirrel_data_df.to_csv("squirrel_count.csv")

#Fur Color, Count, Grey, Red, Black








