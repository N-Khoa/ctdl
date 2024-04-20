class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoNutLa(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1  # Nếu là nút lá thì trả về 1
        else:
            # Đếm số nút lá của cây con bên trái và bên phải
            nut_la_trai = self.SoNutLa(node.left)
            nut_la_phai = self.SoNutLa(node.right)

            return nut_la_trai + nut_la_phai

    def SoNutLaCay(self):
        if self.root is None:
            return 0
        else:
            return self.SoNutLa(self.root)

# Ví dụ sử dụng:
# Xây dựng cây nhị phân
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

# In số nút lá của cây
print("Số nút lá của cây là:", tree.SoNutLaCay()) # Kết quả: 4
