class DSLK:
    class Node:
        def __init__(self, info):
            self.info = info
            self.next = None

    def __init__(self):
        self.head = None

    def themNode(self, info):
        new_node = self.Node(info)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def inNguocDeQui(self, node):
        if node is None:
            return
        self.inNguocDeQui(node.next)
        print(node.info, end=" ")

    def inNguocKhongDeQui(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.info)
            current = current.next
        while stack:
            print(stack.pop(), end=" ")
