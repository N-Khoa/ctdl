class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = None

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self, value):
        if self.isFull():
            return  "The stack is full"
        else:
            self.list.append(value)
            return "The element has been seccessed inserted"
        
customSack = Stack(4)
print(customSack.isEmpty())
print(customSack.isFull())
customSack.push(1)
customSack.push(2)
customSack.push(3)
print(customSack)