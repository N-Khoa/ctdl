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

def tamGiacDuoi(mang):
    bac = len(mang)
    for i in range(bac):
        for j in range(i+1,bac):
            if mang[i][j] != 0:
                return False          
    return True 

print(tamGiacDuoi([[1,0,0],[1,2,0],[1,2,3]]))
