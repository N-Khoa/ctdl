def giaiThua(n):
    if n == 1:
        return 1
    return giaiThua(n-1) *n

print(giaiThua(4))