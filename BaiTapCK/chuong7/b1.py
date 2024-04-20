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

    def LienThong(self):
        visited = [False] * self.V
        self.DFS_util(0, visited)  # Duyệt từ đỉnh 0

        # Kiểm tra xem tất cả các đỉnh có được duyệt qua không
        for v in range(self.V):
            if not visited[v]:
                return False
        
        return True

# Ví dụ sử dụng:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 4)

if g.LienThong():
    print("Đồ thị là đồ thị liên thông.")
else:
    print("Đồ thị không liên thông.")
