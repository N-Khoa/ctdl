class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def ChieuCao(self, node):
        if node is None:
            return 0
        else:
            return max(self.ChieuCao(node.left), self.ChieuCao(node.right)) + 1

    def KiemTraAVL(self):
        if self.root is None:
            return True
        
        queue = [(self.root, float('-inf'), float('inf'))]  # Hàng đợi chứa các nút cần kiểm tra
        while queue:
            node, min_val, max_val = queue.pop(0)
            
            # Kiểm tra độ cân bằng của nút
            balance_factor = self.ChieuCao(node.left) - self.ChieuCao(node.right)
            if abs(balance_factor) > 1:
                return False
            
            # Kiểm tra giá trị của nút
            if not (min_val < node.info < max_val):
                return False
            
            # Thêm cây con bên trái và bên phải vào hàng đợi
            if node.left:
                queue.append((node.left, min_val, node.info))
            if node.right:
                queue.append((node.right, node.info, max_val))
        
        return True

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

# Kiểm tra xem cây có phải là AVL hay không
if tree.KiemTraAVL():
    print("Cây là một cây AVL.")
else:
    print("Cây không phải là một cây AVL.")
