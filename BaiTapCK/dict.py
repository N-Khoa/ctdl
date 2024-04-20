keys   = ['a', 'b', 'c']
values = [1, 2, 3]

a_dictionary = {(k,v) for (k,v) in zip(keys,values)}
print(a_dictionary)
print(type(a_dictionary))

parameters = {'learning_rate': 0.1,
              'optimizer': 'Adam',
              'metric': 'Accuracy'}

print(parameters)
print(type(parameters))

parameters = {'learning_rate': 0.1,
              'optimizer': 'Adam',
              'metric': 'Accuracy'}

keys   = parameters.keys()
print(keys)

for key in keys:
    print(key)


keys = parameters.keys()
for key in keys:
    print(key)

values = parameters.values()
for value in values:
    print(value)

parameters = {'learning_rate': 0.1,
              'optimizer': 'Adam',
              'metric': 'Accuracy'}

items = parameters.items()
for key, value in items:
    print(key, value)


parameters = {'learning_rate': 0.1,
              'optimizer': 'Adam',
              'metric': 'Accuracy'}

for key in parameters:
    print(key)

parameters = {'learning_rate': 0.1,
              'optimizer': 'Adam',
              'metric': 'Accuracy'}

value = parameters.get('learning_rate')
print(value)

print('\nAfter using get() function')
print(parameters)

parameters = {'learning_rate': 0.1,
              'optimizer': 'Adam',
              'metric': 'Accuracy'}

value = parameters.pop('learning_rate')
print(value)

print('\nAfter using pop() function')
print(parameters)

parameters = {'learning_rate': 0.1,
              'optimizer': 'Adam',
              'metric': 'Accuracy'}

value = parameters.get('algorithm')
print(value)

# parameters = {'learning_rate': 0.1,
#               'optimizer': 'Adam',
#               'metric': 'Accuracy'}

# value = parameters.pop('algorithm')

parameters = {'learning_rate': 0.1,
              'optimizer': 'Adam',
              'metric': 'Accuracy'}

item = parameters.popitem()

print(item)
print(parameters)

parameters = {'learning_rate': 0.1,
              'metric': 'Accuracy'}

print('Before using clear() function')
print(parameters)

parameters.clear()

print('\nAfter using clear() function')
print(parameters)

# parameters = {'learning_rate': 0.1,
#               'metric': 'Accuracy'}

# del parameters['algorithm']

parameters = {'learning_rate': 0.1,
              'metric': 'Accuracy'}

a_copy = parameters.copy()
a_copy['learning_rate'] = 0.2

print(parameters)
print(a_copy)

parameters = {'learning_rate': 0.1,
              'metric': 'Accuracy'}

parameters['learning_rate'] = 0.2
print(parameters)

for key in parameters:
    print(key, parameters.get(key))

d = {'first':'string value', 'second':[1,2]}
keys = d.keys()
values = d.values()

print(keys)
print(values)

d = {'first':'string value', 'second':[1,2]}
d.values()

d = {'first':'string value', 'second':[1,2]}
print(d['first'])
print(d['second'])

d = {'first':'string value', 'second':[1,2]}
items = d.items()

print('items:', items)
for k,v in items:
    print(k, v)

# d = {'first':'string value', 'second':[1,2]}
# d._contain_('first')

d = {'first':'string value', 'second':[1,2]}
value = d.get('first')

print(value)
print(d)

d = {'first':'string value', 'second':[1,2]}
value = d.pop('first')

print(value)
print(d)

d = {'1':'value1', '2':'value2', '3':'value3', '4':'value4'}
item = d.popitem()

print(item)
print(d)

# d1 = {'a': [1,2]}
# d2 = d1
# d2['a'] = [1,2,3,4]
# d1['a]

d1 = {'a': [1,2]}
d2 = d1.copy()

print('d1:', d1)
print('d2:', d2)

d1 = {'a': [1,2], 'b': 5}
d2 = d1.copy()

# thay đổi giá trị d2 sẽ ảnh hưởng đến d1
d2['a'][0] = 3
d2['a'][1] = 4

print('d1:', d1)
print('d2:', d2)

import copy

d1 = {'a': [1,2], 'b': 5}
d2 = copy.deepcopy(d1)

# thay đổi giá trị d2 
d2['a'][0] = 3
d2['a'][1] = 4

print('d1:', d1)
print('d2:', d2)

d = {'a': [1,2], 'b': 5}
print(d)

d.clear()
print(d)

d = {'a': [1,2], 'b': 5}
print(d)

del d['a']
print(d)

# d = {'a': [1,2], 'b': 5}
# print(d)

# del d
# print(d)

d = {'a':1, 'b':2, 'c':3}
del d['a']
print(d)

d1 = {'a': [1,2]}
d2 = d1.copy()
d2.setdefault('third', '')
d2['third']
print(d2)

d = {'a':1, 'b':2, 'c':3}

d2.setdefault('third', '')

d1 = {'a': [1,2]}
d2 = d1.copy()
d2.fromkeys(['first', 'second'])

{}.fromkeys(['first', 'second'])

# d1 = {'a':1}
# d2 = {'a':2; 'b':2}
# d1.update(d2)
# d1['a']
# d2['b']

d1 = {'a':1}
d2 = {'b':2, 'c':3}

print('d1:', d1)
print('d2:', d2)

d1.update(d2)
print('d1 sau khi update:', d1)

# [x for x in t.itervalues()]
# [x for x in t.iterkeys()]
# [x for x in t.iteritems()]

l_keys   = ['a', 'b', 'c', 'd', 'e']
l_values = [1, 2, 3, 4, 5]

d = {(k,v) for (k,v) in zip(l_keys,l_values)}
print(d)

# dic comprehension

aDict = {str(i):i for i in range(5)}
print(aDict)

# from zip

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

a_dict = dict(zip(tuple1, tuple2))
print(type(a_dict))
print(a_dict)

# from zip

set1 = {1, 2, 3}
set2 = {4, 5, 6}

a_dict = dict(zip(set1, set2))
print(type(a_dict))
print(a_dict)

# from zip

list1 = [1, 2, 3]
list2 = [4, 5, 6]

a_dict = dict(zip(list1, list2))
print(type(a_dict))
print(a_dict)

# setdefault()

fruits = {'banana': 2}
fruits.setdefault('apple', 0)

print(fruits)

# setdefault()

fruits = {'banana': 2, 'apple': 4}
fruits.setdefault('apple', 0)

print(fruits)

# setdefault()

fruits = {'banana': 2}
fruits.setdefault('apple', 0)

fruits['apple'] += 10
print(fruits)

# # setdefault()

# fruits = {'banana': 2}

# fruits['apple'] += 10
# print(fruits)

# fruits = {'banana': 2, 'apple': 4}
# result = {**fruits, **cereal}
# print(**fruits)

# merge two dicts

fruits = {'banana': 2, 'apple': 4}
cereal = {'rice': 3, 'corn': 7}

result = {**fruits, **cereal}
print(result)

# check if a key exists

fruits = {'banana': 2, 'apple': 4}

print('apple' in fruits)
print('corn' in fruits)

# remove empty items

fruits = {'banana': 2, 'apple': None}

dict1 = {key:value for (key, value) 
                     in fruits.items() 
                     if value is not None}
print(dict1)

# access value via key

fruits = {'banana': 2, 'apple': 4}
print(fruits.get('apple'))
print(fruits.get('corn'))

# # access value via key

# fruits = {'banana': 2, 'apple': 4}
# print(fruits['apple'])
# print(fruits['corn'])

# import json

# parameters = {'learning_rate': 0.1,
#               'optimizer': 'Adam',
#               'metric': 'Accuracy'}

# with open('data.json', 'w') as fp:
#     json.dump(parameters, fp)

# with open('data.json', 'r') as fp:
#     data = json.load(fp)
#     print(data)

# create a list
aList = [1, 5, 3, 7, 4]
print(aList)

# sort
sortedList = sorted(aList)
print(sortedList)

# create a list
aList = [1, 5, 3, 7, 4]
print(aList)

# function for sorting
def compare(item):
    return item

# sort
sortedList = sorted(aList, key=compare)
print(sortedList)


# data
list1 = [1, 5, 3, 7, 4]
list2 = [16, 13, 18, 11, 15]

# create a dictionary
dictionary = dict(zip(list1, list2))
print(dictionary)

sortedDict = sorted(dictionary)
print(sortedDict)

# data
list1 = ['a', 'g', 'e', 'h', 'b']
list2 = [16, 13, 18, 11, 15]

# create a dictionary
list3 = list(zip(list1, list2))
print(list3)

list4 = sorted(list3)
print(list4)

# data
list1 = ['a', 'g', 'e', 'h', 'b']
list2 = [16, 13, 18, 11, 15]

# function for sorting
def compare(item):
    return item[0]

# create a dictionary
list3 = list(zip(list1, list2))
print(list3)

list4 = sorted(list3, key=compare)
print(list4)

# data
list1 = ['a', 'g', 'e', 'h', 'b']
list2 = [16, 13, 18, 11, 15]

# function for sorting
def compare(item):
    return item[1]

# create a dictionary
list3 = list(zip(list1, list2))
print(list3)

list4 = sorted(list3, key=compare)
print(list4)

# data
list1 = ['a', 'g', 'e', 'h', 'b']
list2 = [16, 13, 18, 11, 15]

# create a dictionary
list3 = list(zip(list1, list2))
print(list3)

list4 = sorted(list3, key=lambda item: item[1])
print(list4)







