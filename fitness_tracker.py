import pandas as pd

class FitnessTracker:
    def __init__(self):
        self.users = {}
        self.data = None

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)

        except FileNotFoundError:
            print("File not found!")

    def register_user(self, username):
        try:
            if username in self.users:
                raise ValueError("User already exists!")

            self.users[username] = {
                "workouts": [],
                "meals": []
            }
            print(f"User '{username}' added successfully")
            print(self.users)


        except ValueError as e:
            print(f"Error: {e}")

    def log_workouts(self, username):
        try:
            if username not in self.users:
                raise ValueError("User does not exists")

            user = self.users[username]
            print(user)

            # data = {index: row for (index, row ) in self.data.iterrows() if row["username"] == username }

            if self.data is None:
                raise ValueError("Data is not loaded")

            for index, row in self.data.iterrows():
                if row["username"] == username:
                    data = {"type": row["type"], "duration": row["duration_minutes"], "calories": row["calories_burned"]}
                    print(data)
                    user["workouts"].append(data)
                    print(self.users)

        except ValueError as e:
            print(f"Error: {e}")



system = FitnessTracker()

system.load_data("workouts.csv")


while True:
    print("1. Register User")
    print("2. log workouts")

    choice = int(input("Enter choice"))

    if choice == 1:
        username = input("Enter username: ")
        system.register_user(username)
    elif choice == 2:
        username = input("Enter username: ")
        system.log_workouts(username)