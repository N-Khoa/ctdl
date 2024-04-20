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
            # Tính chiều cao của cây con bên trái và bên phải
            chieucao_trai = self.ChieuCao(node.left)
            chieucao_phai = self.ChieuCao(node.right)

            # Trả về chiều cao lớn nhất cộng thêm 1 cho nút hiện tại
            return max(chieucao_trai, chieucao_phai) + 1

    def ChieuCaoCay(self):
        return self.ChieuCao(self.root)

# Ví dụ sử dụng:
# Xây dựng cây nhị phân
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.right = Node(5)


# In chiều cao của cây
print("Chiều cao của cây là:", tree.ChieuCaoCay()) # Kết quả: 4
