class User:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.follower = 0
        self.following = 0
        self.following_list = []
    
    def follow(self, user):
        user.follower += 1
        self.following += 1
        self.following_list.append(user)


user1 = User("001", "John")
user2 = User("002", "Smith")

user1.follow(user2)
print(user1.following_list[0].name)
print(user2.follower)