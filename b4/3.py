def reversion_exercise(a):
    temp = 0
    while a !=0:
        temp = temp*10 + a%10
        a=a//10
    return temp

a=12345
print(reversion_exercise(a))
