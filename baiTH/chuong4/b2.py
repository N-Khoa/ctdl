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

    def DaoNguoc(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def inDanhSach(self):
        current = self.head
        while current:
            print(current.info, end=" ")
            current = current.next
        print()

