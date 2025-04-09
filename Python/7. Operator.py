# Operators
# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# # Arithmetic Operators
# # Arithmetic operators are used with numeric values to perform common mathematical operations:
# # Operator	Name	Example
# # +	Addition	x + y
# # int 
# x = 6
# u = 9
# print(x+u) # 15
# # float
# w = 9.7
# z = 6.9
# print(w+z) # 16.7
# # complex
# o = 7 + 8j
# l = 9 + 6j
# print(o+l) # (16+14j)
# # boolean
# a = True
# b = False
# print(a+b) # 1
# # string
# p = 'Hello'
# q = ' World'
# print(p+q) # Hello World
# # list
# w = [1,2,3]
# z = [4,5,6]
# print(w+z) # [1, 2, 3, 4, 5, 6]
# # tuple
# k = (1,2,3)
# m = (4,5,6)
# print(k+m) # (1, 2, 3, 4, 5, 6)
# # set
# q = {1,2,3}
# p = {4,5,6}
# # print(q+p) # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# # dictionary
# h = {1:2,3:4}
# g = {1:6,7:8}
# # print(h+g) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# # -	Subtraction	x - y
# # int
# x = 6
# u = 9
# print(x-u) # -3
# # float
# w = 9.2
# z = 6
# print(w-z) # 3.2
# # complex
# o = 7 + 8j
# l = 9 + 6j
# print(o-l) # (-2+2j)
# # boolean
# a = True
# b = False
# print(a-b) # 1
# # string
# p = 'Hello'
# q = 'World'
# # print(p-q) # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# # list
# w = [1,2,3]
# z = [4,5,6]
# # print(w-z) # TypeError: unsupported operand type(s) for -: 'list' and 'list'
# # tuple
# k = (1,2,3)
# m = (4,5,6)
# # print(k-m) # TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
# # set
# q = {1,2,3,4,6,3}
# p = {5,6,4,7,3,4}
# print(q-p) # {1, 3}
# # dictionary
# h = {1:2,3:9}
# g = {5:6,3:8}
# # print(h-g) # TypeError: unsupported operand type(s) for -: 'dict' and 'dict'

# # *	Multiplication	x * y
# # int
# d = 6
# f = 9
# print(d*f) # 54
# # float
# w = 9.2
# z = 6.1
# print(w*z) # 56.12
# # complex
# o = 7 + 8j
# l = 9 + 6j
# print(o*l) # (15+110j)
# # boolean
# a = True
# b = False
# print(a*b) # 0
# # string
# p = 'Hello'
# q = 3
# print(p*q) # HelloHelloHello
# o = "test"
# p = "best"
# # print(o*p) # TypeError: can't multiply sequence by non-int of type 'str'
# # list
# w = [1,2,3]
# z = 3
# print(w*z) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# l = [1,2,3]
# m = [4,5,6]
# # print(l*m) # TypeError: can't multiply sequence by non-int of type 'list'
# # tuple
# k = (1,2,3)
# m = 3
# print(k*m) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# s = (1,2,3)
# t = (4,5,6)
# # print(s*t) # TypeError: can't multiply sequence by non-int of type 'tuple'
# # set
# q = {1,2,3}
# p = 3
# # print(q*p) # TypeError: unsupported operand type(s) for *: 'set' and 'int'
# a = {1,2,3}
# b = {4,5,6}
# # print(a*b) # TypeError: unsupported operand type(s) for *: 'set' and 'set'
# # dictionary
# h = {1:2,3:4}
# g = 3
# # print(h*g) # TypeError: unsupported operand type(s) for *: 'dict' and 'int'
# a = {1:2,3:4}
# b = {5:6,7:8}
# # print(a*b) # TypeError: unsupported operand type(s) for *: 'dict' and 'dict'

# # 	 Divisions
# # /	 True Division	x / y
# # int
# x = 6
# u = 9
# print(x/u) # 0.6666666666666666
# # float
# w = 9.2
# z = 6.1
# print(w/z) # 1.5081967213114754
# # complex
# o = 99 + 9j
# l = 9 + 9j
# print(o/l) # 6-5j
# # boolean
# a = True
# b = False
# # print(a/b) # ZeroDivisionError: division by zero
# print(b/a) # 0

# # // Floor division	x // y
# # int
# x = 99
# u = 6
# print(x//u) # 16
# # float
# w = 9.2
# z = 6.1
# print(w//z) # 1.0
# # complex
# o = 99 + 9j
# l = 9 + 9j
# # print(o//l) # TypeError: can't take floor of complex number.
# # boolean
# a = True
# b = False
# # print(a//b) # ZeroDivisionError: division by zero
# print(b//a) # 0

# # %	 Modulus	x % y
# # int 
# x = 9
# u = 6
# print(x%u) # 3
# # float
# w = 9.2
# z = 6.1
# print(w%z) # 3.1
# # complex
# o = 99 + 9j
# l = 9 + 9j
# # print(o%l) # TypeError: can't mod complex numbers.
# # boolean
# a = True
# b = False
# # print(a%b) # ZeroDivisionError: division by zero
# print(b%a) # 0

# # ** Exponentiation/Power	x ** y
# # int
# j = 2
# k = 3
# print(j**k) # 8
# # float
# w = 3.5
# z = 5.2
# print(w**z) # 674.7669933054266
# p = 3.5
# q = 5
# print(p**q) # 525.21875
# # complex
# o = 3 + 9j
# l = 2 + 3j
# print(o**l) # (-2.089511684874167+0.3736942957721984j)
# e = 3 + 9j
# f = 2
# print(e**f) # (-72+54j)
# l = True
# m = False
# print(l**m) # 1
# print(m**l) # 0
# print(l**6) # 1
# print(6**l) # 6
# print(m**7) # 0
# print(7**m) # 1
# # string
# p = 'Hello'
# q = 3
# # print(p**q) # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# p = 'Hello'
# q = "World"
# # print(p**q) # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
# f = [1,2,3]
# g = 3
# # print(f**g) # TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
# f = [1,2,3]
# g = [4,5,6]
# # print(f**g) # TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'list'
# f = (1,2,3)
# g = 3
# # print(f**g) # TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'
# f = (1,2,3)
# g = (4,5,6)
# # print(f**g) # TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'tuple'
# f = {1,2,3}
# g = 3
# # print(f**g) # TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'int'
# f = {1,2,3}
# g = {4,5,6}
# # print(f**g) # TypeError: unsupported operand type(s) for ** or pow(): 'set' and 'set'
# f = {1:2,3:4}
# g = 3
# # print(f**g) # TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'int'
# f = {1:2,3:4}
# g = {5:6,7:8}
# # print(f**g) # TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'dict'



# # Relational Operators
# # Relational operators are used to compare values. It either returns True or False according to the condition.
# # Operator	Name	Example
# # ==	Equal	x == y
# # int
# x = 6
# u = 9
# print("6 == 9 : ",x==u) # False
# l = 6
# print("6 == 6 : ",x==l) # True
# # float
# w = 9.2
# z = 6.1
# print("9.2 == 6.1 : ",w==z) # False
# f = 9.2
# print("9.2 == 9.2 : ",w==f) # True
# # complex
# o = 7 + 8j
# l = 7 + 8j
# print("7 + 8j == 7 + 8j : ",o==l) # True
# d = 5 + 8j
# print("7 + 8j == 5 + 8j : ",o==d) # False
# # boolean
# a = True
# b = False
# print("True == False : ",a==b) # False
# c = True
# print("True == True : ",a==c) # True
# # string
# p = 'Hello'
# q = 'World'
# print("Hello == World : ",p==q) # False
# k = 'Hello'
# print("Hello == Hello : ",p==k) # True
# k = 'hello'
# print("Hello == hello : ",p==k) # False
# d = 'hlleo'
# print("hello == hlleo : ", k==d) # False
# # list
# w = [1,2,3]
# k = [1,2,3]
# print("[1,2,3] == [1,2,3] : ",w==k) # True
# l = [8,9,0]
# print("[1,2,3] == [8,9,0] : ",w==l) # False
# l = [3,2,1]
# print("[1,2,3] == [3,2,1] : ",w==l) # False
# # tuple
# k = (1,2,3)
# m = (1,2,3)
# print("(1,2,3) == (1,2,3) : ",k==m) # True
# o = (8,9,0)
# print("(1,2,3) == (8,9,0) : ",k==o) # False
# o = (3,2,1)
# print("(1,2,3) == (3,2,1) : ",k==o) # False
# # set
# q = {1,2,3}
# i = {3,2,1,1}
# print("{1,2,3} == {3,2,1,1} : ",q==i) # True
# x = {1,2,4}
# print("{1,2,3} == {1,2,4} : ",q==x) # False
# # dictionary
# h = {1:2,3:4}
# g = {1:2,3:4}
# print("{1:2,3:4} == {1:2,3:4} : ",h==g) # True
# k = {1:5, 3:2}
# print("{1:2,3:4} == {1:5, 3:2} : ",h==k) # False

# # !=	Not equal	x != y
# # int
# x = 6
# u = 9
# print("6 != 9 : ",x!=u) # True
# l = 6
# print("6 != 6 : ",x!=l) # False
# # float
# w = 9.2
# z = 6.1
# print("9.2 != 6.1 : ",w!=z) # True
# f = 9.2
# print("9.2 != 9.2 : ",w!=f) # False
# # complex
# o = 7 + 8j
# l = 7 + 8j
# print("7 + 8j != 7 + 8j : ",o!=l) # False
# d = 5 + 8j
# print("7 + 8j != 5 + 8j : ",o!=d) # True
# # boolean
# a = True
# b = False
# print("True != False : ",a!=b) # True
# c = True
# print("True != True : ",a!=c) # False
# # string
# p = 'Hello'
# q = 'World'
# print("Hello != World : ",p!=q) # True
# k = 'Hello'
# print("Hello != Hello : ",p!=k) # False
# k = 'hello'
# print("Hello != hello : ",p!=k) # True
# d = 'hlleo'
# print("hello != hlleo : ", k!=d) # True
# # list
# w = [1,2,3]
# k = [1,2,3]
# print("[1,2,3] != [1,2,3] : ",w!=k) # False
# l = [8,9,0]
# print("[1,2,3] != [8,9,0] : ",w!=l) # True
# l = [3,2,1]
# print("[1,2,3] != [3,2,1] : ",w!=l) # True
# # tuple
# k = (1,2,3)
# m = (1,2,3)
# print("(1,2,3) != (1,2,3) : ",k!=m) # False
# o = (8,9,0)
# print("(1,2,3) != (8,9,0) : ",k!=o) # True
# o = (3,2,1)
# print("(1,2,3) != (3,2,1) : ",k!=o) # True
# # set
# q = {1,2,3}
# i = {3,2,1,1}
# print("{1,2,3} != {3,2,1,1} : ",q!=i) # False
# x = {1,2,4}
# print("{1,2,3} != {1,2,4} : ",q!=x) # True
# # dictionary
# h = {1:2,3:4}
# g = {1:2,3:4}
# print("{1:2,3:4} != {1:2,3:4} : ",h!=g) # False
# k = {1:5, 3:2}
# print("{1:2,3:4} != {1:5, 3:2} : ",h!=k) # True

# # >	Greater than	x > y
# # int
# x = 6
# u = 9
# print("6 > 9 : ",x>u) # False
# l = 6
# print("6 > 6 : ",x>l) # False
# k = 3
# print("6 > 3 : ",x>k) # True
# # float
# w = 9.2
# z = 6.1
# print("9.2 > 6.1 : ",w>z) # True
# f = 9.2
# print("9.2 > 9.2 : ",w>f) # False
# g = 9.3
# print("9.2 > 9.3 : ",w>g) # False
# # complex
# o = 7 + 8j
# l = 7 + 8j
# # print("7 + 8j > 7 + 8j : ",o>l) # TypeError: '>' not supported between instances of 'complex' and 'complex'
# e = 7 + 9j
# # print("7 + 8j > 7 + 9j : ",o>e) # TypeError: '>' not supported between instances of 'complex' and 'complex'
# # boolean
# a = True
# b = False
# print("True > False : ",a>b) # True
# print("False > True : ",b>a) # False
# c = True
# print("True > True : ",a>c) # False
# # string
# h = 'Hello'
# g = 'World'
# print("Hello > World : ",h>g) # False
# print("World > Hello : ",g>h) # True
# k = "hello"
# print("Hello > hello : ",h>k) # False

# # Concpect of ASCII value
# # ASCII value of 'A' is 65
# # ASCII value of 'a' is 97
# # Use ord() to get the ASCII value of a character
# print(ord('A')) # 65
# print(ord('a')) # 97
# # Use chr() to get the character of a ASCII value
# print(chr(65)) # A
# print(chr(97)) # a

# # list
# w = [1,2,2] 
# k = [1,2,3]
# print("[1,2,2] > [1,2,3] : ",w>k) # False
# print("[1,2,3] > [1,2,2] : ",k>w) # True
# l = [8,9,0]
# print("[1,2,3] > [8,9,0] : ",w>l) # False
# l = [3,2,1]
# print("[1,2,3] > [3,2,1] : ",w>l) # False

# # tuple 
# k = (1,2,3)
# m = (1,2,3)
# print("(1,2,3) > (1,2,3) : ",k>m) # False
# o = (8,9,0)
# print("(1,2,3) > (8,9,0) : ",k>o) # False
# print("(8,9,0) > (1,2,3) : ",o>k) # True
# o = (3,2,1)
# print("(1,2,3) > (3,2,1) : ",k>o) # False
# print("(3,2,1) > (1,2,3) : ",o>k) # True

# # set
# k = {1,2,3}
# m = {1,2,3}
# print("{1,2,3} > {1,2,3} : ",k>m) # False
# f = {2,1,2,1}
# print("{1,2,3} > {2,1,2,1} : ",k>f) # True
# print("{2,1,2,1} > {1,2,3} : ",f>k) # False
# s = {3,2,2}
# print("{1,2,3} > {3,2,2} : ",k>s) # True

# # dictionary
# h = {1:2,3:4}
# g = {1:2,3:4}
# # print("{1:2,3:4} > {1:2,3:4} : ",h>g) # TypeError: '>' not supported between instances of 'dict' and 'dict'
# k = {1:5, 3:2}
# # print("{1:2,3:4} > {1:5, 3:2} : ",h>k) # TypeError: '>' not supported between instances of 'dict' and 'dict'
# # print("{1:5, 3:2} > {1:2,3:4} : ",k>h) # TypeError: '>' not supported between instances of 'dict' and 'dict'


# # <	Less than	x < y
# # int
# x = 6
# u = 9
# print("6 < 9 : ",x<u) # True
# l = 6
# print("6 < 6 : ",x<l) # False
# k = 3
# print("6 < 3 : ",x<k) # False
# # float
# w = 9.2
# z = 6.1
# print("9.2 < 6.1 : ",w<z) # False
# f = 9.2
# print("9.2 < 9.2 : ",w<f) # False
# g = 9.3
# print("9.2 < 9.3 : ",w<g) # True
# # complex
# o = 7 + 8j
# l = 7 + 8j
# # print("7 + 8j < 7 + 8j : ",o<l) # TypeError: '<' not supported between instances of 'complex' and 'complex'
# e = 7 + 9j
# # print("7 + 8j < 7 + 9j : ",o<e) # TypeError: '<' not supported between instances of 'complex' and 'complex'
# # boolean
# a = True
# b = False
# print("True < False : ",a<b) # False
# print("False < True : ",b<a) # True
# c = True
# print("True < True : ",a<c) # False
# # string
# h = 'Hello'
# g = 'World'
# print("Hello < World : ",h<g) # True
# print("World < Hello : ",g<h) # False
# k = "hello"
# print("Hello < hello : ",h<k) # True

# # list
# w = [1,2,2] 
# k = [1,2,3]
# print("[1,2,2] < [1,2,3] : ",w<k) # True
# print("[1,2,3] < [1,2,2] : ",k<w) # False
# l = [8,9,0]
# print("[1,2,3] < [8,9,0] : ",w<l) # True
# l = [3,2,1]
# print("[1,2,3] < [3,2,1] : ",w<l) # True

# # tuple 
# k = (1,2,3)
# m = (1,2,3)
# print("(1,2,3) < (1,2,3) : ",k<m) # False
# o = (8,9,0)
# print("(1,2,3) < (8,9,0) : ",k<o) # True
# print("(8,9,0) < (1,2,3) : ",o<k) # False
# o = (3,2,1)
# print("(1,2,3) < (3,2,1) : ",k<o) # True
# print("(3,2,1) < (1,2,3) : ",o<k) # False

# # set
# k = {1,2,3}
# m = {1,2,3}
# print("{1,2,3} < {1,2,3} : ",k<m) # False
# f = {2,1,2,1}
# print("{1,2,3} < {2,1,2,1} : ",k<f) # False
# print("{2,1,2,1} < {1,2,3} : ",f<k) # True
# s = {3,2,2}
# print("{1,2,3} < {3,2,2} : ",k<s) # False

# # dictionary
# h = {1:2,3:4}
# g = {1:2,3:4}
# # print("{1:2,3:4} < {1:2,3:4} : ",h<g) # TypeError: '<' not supported between instances of 'dict' and 'dict'
# k = {1:5, 3:2}
# # print("{1:2,3:4} < {1:5, 3:2} : ",h<k) # TypeError: '<' not supported between instances of 'dict' and 'dict'
# # print("{1:5, 3:2} < {1:2,3:4} : ",k<h) # TypeError: '<' not supported between instances of 'dict' and 'dict'

# # >= Greater than or equal to x >= y
# # int
# x = 6
# u = 9
# print("6 >= 9 : ",x>=u) # False
# l = 6
# print("6 >= 6 : ",x>=l) # True
# k = 3
# print("6 >= 3 : ",x>=k) # True
# # float
# w = 9.2
# z = 6.1
# print("9.2 >= 6.1 : ",w>=z) # True
# f = 9.2
# print("9.2 >= 9.2 : ",w>=f) # True
# g = 9.3
# print("9.2 >= 9.3 : ",w>=g) # False
# # complex
# o = 7 + 8j
# l = 7 + 8j
# # print("7 + 8j >= 7 + 8j : ",o>=l) # TypeError: '>=' not supported between instances of 'complex' and 'complex'
# e = 7 + 9j
# # print("7 + 8j >= 7 + 9j : ",o>=e) # TypeError: '>=' not supported between instances of 'complex' and 'complex'
# # boolean
# a = True
# b = False
# print("True >= False : ",a>=b) # True
# print("False >= True : ",b>=a) # False
# c = True
# print("True >= True : ",a>=c) # True
# # string
# h = 'Hello'
# g = 'World'
# print("Hello >= World : ",h>=g) # False
# print("World >= Hello : ",g>=h) # True
# k = "hello"
# print("Hello >= hello : ",h>=k) # False

# # list
# w = [1,2,2] 
# k = [1,2,3]
# print("[1,2,2] >= [1,2,3] : ",w>=k) # False
# print("[1,2,3] >= [1,2,2] : ",k>=w) # True
# l = [8,9,0]
# print("[1,2,3] >= [8,9,0] : ",w>=l) # False
# l = [3,2,1]
# print("[1,2,3] >= [3,2,1] : ",w>=l) # False

# # tuple 
# k = (1,2,3)
# m = (1,2,3)
# print("(1,2,3) >= (1,2,3) : ",k>=m) # True
# o = (8,9,0)
# print("(1,2,3) >= (8,9,0) : ",k>=o) # False
# print("(8,9,0) >= (1,2,3) : ",o>=k) # True
# o = (3,2,1)
# print("(1,2,3) >= (3,2,1) : ",k>=o) # False
# print("(3,2,1) >= (1,2,3) : ",o>=k) # True

# # set
# k = {1,2,3}
# m = {1,2,3}
# print("{1,2,3} >= {1,2,3} : ",k>=m) # True
# f = {2,1,2,1}
# print("{1,2,3} >= {2,1,2,1} : ",k>=f) # True
# print("{2,1,2,1} >= {1,2,3} : ",f>=k) # False
# s = {3,2,2}
# print("{1,2,3} >= {3,2,2} : ",k>=s) # True

# # dictionary
# h = {1:2,3:4}
# g = {1:2,3:4}
# # print("{1:2,3:4} >= {1:2,3:4} : ",h>=g) # TypeError: '>=' not supported between instances of 'dict' and 'dict'
# k = {1:5, 3:2}
# # print("{1:2,3:4} >= {1:5, 3:2} : ",h>=k) # TypeError: '>=' not supported between instances of 'dict' and 'dict'

# # <= Less than or equal to x <= y
# # int
# x = 6
# u = 9
# print("6 <= 9 : ",x<=u) # True
# l = 6
# print("6 <= 6 : ",x<=l) # True
# k = 3
# print("6 <= 3 : ",x<=k) # False
# # float
# w = 9.2
# z = 6.1
# print("9.2 <= 6.1 : ",w<=z) # False
# f = 9.2
# print("9.2 <= 9.2 : ",w<=f) # True
# g = 9.3
# print("9.2 <= 9.3 : ",w<=g) # True
# # complex
# o = 7 + 8j
# l = 7 + 8j
# # print("7 + 8j <= 7 + 8j : ",o<=l) # TypeError: '<=' not supported between instances of 'complex' and 'complex'
# e = 7 + 9j
# # print("7 + 8j <= 7 + 9j : ",o<=e) # TypeError: '<=' not supported between instances of 'complex' and 'complex'
# # boolean
# a = True
# b = False
# print("True <= False : ",a<=b) # False
# print("False <= True : ",b<=a) # True
# c = True
# print("True <= True : ",a<=c) # True
# # string
# h = 'Hello'
# g = 'World'
# print("Hello <= World : ",h<=g) # True
# print("World <= Hello : ",g<=h) # False
# k = "hello"
# print("Hello <= hello : ",h<=k) # True

# # list
# w = [1,2,2] 
# k = [1,2,3]
# print("[1,2,2] <= [1,2,3] : ",w<=k) # True
# print("[1,2,3] <= [1,2,2] : ",k<=w) # False
# l = [8,9,0]
# print("[1,2,3] <= [8,9,0] : ",w<=l) # True
# l = [3,2,1]
# print("[1,2,3] <= [3,2,1] : ",w<=l) # True

# # tuple 
# k = (1,2,3)
# m = (1,2,3)
# print("(1,2,3) <= (1,2,3) : ",k<=m) # True
# o = (8,9,0)
# print("(1,2,3) <= (8,9,0) : ",k<=o) # True
# print("(8,9,0) <= (1,2,3) : ",o<=k) # False
# o = (3,2,1)
# print("(1,2,3) <= (3,2,1) : ",k<=o) # True
# print("(3,2,1) <= (1,2,3) : ",o<=k) # False

# # set
# k = {1,2,3}
# m = {1,2,3}
# print("{1,2,3} <= {1,2,3} : ",k<=m) # True
# f = {2,1,2,1}
# print("{1,2,3} <= {2,1,2,1} : ",k<=f) # False
# print("{2,1,2,1} <= {1,2,3} : ",f<=k) # True
# s = {3,2,2}
# print("{1,2,3} <= {3,2,2} : ",k<=s) # False

# # dictionary
# h = {1:2,3:4}
# g = {1:2,3:4}
# # print("{1:2,3:4} <= {1:2,3:4} : ",h<=g) # TypeError: '<=' not supported between instances of 'dict' and 'dict'
# k = {1:5, 3:2}
# # print("{1:2,3:4} <= {1:5, 3:2} : ",h<=k) # TypeError: '<=' not supported between instances of 'dict' and 'dict'
# # print("{1:5, 3:2} <= {1:2,3:4} : ",k<=h) # TypeError: '<=' not supported between instances of 'dict' and 'dict'

# # Logical Operators
# Logical Operators are used to combine conditional statements. It either returns True or False according to the condition. 
# # Logical And
# print("12 > 5 and 6 > 3 : ",12 > 5 and 6 > 3) # True
# print("12 > 5 and 6 < 3 : ",12 > 5 and 6 < 3) # False
# print("12 < 5 and 6 < 3 : ",12 < 5 and 6 < 3) # False
# print("10 > 5 and 5 < 20 : ",10 > 5 and 5 < 20) # True

# # Logical OR
# print("12 > 5 or 6 > 3 : ",12 > 5 or 6 > 3) # True
# print("12 > 5 or 6 < 3 : ",12 > 5 or 6 < 3) # True
# print("12 < 5 or 6 < 3 : ",12 < 5 or 6 < 3) # False
# print("10 < 5 or 5 > 20 : ",10 < 5 or 5 > 20) # False

# # Logical NOT
# print("not 12 > 5 : ",not 12 > 5) # False
# print("not 12 < 5 : ",not 12 < 5) # True
# print("not '' : ",not '') # True
# print("not 'Hello' : ",not 'Hello') # False

# # Bitwise Operators
# # Bitwise AND
# print("12 & 13 : ",12 & 13) # 12
# print("Binary of 12 : ",bin(12)) # 0b1100
# print("Binary of 13 : ",bin(13)) # 0b1101
# print("        And  : ",bin(12 & 13)) # 0b1100
# # Binary of 12 is 1100
# # Binary of 13 is 1101
# # And :           1100
# print("10 & 13 : ",10 & 13) # 8

# # Bitwise OR
# print("12 | 13 : ",12 | 13) # 13
# # Binary of 12 is 1100
# # Binary of 13 is 1101
# # Or :            1101
# print("10 | 13 : ",10 | 13) # 15

# # Bitwise XOR
# print("12 ^ 13 : ",12 ^ 13) # 1
# # Binary of 12 is 1100
# # Binary of 13 is 1101
# # XOR :           0011
# print("10 ^ 13 : ",10 ^ 13) # 7

# # Bitwise NOT
# print("~12 : ",~12) # -13
# # -(op + 1)
# # -(12 + 1) = -13
# print("~-10 : ",~-10) # 9
# # -(-10 + 1) = 9

# # Bitwise Left Shift
# print("12 << 2 : ",12 << 2) # 48
# # Binary of 12 is 1100
# # Left shift by 2
# # 110000 = 48
# print("10 << 2 : ",10 << 2) # 40

# # Bitwise Right Shift
# print("12 >> 2 : ",12 >> 2) # 3
# # Binary of 12 is 1100
# # Right shift by 2
# # 11 = 3
# print("10 >> 2 : ",10 >> 2) # 2


# # ord and char
# print(ord('A')) # 65
# print(ord('a')) # 97
# print(ord('@')) # 64
# print(ord('[')) # 91
# print(ord('1')) # 49
# print(ord('^')) # 94
# print(ord('`')) # 96
# print(ord('{')) # 123

# print(chr(65)) # A
# print(chr(97)) # a
# print(chr(104)) # h
# print(chr(122)) # z
# print(chr(50)) # 2
# print(chr(2)) # 
# print(chr(1)) # 
# print(chr(9)) # invisible tab

# # # Assignment Operators
# # # Assignment operators are used to assign values to variables.
# a = 10
# b = 5
# print("a = 10 : ",a) # 10
# print("b = 20 : ",b) # 20
# a += b # a = a + b
# print("a += b : ",a) # 15
# a -= b # a = a - b
# print("a -= b : ",a) # 10
# a *= b # a = a * b
# print("a *= b : ",a) # 50
# a /= b # a = a / b
# print("a /= b : ",a) # 10.0
# a **= b # a = a ** b
# print("a **= b : ",a) # 100000
# a //= b # a = a // b
# print("a //= b : ",a) # 20000
# a %= b # a = a % b
# print("a %= b : ",a) # 0.0

# c = 10
# d = 7
# print("c = 10 : ",c) # 10
# print("d = 7 : ",d) # 7
# c &= d # c = c & d
# print("c &= d : ",c) # 2
# c |= d # c = c | d
# print("c |= d : ",c) # 7
# c ^= d # c = c ^ d
# print("c ^= d : ",c) # 5
# c = 14
# d = 3
# c >>= d # c = c >> d
# print("c >>= d : ",c) # 1
# c <<= d # c = c << d
# print("c <<= d : ",c) # 8

# # Membership Operators
# # Membership operators are used to test if a sequence is presented in an object.
# # In 
# print("2 in [1,2,3] : ",2 in [1,2,3]) # True
# print("5 in [1,2,3] : ",5 in [1,2,3]) # False
# print("20 in [10,[20,30],40] : ",20 in [10,[20,30],40]) # False
# print("'World' in 'Hello World' : ",'World' in 'Hello World') # True
# print("'H' in 'Hello' : ",'H' in 'Hello') # True
# print("'h' in 'Hello' : ",'h' in 'Hello') # False
# print("4 in (1,2,3) : ",4 in (1,2,3)) # False
# print("2 in (1,2,3) : ",2 in (1,2,3)) # True
# print("5 in {1,2,3} : ",5 in {1,2,3}) # False
# print("3 in {1,2,3} : ",3 in {1,2,3}) # True
# print("4 in {1:2,3:4} : ",4 in {1:2,3:4}) # False
# print("3 in {1:2,3:4} : ",3 in {1:2,3:4}) # True

# # Not In
# print("2 not in [1,2,3] : ",2 not in [1,2,3]) # False
# print("5 not in [1,2,3] : ",5 not in [1,2,3]) # True
# print("'H' not in 'Hello' : ",'H' not in 'Hello') # False
# print("'h' not in 'Hello' : ",'h' not in 'Hello') # True
# print("4 not in (1,2,3) : ",4 not in (1,2,3)) # True
# print("2 not in (1,2,3) : ",2 not in (1,2,3)) # False
# print("5 not in {1,2,3} : ",5 not in {1,2,3}) # True
# print("3 not in {1,2,3} : ",3 not in {1,2,3}) # False
# print("4 not in {1:2,3:4} : ",4 not in {1:2,3:4}) # True
# print("3 not in {1:2,3:4} : ",3 not in {1:2,3:4}) # False

# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
# IS 
# print("5 is 5 : ",5 is 5) # True
# print("5.9 is 6.9 : ",5.9 is 6.9) # False
# print("[10, 20] is [10, 20] : ",[10, 20] is [10, 20]) # False
# print("8+9j is 8+9j : ",8+9j is 8+9j) # True
# print("True is True : ",True is True) # True
# print("'p' is 'P : ", 'p' is 'P') # False
# print("'Hello' is 'Hello' : ", 'Hello' is 'Hello') # True
# print("{'a':1} is {'a':1} : ",{'a':1} is {'a':1}) # False

# # IS NOT
# print("5 is not 5 : ",5 is not 5) # False
# print("5.9 is not 6.9 : ",5.9 is not 6.9) # True
# print("[10, 20] is not [10, 20] : ",[10, 20] is not [10, 20]) # True
# print("8+9j is not 8+9j : ",8+9j is not 8+9j) # False
# print("True is not True : ",True is not True) # False
# print("'p' is not 'P : ", 'p' is not 'P') # True
# print("'Hello' is not 'Hello' : ", 'Hello' is not 'Hello') # False
# print("{'a':1} is not {'a':1} : ",{'a':1} is not {'a':1}) # True