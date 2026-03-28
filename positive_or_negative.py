is_on = True


while is_on:
    number = int(input("Please enter the number you want to check"))

    if number < 0:
        print("The number is negative ")
    else:
        print("The number is positive")

    decision = input("Do you want to check another number? y or no").lower()
    if decision == "y":
        continue
    else:
        print("Logged out")
        is_on = False