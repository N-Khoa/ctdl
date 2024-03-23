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


def trungHang(mang):
    bac = len(mang)
    for i in range(0,bac):
        for j in range(i+1,bac):
            if mang[i]==mang[j]:
                return True
    return False

mang = nhapMaTran()
print(trungHang(mang))
