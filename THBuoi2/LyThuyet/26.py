def My_function(integers, number=1):
    # Tạo danh sách boolean kết quả
    result = [x == number for x in integers]
    return any(result)

# Kiểm tra hàm với các test cases
my_list = [1, 3, 9, 4]
assert My_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(My_function(my_list))
