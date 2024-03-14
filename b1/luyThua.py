# n^m 
def luyThua(n,m):
    if m==1:
        return n
    else: 
        return n*luyThua(n,m-1)
    
print(luyThua(2,5)) 