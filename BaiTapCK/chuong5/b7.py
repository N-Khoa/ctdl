class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def Chep(self, node):
        if node is None:
            return None
        
        # Tạo một nút mới với thông tin từ nút gốc ban đầu
        new_node = Node(node.info)
        
        # Sao chép các cây con bên trái và bên phải của nút
        new_node.left = self.Chep(node.left)
        new_node.right = self.Chep(node.right)
        
        return new_node

    def SaoChep(self):
        return self.Chep(self.root)

# Ví dụ sử dụng:
# Xây dựng cây nhị phân gốc
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Sao chép cây nhị phân gốc
copied_tree = BinaryTree()
copied_tree.root = tree.SaoChep()

# In thông tin của cây nhị phân gốc và cây đã sao chép
def inCay(node):
    if node:
        inCay(node.left)
        print(node.info, end=" ")
        inCay(node.right)

print("Cây nhị phân gốc:")
inCay(tree.root)
print("\nCây đã sao chép:")
inCay(copied_tree.root)
