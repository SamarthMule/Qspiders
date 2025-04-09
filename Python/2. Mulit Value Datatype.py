# h = '''

# This is 
# Multi's "Line"

# '''
# print(h)

# a = 'py'
# b = "Batch"
# c = "Batch"
# print(a , b )
# print(id(a) , id(b) , id(c))
# print(id(b) == id(c))
# print(bool(a), bool(b))
# print(str())

# print(a[1])
# print(b[3])
# print(b[2] + b[3])

# x = '''Python's Class'''
# print(x[-8])
# print(x[-1])
# print(x[-11 : -8])
# print(x[3 : 11])

# x = [10, 4.5, 9+6j , False, 'session']
# print(x)
# print(x[2])
# print(x[4][4])
# x[1] = 14.15
# print(x)
# # x[4][4] = 'z' # Error : 'str' object does not support item assignment
# # print(x)

u = [1,     'c',    4.4,   8+3j,    True,   'python', {2,3,3,5,9,9,9}, (10,20,30), {'a':10, 'b':20}, [10,20,30]]
#    0       1       2       3       4       5           6               7           8                  9
#    -10     -9      -8      -7      -6      -5          -4              -3          -2                 -1
#    int    str    float   complex  bool    str         set             tuple       dict                list

print(u)

# # In built functions on List
# y = [10, 4.5, 9+6j , False,]
# print(y)
# # lenght of list
# print(len(x))
# # Append
# y.append(100)
# y.append('python')
# print(y)
# # Insert
# y.insert(2, 'Java')
# y.insert(6, 8+9j)
# print(y)
# # Extend
# z = [6.9, 5+5j, 'html']
# y.extend([1,2,3])
# y.extend(z)
# print(y)
# k = [1,2,3]
# print(k)
# k.extend('python')
# k.extend([4,5,6])
# print(k)

# j = [1,6.6,'py']
# print("j : ", j)
# j.extend([10,[20,30,['python']]])
# print("j : ", j)
# print("-"*50 + "\n")
# a , b , c = [1] , [2] , [3]
# print("a : " , a) 
# a.extend('python')
# print("a : " , a)
# a.extend([10,30])
# print("a : " , a)

# print("b : " , b)
# b.extend([10, 20,[30]])
# print("b : " , b)

# print("c : " , c)
# c.extend([10,20,30,[1,[3,4]]])
# print("c : " , c)

# print("\n")

# # pop
# z = [10, 4.5, 9+6j , False, 8+9j, 'html', 3]
# print("z : ", z) # [10, 4.5, (9+6j), False, (8+9j), 'html', 3]
# z.pop() # last element pop
# print("z : ", z) # [10, 4.5, (9+6j), False, (8+9j), 'html']
# z.pop(2) # index based pop
# print("z : ", z) # [10, 4.5, False, (8+9j), 'html']
# # z.pop(7) # Error : IndexError: pop index out of range 

# # remove
# z.remove(4.5) # value based remove
# print("z : ", z) # [10, False, (8+9j), 'html']
# z.remove(10) # value based remove
# print("z : ", z) # [False, (8+9j), 'html']
# # z.remove(20) # Error : list.remove(x): x not in list

# print("\n")

# # clear
# z.clear()
# print("z : ", z) # []

# # index
# z = [10, 4.5, 9+6j , False, 8+9j, 'html', 3]
# print("z : ", z) # [10, 4.5, (9+6j), False, (8+9j), 'html', 3]
# print(z.index(4.5)) # 1
# print(z.index(3)) # 6
# # print(z.index(20)) # Error : ValueError

# # count
# print(z.count(10)) # 1
# print(z.count(4.5)) # 1
# print(z.count(3)) # 1

# # reverse
# z.reverse()
# print("z : ", z) # [3, 'html', (8+9j), False, (9+6j), 4.5, 10]

# # sort
# z = [10, 40 , 5 , 2 , 1]
# print("z : ", z) # [10, 4.5, (9+6j), False, (8+9j), 3]
# z.sort()
# print("z : ", z) # [False, 3, 4.5, 10, (3+4j), (8+9j)]
# print("\n")



# # Tulpe
# t = (10, 4.5, 9+6j , False, 8+9j, 3)
# p = 10, 4.5, 9+6j , False, 'class', 3
# print("t : ", t)
# print("p : ", p)
# print(id(t) , id(p))
# print(type(t) , type(p))
# print("t[2] : ", t[2])
# print("p[4][2] : ", p[4][2])
# print(bool(t))
# print(tuple())
# o = ([1,2,3], [4,5,6])
# print("o : ", o)
# print(o[0][1])
# o[1].append(7)
# print(o)
# print(type(o))

u = (1,     'c',    4.4,   8+3j,    True,   'python', {2,3,3,5,9,9,9}, (10,20,30), {'a':10, 'b':20} , [10,20,30])
#    0       1       2       3       4       5           6               7           8                 9
#    -10     -9      -8      -7      -6      -5          -4              -3          -2                -1
#    int    str    float   complex  bool    str         set             tuple       dict              list
print(u)

# l = ('python', 'java', 'html')
# print("l : ", l)
# # l[1] = 'c' # Error : 'tuple' object does not support item assignment
# # print(l)

# # In built functions on Tuple
# print(t)
# print(len(t))
# print(t.index(4.5))
# print(t.count(3))

# # t[2] = 10 # Error : 'tuple' object does not support item assignment
# print("\n")

# t = ([1,2,3], [4,5,6])
# print("t : ", t, "id : " ,id(t) , "size : ", len(t))
# t[1].append(7)
# print(type(t))
# print("t : ", t, "id : " ,id(t) , "size : ", len(t))

# u = (1,2,3)
# print("u : ", u, "\tid : " ,id(u) , "\tsize : ", len(u))
# u = u + (4,5,6)
# print("u : ", u, "\tid : " ,id(u) , "\tsize : ", len(u))
# for i in u:
#     del i

# print("u : ", u, "\tid : " ,id(u) , "\tsize : ", len(u))
# del u
# # print(u) # Error : NameError: name 'u' is not defined

# print("\n")

# # Set 
# s = {10,20,30,10,40}
# print("s : ", s)
# print(type(s))
# p = {10,"Batch", 10.5, 10+5j, "Batch"}
# print("p : ", p)
# print(type(p))
# print(bool(s))
# o = set()
# print("o : ", o)
# print(type(o))
# print(bool(o))
# print(set())
# # k = {[10,20] , [30,40]} # Error : unhashable type: 'list'
# # print(k)
# k = {(10,20) , (30,40)}
# print(k)

u = {1,     'c',    4.4,   8+3j,    True,   'python'}
#    0       1       2       3       4       5
#    -6     -5      -4      -3      -2      -1
#    int    str    float   complex  bool    str
print(u)

# u = {{1,2,3}, {4,5,6}} # Error : unhashable type: 'set'
# print(u) 

# u = {{1:10, 2:20}, {3:30, 4:40}} # Error : unhashable type: 'dict'
# print(u) 

# # In built functions on Set
# s = {"Sikander", 90, 7+5j , 8.5, 90, 7+5j}
# print("s : ", s) # {90, 8.5, (7+5j), 'Sikander'}
# s.add(100)
# s.add(90)
# print("s : ", s) # {100, 90, 8.5, (7+5j), 'Sikander'}
# s.remove(90)
# print("s : ", s) # {100, 8.5, (7+5j), 'Sikander'}
# i = s.pop()
# print("i : ", i) # 100
# print("s : ", s) # {8.5, (7+5j), 'Sikander'}
# print("\n")

# # dictionary
# d = {1:'python', 2:'java', 3:'html'}
# print("d : ", d) 
# print(id(d)) # 140707366366784
# print(type(d)) # <class 'dict'>
# print(bool(d)) # True
# print(dict()) # {}
# # k = {[1,2] : 'python'} # Error : unhashable type: 'list'
# d = {'a' : [67, 12], 'b': 7+9j, 'c': 'python', 'd':[10,20j,30,'java'], (20,3j+4) : 'html'}
# print("d : ", d)
# print(d["b"]) # (7+9j)
# print(d['d'][2]) # 30
# print(d['d'][3][2]) # v
# f = {'a':20,10:'cid','a':80, 'a':60, 'a':30, 'a':10}
# print("f : ", f) # {'a': 20, 10: 'cid'}
# print("\n")

# # In built functions on Dictionary
# x = {'a':10, 'b':20, 'c':'Book', 10:400, 59:'algebra'}
# print("x : ", x)
# # To extract the value from dict :- var[key]
# print(x['a']) # 10
# print(x[10]) # 400

# # To add new key value pair in dict :- var[key] = value
# x['d'] = 'python'
# print("x : ", x) # {'a': 10, 'b': 20, 'c': 'Book', 10: 400, 59: 'algebra', 'd': 'python'}

# # To modify the value of key in dict :- var[key] = value
# x[10] = 'meme'
# print("x : ", x)
# x['b'] = 2000 # 20 -> 2000

# # To delete the key value pair in dict :- pop(key)
# x.pop(59)
# print("x : ", x) # {'a': 10, 'b': 2000, 'c': 'Book', 10: 'meme', 'd': 'python'}

# # To delete the key value pair in dict :- popitem()
# x.popitem()
# print("x : ", x) # {'a': 10, 'b': 2000, 'c': 'Book', 10: 'meme'}

# # To extract all the keys from dict :- keys()
# print(x.keys()) # dict_keys(['a', 'b', 'c', 10])

# # To extract all the values from dict :- values()
# print(x.values()) # dict_values([10, 2000, 'Book', 'meme'])

# # To extract all the key value pair from dict :- items()
# print(x.items()) # dict_items([('a', 10), ('b', 2000), ('c', 'Book'), (10, 'meme')])

# # To clear the dict :- clear()
# x.clear()
# print("x : ", x) # {}

# # To delete the dict :- del
# del x
# # print(x) # Error : NameError: name 'x' is not defined