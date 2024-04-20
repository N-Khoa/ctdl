class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Đồ thị vô hướng

    def BacDinh(self, v):
        # Đếm số cạnh kết nối với đỉnh v
        degree = len(self.adj[v])
        return degree

# Ví dụ sử dụng:
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Tính bậc của đỉnh 2
degree_of_2 = g.BacDinh(2)
print("Bậc của đỉnh 2 là:", degree_of_2)

# Tính bậc của đỉnh 4
degree_of_4 = g.BacDinh(4)
print("Bậc của đỉnh 4 là:", degree_of_4)
