# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())

# get data in row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp_F = monday.temp * 1.8 + 32
# # def to_fahrenheit(x):
# #     x = x * 1.8 + 32
# #     return float(x)
#
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"]

gray_count = fur_color.where(fur_color == "Gray").count()
red_count = fur_color.where(fur_color == "Cinnamon").count()
black_count = fur_color.where(fur_color == "Black").count()

# gray_count = data[data["Primary Fur Color"] == "Gray"].X.count()
# red_count = data[data["Primary Fur Color"] == "Cinnamon"].X.count()
# black_count = data[data["Primary Fur Color"] == "Black"].X.count()
#
data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count],
}

fur_color_df = pandas.DataFrame(data_dict)
fur_color_df.to_csv("squirrel_count.csv")
