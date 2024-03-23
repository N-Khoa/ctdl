def nhapMaTran():
    mang = []
    bac = int(input("Nhap bac cua ma tran: "))
    for i in range(bac):
        row = []
        for j in range(bac):
            phan_tu = int(input(f"Nhap phan tu tai vi tri [{i}][{j}]: "))
            row.append(phan_tu)
        mang.append(row)
    return mang

def dao(mang):
    def is_land(x, y):
        return 0 <= x < n and 0 <= y < n and mang[x][y] == 1

    def dfs(x, y):
        if not is_land(x, y):
            return 0
        mang[x][y] = 0 
        area = 1
        for dx, dy in directions:
            area += dfs(x + dx, y + dy)
        return area

    n = len(mang)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    max_area = 0

    for i in range(n):
        for j in range(n):
            if mang[i][j] == 1:
                max_area = max(max_area, dfs(i, j))
    print("Diện tích lớn nhất của các đảo là:", max_area)

