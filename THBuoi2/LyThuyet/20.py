def my_function ( my_data ):
    rs = 0
    for i in my_data :
        rs = rs + i
    return rs
my_list = [1 , 2 , 3]
print ( my_function ( my_data = my_list ) )