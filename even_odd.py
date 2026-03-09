def even_odd(number):
    if number % 2 == 0 and number > 0:
        print("The number is even and positive")
    elif number % 2 == 0 and number < 0:
        print("The number is even and negative")
    elif number % 2 != 0 and number > 0:
       print("The number is odd and positive")
    else:
        print("The number is odd and negative")

check = True
while check:
    inp = int(input("Enter a number:"))
    even_odd(inp)
    again = input("Do you want to check another number? Type 'yes' or 'no'")

    if again == "no":
        check = False
        print("Good bye!")
