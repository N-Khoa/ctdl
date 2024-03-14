def max_value_key(my_dict):
    max_key = max(my_dict, key=my_dict.get)  # Sử dụng hàm max để tìm key có giá trị lớn nhất, với key được xác định bằng cách sử dụng phương thức get() của từ điển
    print( max_key)

my_dict={'a':5, 'b':9, 'c':2}
max_value_key(my_dict)