class HanoiTower:
    def __init__(self, n):
        self.n = n
        self.towers = [[], [], []]
        for i in range(n, 0, -1):
            self.towers[0].append(i)

    def move(self, n, source, target, auxiliary):
        if n > 0:
            self.move(n-1, source, auxiliary, target)
            moved_disk = self.towers[source].pop()
            self.towers[target].append(moved_disk)
            print(f"Di chuyển tầng {moved_disk} từ tháp {source+1} đến tháp {target+1}")
            self.move(n-1, auxiliary, target, source)

    def display(self):
        for i in range(self.n):
            print("Tầng", i+1, ":", self.towers[i])


