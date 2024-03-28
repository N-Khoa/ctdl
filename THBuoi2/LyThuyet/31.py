def my_function ( x ) :
    for i in range ( x ) :
        for j in range ( x ) :
            if i == j :
                print (" 1 ", end =" ")
            else :
                print (" 0 ", end =" ")
        print ()    

my_function (2)
