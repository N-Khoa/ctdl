t = (1, 2, 3)

print(t[0])
print(t[1])
print(t[2])

t = 1, 2
print(t)
print(type(t))

singleton = (1, )
print(singleton)

var1 = (1 + 2) * 5
print(type(var1), ' ', var1)

var2 = (1)
print(type(var2), ' ', var2)

var3 = (1,)
print(type(var3), ' ', var3)

t = (1,) * 5
print(t)

t1 = (1, 0)
print(t1)

t1 += (2,)
print(t1)

t = (1,2,3,1)
count = t.count(1)
index = t.index(2)

print(count)
print(index)

d = dict([('jan', 1), ('feb', 2), ('march', 3)])

print(d['jan'])
print(d['feb'])
print(d['march'])

x1,y1,z1   = ('a','b','c')
(x2,y2,z2) = ('a','b','c')
(x3,y3,z3) = range(3)

print(x1)
print(x2)
print(x3)

x1,y1,z1   = ('a','b','c')
(x2,y2,z2) = ('a','b','c')
print(x1)
print(x2)

(x,y,z) = range(3)
print(x,y,z)

a = range(3)
print(type(a))

d = {'first':'string value', 'second':1}
for a in d:
    print(a)

d = {'first':'string value', 'second':[1,2]}
items = d.items()
print('items:', items)
for k,v in items:
    print(k, v)

data  = (1,2,3)
x, y, z = data
print(x)

x = 4
y = 5

print(x, y)

#(x,y) = (y,x)
x,y = y,x
print(x, y)

def swap(v1, v2):
    (v2, v1) = (v1, v2)
    return (v1, v2)


v1 = 2
v2 = 3
(v1, v2) = swap(v1, v2)

# print
print(v1)
print(v2)

t = (1, 2, 3, 4)
len(t)

data = (1, 2, 3, 4, 5)
print(data[2:])
print(data[::-1])

# t = (1, 2, 3, 4, 5)

# new_t = t.copy()
# print(new_t)

t = (1, 2, [3, 10])
t[2][0] = 9
print(t)

t = (1, 2, [3, 10])
t[2][1] = 4
print(t)

# t = (1, 2, 3, 4, 5)
# t[2] = 9
# print(t)

data = (1, 2, 3, 4, 5)
data_str = str(data)
print(data_str)
print(type(data_str))

print(data_str[0])

t = (1, 2, 3, 4, 5)

print(min(t))
print(max(t))
print(sum(t))

t = (4, 7, 3, 9, 6)
t_s = sorted(t)
print(t_s)

t1 = (1, 2, 3, 4, 5)
t2 = ('a', 'b', 'c', 'd', 'e')

print(t1)
print(t2)

t3 = zip(t1, t2)
for x,y in t3:
    print(x, y)

import math

def quadratic_equation(a, b, c):
    '''
    This function aims at solving the quadratic equation
    a, b, c --- three parameters and a =! 0
    '''
    
    # compute delta
    delta = b*b - 4*a*c

    if delta < 0:
        return ()
    elif delta == 0:
        x = (-b+math.sqrt(delta))/2*a
        return (x,)
    else:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        return (x1,x2)


result = quadratic_equation(a=5, b=0, c=1)
print(type(result))
print(len(result))
print(result)

result = quadratic_equation(a=5, b=5, c=1)
print(type(result))
print(len(result))
print(result)

result = quadratic_equation(a=4, b=4, c=1)
print(type(result))
print(len(result))
print(result)

# result = quadratic_equation(a=4, b=4, c=1)
# result[0] = 1

# tuple and zip

x_data = [1, 2, 3]
y_data = [5, 6, 7]
data = zip(x_data, y_data)

# print
for d in data:
    print(d)
    print(type(d))

# memory comparison
import sys

aList  = [3, 4, 5, 6, 7]
aTuple = (3, 4, 5, 6, 7)

print(sys.getsizeof(aList))
print(sys.getsizeof(aTuple))

# convert from list to tuple
aList  = [3, 4, 5, 6, 7]
aTuple = tuple(aList)

print(aTuple)
print(type(aTuple))

# convert from tuple to list
aTuple  = (3, 4, 5, 6, 7)
aList = list(aList)

print(aList)
print(type(aList))

