def pascal(n):
    for i in range(n+1):
        C = 1
        for j in range(1, i+1):
            print(' ', C, sep='', end='')
            C = C * (i - j) // j
        print()

