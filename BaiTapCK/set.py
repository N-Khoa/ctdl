# create a set
animals = {"cat", "dog", "tiger"}

print(type(animals))
print(animals)

# create a set
a_set = {"cat", 5, True, 40.0}

print(type(a_set))
print(a_set)

# No duplication
animals = {"cat", "dog", "tiger"}
print(animals)

animals.add("cat")
print(animals)

# copy
animals = {"cat", "dog", "tiger"}
print("Animals:", animals)

a_copy = animals.copy()
print("Copy:", a_copy)

# accessing items
animals = {"cat", "dog", "tiger"}
for animal in animals:
    print(animal)

# # not support indexing
# animals = {"cat", "dog", "tiger"}
# print(animals[1])

# add an item
animals = {"cat", "dog", "tiger"}
animals.add("bear")
print(animals)

# insert a set to another set
animals = {"cat", "dog", "tiger"}
animals.update({"chicken","Duck"})
print(animals)

# join two sets
set1 = {"cat", "dog"}
set2 = {"duck", "tiger"}

set3 = set1.union(set2)
print(set3)

# remove an item
animals = {"cat", "dog", "tiger"}
animals.remove("dog")
print(animals)

# remove an item
animals = {"cat", "dog", "tiger"}
animals.discard("tiger")
print(animals)

# # remove an item
# animals = {"cat", "dog", "tiger"}
# animals.remove("duck")
# print(animals)

# remove an item
animals = {"cat", "dog", "tiger"}
animals.discard("duck")
print(animals)

# create a set
# a_list = [1, 2, 3]
# a_set  = {"cat", a_list}
# print(a_set)

# difference 

set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "apple"}

set3 = set1.difference(set2)

print(set3)

# difference_update

set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "apple"}

set1.difference_update(set2)

print(set1)

# difference_update

set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "apple"}

set1.difference_update(set2)

print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "apple"}

print(id(set1))
set1.difference_update(set2)

print(set1)
print(id(set1))

# symmetric_difference

set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# symmetric_difference_update

set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

# AND (&)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 & set2)

# OR (|)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)

# XOR (^)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 ^ set2)

# subtraction (-)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 - set2)

# set comprehension

aSet = {i*i for i in range(10)}
print(aSet)

# convert from set to list
aSet = {1, 2, 3, 4, 5}

aList = list(aSet)
print(aList)
print(type(aList))

# convert from set to tuple
aSet = {1, 2, 3, 4, 5}

aTuple = tuple(aSet)
print(aTuple)
print(type(aTuple))

# convert from list to set
aList = [1, 2, 3, 2, 1]

aSet = set(aList)
print(aSet)
print(type(aSet))

# convert from tuple to set
aTuple = (1, 2, 3, 2, 1)

aSet = set(aTuple)
print(aSet)
print(type(aSet))

# # kết nối với file
# a_file = open('data.txt','r') 

# # read content
# data = a_file.read()
# print(data)

# # Đóng kết nối với file
# a_file.close()