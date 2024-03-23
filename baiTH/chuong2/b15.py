def dayConDaiNhat(a,b):
    lenA = len(a)
    lenB = len(b)
    max_len = 0 
    max_end = 0  
    i = 0 
    j = 0
    while i < lenA and j < lenB:
        length = 0
        while i + length < lenA and j + length < lenB and a[i + length] == b[j + length]:
            length += 1
            if length > max_len:
                max_len = length
                max_end = i + length
        if length == 0:
            i += 1
        else:
            j += 1
    c = a[max_end - max_len:max_end]
    return c