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

def tamGiacTren(mang):
    bac = len(mang)
    for i in range(1,bac):
        for j in range(0,i):
            if mang[i][j] != 0:
                return False          
    return True 

mang = nhapMaTran()
print(tamGiacTren(mang))
