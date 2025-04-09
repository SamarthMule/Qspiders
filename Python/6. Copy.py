# General Copy:
# Integers, Floats, Strings, Tuples, Frozensets, Booleans, None, and built-in functions are immutable.
# Lists, Dictionaries, Sets, and all other objects are mutable.
# Immutable objects are copied by value, mutable objects are copied by reference.

# # Int / Float / String / Tuple / Frozenset / Boolean / None / Built-in Function
# a = 12
# b = a
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# a = 15
# print(a)
# print(b)

# # List
# a = [1,2,3]
# b = a
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# a[1] = 200
# print(a)
# print(b)

# # String
# s = "Hello"
# t = s
# print(s)
# print(t)
# print(id(s))
# print(id(t))
# s = "Hi"
# print(s)
# print(t)

# # Dictionary
# d = {"a":1, "b":2}
# e = d
# print(d)
# print(e)
# print(id(d))
# print(id(e))
# d["a"] = 100
# print(d)
# print(e)

# # Set
# g = {2,4,3,5,6,0,2,3,4,5,5}
# h = g
# print(g)
# print(h)
# print(id(g))
# print(id(h))
# g.add(100)
# g.remove(0)
# print(g)
# print(h)

# Shallow Copy:
# A shallow copy creates a new object, but does not create new objects for the elements within the original object.
# Shallow copies are created using the copy() method or the copy module.
# Shallow copies are used to create a new object, but the elements within the object are not copied.
# Shallow copies are used when the original object has elements that are immutable.
# Shallow copies are used when the original object has elements that are mutable, but you don't want to copy them.

# a = [23,45,87]
# b = a.copy()
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# a[1] = 200
# print(a)
# print(b)

# # In case of nested lists, the outer list is copied by value, but the inner list is copied by reference. 
# # This means that if you modify the inner list, the changes will be reflected in both the original and the copied list.
# j = [22,33,44,[55,66,77]]
# k = j.copy()
# print(j)
# print(k)
# print(id(j))
# print(id(k))
# k[3][1] = 200
# print(j)
# print(k)

# d = {"a":1, "b":2, "c":[20,44,27]}
# e = d.copy()
# print(d)
# print(e)
# print(id(d))
# print(id(e))
# e["c"][1] = 200
# print(d)
# print(e)

# # Deep Copy:
# # A deep copy creates a new object and recursively adds the copies of the nested objects present in the original elements.
# # Deep copies are created using the deepcopy() method from the copy module.
# # Deep copies are used when the original object has elements that are mutable and you want to copy them.
# # Deep copies are used when the original object has elements that are mutable and you don't want to modify the original object.
# g = [23,45,87,[22,33,44]]
# h = g.copy()
# print(g)
# print(h)
# print(id(g))
# print(id(h))
# import copy
# i = copy.deepcopy(g)
# print(i)
# print(id(i))
# g[3][1] = 200
# print(g)
# print(h)
# print(i)
# h[3][0] = 100
# print(g)
# print(h)
# print(i)
# i[3][2] = 300
# print(g)
# print(h)
# print(i)

# Some differences between shallow copy and deep copy:
# 1. Shallow copies do not create new objects for the elements within the original object.
#    Deep copies create new objects for the elements within the original object.
# 2. Shallow copies are used when the original object has elements that are immutable.
#    Deep copies are used when the original object has elements that are mutable.
# 3. Shallow copies are used when the original object has elements that are mutable, but you don't want to copy them.
#    Deep copies are used when the original object has elements that are mutable and you want to copy them.
# 4. Shallow copies are created using the copy() method or the copy module.
#    Deep copies are created using the deepcopy() method from the copy module.

