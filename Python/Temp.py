# n=[2,5,6,3]
# # output=[14,11,10,13]

# output = []
# for i in range(len(n)):
#     sums = sum(n[ : i]) + sum(n[i+1 : ])
#     output.append(sums)

# print(output)

# #wap to find all the prime number in given range 
# # n1=53 n2=75
# n1, n2 = 74, 81

# def prime_number(n):
#     for i in range(2, n//2 + 1):
#         if n % i == 0:
#             return False
#     return True

# for i in range(n1, n2+1):
#     if prime_number(i):
#         print(i, end=" ")