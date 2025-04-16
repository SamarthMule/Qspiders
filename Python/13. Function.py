# Functions
# A function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# In Python, there are two types of functions:
# 1. Built-in functions: These are functions that are already defined in Python.
# 2. User-defined functions: These are functions that you define yourself.

# Function Syntax
# def function_name(parameters):
#     """docstring"""
#     statement(s)
#     return value
# The 'def' keyword is used to define a function.
# The 'function_name' is the name of the function. The 'parameters' are optional inputs to the function.
# The 'docstring' is a string that describes the function. The 'statement(s)' are the code that will be executed when the function is called. The 'return' statement is used to return a value from the function.
# The 'return' statement is optional. If there is no return statement, the function will return None by default.
# The 'return' statement can return multiple values in the form of a tuple.
# The function name should be descriptive and should follow the naming conventions of Python.

# Example of a built-in function
# 1) Utility function
print("\n Utility Functions")
print(type("Hello World!"))  # str
print(type(123))  # int

print(len([1, 2, 3, 4, 5]))  # 5
print(len({'java' : 4, 'python': 6 , 'HTML' : 4}))  # 3

print(id((1, 2, 3)))  # 140706792032064
print(id({2,2,1,1,4,4}))  # 140706792032064

# 2) On String
print("\n Functions on String")
print("Hello World".upper())  # HELLO WORLD
print("Hello World".lower())  # hello world
print("hello world".capitalize())  # Hello world
print("hello world".title())  # Hello World
print("heLlO WoRld".swapcase())  # HElLo wOrLD
print("Hello World".count('l'))  # 3
print("Hello World".find('l'))  # 2
print("Hello World".replace('World', 'Python'))  # Hello Python
print("Hello World".replace('l', 'L'))  # HeLLo WorLd
print("Hello World".split())  # ['Hello', 'World']
print("Hello World".index('l'))  # 2
print("@".join(['Hello', 'World', 'Again']))  # Hello@World@Again
print("          Hello      World               ".strip())  # Hello      World
print("          Hello      World               ".lstrip())  # Hello      World
print("          Hello      World               ".rstrip())  #           Hello      World
print("Hello World".startswith('H'))  # True
print("Hello World".endswith('d'))  # True
print("Hello World".isalpha())  # False
print("Hello World".isalnum())  # False
print("Hello World".isnumeric())  # False
print("Hello World".isdecimal())  # False
print("Hello World".isnumeric())  # False
print("Hello World".isupper())  # False
print("Hello World".islower())  # False
print("Hello World".istitle())  # True
print("Hello World".isidentifier())  # False
print("Hello World".isprintable())  # True

# On List
print("\n Functions on List")
print([1, 2, 3, 4, 5].append(6))  # [1, 2, 3, 4, 5, 6]
print([1, 2, 3, 4, 5].extend([6, 7, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]
print([1, 2, 3, 4, 5].insert(2, 6))  # [1, 2, 6, 3, 4, 5]
print([1, 2, 3, 4, 5].remove(3))  # [1, 2, 4, 5]
print([1, 2, 3, 4, 5].pop())  # 5
print([1, 2, 3, 4, 5].clear())  # []
print([1, 2, 3, 4, 5].index(3))  # 2
print([1, 2, 3, 4, 5].count(3))  # 1
print([22,11,44,33,55].sort()) # [11, 22, 33, 44, 55]
print([22,11,44,33,55].sort(reverse=True))  # [55, 44, 33, 22, 11]
print([22,11,44,33,55].reverse())  # [55, 33, 44, 11, 22]

# On Tuple
print("\n Functions on Tuple")
print((1, 2, 3, 4, 5).count(3))  # 1
print((1, 2, 3, 4, 5).index(3))  # 2

# On Set
print("\n Functions on Set")
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a, "\t", a.add(6))  # {1, 2, 3, 4, 5, 6}
print(a, "\t", a.remove(6))  # {1, 2, 3, 4, 5}
print(a, "\t", a.discard(3))  # {1, 2, 4, 5}
print(a, "\t", a.pop())  # {2, 4, 5}
print(a, "\t", a.clear())  # set()
print(a, "\t", a.update(b))  # {3, 4, 5, 6, 7}
print(a, "\t", b, "\t", a.union(b)) # {1, 2, 3, 4, 5} {3, 4, 5, 6, 7} {1, 2, 3, 4, 5, 6, 7}
print(a, "\t", b, "\t", a.intersection(b)) # {1, 2, 3, 4, 5} {3, 4, 5, 6, 7} {3, 4, 5}
print(a, "\t", b, "\t", a.difference(b)) # {1, 2, 3, 4, 5} {3, 4, 5, 6, 7} {1, 2}
a.difference_update(b)  # {1, 2}
print(a) # {1, 2}
a.intersection_update(b)  # {3, 4, 5}
print(a) # {3, 4, 5}
print(a, "\t", a.isdisjoint(b))  # True
print(a, "\t", a.issubset(b))  # False
print(a, "\t", a.issuperset(b))  # False
print(a, "\t", b, "\t", a.symmetric_difference(b)) # {1, 2, 3, 4, 5} {3, 4, 5, 6, 7} {1, 2, 6, 7}
print(a, "\t", b, "\t", a.issubset(b)) # {1, 2, 3, 4, 5} {3, 4, 5, 6, 7} False

print({1, 2, 3, 4, 5}.union({6, 7, 8}))  # {1, 2, 3, 4, 5, 6, 7, 8}
print({1, 2, 3, 4, 5}.intersection({3, 4, 6, 7}))  # {3, 4}
print({1, 2, 3, 4, 5}.difference({3, 4, 6, 7}))  # {1, 2, 5}
print({1, 2, 3, 4, 5}.symmetric_difference({3, 4, 6, 7}))  # {1, 2, 5, 6, 7}
print({1, 2, 3, 4, 5}.issubset({1, 2, 3, 4, 5, 6}))  # True
print({1, 2, 3, 4, 5}.issuperset({1, 2, 3}))  # True
print({1, 2, 3, 4, 5}.isdisjoint({6, 7, 8}))  # True
print({1, 2, 3, 4, 5}.copy())  # {1, 2, 3, 4, 5}
print({1, 2, 3, 4, 5}.update({6, 7, 8}))  # {1, 2, 3, 4, 5, 6, 7, 8}
print({1, 2, 3, 4, 5}.intersection_update({3, 4, 6, 7}))  # {3, 4}
print({1, 2, 3, 4, 5}.difference_update({3, 4, 6, 7}))  # {1, 2, 5}
print({1, 2, 3, 4, 5}.symmetric_difference_update({3, 4, 6, 7}))  # {1, 2, 5, 6, 7}

# On Dictionary
print("\n Functions on Dictionary")
k = {'a': 1, 'b': 2, 'c': 3}
k['g'] = 99
print(k)  # {'a': 1, 'b': 2, 'c': 3, 'g': 99}
print(k['g'])  # 99
print(k.get('g'))  # 99
print({'a': 1, 'b': 2, 'c': 3}.keys())  # dict_keys(['a', 'b', 'c'])
print({'a': 1, 'b': 2, 'c': 3}.values())  # dict_values([1, 2, 3])
print({'a': 1, 'b': 2, 'c': 3}.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
print({'a': 1, 'b': 2, 'c': 3}.get('a'))  # 1
print({'a': 1, 'b': 2, 'c': 3}.get('d'))  # None
print({'a': 1, 'b': 2, 'c': 3}.get('d', 4))  # 4
print({'a': 1, 'b': 2, 'c': 3}.setdefault('d', 4))  # 4
print({'a': 1, 'b': 2, 'c': 3}.setdefault('a', 4))  # 1
print({'a': 1, 'b': 2, 'c': 3}.pop('a'))  # 1
print({'a': 1, 'b': 2, 'c': 3}.popitem())  # ('c', 3)
print({'a': 1, 'b': 2, 'c': 3}.update({'d': 4}))  # None
print({'a': 1, 'b': 2, 'c': 3}.clear())  # {}


# User-defined function
# A user-defined function is a function that you define yourself.
# It can take parameters and return a value. 
# The syntax for defining a user-defined function is as follows:
# def function_name(parameters):    
#     """docstring"""
#     statement(s)
#     return value

# The 'function_name' is the name of the function. The 'parameters' are optional inputs to the function.
# The 'docstring' is a string that describes the function. The 'statement(s)' are the code that will be executed when the function is called. The 'return' statement is used to return a value from the function.
# The 'return' statement is optional. If there is no return statement, the function will return None by default.
# The 'return' statement can return multiple values in the form of a tuple.
# The function name should be descriptive and should follow the naming conventions of Python.   
# The function can take any number of parameters, including zero parameters.

print("\n User-defined Functions")
# 1) Function with no parameters and no return value
def greet():
    print("Hello World!")
greet()  # Hello World!

# 2) Function with no parameters but return value
def greet():
    return "Hello World !!!"
print(greet()) # Hello World !!!

# 3) Function with parameters and no return value
def greet(name):
    print("Hello " + name + "!")
greet("John")  # Hello John!
greet("Jane")  # Hello Jane!

# 4) Function with parameters and return value
def add(a, b):
    return a + b
def subtract(a, b):
    print(a - b)
print(add(22, 11)) # 11
subtract(87, 29) # 58