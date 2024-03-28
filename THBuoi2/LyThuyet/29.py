def my_function ( signal1 , signal2 ) :
    var = False
    for s1 in signal1 :
        for s2 in signal2 :
            if s1 == s2 :
                var = True
    return var
print ( my_function ([1 , 2 , 3] , [2 , 2]) )