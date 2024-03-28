def my_function(x, y):
    # Sử dụng phương thức extend để nối danh sách y vào danh sách x
    x.extend(y)
    # Trả về danh sách x mới đã nối
    return x

# Kiểm tra hàm với các test cases
list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

assert my_function(list_num1, my_function(list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

print(my_function(list_num1, my_function(list_num2, list_num3)))
