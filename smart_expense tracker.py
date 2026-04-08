from datetime import datetime
class ExpenseTracker:
    def __init__(self):
        self.users= {}

    def get_username(self):
        username = input("Enter username: ")
        return username

    def register_user(self, username):
        try:
            if username in self.users:
                raise ValueError("User already exists")

            self.users[username]= {
                "expenses": [],
                "budget": 0
            }

            print(f"User '{username}' registered successfully!")
            print(self.users)

        except ValueError as e:
            print(f"Error: {e}")

    def monthly_budget(self, username, m_budget):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            user = self.users[username]
            user["budget"] = m_budget


            print("Budget set successfully!")
            print(f"User: {username}")
            print(f"Budget: {m_budget}")
            print(self.users)

        except ValueError as e:
            print(f"Error: {e}")

    def add_expense(self, username, category, amount):
        try:
            if username not in self.users:
                raise ValueError("User does not exists!")

            user = self.users[username]
            date = datetime.now().date()

            user["expenses"].append({"category": category, "amount": amount, "date":f"{date}"})
            print("Expense added successfully!")
            print(self.users)

        except ValueError as e:
            print(f"Error: {e}")

    def view_expenses(self, username):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            print("-------- EXPENSE LIST --------")
            print(f"User: {username}")

            user = self.users[username]
            expenses = user["expenses"]

            if len(expenses) == 0:
                print("No expenses found for this user!")
                return

            counter = 1
            for expense in expenses:
                print(f"{counter}. {expense['category']} | {expense['amount']} PKR | {expense['date']}")
                counter+=1
            print("-----------------------------")
            print(f"Total Entries: {len(expenses)}")
        except ValueError as e:
            print(f"Error: {e}")

    def expense_analytics(self, username):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            print("-------- EXPENSE ANALYTICS --------")
            print(f"User: {username}")

            # EXPENSE
            total_expense = 0
            user = self.users[username]
            expenses = user["expenses"]

            if len(expenses) == 0:
                print("No expenses to analyze")
                return

            for expense in expenses:
                total_expense += expense["amount"]
            print(f"Total spending: {total_expense} PKR")

            # BUDGET
            budget = user["budget"]
            if budget == 0:
                print("Budget not set!")
                return

            print(f"Budget: {budget} PKR")

            # REMAINING BUDGET
            remaining_budget = budget - total_expense
            print(f"Remaining Budget: {remaining_budget} PKR")

            # CATEGORY BREAKDOWN
            print("Category Breakdown")
            for expense in expenses:
                print(f"- {expense['category']} : {expense['amount']} PKR")

            # MAXIMUM AMOUNT
            print("Most Spent Category: ")

            most_expense = 0
            most_category = ""

            for item in expenses:
                if item["amount"] > most_expense:
                    most_expense = item["amount"]
                    most_category = item["category"]

            print(f"{most_category} ({most_expense} PKR)")

            # AVERAGE SPENDING
            print("Daily Average Spending:")
            print(f"{int(total_expense/ 30)} PKR/day")


        except ValueError as e:
            print(f"Error: {e}")



system = ExpenseTracker()

while True:
    print("--------SMART EXPENSE ANALYZER--------")
    print("1. Register User")
    print("2. Set Monthly Budget")
    print("3. Add Expense")
    print("4. View Expense")
    print("5. Expense Analytics")

    try:
        choice = int(input("Enter choice"))

        if choice == 1:
            system.register_user(system.get_username())
        elif choice == 2:
            username = system.get_username()
            budget = int(input("Enter monthly budget (PKR): "))
            if budget < 0:
                print("Budget must be a positive number!")
            system.monthly_budget(username, budget)
        elif choice == 3:
            username = system.get_username()
            category = input("(Food/Transport/Shopping/Bills): ")
            amount = int(input("Enter amount (PKR): "))
            if amount < 0:
                print("Amount must be greater than  0!")
            system.add_expense(username,category,amount)
        elif choice == 4:
            username = system.get_username()
            system.view_expenses(username)
        elif choice == 5:
            username = system.get_username()
            system.expense_analytics(username)

    except:
        print("Please enter choice in Digits")