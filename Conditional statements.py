print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
age = int(input("What is your age"))
bill = 0

if height >= 120:
    print("You can ride rollercoaster")

    if age<=12:
        bill = 5
        print("Child tickets are 5$")
    elif age<=18:
        bill = 7
        print("Youth tickets are 7$")
    elif age>=45 and age<=55:
        print("Everything is going to be ok, Have a free ride on us")
    else:
        bill = 12
        print("Adult tickets are 12$")

    wantsPhoto = input("Do you want to have a photo taken? Type y for Yes and n for No")
    if wantsPhoto == "y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, You have to grow taller before you can ride")

# num = int(input("Enter the number"))
#
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M OR L: ")
# pepperoni = input("Do you want pepperoni on your pizza Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# price = 0
#
# if size =="S":
#     price = 15
#     if pepperoni == "Y":
#         price +=2
#     if extra_cheese == "Y":
#         price +=1
# elif size == "M":
#     price = 20
#     if pepperoni == "Y":
#         price +=3
#     if extra_cheese == "Y":
#         price +=1
# elif size == "L":
#     price = 25
#     if pepperoni == "Y":
#         price +=3
#     if extra_cheese == "Y":
#         price +=1
# else:
#     print("You typed the wrong input")
#
# print(f"{price}$")

