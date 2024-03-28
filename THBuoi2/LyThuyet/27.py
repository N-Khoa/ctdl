def my_function(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)

# Kiểm tra hàm với các test cases
assert my_function([4, 6, 8]) == 6
print(my_function())
