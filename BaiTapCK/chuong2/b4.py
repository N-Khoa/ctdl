def inNhomChung(mang):
    bac = len(mang)
    for i in range(bac):
        for j in range(i + 1, bac):
            if mang[i] == mang[j]:
                print("Nhóm chỉ mục hàng giống nhau:")
                print("Hàng", i + 1)
                print("Hàng", j + 1)
                print()

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

mang = nhapMaTran()
print(inNhomChung(mang))