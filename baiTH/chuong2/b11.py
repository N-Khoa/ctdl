def cong(dauA, soA, dauB, soB):
    a = int(''.join(map(str, soA)))
    b = int(''.join(map(str, soB)))
    if dauA == 1:
        a *= -1
    if dauB == 1:
        b *= -1
    result = a + b
    if result > 2**31 - 1 or result < -(2**31):
        return [-1]
    else:
        return result
    