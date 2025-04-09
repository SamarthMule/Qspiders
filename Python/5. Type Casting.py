# # Type Casting: Converting one data type to another data type

# Int
# print("\nint to other data types")
# a = 10
# print(str(a)) # 10
# print(float(a)) # 10.0
# print(complex(a)) # (10+0j)
# print(bool(a)) # True
# # print(list(a)) # TypeError: 'int' object is not iterable
# # print(tuple(a)) # TypeError: 'int' object is not iterable
# # print(set(a)) # TypeError: 'int' object is not iterable
# # print(dict(a)) # TypeError: 'int' object is not iterable

# Float
# print("\nfloat to other data types")
# b = 10.5
# print(str(b)) # 10.5
# print(int(b)) # 10
# print(complex(b)) # (10.5+0j)
# print(bool(b)) # True
# # print(list(b)) # TypeError: 'float' object is not iterable
# # print(tuple(b)) # TypeError: 'float' object is not iterable
# # print(set(b)) # TypeError: 'float' object is not iterable
# # print(dict(b)) # TypeError: 'float' object is not iterable

# Complex
# print("\ncomplex to other data types")
# c = 10+5j
# print(str(c)) # (10+5j)
# # print(int(c)) # TypeError: can't convert complex to int
# # print(float(c)) # TypeError: can't convert complex to float
# print(bool(c)) # True
# # print(list(c)) # TypeError: 'complex' object is not iterable
# # print(tuple(c)) # TypeError: 'complex' object is not iterable
# # print(set(c)) # TypeError: 'complex' object is not iterable
# # print(dict(c)) # TypeError: 'complex' object is not iterable

# Boolean
# print("\nbool to other data types")
# d = True
# print(str(d)) # True
# print(int(d)) # 1
# print(float(d)) # 1.0
# print(complex(d)) # (1+0j)
# # print(list(d)) # TypeError: 'bool' object is not iterable
# # print(tuple(d)) # TypeError: 'bool' object is not iterable
# # print(set(d)) # TypeError: 'bool' object is not iterable
# # print(dict(d)) # TypeError: 'bool' object is not iterable

# Exmaple of conversion of int to other data types
a = 10
print(str(a)) # 10
print(float(a)) # 10.0
print(complex(a)) # (10+0j)
print(bool(a)) # True
# print(list(a)) # TypeError: 'int' object is not iterable
# print(tuple(a)) # TypeError: 'int' object is not iterable
# print(set(a)) # TypeError: 'int' object is not iterable
# print(dict(a)) # TypeError: 'int' object is not iterable

# Exmaple of conversion of float to other data types
b = 10.5
print(str(b)) # 10.5
print(int(b)) # 10
print(complex(b)) # (10.5+0j)
print(bool(b)) # True
# print(list(b)) # TypeError: 'float' object is not iterable
# print(tuple(b)) # TypeError: 'float' object is not iterable
# print(set(b)) # TypeError: 'float' object is not iterable
# print(dict(b)) # TypeError: 'float' object is not iterable

# Exmaple of conversion of complex to other data types
c = 10+5j
print(str(c)) # (10+5j)
# print(int(c)) # TypeError: can't convert complex to int
# print(float(c)) # TypeError: can't convert complex to float
print(bool(c)) # True
# print(list(c)) # TypeError: 'complex' object is not iterable
# print(tuple(c)) # TypeError: 'complex' object is not iterable
# print(set(c)) # TypeError: 'complex' object is not iterable
# print(dict(c)) # TypeError: 'complex' object is not iterable


# String
# print("\nstr to other data types")
# e = "10"
# print(int(e)) # 10
# print(float(e)) # 10.0
# print(complex(e)) # (10+0j)
# print(bool(e)) # True
# print(list(e)) # ['1', '0']
# print(tuple(e)) # ('1', '0')
# print(set(e)) # {'0', '1'}
# # print(dict(e)) # TypeError: 'str' object is not iterable
# e = "Class Room"
# # print(int(e)) # ValueError: invalid literal for int() with base 10: 'Class Room'
# # print(float(e)) # ValueError: could not convert string to float: 'Class Room'
# # print(complex(e)) # ValueError: complex() arg is a malformed string
# print(bool(e)) # True
# print(list(e)) # ['C', 'l', 'a', 's', 's', ' ', 'R', 'o', 'o', 'm']
# print(tuple(e)) # ('C', 'l', 'a', 's', 's', ' ', 'R', 'o', 'o', 'm')
# print(set(e)) # {'C', 'l', 'a', 's', ' ', 'R', 'o', 'm'}
# # print(dict(e)) # TypeError: 'str' object is not iterable
# e = 'j'
# print(complex(e)) # (0+1j)

# List
# print("\nlist to other data types")
# f = [10, 4.5, 9+6j , False, 8+9j, 'html', 3]
# print(str(f)) # [10, 4.5, (9+6j), False, (8+9j), 'html', 3]
# # print(int(f)) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# # print(float(f)) # TypeError: float() argument must be a string or a number, not 'list'
# # print(complex(f)) # TypeError: can't convert list to complex
# print(bool(f)) # True
# print(tuple(f)) # (10, 4.5, (9+6j), False, (8+9j), 'html', 3)
# print(set(f)) # {False, 3, 4.5, 8, 9, 10, 'html', (9+6j), (8+9j)}
# # print(dict(f)) # TypeError: 'list' object is not iterable

# Tuple
# print("\ntuple to other data types")
# g = (10,7.5,3+4j,False,8+9j,'html',3)
# print(str(g)) # (10, 7.5, (3+4j), False, (8+9j), 'html', 3)
# # print(int(g)) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
# # print(float(g)) # TypeError: float() argument must be a string or a number, not 'tuple'
# # print(complex(g)) # TypeError: can't convert tuple to complex
# print(bool(g)) # True
# print(list(g)) # [10, 7.5, (3+4j), False, (8+9j), 'html', 3]
# print(set(g)) # {False, 3, 7.5, 8, 9, 10, 'html', (3+4j), (8+9j)}
# # print(dict(g)) # TypeError: 'tuple' object is not iterable

# Set
# print("\nset to other data types")
# h = {10,20,30}
# print(str(h)) # {10, 20, 30}
# # print(int(h)) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
# # print(float(h)) # TypeError: float() argument must be a string or a number, not 'set'
# # print(complex(h)) # TypeError: can't convert set to complex
# print(bool(h)) # True
# # print(list(h)) # TypeError: 'set' object is not subscriptable
# # print(tuple(h)) # TypeError: 'set' object is not subscriptable
# # print(dict(h)) # TypeError: 'set' object is not subscriptable

# Dictionary
print("\n","-"*5,"dict to other data types","-"*5)
i = {10:20,30:40}
print(str(i)) # {10: 20, 30: 40}
# print(int(i)) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
# print(float(i)) # TypeError: float() argument must be a string or a number, not 'dict'
# print(complex(i)) # TypeError: can't convert dictionary to complex
print(bool(i)) # True
print(list(i)) # [10, 30]
print(tuple(i)) # (10, 30)
print(set(i)) # {10, 30}
print(dict(i)) # {10: 20, 30: 40}

# Exmaple of conversion of string to list, tuple, set and dictionary
print("\n","-"*5,"Example of conversion of string to list, tuple, set and dictionary","-"*5)
j = "Python"
print(list(j)) # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(j)) # ('P', 'y', 't', 'h', 'o', 'n')
print(set(j)) # {'P', 'y', 't', 'h', 'o', 'n'}
print(dict(j)) # TypeError: 'str' object is not iterable

# Exmaple of conversion of list of characters to string
print("\n","-"*5,"Example of conversion of list of characters to string","-"*5)
k = ['P', 'y', 't', 'h', 'o', 'n']
print(str(k)) # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(k)) # ('P', 'y', 't', 'h', 'o', 'n')
print(set(k)) # {'P', 'y', 't', 'h', 'o', 'n'}
print(dict(k)) # TypeError: 'list' object is not iterable

# Exmaple of conversion of tuple of characters to string
print("\n","-"*5,"Example of conversion of tuple of characters to string","-"*5)
l = ('P', 'y', 't', 'h', 'o', 'n')
print(str(l)) # ('P', 'y', 't', 'h', 'o', 'n')
print(list(l)) # ['P', 'y', 't', 'h', 'o', 'n']
print(set(l)) # {'P', 'y', 't', 'h', 'o', 'n'}
print(dict(l)) # TypeError: 'tuple' object is not iterable

# Exmaple of conversion of set of characters to string
print("\n","-"*5,"Example of conversion of set of characters to string","-"*5)
m = {'P', 'y', 't', 'h', 'o', 'n'}
print(str(m)) # {'P', 'y', 't', 'h', 'o', 'n'}
print(list(m)) # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(m)) # ('P', 'y', 't', 'h', 'o', 'n')
print(dict(m)) # TypeError: 'set' object is not subscriptable

# Exmaple of conversion of dictionary of characters to string
print("\n","-"*5,"Example of conversion of dictionary of characters to string","-"*5)
n = {'P':'Python'}
print(str(n)) # {'P': 'Python'}
print(list(n)) # ['P']
print(tuple(n)) # ('P',)
print(set(n)) # {'P'}
print(dict(n)) # {'P': 'Python'}


# # Conversion of string to list of characters
# j = "Python"
# print(list(j)) # ['P', 'y', 't', 'h', 'o', 'n']
# print(tuple(j)) # ('P', 'y', 't', 'h', 'o', 'n')
# print(set(j)) # {'P', 'y', 't', 'h', 'o', 'n'}
# print(dict(j)) # TypeError: 'str' object is not iterable

# # Conversion of list of characters to string
# k = ['P', 'y', 't', 'h', 'o', 'n']
# print(str(k)) # ['P', 'y', 't', 'h', 'o', 'n']
# print(tuple(k)) # ('P', 'y', 't', 'h', 'o', 'n')
# print(set(k)) # {'P', 'y', 't', 'h', 'o', 'n'}
# print(dict(k)) # TypeError: 'list' object is not iterable

# # Conversion of tuple of characters to string
# l = ('P', 'y', 't', 'h', 'o', 'n')
# print(str(l)) # ('P', 'y', 't', 'h', 'o', 'n')
# print(list(l)) # ['P', 'y', 't', 'h', 'o', 'n']
# print(set(l)) # {'P', 'y', 't', 'h', 'o', 'n'}
# print(dict(l)) # TypeError: 'tuple' object is not iterable

# # Conversion of set of characters to string
# m = {'P', 'y', 't', 'h', 'o', 'n'}
# print(str(m)) # {'P', 'y', 't', 'h', 'o', 'n'}
# print(list(m)) # ['P', 'y', 't', 'h', 'o', 'n']
# print(tuple(m)) # ('P', 'y', 't', 'h', 'o', 'n')
# print(dict(m)) # TypeError: 'set' object is not subscriptable

# # Conversion of dictionary of characters to string
# n = {'P':'Python'}
# print(str(n)) # {'P': 'Python'}
# print(list(n)) # ['P']
# print(tuple(n)) # ('P',)
# print(set(n)) # {'P'}
# # print(dict(n)) # TypeError: 'dict' object is not subscriptable