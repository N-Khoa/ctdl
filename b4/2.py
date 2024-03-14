def palindrome(a):
    b=a[::-1]
    return a==b

print(palindrome("123456789"))
print(palindrome("123456789987654321"))
print(palindrome("hello"))
print(palindrome("hellolleh"))
