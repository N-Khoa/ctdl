max_int = 2**31 - 1

def nhan(mang):
    temp = 1
    temp = sum(temp*i for i in mang)
    if temp > max_int:
        return -1
    return temp
