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

def DoiXung(mang):
    n = len(mang)
    for i in range(n):
        for j in range(n):
            if mang[i][j] != mang[j][i]:
                return False          
    return True 


mang = nhapMaTran()
print(DoiXung(mang))
