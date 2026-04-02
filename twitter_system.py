from twitteruser import User

user  = User()

is_on = True

while is_on:
    user.menu()

    choice = int(input("Enter the operation you want to perform"))

    if choice ==1:
        user.register_user()
    elif choice == 2:
        user.post_tweet()
    elif choice == 3:
        user.follow_user()
    elif choice == 4:
        user.view_feed()
    else:
        is_on = False
        print("👋🏻Exiting... Goodbye!")