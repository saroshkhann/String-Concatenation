class User:
    def __init__(self):
        self.users = []
        self.tweets = []

    def menu(self):
        print("1. Register User")
        print("2. Post Tweet")
        print("3. Follow User")
        print("4. View Feed")
        print("5. Exit")

    def register_user(self):
        username = input("Enter username: ")

        if username in self.users:
            print("Username already exists! ")
            return

        self.users.append({"username": username, "following_list": [], "follower_list": [], "following": 0, "followers": 0})
        print(self.users)
        print(f"User '{username}' registered successfully")

    def post_tweet(self):
        found = False
        username = input("Enter username")
        for user in self.users:
            if user["username"].lower() == username.lower():
                found = True
                tweet = input("Enter tweet: ")
                length_of_tweet = tweet.replace(" ", "")
                if len(length_of_tweet) > 200:
                    print("❌ Tweet exceeds 200 Characters")
                    return
                self.tweets.insert(0, {"username": username, "tweet": tweet})
                print("✅ Tweet posted successfully")

        if not found:
            print("❌ User not found")

    def follow_user(self):
        your_username = input("Enter your username: ")
        user_to_follow = input("Enter user to follow: ")

        if your_username == user_to_follow:
            print("❌ Cannot follow yourself")
            return

        found1 = False
        found2 = False
        for user in self.users:
            if user["username"].lower() == your_username.lower():
                found1 = True
                print(your_username)
        for user in self.users:
            if user["username"].lower() == user_to_follow.lower():
                found2 = True
        if found1 and found2:
            for user in self.users:
                if user["username"] == your_username:
                    user["following"] +=1
                    user["following_list"].append(user_to_follow)
                    print(f"✅ {your_username} is now following {user_to_follow}")
                    print(self.users)

                if user["username"] == user_to_follow:
                    user["followers"] +=1
                    user["follower_list"].append(your_username)
                    print(self.users)
        else:
            print("❌ User not found")

    def view_feed(self):
        if len(self.tweets) == 0:
            print("⚠️ No tweets available")
            return

        for tweet in self.tweets:
            print(f"{tweet['username']}: {tweet['tweet']}")





