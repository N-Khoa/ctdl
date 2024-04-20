class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def CanBangHoanToan(self):
        if self.root is None:
            return True
        
        stack = [(self.root, 0)]  # Stack chứa các cặp (node, height)
        while stack:
            node, height = stack.pop()
            
            # Kiểm tra nút hiện tại
            if node.left is None and node.right is None:
                continue
            
            # Tính chiều cao của cây con bên trái và bên phải
            left_height = self.ChieuCao(node.left)
            right_height = self.ChieuCao(node.right)

            # Kiểm tra độ chênh lệch
            if abs(left_height - right_height) > 1:
                return False

            # Thêm các nút con vào stack để kiểm tra tiếp
            if node.left:
                stack.append((node.left, height + 1))
            if node.right:
                stack.append((node.right, height + 1))

        return True

    def ChieuCao(self, node):
        if node is None:
            return 0
        else:
            return max(self.ChieuCao(node.left), self.ChieuCao(node.right)) + 1

# Ví dụ sử dụng:
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

if tree.CanBangHoanToan():
    print("Cây là cây cân bằng hoàn toàn.")
else:
    print("Cây không phải là cây cân bằng hoàn toàn.")
