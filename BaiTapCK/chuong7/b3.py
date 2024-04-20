class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Đồ thị vô hướng

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def ChuTrinh(self):
        visited = [False] * self.V
        for v in range(self.V):
            if not visited[v]:
                if self.is_cyclic_util(v, visited, -1):
                    return True
        return False

# Ví dụ sử dụng:
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 0)

if g.ChuTrinh():
    print("Đồ thị chứa chu trình.")
else:
    print("Đồ thị không chứa chu trình.")
