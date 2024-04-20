# walrus operator creates an assignment expression

is_new = True
print(is_new)

print(is_new := True)

words = ['falcon', 'sky', 'ab', 'water', 'a', 'forest']

for word in words:
    if ((n := len(word)) < 3):
        print(f'warning, the word {word} has {n} characters')

def say_hi(name):
    return f'Hi {name}'

greeting = say_hi('John')
print(greeting)

def say_hi(name: str) -> str:
    print(type(name))
    return f'Hi {name}'

greeting = say_hi('John')
print(greeting)

greeting = say_hi(123)
print(greeting)

# lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def square(x): 
    return x*x
[square(x) for x in range(10)]

f = lambda x: x*x
[f(x) for x in range(10)]

[(lambda x: x*x)(x) for x in range(10)]

[lambda x: x*x for x in range(10)]

