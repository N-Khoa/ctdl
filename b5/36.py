class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

new_linker_list = LinkedList(10)
print(new_linker_list)
