import json

print("Welcome to ATM Machine")

def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

users_database = load_data()

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def withdraw_money(money_withd, username):
    if money_withd > users_database[username]['balance']:
       print(f"Sorry you have only {users_database[username]['balance']}PKR in your account")
    else:
        users_database[username]['balance'] -= money_withd
        save_data(users_database)
        return users_database[username]['balance']

def dep_money(dep, username):
    users_database[username]['balance'] += dep
    save_data(users_database)
    return users_database[username]['balance']

def user_login():
    login = input("Please enter your name: ")
    return login

def transfer_amount(t_money, t_name, sender_name):

    if t_name not in users_database:
        print("Please write the correct name: ")
        return

    if t_name == sender_name:
        print("You cannot transfer money to yourself")
        return

    if t_money > users_database[sender_name]["balance"]:
        print("Insufficient Balance")
        return
    else:
        print(f"Transfer {t_money} to {t_name}")
        users_database[sender_name]["balance"] -= t_money
        users_database[t_name]["balance"] += t_money
        users_database[sender_name]['history_list'].append(f"Transfer {t_money} to {t_name}")
        save_data(users_database)

def changepin(oldpin, npin, user):
    users_database[user]["PIN"] = npin
    save_data(users_database)
    print("PIN Changed successfully")

def menu():
    print("Press 1 to Withdraw money")
    print("Press 2 to Deposit money")
    print("Press 3 to Transfer money")
    print("Press 4 to Check balance")
    print("Press 5 to Check history")
    print("Press 6 to Change PIN")

is_on = True

while is_on:
    pinAttempts = 3
    user_name = user_login()

    if user_name not in users_database:
        print("Please write the correct name: ")
        continue

    while pinAttempts > 0:
        user_pin = users_database[user_name]["PIN"]

        PIN= int(input("Please enter your PIN: "))

        if user_pin == PIN:
            menu()
            choice = int(input("Press the button of the operation"))

            if choice == 1:
                print("\n"*20)
                money = int(input("How much money you want to withdraw?"))
                withdrawn_amount = withdraw_money(money, user_name)
                print(f"You have withdrawn {money}PKR from Your Account")
                users_database[user_name]['history_list'].append(f"Withdraw {money}")

            elif choice == 2:
                print("\n" * 20)
                deposit_money = int(input("How much money you want to deposit? "))
                deposited_amount = dep_money(deposit_money, user_name)
                print(f"You have deposited {deposit_money}PKR in Your Account")
                users_database[user_name]['history_list'].append((f"Deposit {deposit_money}"))

            elif choice == 3:
                print("\n" * 20)
                transfer_money = int(input("How much money you want to transfer?"))
                transfer_name = input("Enter the name of account you want to transfer money in")
                transfer_amount(transfer_money,transfer_name, user_name)

            elif choice == 4:
                print("\n" * 20)
                print(f"Your current balance is {users_database[user_name]['balance']}PKR")

            elif choice == 5:
                print("\n" * 20)
                history = input("Do you want to check history? 'y' or 'n'")

                if history == "y":
                    for item in users_database[user_name]['history_list']:
                        print(item)
                else:
                    continue

            elif choice == 6:
                print("\n" * 20)
                currentpin = int(input("Enter your current PIN: "))

                if currentpin != users_database[user_name]["PIN"]:
                    print("Incorrect PIN")

                newpin = int(input("Please enter the new PIN"))
                changepin(user_pin, newpin, user_name)

            checking = input("Do you want to perform the task again? 'y' or 'n'")
            if checking == "n":
                is_on = False
            break
        else:
            pinAttempts -=1
            print("Incorrect PIN")
            print(f"Attempts left: {pinAttempts}")
            continue