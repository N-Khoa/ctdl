import array

def twoSum(arr,target):
    temp=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] ==target:
                temp.append(f"[{i}, {j}]")
    if len(temp)==0:
        return "none"
    else:
        return temp

nums=array.array("i",[2,7,11,5,4])
target= 9
print(*twoSum(nums,target))

    