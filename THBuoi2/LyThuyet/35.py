def my_function(x):
    # Sử dụng cách cắt chuỗi với bước -1 để đảo ngược chuỗi
    reversed_x = x[::-1]
    return reversed_x

# Kiểm tra hàm với các test cases
x = 'I can do it'
assert my_function(x) == " ti od nac I "

x = 'apricot'
print(my_function(x))
