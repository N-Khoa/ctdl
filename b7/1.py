class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False
        
custonStack = Stack()
print(custonStack.isEmpty())