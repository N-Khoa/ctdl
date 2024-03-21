def uoc(n):
    temp =[]   
    for i in range(1,n):
        if n % i == 0: 
            temp.append(i)
    return temp

def number(x,y):
    for n in range(x,y+1):
        temp = uoc(n)
        s = 0
        for j in temp:
            s = s +j
        if s<n:
            print(n, "is defcient")
        elif s == x:
            print(n, "is prefect")
        else:
            print(n, "is abundant")

