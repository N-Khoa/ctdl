class YouTube:
    def __init__(self,username,subscribers):
        self.username = username
        self.subscribers = subscribers

user1 = YouTube("Khoa",1000)
print(user1.username)
print(user1.subscribers)