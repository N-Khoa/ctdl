import numpy as np

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
n=len(matrix)
for i in range(0,n):
    for j in range (i,n):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp
for i in range(len(matrix)):
    low = 0
    high = n-1
    while(low < high):
        temp = matrix[i][low]
        matrix[i][low] = matrix[i][high]
        matrix[i][high] = temp
        low+=1
        high-=1
print(matrix)

