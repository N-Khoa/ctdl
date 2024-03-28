def my_function(n):
    # Trả về giá trị nhỏ nhất trong danh sách
    return min(n)

# Kiểm tra hàm với các test cases
my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function(my_list))
