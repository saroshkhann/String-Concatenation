class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1


user_1 = User("001", "Sarosh")
user_2 = User("002", "Jack")
user_3 = User("003", "Abdulllah")
user_4 = User("003", "Abdulllah")
user_5 = User("003", "Abdulllah")
user_6 = User("003", "Abdulllah")
user_7 = User("003", "Abdulllah")

user_3.follow(user_1)

print(user_3.following)
print(user_3.followers)
print(user_1.following)
print(user_1.followers)