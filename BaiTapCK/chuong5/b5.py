class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def KiemTraBST(self, node, min_val=float("-inf"), max_val=float("inf")):
        if node is None:
            return True
        
        # Kiểm tra giá trị của nút hiện tại
        if not (min_val < node.info < max_val):
            return False
        
        # Kiểm tra cây con bên trái và bên phải của nút hiện tại
        return (self.KiemTraBST(node.left, min_val, node.info) and
                self.KiemTraBST(node.right, node.info, max_val))

    def LaCayBST(self):
        return self.KiemTraBST(self.root)

# Ví dụ sử dụng:
# Xây dựng cây nhị phân
tree = BinaryTree()
tree.root = Node(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

# Kiểm tra xem cây có phải là BST hay không
if tree.LaCayBST():
    print("Cây là một cây BST.")
else:
    print("Cây không phải là một cây BST.")
