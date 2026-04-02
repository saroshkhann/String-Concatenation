class Chatbot:
    def __init__(self):
        self.users = []
        self.messages = []

    def menu(self):
        print("1. Register User")
        print("2. Send Message")
        print("3. View Inbox")
        print("4. View Chat History")
        print("5. Exit")

    def register_user(self):
        username = input("Enter username: ")

        for user in self.users:
            if user["name"] == username:
                print("User already exists!")
                return

        self.users.append({"name": username, "messages": []})
        print(self.users)

    def send_message(self):
        sender_name = input("Enter sender name: ")

        receiver_name = input("Enter receiver name: ")

        if sender_name == receiver_name:
            print("You cannot send message to yourself!")
            return

        message = input("Enter message: ")
        found = False

        for user in self.users:
            if user["name"] == receiver_name and user["name"] == sender_name:
                found = True
                user["messages"].append({"from": sender_name, "message": message})
                self.messages.append({"from": sender_name, "to": receiver_name, "message": message})
                print("Message sent successfully!")
                print(self.users)


        if not found:
            print("User not found!")

    def view_inbox(self):
        name = input("Enter your name: ")
        print("Inbox: ")

        found = False

        index = 0
        for user in self.users:
            if user["name"] == name:
                found = True
                if len(user["messages"]) == 0:
                    print("No messages yet!")

                # while index != len(user["messages"]):
                #     print(f"From: {user['messages'][index]['from']} -> {user['messages'][index]['message']}")
                #     index += 1

                for msg in user["messages"]:
                    print(f"From: {msg['from']} -> {msg['message']}")

        if not found:
            print("User not found!")

    def view_chat_history(self):
        your_name = input("Enter your name: ")
        other_user = input("Enter other user: ")

        print("Chat: ")

        for msg in self.messages:
            if (msg["from"] == your_name and msg["to"] == other_user) or (msg["from"] == other_user and msg["to"] == your_name):
                print(f"{msg['from']}: {msg['message']}")


chatbot = Chatbot()

is_on = True

while is_on:
    chatbot.menu()
    choice = int(input("Enter the operation you want to perform"))

    if choice == 1:
        chatbot.register_user()
    elif choice == 2:
        chatbot.send_message()
    elif choice == 3:
        chatbot.view_inbox()
    elif choice == 4:
        chatbot.view_chat_history()
    else:
        is_on = False
