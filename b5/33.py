class YouTube:
    def __init__(self,username,subscribers=0):
        self.username = username
        self.subscribers = subscribers

user1 = YouTube("Khoa",1000)
print(user1.username)
print(user1.subscribers)

user2 = YouTube("bi")
print(user2.username)
print(user2.subscribers)