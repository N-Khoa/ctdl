class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def SoCungVao(self, v):
        count = 0
        for i in range(self.V):
            for j in self.adj[i]:
                if j == v:
                    count += 1
        return count

# Ví dụ sử dụng:
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

# Tính số cung vào đỉnh 3
so_cung_vao_3 = g.SoCungVao(3)
print("Số cung vào đỉnh 3 là:", so_cung_vao_3)

# Tính số cung vào đỉnh 5
so_cung_vao_5 = g.SoCungVao(5)
print("Số cung vào đỉnh 5 là:", so_cung_vao_5)
