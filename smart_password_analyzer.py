def strength_of_password(length, letters, digits, special):
    if length >= 8 and letters > 0 and digits > 0 and special > 0:
        return "Strength: Strong"
    elif length >= 6 and letters > 0 and digits > 0:
        return "Strength: Medium"
    elif length < 6:
        return "Strength: Weak"


def counting(password):
    u_amount = 0
    l_amount = 0
    d_amount = 0
    s_amount = 0
    for char in password:
        if char.isupper():
            u_amount += 1

        elif char.islower():
            l_amount += 1

        elif char.isdigit():
            d_amount += 1

        else:
            s_amount += 1

    print(f"Length: {len(password)}")
    print(f"Uppercase: {u_amount}")
    print(f"Lowercase: {l_amount}")
    print(f"Digits: {d_amount}")
    print(f"Special Characters: {s_amount}")
    collect = strength_of_password(len(password), u_amount + l_amount, d_amount, s_amount)
    print(collect)
    return collect

is_on = True
while is_on:

    password = input("Enter your password")

    weak_strength = counting(password)

    if weak_strength == "Strength: Weak":
        check = input("Do you want to make your password strong?")
        if check == "y":
            strong = input("Add more letters, digits and special characters")
            new = password + strong
            length_of_new = len(new)
            counting(new)
        else:
            is_on = False
    else:
        is_on = False



