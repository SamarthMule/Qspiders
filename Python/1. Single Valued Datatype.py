# Integers
print("\nIntegers")
a , b =10, 0
print(a, b)  # 10 0
print(bool(a), bool(b))  # True False
print(type(a), type(b)) # <class 'int'> <class 'int'>
print("Default Value : " , int())  # 0

# Multiple Values to Multiple Variables
print("\nMultiple Values to Multiple Variables")
a, b, c , a , c = 1, 2, 3, 4, 5
print(a, b, c)
print(id(a), id(b), id(c))

a, b, c, d, e = 1, 2, 3, 1, 3
print(a, b, c, d, e)
print(id(a), id(b), id(c), id(d), id(e))

a, b, c, d, e = 1000, 2000, 3000, 1000, 3000
print(a, b, c, d, e)
print(id(a), id(b), id(c), id(d), id(e))

a, b, c, d, e = -100000000, -200000000, -300000000, -100000000, -300000000
print(a, b, c, d, e)
print(id(a), id(b), id(c), id(d), id(e))

# Float
print("\nFloat")
a, b = 10.0, 0.0
print(a, b) # 10.0 0.0
print(bool(a), bool(b))  # True False
print(type(a), type(b))  # <class 'float'> <class 'float'>
print("Default Value : " , float())  # 0.0

# Complex
print("\nComplex")
a, b = 10+20j, 0+0j 
print(a, b)  # (10+20j) 0j
print(bool(a), bool(b))  # True False
print(type(a), type(b))  # <class 'complex'> <class 'complex'>
print("Default Value : " ,  complex()) # 0j

# m = 2 + j   # NameError: name 'j' is not defined
m = 3j + 2
print(m)    
n = 3j + 2j
print(n)  # 5j

# Boolean
print("\nBoolean")
a, b = True, False
print(a, b)  # True False
print(bool(a), bool(b))  # True False
print(type(a), type(b))  # <class 'bool'> <class 'bool'>
print("Default Value : " , bool())  # False

# Bool as resultant
m, n = 10, 5
print("m > n : ",m > n,"\nm < n : ", m < n)  # True False
# Boolean as stored value
a, b = True, False
print(a , b)  # True False