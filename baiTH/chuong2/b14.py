def dayConDauTien(a,b):
    c=[]
    lenA=len(a)
    for i in range(0,lenA-1):
        if a[i]in b:
            index = b.index(a[i]) +1
            if a[i+1] == b[index]:
                c.append(a[i])
                c.append(a[i+1])
                return c
    return c    

print(dayConDauTien([1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5],[6, 2, 5, 3, 7, 9, 8, 1, 5]))