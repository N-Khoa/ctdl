def anagram(a,b):
    a=a.replace(" ", "")
    list_1 = list(a)
    list_1.sort()
    b=b.replace(" ", "")
    list_2 = list(b)
    list_2.sort()
    return list_1 ==list_2

print(anagram("restful",  "fluster"))
