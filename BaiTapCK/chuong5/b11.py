class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def KiemTraBSTTuanTu(self):
        if self.root is None:
            return True
        
        # Duyệt cây theo thứ tự tuần tự
        in_order = self.InOrder(self.root)

        # Kiểm tra nếu tất cả các nút đều chỉ có nút con bên trái hoặc bên phải
        for i in range(len(in_order) - 1):
            if (in_order[i].left is not None and in_order[i].right is not None) or \
               (in_order[i].left is None and in_order[i].right is None):
                continue
            else:
                return False
        
        return True

    def InOrder(self, node):
        result = []
        stack = []

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node)
                node = node.right

        return result

# Ví dụ sử dụng:
tree = BinaryTree()
tree.root = Node(2)
tree.root.left = Node(1)
tree.root.right = Node(3)
tree.root.right.right = Node(4)

if tree.KiemTraBSTTuanTu():
    print("Cây là cây BST tìm kiếm tuần tự.")
else:
    print("Cây không phải là cây BST tìm kiếm tuần tự.")
