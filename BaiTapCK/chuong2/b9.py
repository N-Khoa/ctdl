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

def trungCot(mang):
    bac = len(mang)
    for j in range(bac):
        for k in range(j + 1, bac):
            cot_j = [mang[i][j] for i in range(bac)]
            cot_k = [mang[i][k] for i in range(bac)]
            if cot_j == cot_k:
                return True
    return False
