def intersection(lst1, lst2):
    count_lst1 = {}
    for num in lst1:
        count_lst1[num] = count_lst1.get(num, 0) + 1
    result = []
    for num in lst2:
        if num in count_lst1 and count_lst1[num] > 0:
            result.append(num)
            count_lst1[num] -= 1
    
    return result
test_list1 = [4, 9]
test_list2 = [9, 2]
assert intersection(lst1=test_list1, lst2=test_list2) == [9]

num_list1 = [4, 9, 5]
num_list2 = [9, 4, 9, 8, 4]
print(intersection(num_list1, num_list2))
