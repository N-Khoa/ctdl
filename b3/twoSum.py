
def twoSum(list,target):
    temp=[]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j] ==target:
                temp.append(f"[{i}, {j}]")
    if len(temp)==0:
        return "none"
    else:
        return temp
    
list =[2,7,11,5,4]
target= 9
print(*twoSum(list,target))

    