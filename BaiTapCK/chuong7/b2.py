class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Đồ thị vô hướng

    def DFS_util(self, v, visited):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                self.DFS_util(i, visited)

    def SoThanhPhan(self):
        visited = [False] * self.V
        count = 0
        for v in range(self.V):
            if not visited[v]:
                self.DFS_util(v, visited)
                count += 1
        return count

# Ví dụ sử dụng:
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 4)
g.add_edge(5, 6)

so_thanh_phan = g.SoThanhPhan()
print("Số thành phần liên thông của đồ thị:", so_thanh_phan)
