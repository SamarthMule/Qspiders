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
# # 1) Utility function
# print("\n Utility Functions")
# print(type("Hello World!"))  # str
# print(type(123))  # int

# print(len([1, 2, 3, 4, 5]))  # 5
# print(len({'java' : 4, 'python': 6 , 'HTML' : 4}))  # 3

# print(id((1, 2, 3)))  # 140706792032064
# print(id({2,2,1,1,4,4}))  # 140706792032064

# # 2) On String
# print("\n Functions on String")
# print("Hello World".upper())  # HELLO WORLD
# print("Hello World".lower())  # hello world
# print("hello world".capitalize())  # Hello world
# print("hello world".title())  # Hello World
# print("heLlO WoRld".swapcase())  # HElLo wOrLD
# print("Hello World".count('l'))  # 3
# print("Hello World".find('l'))  # 2
# print("Hello World".replace('World', 'Python'))  # Hello Python
# print("Hello World".replace('l', 'L'))  # HeLLo WorLd
# print("Hello World".split())  # ['Hello', 'World']
# print("Hello World".index('l'))  # 2
# print("@".join(['Hello', 'World', 'Again']))  # Hello@World@Again
# print("          Hello      World               ".strip())  # Hello      World
# print("          Hello      World               ".lstrip())  # Hello      World
# print("          Hello      World               ".rstrip())  #           Hello      World
# print("Hello World".startswith('H'))  # True
# print("Hello World".endswith('d'))  # True
# print("Hello World".isalpha())  # False
# print("Hello World".isalnum())  # False
# print("Hello World".isnumeric())  # False
# print("Hello World".isdecimal())  # False
# print("Hello World".isupper())  # False
# print("Hello World".islower())  # False
# print("Hello World".istitle())  # True
# print("Hello World".isidentifier())  # False
# print("Hello World".isprintable())  # True

# # On List
# print("\n Functions on List")
# print([1, 2, 3, 4, 5].append(6))  # [1, 2, 3, 4, 5, 6]
# print([1, 2, 3, 4, 5].extend([6, 7, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]
# print([1, 2, 3, 4, 5].insert(2, 6))  # [1, 2, 6, 3, 4, 5]
# print([1, 2, 3, 4, 5].remove(3))  # [1, 2, 4, 5]
# print([1, 2, 3, 4, 5].pop())  # 5
# print([1, 2, 3, 4, 5].clear())  # []
# print([1, 2, 3, 4, 5].index(3))  # 2
# print([1, 2, 3, 4, 5].count(3))  # 1
# print([22,11,44,33,55].sort()) # [11, 22, 33, 44, 55]
# print([22,11,44,33,55].sort(reverse=True))  # [55, 44, 33, 22, 11]
# print([22,11,44,33,55].reverse())  # [55, 33, 44, 11, 22]

# # On Tuple
# print("\n Functions on Tuple")
# print((1, 2, 3, 4, 5).count(3))  # 1
# print((1, 2, 3, 4, 5).index(3))  # 2

# # On Set
# print("\n Functions on Set")
# a = {1, 2, 3, 4, 5}
# b = {3, 4, 5, 6, 7}

# print(a, "\t", a.add(6))  # {1, 2, 3, 4, 5, 6}
# print(a, "\t", a.remove(6))  # {1, 2, 3, 4, 5}
# print(a, "\t", a.discard(3))  # {1, 2, 4, 5}
# print(a, "\t", a.pop())  # {2, 4, 5}
# print(a, "\t", a.clear())  # set()
# print(a, "\t", a.update(b))  # {3, 4, 5, 6, 7}
# print(a, "\t", b, "\t", a.union(b)) # {1, 2, 3, 4, 5} {3, 4, 5, 6, 7} {1, 2, 3, 4, 5, 6, 7}
# print(a, "\t", b, "\t", a.intersection(b)) # {1, 2, 3, 4, 5} {3, 4, 5, 6, 7} {3, 4, 5}
# print(a, "\t", b, "\t", a.difference(b)) # {1, 2, 3, 4, 5} {3, 4, 5, 6, 7} {1, 2}
# a.difference_update(b)  # {1, 2}
# print(a) # {1, 2}
# a.intersection_update(b)  # {3, 4, 5}
# print(a) # {3, 4, 5}
# print(a, "\t", a.isdisjoint(b))  # True
# print(a, "\t", a.issubset(b))  # False
# print(a, "\t", a.issuperset(b))  # False
# print(a, "\t", b, "\t", a.symmetric_difference(b)) # {1, 2, 3, 4, 5} {3, 4, 5, 6, 7} {1, 2, 6, 7}
# print(a, "\t", b, "\t", a.issubset(b)) # {1, 2, 3, 4, 5} {3, 4, 5, 6, 7} False

# print({1, 2, 3, 4, 5}.union({6, 7, 8}))  # {1, 2, 3, 4, 5, 6, 7, 8}
# print({1, 2, 3, 4, 5}.intersection({3, 4, 6, 7}))  # {3, 4}
# print({1, 2, 3, 4, 5}.difference({3, 4, 6, 7}))  # {1, 2, 5}
# print({1, 2, 3, 4, 5}.symmetric_difference({3, 4, 6, 7}))  # {1, 2, 5, 6, 7}
# print({1, 2, 3, 4, 5}.issubset({1, 2, 3, 4, 5, 6}))  # True
# print({1, 2, 3, 4, 5}.issuperset({1, 2, 3}))  # True
# print({1, 2, 3, 4, 5}.isdisjoint({6, 7, 8}))  # True
# print({1, 2, 3, 4, 5}.copy())  # {1, 2, 3, 4, 5}
# print({1, 2, 3, 4, 5}.update({6, 7, 8}))  # {1, 2, 3, 4, 5, 6, 7, 8}
# print({1, 2, 3, 4, 5}.intersection_update({3, 4, 6, 7}))  # {3, 4}
# print({1, 2, 3, 4, 5}.difference_update({3, 4, 6, 7}))  # {1, 2, 5}
# print({1, 2, 3, 4, 5}.symmetric_difference_update({3, 4, 6, 7}))  # {1, 2, 5, 6, 7}

# # On Dictionary
# print("\n Functions on Dictionary")
# k = {'a': 1, 'b': 2, 'c': 3}
# k['g'] = 99
# print(k)  # {'a': 1, 'b': 2, 'c': 3, 'g': 99}
# print(k['g'])  # 99
# print(k.get('g'))  # 99
# print({'a': 1, 'b': 2, 'c': 3}.keys())  # dict_keys(['a', 'b', 'c'])
# print({'a': 1, 'b': 2, 'c': 3}.values())  # dict_values([1, 2, 3])
# print({'a': 1, 'b': 2, 'c': 3}.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
# print({'a': 1, 'b': 2, 'c': 3}.get('a'))  # 1
# print({'a': 1, 'b': 2, 'c': 3}.get('d'))  # None
# print({'a': 1, 'b': 2, 'c': 3}.get('d', 4))  # 4
# print({'a': 1, 'b': 2, 'c': 3}.setdefault('d', 4))  # 4
# print({'a': 1, 'b': 2, 'c': 3}.setdefault('a', 4))  # 1
# print({'a': 1, 'b': 2, 'c': 3}.pop('a'))  # 1
# print({'a': 1, 'b': 2, 'c': 3}.popitem())  # ('c', 3)
# print({'a': 1, 'b': 2, 'c': 3}.update({'d': 4}))  # None
# print({'a': 1, 'b': 2, 'c': 3}.clear())  # {}


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

# print("\n User-defined Functions Types")
# print("1) Function with no parameters and no return value")
# def greet():
#     print("Hello World!")
# greet()  # Hello World!

# print("2) Function with no parameters but return value")
# def greet():
#     return "Hello World !!!"
# print(greet()) # Hello World !!!

# print("3) Function with parameters and no return value")
# def greet(name):
#     print("Hello " + name + "!")
# greet("John")  # Hello John!
# greet("Jane")  # Hello Jane!

# print("4) Function with parameters and return value")
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     print(a - b)
# print(add(22, 11)) # 11
# subtract(87, 29) # 58

# print("5) Function with default parameters")
# def add(a, b=10):
#     return a + b
# def subtract(a, b=10):
#     print(a - b)
# print(add(22)) # 32
# print(add(22, 11)) # 33
# subtract(87) # 77
# subtract(87, 29) # 58

# print("6) Function with variable number of parameters")
# def add(*args):
#     sum = 0
#     print(args)
#     for arg in args:
#         sum += arg
#     return sum

# print(add(1, 2, 3)) # 6
# print(add(1, 2, 3, 4, 5)) # 15

# def multiply(**kwargs):
#     product = 1
#     print(kwargs)
#     for key, value in kwargs.items():
#         product *= value
#     return product

# print(multiply(a=2, b=3, c=4)) # 24
# print(multiply(a=2, b=3, c=4, d=5)) # 120

# print("\n User-defined Functions Examples (Without Arg & return)")
# print("\nWAP to convert the string to upper case")
# def convert_to_upper():
#     string = input()
#     for i in string:
#         if 'a' <= i <= 'z':
#             string = string.replace(i, chr(ord(i) - 32))
#     print(string)
# convert_to_upper()

# print("\nWAP to count the number of occurrences of a given char in given string.")
# def count_occurrences():
#     string = input()
#     char = input()
#     count = 0
#     for i in string:
#         if i == char:
#             count += 1
#     print(count)
# count_occurrences()

# print("WAP to print the following using while loop. First 10 even numbers.")
# def even_numbers():
#     print("First 10 even numbers : ")
#     count = 0
#     i = 0
#     while count < 10:
#         print(i, end=" ")
#         i += 2
#         count += 1
# even_numbers()

# print("\n User-defined Function Examples (with Arg, without return)")
# print("\nWAP to extract string from list which are palindrome")
# def find_palindrome(input):
#     print("Input List : ", input)
#     output = []
#     for i in input:
#         if type(i) == str:
#             if i == i[::-1]:
#                 output.append(i)
#     print("Output List : ", output)
# find_palindrome([10, 'aba', 'hello', 5+2j, 8.6, 'naman', 'amrit'])

# print("\nWAP to find greatest among three numbers")
# def greatest(a, b, c):
#     print("Given Numbers : ", a, b, c)
#     if a >= b and a >= c:
#         print(a, "is greatest")
#     elif b >= a and b >= c:
#         print(b, "is greatest")
#     else:
#         print(c, "is greatest")
# greatest(55,22,33)

# print("\nWAP to concatenate two list collections without using '+' Operator")
# def concate_list(l1, l2):
#     print("L1 : ", l1)
#     print("L2 : ", l2)
    
#     out = l1
#     for j in l2:
#         out.append(j)
#     print("Output : ", out)
    
# concate_list([1,2,3], [10,20,30])

# print("\n User-defined Function Examples (without Arg, with return)")
# print("\nWAP to find multiles of 5")
# def multiples_of_five():
#     l = eval(input("Enter List : "))
#     output = []
#     for i in l:
#         if i % 5 == 0:
#             output.append(i)
#     return output
# print("Output List : ", multiples_of_five())

# print("\nWAP to find the sum of integers present in given list")
# def sum_of_integers():
#     l = eval(input("Enter List : "))
#     sum = 0
#     for i in l:
#         if type(i) == int:
#             sum += i
#     return sum
# print("Sum of Integers : ", sum_of_integers())

# print("\nWAP to return the square of the first 5 natural numbers")
# def square_of_natural_numbers():
#     output = []
#     for i in range(1, 6):
#         output.append(i * i)
#     return output
# print("Output List : ", square_of_natural_numbers())

# print("\n User-defined Function Examples (with Arg, with return)")
# print("\nWAP to print the initial index of char in given string")
# def initial_index(string, char):
#     for i in string:
#         if i == char:
#             return string.index(i)
#     return 'Not Found'
# print("Initial Index : ", initial_index(input("Enter a string: "), input("Enter a char: ")))
# print("Initial Index : ", initial_index(input("Enter a string: "), input("Enter a char: ")))

# print("\nWAP to map two list collections in form of dictionary")
# def map_to_dict(l1, l2):
#     output = {}
#     for i in range(len(l1)):
#         output[l1[i]] = l2[i]
#     return output
# print("Output Dictionary : ", map_to_dict(['a', 'b', 'c'], [10, 20, 30]))

# print("\nWAP to extract all the negative numbers from list")
# def extract_negative_numbers(l):
#     output = []
#     for i in l:
#         if i < 0:
#             output.append(i)
#     return output
# print("Output List : ", extract_negative_numbers([-1, 2, -3, 4, -5]))


# # Assignment
# print("Basic Calculator Program")
# def calculator():
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     # print("5. Modulus")
#     # print("6. Exponentiation")
#     # print("7. Floor Division")
#     print("5. Exit")

#     while True:
#         choice = input("Enter your choice (1-5): ")
#         if choice == '5':
#             print("Exiting the calculator.")
#             break
#         elif choice in ['1', '2', '3', '4']:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))

#             if choice == '1':
#                 result = num1 + num2
#                 print(f"The result of addition is: {result}")
#             elif choice == '2':
#                 result = num1 - num2
#                 print(f"The result of subtraction is: {result}")
#             elif choice == '3':
#                 result = num1 * num2
#                 print(f"The result of multiplication is: {result}")
#             elif choice == '4':
#                 if num2 != 0:
#                     result = num1 / num2
#                     print(f"The result of division is: {result}")
#                 else:
#                     print("Error: Division by zero is not allowed.")
#         else:
#             print("Invalid choice. Please try again.")

# calculator()


# print("\n Global and Local Variables")
# # Example of global variable
# # A global variable is a variable that is defined outside of any function and can be accessed from anywhere in the code.
# # A local variable is a variable that is defined inside a function and can only be accessed from within that function.

# # Global variable
# x = 10
# y = 20
# def my_function():
#     print("This is my function.")
#     print("Global variable x:", x)  # Accessing global variable
#     y = 30  # This will create a new local variable y
#     print("Local variable y:", y)  # Accessing local variable

# my_function()
# print("Global variable x:", x)  # Accessing global variable
# print("Global variable y:", y)  # Accessing global variable

# m = 100
# n = 2000
# def my_function2():
#     global m  # Declare m as a global variable
#     m = 200  # This will modify the global variable m
#     print("Global variable m:", m)  # Accessing global variable
#     # print("Local variable n:", n)  # Accessing global variable giving error because n is not defined in this function
#     n = 3000  # This will create a new local variable n
#     print("Local variable n:", n)  # Accessing local variable
# my_function2()
# print("Global variable m:", m)  # Accessing global variable
# print("Global variable n:", n)  # Accessing global variable giving error because n is not defined in this function


# # Local variable
# k = 1000
# l = 2000
# def my_function3():
#     k = 2000  # This will create a new local variable k
#     print("Local variable k:", k)  # Accessing local variable
#     print("Global variable l:", l)  # Accessing global variable
# my_function3()

# s = 10000
# def my_new_function():
#     print("This is my new function.")
#     o = 3000  # This will create a new local variable o
#     print("Local variable o:", o)  # Accessing local variable
#     def inner_function():
#         s = 20000
#         print("Local variable s:", s)
#         print("Local variable o:", o)
#     inner_function()
#     print("Global variable s:", s)  # Accessing global variable
#     print("Local variable o:", o)  # Accessing local variable
# my_new_function()
# print("Global variable s:", s)  # Accessing global variable


# Example of nonlocal variable
# A nonlocal variable is a variable that is defined in the nearest enclosing scope that is not global.
# It can be accessed from within nested functions.
# Nonlocal variables are used to modify variables in the enclosing scope.
# They are declared using the nonlocal keyword.
# Nonlocal variables are not available in the global scope.
# They are only available in the enclosing scope.

# # Example of nonlocal variable
# j = 2000
# def my_function_new():
#     l = 3000  # This will create a new local variable l
#     print("Local variable l:", l)  # Accessing local variable
#     def inner_function_new():
#         nonlocal l  # Declare l as a nonlocal variable
#         l = 4000  # This will modify the nonlocal variable l
#         print("Nonlocal variable l:", l)  # Accessing nonlocal variable
#         print("Global variable j:", j)
#     inner_function_new()
#     print("Local variable l after modification:", l)  # Accessing local variable
#     print("Global variable j:", j)  # Accessing global variable
# my_function_new()
# print("Global variable l:", j)  # Accessing global variable

# print("\n Function with variable number of arguments : Packing and Unpacking")
# # Packing and Unpacking are used to pass a variable number of arguments to a function.
# # Packing is the process of collecting multiple arguments into a single argument.

# # Unpacking is the process of extracting multiple arguments from a single argument.
# # Packing is done using the * operator and Unpacking is done using the ** operator.
# # Packing is used to pass a variable number of arguments to a function.
# # Unpacking is used to extract multiple arguments from a single argument.
# # Packing is done using the * operator and Unpacking is done using the ** operator.
# # Packing is used to pass a variable number of arguments to a function.
# # Unpacking is used to extract multiple arguments from a single argument.

# # Packing 
# def sam(*args):
#     print(args)
# sam("pratik Sutar","Data Analyst")

# def add(*args):
#     print(args)
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# add(1,2,3,4,5,6,7,8,9,10)

# def man(**kwargs):
#     print(kwargs)
# man(name="Pratik",age=22,phone=7795868788)

# def home(args,*kwargs):
#     print(args,kwargs)
# home(1,2,3,4,5,a=20,b=30,c=40)

# # def home(**kwargs,*args): # This will give error because **kwargs should be at the end of the function definition
# #     print(args,kwargs)
# # home(1,2,3,4,5,a=20,b=30,c=40)

# # def home(args,*kwargs):
# #     print(args,kwargs)
# # home(a=20,b=30,c=40,1,2,3,4,5) # This will give error because *args should be at the end of the function definition

# # Unpacking
# # Unpacking is the process of extracting multiple arguments from a single argument.
# # Unpacking is done using the * operator and ** operator.
# # Unpacking is used to extract multiple arguments from a single argument.
# num=[1,2,3]
# def fan(a,b,c):
#     print(a+b+c)
# fan(*num)

# d={'name':'pratik','age':20}
# def some(name,age):
#     print(name)
#     print(age)
# some(**d)


# print("\nTypes Of Arguments")
# 1. Positional Arguments
# Positional arguments are the most common type of arguments.
# They are passed to a function in the order in which they are defined.
# They are also called required arguments.
# 2. Keyword Arguments
# Keyword arguments are passed to a function using the name of the parameter.
# They are also called named arguments.
# Keyword arguments can be passed in any order.
# They are optional arguments.
# 3. Default Arguments
# Default arguments are the arguments that have a default value.
# They are optional arguments.
# If a default argument is not passed, the default value will be used.
# Default arguments are defined using the assignment operator (=).
# They are also called optional arguments.
# 4. Variable-length Arguments
# Variable-length arguments are the arguments that can take any number of values.
# They are also called arbitrary arguments.
# They are defined using the * operator.
# They can take any number of values.
# They are used to pass a variable number of arguments to a function.

# print("\nWAP to add minimum 2 numbers and maximum 5 numbers")
# def add(num1,num2,num3=0,num4=0,num5=0):
#     return num1+num2+num3+num4+num5
# print(add(1,2)) # 3
# print(add(1,2,3)) # 6
# print(add(1,2,3,4,5)) # 15

# print("\nWAP to find the product of minimum 3 and maximum 7 numbers ")
# def product(num1,num2,num3,num4=1,num5=1,num6=1,num7=1):
#     return num1*num2*num3*num4*num5*num6*num7
# print(product(1,2,3)) # 6
# print(product(4,8,2,9,3,6,5)) # 51840

# print("\nWAP to extract float numbers from tuple")
# def extract_float(tuple):
#     for i in tuple:
#         if type(i) == float:
#             print(i, end=" ")
# extract_float((2,3.9,4,5.2,6))

# print("\nWAP to find the sum of individual digits in a given int.")
# def sum_of_digits(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum
# print(sum_of_digits(12345)) # 15

# print("\nWAP to check even, odd (Input in form of packing (*nums))")
# def check_even_odd(*nums):
#     for i in nums:
#         if i % 2 == 0:
#             print(i , " is even")
#         else:
#             print(i , " is odd")

# check_even_odd(1,2,3,4,5,6,7,8,9,10)

# Recursion
# Recursion is a programming technique where a function calls itself to solve a problem.
# It is used to solve problems that can be broken down into smaller subproblems.
# Recursion is a powerful tool, but it can also lead to infinite loops if not used carefully.
# It is important to have a base case to stop the recursion.
# A base case is a condition that stops the recursion.
# It is the simplest case of the problem that can be solved without recursion.
# Recursion can be used to solve problems such as factorial, Fibonacci series, and tower of Hanoi.

# Two types of recursion:
# 1. Without return value: A function that calls itself without returning a value.
# Syntax:
# def function_name(parameters):
#     """docstring"""
#     # termination condition:
#     #     statement(s)
#     #     return
#     # statement(s)
#     # function_name(parameters) #     # function calling itself

# function_name(parameters) # function call

# 2. With return value: A function that calls itself and returns a value.
# Syntax:
# def function_name(parameters):
#     """docstring"""
#     # termination condition:
#     #     statement(s)
#     #     return values
#     # statement(s)
#     # return function_name(parameters) # function calling itself and returning a value

# function_name(parameters) # function call

# Examples
def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 

print("Factorial of 5:", factorial(5))  # Output: 120
print("Factorial of 0:", factorial(0))  # Output: 1 

def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 

print("Fibonacci of 5:", fibonacci(5))  # Output: 5
print("Fibonacci of 10:", fibonacci(10))  # Output: 55

print("\nWAP to find the sum of n natural numbers using recursion")
def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    
    return n + sum_of_natural_numbers(n - 1)

print("Sum of first 5 natural numbers:", sum_of_natural_numbers(5))  # Output: 15
print("Sum of first 10 natural numbers:", sum_of_natural_numbers(10))  # Output: 55

print('''WAP to print 5 4 3 2 1 2 3 4 5 if n=5 using recursion.''')
def pattern(n):
    if n == 1:
        print(n, end=" ")
        return 
    
    print(n, end=" ")
    pattern(n-1)
    print(n, end=" ")

pattern(5)

print("\nWAP to find the sum of all integers in given list using recursion")
def sum_of_integers(lst):
    if not lst:
        return 0
    if isinstance(lst[0], int):
        return lst[0] + sum_of_integers(lst[1:])
    return sum_of_integers(lst[1:])

l = [1, 2, 3, 4, 5]
print("Sum of integers in list:", sum_of_integers(l))

print('''\nWAP to print following: (Using Recursion)
      l = ['hey', 76, True, 56, 'data', 'nice', False]
      output : ['yehhey', 76, True, 56, 'ataddate', 'ecinnice', False]''')
def modify_list(lst):
    if not lst:
        return []
    
    first = lst[0]
    if isinstance(first, str):
        first = first[::-1] + first
    elif isinstance(first, bool):
        first = not first
    
    return [first] + modify_list(lst[1:])
print(modify_list(['hey', 76, True, 56, 'data', 'nice', False]))

print("\nWAP to reverse the given string without using slicing (Using Recursion)")
def reveres(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + reveres(string[:-1])
print(reveres(input("Enter a string: "))) # Reverse of the string

print("\nWAP to chech whether the data is palindrome or not")
def check_palindrome(str):
    if len(str) == 0 or len(str) == 1:
        return "Given string is palindrome"
    if str[0] != str[-1]:
        return "Given string is not palindrome"
    return check_palindrome(str[1:-1])
print(check_palindrome(input("Enter a string: "))) 

print("\nWAP to find the lenght of given list without using inbuilt function")
def find_length(lst):
    if not lst:
        return 0
    return 1 + find_length(lst[1:])
print("Length of the list:", find_length([1, 2, 3, 4, 5]))

print("\nWAP to find the maximum counted number in the list (Using Recursion)")

def find_max_count(lst, max_count=0, max_num=None):
    if not lst:
        return max_num, max_count
    
    current_num = lst[0]
    count = lst.count(current_num)
    
    if count > max_count:
        max_count = count
        max_num = current_num
    
    return find_max_count(lst[1:], max_count, max_num)

l = [1,2,4,1,2,7,3,2,3,2,6,7,4,1]
print("Maximum counted number in the list:", find_max_count(l)[0], "Max count :", find_max_count(l)[1]) 