def toBinary(n):
    if n > 1:
        toBinary(n//2)
    print(n % 2, end='')

toBinary(15)