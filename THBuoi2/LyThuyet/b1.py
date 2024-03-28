def max_in_window(num_list, k=3):
    result = []
    for i in range(len(num_list) - k + 1):
        max_num = max(num_list[i:i+k])
        result.append(max_num)
    return result


test = [3, 4, 5, 1, -44]
assert max_in_window(num_list=test, k=3) == [5, 5, 5]

num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
print(max_in_window(num_list=num_list, k=3))