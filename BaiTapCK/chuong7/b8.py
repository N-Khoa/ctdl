class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def DFS(self, v, visited, target):
        visited[v] = True
        if v == target:
            return True
        for i in self.adj[v]:
            if not visited[i]:
                if self.DFS(i, visited, target):
                    return True
        return False

    def DuongDi(self, v1, v2):
        visited = [False] * self.V
        return self.DFS(v1, visited, v2)

# Ví dụ sử dụng:
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

# Kiểm tra có đường đi từ đỉnh 0 đến đỉnh 5
if g.DuongDi(0, 5):
    print("Có đường đi từ đỉnh 0 đến đỉnh 5.")
else:
    print("Không có đường đi từ đỉnh 0 đến đỉnh 5.")
