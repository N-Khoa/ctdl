max_int = 2**31 - 1

def cong(mang):
    temp = sum(i for i in mang)
    if temp > max_int:
        return -1
    return temp

