class NewsSystem:
    def __init__(self):
        self.users = {}
        self.articles = {}

    def register_user(self, username):
        if username in self.users:
            print("User already exists")
        else:
            self.users[username] = {
                "history": [],
                "categories": {}
            }
            print(f" User '{username}' registered successfully!")

    def add_article(self, title, category):
        if title in self.articles:
            print("Article already exists!")
        else:
            self.articles[title] = category
            print(f"Article '{title}' added successfully!")

    def read_article(self, username, title):
        if username not in self.users:
            print("User not found!")
            return

        if title not in self.articles:
            print("Article not found!")
            return

        category = self.articles[title]

        self.users[username]["history"].append((title, category))

        if category in self.users[username]["categories"]:
            self.users[username]["categories"][category] +=1
        else:
            self.users[username]["categories"][category] = 1

        print(f"{username} is reading: {title} ({category})")
        print("Added to history")

    def view_history(self, username):
        if username not in self.users:
            print("User not found!")
            return

        history = self.users[username]["history"]

        if not history:
            print("No reading history found!")
            return

        print("Your Reading History:\n")
        i = 1
        for item in history:
            print(f"{i}. {item[0]} ({item[1]})")
            i+=1

    def get_recommendations(self, username):
        if username not in self.users:
            print("User not found!")
            return

        categories = self.users[username]["categories"]

        if not categories:
            print("Not enought data for recommendations!")
            return

        sorted_categories = sorted(categories.items(), key = lambda x: x[1], reverse = True)

        top_categories = [cat for cat, count in sorted_categories[:2]]

        recommended = []
        for title, category in self.articles.items():
            if category in top_categories and (title,cateogry) not in self.users[username]["history"]:
                recommended.append(f"- {title} ({category})")

        if not recommended:
            print("No new recommendations available!")
        else:
            print("Recommended for you:\n")
            for rec in recommended:
                print(rec)

    def view_interest_profile(self, username):
        if username not in self.users:
            print("User not found!")
            return

        categories = self.users[username]["categories"]
        if not categories:
            print("No interest profile available yet!")
            return

        total_reads = sum(categories.values())

        print("Your Interests:\n")
        for category, count in categories.items():
            percentage = (count / total_reads) * 100
            print(f"{category}: {percentage:.0f}%")

system = NewsSystem()

while True:
    print("\n=== Smart News Recommendation System ===")
    print("1. Register User")
    print("2. Add Article")
    print("3. Read Article")
    print("4. View History")
    print("5. Get Recommendations")
    print("6. View Interest Profile")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        system.register_user(username)
    elif choice == "2":
        title = input("Enter article title: ")
        category = input("Enter article category: ")
        system.add_article(title, category)
    elif choice == "3":
        username = input("Enter username: ")
        title = input("Enter article title to read: ")
        system.read_article(username, title)
    elif choice == "4":
        username = input("Enter username: ")
        system.view_history(username)
    elif choice == "5":
        username = input("Enter username: ")
        system.get_recommendations(username)
    elif choice == "6":
        username = input("Enter username: ")
        system.view_interest_profile(username)
    elif choice == "7":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice! Try again.")
