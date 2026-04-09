from datetime import datetime
class SmartHabit:
    def __init__(self):
        self.users = {}


    def get_username(self):
        username = input("Enter username: ")
        return username

    def register_user(self, username):
        try:
            if username in self.users:
                raise ValueError("User already exists!")

            self.users[username] = {
                "habits": []
            }
            print(self.users)

        except ValueError as e:
            print(f"Error: {e}")

    def add_habit(self, username, habit_name, habit_status):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            user = self.users[username]
            habits = user["habits"]
            date = datetime.now().date()

            habits.append({"name": habit_name, "date": f"{date}", "status": habit_status})

            print(self.users)
        except ValueError as e:
            print(f"Error: {e}")

    def view_habits(self, username):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")
            print("-------- HABIT LOG --------")
            print(f"User: {username}")

            user = self.users[username]
            habits = user["habits"]

            if len(habits) == 0:
                print("No habits found!")
                return

            counter = 1
            for habit in habits:
                if habit["status"] == "done":
                    print(f"{counter}. {habit['name']} | ✅ | {habit['date']}")
                    counter+=1
                else:
                    print(f"{counter}. {habit['name']} | ❌ | {habit['date']}")
                    counter += 1


            print("----------------------------")

            print(f"Total Entries: {len(habits)}")

        except ValueError as e:
            print(f"Error: {e}")


system = SmartHabit()

is_on = True

while is_on:
    print("-------- SMART HABIT TRACKER --------")
    print("1. Register User")
    print("2. Add Habit")
    print("3. View Habits")

    try:
        choice = int(input("Enter your choice"))

        if choice == 1:
            username = system.get_username()
            system.register_user(username)
        elif choice == 2:
            username = system.get_username()
            habit = input("Enter habit name: ")
            status = input("Enter status (done/not done)")
            system.add_habit(username,habit,status)
        elif choice == 3:
            username = system.get_username()
            system.view_habits(username)

    except ValueError:
        print("Please write in Digits!")