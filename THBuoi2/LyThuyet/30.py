def my_function(data):
    var = []
    for i in data:
        if i % 3 == 0:  # Kiểm tra xem i có chia hết cho 3 không
            var.append(i)  # Nếu có, thêm i vào danh sách var
    return var

# Kiểm tra hàm với các test cases
assert my_function([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 5, 6]))
