import keyword
print(keyword.kwlist) 

# Output:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# Same Variable Name Different Values
a = 10
print('a = ', a , "\t&" , 'id(a) = ', id(a)) # a = 10 & id(a) = 1407326744
b = 70
print('b = ', b , "\t&" , 'id(b) = ', id(b)) # b = 70 & id(b) = 1407326904
a = 20
print('a = ', a , "\t&" , 'id(a) = ', id(a)) # a = 20 & id(a) = 1407326774
b = 80
print('b = ', b , "\t&" , 'id(b) = ', id(b)) # b = 80 & id(b) = 1407326944

# Different Variable Name Same Values
c = 10
print('c = ', c , "\t&" , 'id(c) = ', id(c)) # c = 10 & id(c) = 1407326744
d = 10
print('d = ', d , "\t&" , 'id(d) = ', id(d)) # d = 10 & id(d) = 1407326744

# Multiple Value Creation
e, f , g , h = 10, 20, 30, 40
print('e = ', e , "\t&" , 'id(e) = ', id(e)) # e = 10 & id(e) = 1407326744
print('f = ', f , "\t&" , 'id(f) = ', id(f)) # f = 20 & id(f) = 1407326774
print('g = ', g , "\t&" , 'id(g) = ', id(g)) # g = 30 & id(g) = 1407326804
print('h = ', h , "\t&" , 'id(h) = ', id(h)) # h = 40 & id(h) = 1407326834

# Data Type
# Single Valued Data Type
# int
i = 10
print('i = ', i , "\t&" , 'type(i) = ', type(i)) # i = 10 & type(i) = <class 'int'>
print(bool(i)) # True
print(int()) # 0
# Float
j = 10.5
print('j = ', j , "\t&" , 'type(j) = ', type(j)) # j = 10.5 & type(j) = <class 'float'>
print(bool(j)) # True
print(float()) # 0.0
# Complex  
q = 10 + 5j
print('q = ', q , "\t&" , 'type(q) = ', type(q)) # q = (10+5j) & type(q) = <class 'complex'>
print(bool(q)) # True
print(complex()) # 0j
# Boolean
l = True
print('l = ', l , "\t&" , 'type(l) = ', type(l)) # l = True & type(l) = <class 'bool'>
print(bool(l)) # True
print(bool()) # False

# Multi Valued Data Type
# List
m = [10, 20, 30, 40]
print('m = ', m , "\t&" , 'type(m) = ', type(m)) # m = [10, 20, 30, 40] & type(m) = <class 'list'>
print(bool(m)) # True
print(list()) # []
# Built-in Functions on List
m = [10, 20, 30, 40]
print(len(m)) # 4
m.append(50)
print('m = ', m) # m = [10, 20, 30, 40, 50]
m.insert(2, 25)
print('m = ', m) # m = [10, 20, 25, 30, 40, 50]
m.remove(25)
print('m = ', m) # m = [10, 20, 30, 40, 50]
m.pop()
print('m = ', m) # m = [10, 20, 30, 40]
m.pop(1)
print('m = ', m) # m = [10, 30, 40]
m.clear()
print('m = ', m) # m = []  

# String
k = 'Python'
print('k = ', k , "\t&" , 'type(k) = ', type(k)) # k = Python & type(k) = <class 'str'>
print(bool(k)) # True
print(str()) # ''
# Built-in Functions on String
k = 'Python'
print(k.upper()) # PYTHON
print(k.lower()) # python
print(k.capitalize()) # Python
print(k.title()) # Python
print(k.swapcase()) # pYTHON
print(k.count('P')) # 1
print(k.find('P')) # 0
print(k.index('P')) # 0
print(k.replace('P', 'J')) # Jython
print(k.split('t')) # ['Py', 'hon']

# Tuple
n = (10, 20, 30, 40)
print('n = ', n , "\t&" , 'type(n) = ', type(n)) # n = (10, 20, 30, 40) & type(n) = <class 'tuple'>
print(bool(n)) # True
print(tuple()) # ()
# Built-in Functions on Tuple
n = (10, 20, 30, 40)
print(len(n)) # 4
print(n.count(10)) # 1
print(n.index(20)) # 1
print(n[2]) # 30


# Set
o = {10, 20, 30, 40}
print('o = ', o , "\t&" , 'type(o) = ', type(o)) # o = {40, 10, 20, 30} & type(o) = <class 'set'>
print(bool(o)) # True
print(set()) # set()
# Built-in Functions on Set
o = {10, 20, 30, 40}
print(len(o)) # 4
o.add(50)
print('o = ', o) # o = {40, 10, 50, 20, 30}
o.remove(50)
print('o = ', o) # o = {40, 10, 20, 30}
o.pop()
print('o = ', o) # o = {10, 20, 30}
o.clear()
print('o = ', o) # o = set()

# Dictionary
p = {1: 'One', 2: 'Two', 3: 'Three'}
print('p = ', p , "\t&" , 'type(p) = ', type(p)) # p = {1: 'One', 2: 'Two', 3: 'Three'} & type(p) = <class 'dict'>
print(bool(p)) # True
print(dict()) # {}
# Built-in Functions on Dictionary
p = {1: 'One', 2: 'Two', 3: 'Three'}
print(len(p)) # 3
print(p.get(2)) # Two
print(p.keys()) # dict_keys([1, 2, 3])
print(p.values()) # dict_values(['One', 'Two', 'Three'])
print(p.items()) # dict_items([(1, 'One'), (2, 'Two'), (3, 'Three')])
p[4] = 'Four'
print('p = ', p) # p = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
p.pop(2)
print('p = ', p) # p = {1: 'One', 3: 'Three'}
p.clear()
print('p = ', p) # p = {}
q = {1: 'One', 2: 'Two', 3: 'Three'}
print(q.popitem()) # (3, 'Three')
print('q = ', q) # q = {1: 'One', 2: 'Two'}
q = {1: 'One', 2: 'Two', 3: 'Three'}
print(q.setdefault(4, 'Four')) # Four
q = {1: 'One', 2: 'Two', 3: 'Three'}
q.update({4: 'Four'})
print('q = ', q) # q = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
q[7] = 'Seven'
q[9+1j] = 'Complex'
print('q = ', q) # q = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 7: 'Seven', (9+1j): 'Complex'}

# Slicing on String
x = "Opportunities don't happen, you create them."
# Positive Indexing
print(x[20:25:1]) # 'happe'
print(x[20:26:1]) # 'happen'
# Negative Indexing
print(x[-21:-16:1]) # 'happe'
print(x[-21:-15:1]) # 'happen'
# SI : start index = 0
print(x[:14:1]) # 'Opportunities'
# ET : end index = -1 or len(x)
print(x[28::1]) # 'you create them.'
# UP : Updation of string = 1
print(x[28:31]) # 'you'
# Full String
print(x[::1]) # 'Opportunities don't happen, you create them.'
# Even index
print(x[::2]) # 'Ootntesdn'hn yucat hm'
# Odd index
print(x[1::2]) # 'ppriie'ohppn o rete'
# Reverse
print(x[::-1]) # '.meht etaerc uoy ,neppah t'nod seunitnoppO'

# Slicing on List
y = [10, 20, 30, 40, 50, 60]
# Positive Indexing
print(y[1:4:1]) # [20, 30, 40]
print(y[1:5:1]) # [20, 30, 40, 50]
# Negative Indexing
print(y[-5:-2:1]) # [20, 30, 40]
print(y[-5:-1:1]) # [20, 30, 40, 50]
# SI : start index = 0
print(y[:3:1]) # [10, 20, 30]
# ET : end index = -1 or len(y)
print(y[2::1]) # [30, 40, 50, 60]
# UP : Updation of list = 1
print(y[2:4]) # [30, 40]
# Full List
print(y[::1]) # [10, 20, 30, 40, 50, 60]
# Even index
print(y[::2]) # [10, 30, 50]
# Odd index
print(y[1::2]) # [20, 40, 60]
# Reverse
print(y[::-1]) # [60, 50, 40, 30, 20, 10]

# Slicing on Tuple
z = (10, 20, 30, 40, 50, 60)
# Positive Indexing
print(z[1:4:1]) # (20, 30, 40)
print(z[1:5:1]) # (20, 30, 40, 50)
# Negative Indexing
print(z[-5:-2:1]) # (20, 30, 40)
print(z[-5:-1:1]) # (20, 30, 40, 50)
# SI : start index = 0
print(z[:3:1]) # (10, 20, 30)
# ET : end index = -1 or len(z)
print(z[2::1]) # (30, 40, 50, 60)
# UP : Updation of tuple = 1
print(z[2:4]) # (30, 40)
# Full Tuple
print(z[::1]) # (10, 20, 30, 40, 50, 60)
# Even index
print(z[::2]) # (10, 30, 50)
# Odd index
print(z[1::2]) # (20, 40, 60)
# Reverse
print(z[::-1]) # (60, 50, 40, 30, 20, 10)

# Slicing on Set
a = {10, 20, 30, 40, 50, 60}
# Positive Indexing
# print(a[1:4:1]) # TypeError: 'set' object is not subscriptable
# Negative Indexing
# print(a[-5:-2:1]) # TypeError: 'set' object is not subscriptable

# Slicing on Dictionary
b = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six'}
# Positive Indexing
# print(b[1:4:1]) # TypeError: 'dict' object is not subscriptable
# Negative Indexing
# print(b[-5:-2:1]) # TypeError: 'dict' object is not subscriptable

# Membership Operator
# in
print(10 in [10, 20, 30, 40]) # True
print('P' in 'Python') # True
print(10 in (10, 20, 30, 40)) # True
print(10 in {10, 20, 30, 40}) # True
print(1 in {1: 'One', 2: 'Two', 3: 'Three'}) # True
# not in
print(50 not in [10, 20, 30, 40]) # True
print('Z' not in 'Python') # True
print(50 not in (10, 20, 30, 40)) # True
print(50 not in {10, 20, 30, 40}) # True
print(4 not in {1: 'One', 2: 'Two', 3: 'Three'}) # False

# Identity Operator
# is
print(10 is 10) # True
print('Python' is 'Python') # True
print(10 is not 20) # True
print('Python' is not 'Java') # True
# is not
print(10 is not 20) # True
print('Python' is not 'Java') # True

# Logical Operator
# and
print(10 and 20) # 20
print(10 and 0) # 0
print(0 and 20) # 0
print(0 and 0) # 0
# or
print(10 or 20) # 10
print(10 or 0) # 10
print(0 or 20) # 20
print(0 or 0) # 0
# not
print(not 10) # False
print(not 0) # True

# Bitwise Operator
# &
print(10 & 20) # 0
# |
print(10 | 20) # 30
# ^
print(10 ^ 20) # 30
# ~
print(~10) # -11
# <<
print(10 << 2) # 40
# >>
print(10 >> 2) # 2

# Assignment Operator
# =
a = 10
print(a) # 10
# +=
a += 10
print(a) # 20
# -=
a -= 10
print(a) # 10
# *=
a *= 10
print(a) # 100
# /=
a /= 10
print(a) # 10.0
# %=
a %= 10
print(a) # 0.0
# //=
a //= 10
print(a) # 0.0
# **=
a **= 10
print(a) # 0.0
# &=
a = 10
a &= 20
print(a) # 0
# |=
a = 10
a |= 20
print(a) # 30
# ^=
a = 10
a ^= 20
print(a) # 30
# >>=
a = 10
a >>= 2
print(a) # 2
# <<=
a = 10
a <<= 2
print(a) #

# Comparison Operator
# ==
print(10 == 20) # False
# !=
print(10 != 20) # True
# >
print(10 > 20) # False
# <
print(10 < 20) # True
# >=
print(10 >= 20) # False
# <=
print(10 <= 20) # True

# Arithmetic Operator
# +
print(10 + 20) # 30
# -
print(10 - 20) # -10
# *
print(10 * 20) # 200
# /
print(10 / 20) # 0.5
# %
print(10 % 20) # 10
# //
print(10 // 20) # 0
# **
# print(10 ** 2) # 100

# Unary Operator
# +
print(+10) # 10
# -
print(-10) # -10

# Ternary Operator
a = 10
b = 20
print(a if a > b else b) # 20

# Operator Precedence
# ()
# **
# ~
# +, -
# *, /, %, //
# +, -
# <<, >>
# &
# ^
# |
# >, >=, <, <=
# ==, !=
# =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
# is, is not
# in, not in
# not
# and
# or

# Operator Associativity
# Left to Right
# Right to Left

# Operator Overloading
# +
print(10 + 20) # 30
print('Python' + 'Java') # PythonJava
# *
print(10 * 20) # 200
print('Python' * 2) # PythonPython
# ==
print(10 == 20) # False
print('Python' == 'Java') # False
# !=
print(10 != 20) # True
print('Python' != 'Java') # True