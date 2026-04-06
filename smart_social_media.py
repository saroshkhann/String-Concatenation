class MediaSystem:
    def __init__(self):
        self.users = {}
        self.post = {}

    def register_user(self, username):
        if username in self.users:
            print("User already exists")
            return
        else:
            self.users[username] = {
                "posts": [],
                "following": [],
                "followers": [],
                "categories": {}
            }
        print(f"User '{username}' registered successfully!")
        print(self.users)

    def follow_user(self, username, to_follow_user):
        if username not in self.users:
            print("User not found!")
            return
        elif username == self.users[username]:
            print("Cannot follow yourself!")
            return
        elif to_follow_user in self.users[username]["following"]:
            print("Already following this user!")
            return
        else:
            self.users[username]["following"].append(to_follow_user)
            self.users[to_follow_user]["followers"].append(username)
            print(f"{username} in now following {to_follow_user}")
            print(self.users)

    def create_post(self, username, content, category):
        if username not in self.users:
            print("User does not exists")
            return

        else:
            self.post[username] = {
                "content": content,
                "category": category,
                "likes": 0
            }
            self.users[username]["posts"].append(content)
            print("Post created successfully!")
            print(self.post)
            print(self.users)

    def like_post(self, username, post_owner, post_number):
        if username not in self.users or post_owner not in self.users:
            print("User not found")
            return
        else:
           if self.users[post_owner]["posts"]:
                self.post[post_owner]["likes"] +=1
                print(f"{username} likes {post_owner}'s post")
                print(self.users)
                print(self.post)

    def view_profile(self, username):
        print(f"Profile {username}")
        print(f"Followers: {len(self.users[username]['followers'])}")
        print(f"Following: {len(self.users[username]['following'])}")

        print("Followers list: ")

        print("Followers list:")
        for follower in self.users[username]["followers"]:
            print(f"- {follower}")

        print("Following list:")
        for following in self.users[username]["following"]:
            print(f"- {following}")



system = MediaSystem()

while True:
    print("1. Register User")
    print("2. Follow User")
    print("3. Create Post")
    print("4. Like Post")
    print("5. View Feed")
    print("6. View Profile")
    print("7. Exit")

    choice = input("Enter choice")

    if choice == "1":
        username1 = input("Enter username: ")
        system.register_user(username1)
    elif choice == "2":
        username2 = input("Enter your username: ")
        to_follow = input("Enter user to follow: ")
        system.follow_user(username2, to_follow)

    elif choice == "3":
        username3 = input("Enter username: ")
        post_content = input("Enter post content: ")
        category = input("Enter category: ")
        system.create_post(username3, post_content, category)
    elif choice == "4":
        username4 = input("Enter your username: ")
        owner_of_post = input("Enter post owner: ")
        post_number = input("Enter post number: ")
        system.like_post(username4, owner_of_post, post_number)
    elif choice == "6":
        username5 = input("Enter your username: ")
        system.view_profile(username5)