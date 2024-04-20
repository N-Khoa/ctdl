class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoSanhCay(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        
        # So sánh giá trị của hai nút
        if node1.info != node2.info:
            return False
        
        # So sánh cây con bên trái và bên phải của từng nút
        return (self.SoSanhCay(node1.left, node2.left) and
                self.SoSanhCay(node1.right, node2.right))

    def CayCon(self, tree1, tree2):
        if tree1 is None or tree2 is None:
            return False
        
        # Duyệt qua từng nút của cây gốc của tree1
        def Duyet(node):
            if node is None:
                return False
            
            # Kiểm tra nút hiện tại có giống với gốc của tree2 không
            if self.SoSanhCay(node, tree2.root):
                return True
            
            # Kiểm tra cây con bên trái và bên phải của nút hiện tại
            return Duyet(node.left) or Duyet(node.right)
        
        return Duyet(tree1.root)

# Ví dụ sử dụng:
# Xây dựng cây nhị phân 1
tree1 = BinaryTree()
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)

# Xây dựng cây nhị phân 2 (là một cây con của cây 1)
tree2 = BinaryTree()
tree2.root = Node(2)
tree2.root.left = Node(4)
tree2.root.right = Node(5)

# Kiểm tra xem cây 2 có phải là cây con của cây 1 không
if tree1.CayCon(tree1, tree2):
    print("Cây 2 là cây con của cây 1.")
else:
    print("Cây 2 không phải là cây con của cây 1.")
