class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while temp:
            if value == temp.value:
                return False
            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right


bst = BinarySearchTree()
bst.insert(19)
bst.insert(3)
bst.insert(22)
bst.insert(10)

def print_tree(node):
    if node is None:
        return
    print(node.value)
    print_tree(node.left)
    print_tree(node.right)

print("Binary Search Tree:")
print_tree(bst.root)