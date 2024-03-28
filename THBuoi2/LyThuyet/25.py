def my_function(n):
    # Loại bỏ số 0 khỏi danh sách
    filtered_list = [x for x in n if x != 0]
    # Trả về giá trị lớn nhất trong danh sách
    return max(filtered_list)

# Kiểm tra hàm với các test cases
my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))
