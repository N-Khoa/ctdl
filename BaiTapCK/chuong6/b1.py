def Duynhat(arr):
    unique_arr = []
    for num in arr:
        if num not in unique_arr:
             unique_arr.append(num)
    unique_arr.sort()
    return unique_arr

# Ví dụ sử dụng:
a = [1, 5, 3, 7, 5, 9, 7]
unique_a =Duynhat(a)
print("Mảng b chứa các số duy nhất từ mảng a:", unique_a)
