def tongChuSo(n):
    if n<10:
        return n
    else:
        return n%10 + tongChuSo(int(n/10))

print(tongChuSo(12345))