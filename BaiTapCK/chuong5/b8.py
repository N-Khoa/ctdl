class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoSanh(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        
        # So sánh giá trị của hai nút
        if node1.info != node2.info:
            return False
        
        # So sánh cây con bên trái và bên phải của từng nút
        return (self.SoSanh(node1.left, node2.left) and
                self.SoSanh(node1.right, node2.right))

# Ví dụ sử dụng:
# Xây dựng cây nhị phân 1
tree1 = BinaryTree()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)

# Xây dựng cây nhị phân 2
tree2 = BinaryTree()
tree2.root = Node(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)

# So sánh hai cây nhị phân
if tree1.SoSanh(tree1.root, tree2.root):
    print("Hai cây nhị phân giống nhau.")
else:
    print("Hai cây nhị phân không giống nhau.")
