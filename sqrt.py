print("Welcome! You will find square root of a number here!")


def sqrt(num):
    '''It calculates the square root of the number'''
    return (num**(1/2))

check = True

while check:
    number = float(input("Enter the number of which of want Sqrt"))

    result = sqrt(number)
    print(result)

    checking = input("Do you want to find Sqrt of another number? Type 'y' for yes and 'n' for no")

    if checking == "y":
        print("\n" * 20)

    if checking == "n":
        check = False
        print("Good bye!")

