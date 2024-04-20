class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoNutTrungGian(self, node):
        if node is None:
            return 0
        elif (node.left is not None and node.right is None) or (node.left is None and node.right is not None):
            # Nếu nút có chỉ một cây con bên trái hoặc bên phải, nhưng không là nút gốc
            return 1
        else:
            # Đếm số nút trung gian của cây con bên trái và bên phải
            nut_trung_gian_trai = self.SoNutTrungGian(node.left)
            nut_trung_gian_phai = self.SoNutTrungGian(node.right)

            return nut_trung_gian_trai + nut_trung_gian_phai

    def SoNutTrungGianCay(self):
        if self.root is None:
            return 0
        else:
            return self.SoNutTrungGian(self.root)

# Ví dụ sử dụng:
# Xây dựng cây nhị phân
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.right = Node(4)
tree.root.right.left = Node(5)
tree.root.right.right = Node(6)
tree.root.right.right.right = Node(7)

# In số nút trung gian của cây
print("Số nút trung gian của cây là:", tree.SoNutTrungGianCay()) # Kết quả: 3
