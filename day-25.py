import pandas

# data = pandas.read_csv("weather_data.csv")
#
# # print(type(data))
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# temp = 0
# for item in temp_list:
#     temp += item
#
# average_temp = temp / len(temp_list)
# print(average_temp)
#
# print(data["temp"].mean())
#
# max = 0
#
# for item in temp_list:
#     if item > max:
#         max = item
#
# print(max)
#
# print(data["temp"].max())
#
# print(data.condition)

# max_temp = data["temp"].max()
# # print(max_temp)
#
# print(data[data.temp == max_temp])

# print(data[data.day == "Monday"])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 +32
# print(monday_temp_f)
#


# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260403.csv")

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")

adult_data = len(data[data["Age"] == "Adult"])
juvenile_data = len(data[data["Age"] == "Juvenile"])

Age_dict ={
    "Age": ["Adult", "Juvenile"],
    "Count": [adult_data, juvenile_data]
}

age_df = pandas.DataFrame(Age_dict)

age_df.to_csv("age_of_squirrel")
