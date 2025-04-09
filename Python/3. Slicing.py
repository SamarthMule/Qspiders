# x = "Opportunities don't happen, you create them."
# print(x[20:25:1]) # 'happe'
# print(x[20:26:1]) # 'happen'
# print(x[10:1:1]) # '' empty string : because start index is greater than end index
# print(x[10::-1]) # 'tunitnoppO'

# # SI : start index = 0
# print(x[:14:1]) # 'Opportunities'
# # ET : end index = -1 or len(x)
# print(x[28::1]) # 'you create them.'
# # UP : Updation of string = 1
# print(x[28:31]) # 'you'

# # Full String
# print(x[::1]) # 'Opportunities don't happen, you create them.'

# # Even index
# print(x[::2]) # 'Ootntesdn'hn yucat hm'
# # Odd index
# print(x[1::2]) # 'ppriie'ohppn o rete'

# # Reverse
# print(x[::-1]) # '.meht etaerc uoy ,neppah t'nod seunitnoppO'

# # negative index
# y = "If you believe in yourself, things are possible."
# print(y[-2]) # 'e'
# print(y[-9 : -1]) # possible
# print(y[-9 : -1 : 1]) # possible
# print(y[-2: -10: -1]) # elbissop
# print(y[-2: -10: 1]) # '' empty string : because start index is greater than end index

# List Slicing
# print("List Slicing")

# b = [10,20,30,40,50,60,70,80,90,100]
# #    0  1  2  3  4  5  6  7  8  9
# #    -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# print(b[2:5:1]) # [30, 40, 50]
# print(b[2:5]) # [30, 40, 50]
# print(b[:]) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(b[2:5:2]) # [30, 50]
# print(b[5:2:-1]) # [60, 50, 40]
# print(b[5:2:-2]) # [60, 40]
# print(b[5:2:1]) # [] empty list : because start index is greater than end index
# print(b[-4:]) # [70, 80, 90, 100]
# print(b[-4:-2]) # [70, 80, 90]
# print(b[-4:-2:-1]) # [] empty list : because start index is greater than end index

# z = [10, 4.5, 9+6j , False, 8+9j, 'html', 3]
# print(z[-3: -1 : 1]) # [(8+9j), 'html']
# print(z[-3: -1 : -1]) # [] empty list : because start index is greater than end index
# print(z[5: 1 : -1]) # [(8+9j), False, (9+6j), 4.5]
# print(z[5: 1 : 1]) # [] empty list : because start index is greater than end index
# print(z[2: 5]) # [(9+6j), False, (8+9j)]
# print(z[1::2]) # [4.5, False, 'html']
# print(z[6: 1: -2]) # [3, (8+9j), 4.5]
# print(z[::-1]) # [3, 'html', (8+9j), False, (9+6j), 4.5, 10]
# print(z[-2][::-1]) # lmth
# print(z[-2][:]) # html
# print(z[-2][1:4]) # tml
# print(z[-2][-2:-3]) # '' empty string : because start index is greater than end index
# print(z[-2][-3:-2]) # t

# # Tuple Slicing
print("\nTuple Slicing")
t = (10, 4.5, 9+6j , False, 8+9j, 3)
print(t[-3: -1 : 1]) # (False, 8+9j)
print(t[-3: -1 : -1]) # () empty tuple : because start index is greater than end index
print(t[5: 1 : -1]) # (3, 8+9j, False, (9+6j))
print(t[5: 1 : 1]) # () empty tuple : because start index is greater than end index
print(t[2: 5]) # ((9+6j), False, (8+9j))
print(t[1::2]) # (4.5, False, 3)
print(t[5: 1: -2]) # (3, 8+9j, 4.5)
print(t[::-1]) # (3, 8+9j, False, (9+6j), 4.5, 10)
print(t[-2][::-1]) # lmth
print(t[-2][:]) # html
print(t[-2][1:4]) # tml
print(t[-2][-2:-3]) # () empty tuple : because start index is greater than end index
print(t[-2][-3:-2]) # t

print("\nPrime Numbers")
for num in range(2,100):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: break
    else: print(num, end=" ")
    