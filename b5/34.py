class YouTube:
    def __init__(self,username,subscribers=0, subcription=0):
        self.username = username
        self.subscribers = subscribers
        self.subcription = subcription
    
    def subscribe(self,user):
        user.subscribers +=1
        self.subcription += 1

user1=YouTube("khoa")
user2=YouTube("bi")
user1.subscribe(user2)
user2.subscribe(user1)

print(f"user1 subscribeds: {user1.subscribers}")
print(f"user1 subscription: {user1.subscribers}")
print(f"user2 subscribeds: {user2.subscribers}")
print(f"user2 subscription: {user2.subscribers}")