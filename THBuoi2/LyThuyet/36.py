def function_helper(x):
    # Kiểm tra xem x có lớn hơn 0 không và trả về 'T' hoặc 'N' tương ứng
    if x > 0:
        return 'T'
    else:
        return 'N'

def my_function(data):
    # Sử dụng function_helper để tạo danh sách mới res
    res = [function_helper(x) for x in data]
    return res

# Kiểm tra hàm với các test cases
data = [10, 0, -10, -1]
assert my_function(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(my_function(data))
