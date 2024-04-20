class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Đồ thị vô hướng

    def ChuaDinh(self, v):
        # Kiểm tra xem có cạnh nào kết nối với đỉnh v không
        if self.adj[v]:
            return True
        else:
            return False

# Ví dụ sử dụng:
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Kiểm tra đỉnh 0
if g.ChuaDinh(0):
    print("Đỉnh 0 thuộc đồ thị.")
else:
    print("Đỉnh 0 không thuộc đồ thị.")

# Kiểm tra đỉnh 5
if g.ChuaDinh(5):
    print("Đỉnh 5 thuộc đồ thị.")
else:
    print("Đỉnh 5 không thuộc đồ thị.")
