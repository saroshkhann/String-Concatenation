list = [1,2,3]

# new_list = []
#
# for item in list:
#     add = item +1
#     new_list.append(add)
# print(new_list)

# List Comprehension

# new_list  = [item+1 for item in list]
# print(new_list)

new_list = [number*2 for number in range(1,5)]

print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
print(numbers)
result = [n for n in numbers if n%2 == 0]
print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
new_sentence = sentence.replace("?", "")
new_sentence1 = new_sentence.split()

result = {word:len(word) for word in new_sentence1  }
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:temp*9/5 + 32 for [day, temp] in weather_c.items()}

print(weather_f)

