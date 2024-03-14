
list = [[1,2,3],[4,5,6],[7,8,9]]

n=len(list)
for i in range(0,n):
    for j in range (i,n):
        temp = list[i][j]
        list[i][j] = list[j][i]
        list[j][i] = temp
for i in range(len(list)):
    low = 0
    high = n-1
    while(low < high):
        temp = list[i][low]
        list[i][low] = list[i][high]
        list[i][high] = temp
        low+=1
        high-=1
print(list,sep="===")
