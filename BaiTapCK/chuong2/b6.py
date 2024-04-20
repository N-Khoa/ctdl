def tru(mang):
    temp = mang[0]
    for i in mang[1:]:
        temp -= i
    return temp