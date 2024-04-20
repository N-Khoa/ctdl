class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def SoCungRa(self, v):
        return len(self.adj[v])

# Ví dụ sử dụng:
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

# Tính số cung ra khỏi đỉnh 2
so_cung_ra_2 = g.SoCungRa(2)
print("Số cung ra khỏi đỉnh 2 là:", so_cung_ra_2)

# Tính số cung ra khỏi đỉnh 3
so_cung_ra_3 = g.SoCungRa(3)
print("Số cung ra khỏi đỉnh 3 là:", so_cung_ra_3)
