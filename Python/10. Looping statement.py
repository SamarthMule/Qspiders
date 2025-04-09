# There are 2 types of Looping statements in python
# 1. while loop
# 2. for loop

# 1. while loop
# Syntax:
# initialization
# while condition:
#     statement
#     updation

# print("\nQ1. WAP to print n natural numbers.")
# n = int(input("Enter any number : "))
# i = 0
# while i < n:
#     print(i+1)
#     i += 1
    
# print("\nQ2. WAP to print all the even numbers between 1 to 50")
# i = 1
# while i <= 50:
#     if i % 2 == 0: print(i)
#     i += 1

# print("\nQ3. WAP to print all the numbers which are multiple of 5 between 1 to N.")
# N = int(input("Enter the number: ")) 
# i = 1
# while i <= N:
#     if i % 5 == 0: print(i)   
#     i += 1

# print("\nQ4. WAP to print multiplications table for N.")
# N = int(input("Enter the number: "))
# i = 1
# while i <= 10:
#     print(N, "X", i, "=", N*i)
#     i += 1

# print("\nQ5. WAP to print numbers from N to 1.")
# N = int(input("Enter the number : "))
# while N > 0:
#     print(N)
#     N -= 1

# print("\nQ6. WAP to reverse the given number")
# num = input("Enter the number : ")
# i = len(num)
# while i > 0:
#     print(num[i-1], end="")
#     i -= 1
# OR
# num = int(input("Enter the number: "))
# reversed_num = 0
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# print("Reversed Number :", reversed_num)
    
# print("\nQ7. WAP to find the sum of individual digit.")
# num = input("Enter the number: ")
# n = len(num)
# i = 0
# sum = 0
# while i < n:
#     sum += int(num[i])
#     i += 1
# print("Sum of digits :", sum)
# OR
# num = int(input("Enter the number: "))
# sum = 0
# while num != 0:
#     sum += num % 10
#     num //= 10
# print("Sum of digits :", sum)

# print("\nQ8. WAP to find the product of even individual digit in a given int.")
# num = input("Enter the number: ")
# n = len(num)
# i = 0
# product = 1
# while i < n:
#     if int(num[i]) % 2 == 0:
#         product *= int(num[i])
#     i += 1
# print("Product of even numbers :", product)
# OR
# num = int(input("Enter the number: "))
# product = 1
# while num != 0:
#     digit = num % 10
#     if digit % 2 == 0:
#         product *= digit
#     num //= 10
# print("Product of even numbers :", product)

# print("\n9. WAP to find the sum of n natural number")
# n = int(input("Enter the number : "))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print(f"Sum of {n} natural number: {sum}")

# print('''\n10. WAP to find the factorial of a given int OR
# Find the product of n natural number. ''')
# n = int(input("Enter the number : "))
# i = 1
# product = 1
# while i <= n:
#     product *= i
#     i += 1
# print(f"Factorial of {n} : {product} OR")
# print(f"Product of {n} natural number: {product}")

# # Ques 1. To print every character from the given string 
# # ex: - 'python'   ----'p' 'y' 't' 'h' 'o' 'n'
# print("\nQ1. WAP to print every character from the given string.")
# s = input("Enter the string : ")
# i = 0
# while i < len(s):
#     print(s[i], end=" ")
#     i += 1


# # Ques2. Wap to extract lowercase character from the given string
# # ex:- 'Do all this PROGRAM' - (all the lowercase character from given str)
# print("\n\nQ2. WAP to extract lowercase character from the given string.")
# s = input("Enter the string : ")
# i = 0
# lowercase = ''
# while i < len(s):
#     if 'a' <= s[i] <= 'z':
#         lowercase += s[i]
#     i += 1
# print("Lowercase characters are : ", lowercase)

# # Ques3. Wap to extract integer from the given list.
# # ex:- l=[1.2, 56, 4+9j,7, True, 'hi', 97,63]    output=[56,7,97,63]
# print("\n\nQ3. WAP to extract integer from the given list.")
# l = [1.2, 56, 4+9j, 7, True, 'hi', 97, 63]
# i = 0
# integers = []
# while i < len(l):
#     if type(l[i]) == int:
#         integers.append(l[i])
#     i += 1
# print("Integer from list are : ", integers)

# # Ques4. Program to extract uppercase character from string.
# # ex:- 'Do all this PROGRAM' - (all the uppercase character from given str)
# print("\n\nQ4. WAP to extract uppercase character from the given string.")
# s = input("Enter the string : ")
# i = 0
# uppercase = ''  
# while i < len(s):
#     if 'A' <= s[i] <= 'Z':
#         uppercase += s[i]
#     i += 1
# print("Uppercase characters are : ", uppercase)


# # Ques5. Program to extract uppercase, lowercase, digit, and special character separately into 4 different output string.
# # ex:- 'Hey Guys 3!!!'   out1='H' 'G'  out2='e''y''u''y''s'   out3='3'   out4='!''!''!'
# print("\n\nQ5. WAP to extract uppercase, lowercase, digit, and special character separately into 4 different output string.")
# s = input("Enter the string : ")
# i = 0
# uppercase = ''
# lowercase = ''
# digit = ''
# special_character = ''
# while i < len(s):
#     if 'A' <= s[i] <= 'Z':
#         uppercase += s[i]
#     elif 'a' <= s[i] <= 'z':
#         lowercase += s[i]
#     elif '0' <= s[i] <= '9':
#         digit += s[i]
#     else:
#         special_character += s[i]
#     i += 1
# print("Uppercase characters are : ", uppercase)
# print("Lowercase characters are : ", lowercase)
# print("Digits are : ", digit)
# print("Special characters are : ", special_character)


# # Ques6. Find the sum of integers in a given list.
# # ex: - [1 , 2 ,3 ,4 ,'hi']   sum=10
# # output = 10
# print("\n\nQ6. WAP to find the sum of integers in a given list.")
# l = eval(input("Enter the list : "))
# i = 0
# sum = 0
# while i < len(l):
#     if type(l[i]) == int:
#         sum += l[i]
#     i += 1
# print("Sum of integers in the list : ", sum)


# # Ques7. Program to find the product of all the float number present at odd position in a given tuple.
# # ex:-   t=(1,2,3.6,9.8,5.5,7.5,'hi')   #3.6+5.5    output= 9.1
# # output= 3.6*5.5=19.8
# print("\n\nQ7. WAP to find the product of all the float number present at odd position in a given tuple.")
# l = eval(input("Enter the tuple : "))
# i = 0
# product = 1
# while i < len(l):
#     if type(l[i]) == float and i % 2 != 0:
#         product *= l[i]
#     i += 1
# print("Product of float numbers at odd position : ", product)


# # Ques8. Program to convert all the lowercase character into uppercase character 
# # #Don't use upper and lower inbuilt function
# print("\n\nQ8. WAP to convert all the lowercase character into uppercase character.")
# s = input("Enter the string : ")
# i = 0
# uppercase = ''
# while i < len(s):
#     if 'a' <= s[i] <= 'z':
#         uppercase += chr(ord(s[i]) - 32)
#     else:
#         uppercase += s[i]
#     i += 1
# print("Uppercase characters are : ", uppercase)


# # Ques9. Program to convert uppercase to lowercase and lowecase to uppercase in a given string
# # # Don't use swapcase inbuilt function 
# print("\n\nQ9. WAP to convert uppercase to lowercase and lowecase to uppercase in a given string.")
# s = input("Enter the string : ")
# i = 0
# k = ''
# while i < len(s):
#     if 'A' <= s[i] <= 'Z':
#         k += chr(ord(s[i]) + 32)
#     elif 'a' <= s[i] <= 'z':
#         k += chr(ord(s[i]) - 32)
#     else:
#         k += s[i]
#     i += 1
# print("Converted string is : ", k)


# # Ques10. Wap to generate the fibonacci series sequence up to n number.
# # ex.  output = 0, 1, 1, 2, 3, 5, 8, 13, 21   #Logic: u have to do sum of current number and previous number to get the next number.  (i.e, 0, 1, 0+1, 1+1, 1+2, 2+3, 3+5, 5+8)
# print("\n\nQ10. WAP to generate the fibonacci series sequence up to n number.")
# n = int(input("Enter the number : "))
# # a = 0
# # b = 1
# # print(a, end=" ")
# # while b <= n:
# #     print(b, end=" ")
# #     c = a + b
# #     a = b
# #     b = c
# # print("\n")
# # OR
# a, b = 0, 1
# i = 0
# while i < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     i += 1
# print("\n")


# # Ques11. WAP to check whether the given number is armstrong or not.
# # ex:- 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# # ex:- 370 = 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370
# # ex:- 371 = 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371
# # ex:- 407 = 4^3 + 0^3 + 7^3 = 64 + 0 + 343 = 407
# # ex:- 1634 = 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
# # ex:- 8208 = 8^4 + 2^4 + 0^4 + 8^4 = 4096 + 16 + 0 + 4096 = 8208
# print("\nQ11. WAP to check whether the given number is armstrong or not.")
# num = int(input("Enter the number : "))
# n = len(str(num))
# sum = 0
# temp = num
# while temp != 0:
#     digit = temp % 10
#     sum += digit ** n
#     temp //= 10
# if num == sum:
#     print(num, "is an Armstrong number.")
# else:
#     print(num, "is not an Armstrong number.")
    
    
# print("\n\nQ12. WAP to print first n armstrong numbers.")
# n = int(input("Enter the number : "))
# i = 0
# armstrong_numbers = []
# while len(armstrong_numbers) < n:
#     num = i
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** len(str(num))
#         temp //= 10
#     if num == sum:
#         print(num, "is an Armstrong number.")
#         armstrong_numbers.append(num)
#     i += 1

# 2. For Loop
# Syntax: 
# For var in collection:
#     Statements Block

# print("\nQ1. WAP to find lenght of a given collection without using len function.")
# a = eval(input("Enter any collection: "))
# count = 0
# for i in a:
#     count += 1
# print("Lenght of given collection is ",count)

# print("\nQ2. WAP to extract vowels from the given string")
# s = input("Enter any String: ")
# result = ''
# for char in s:
#     if char in 'aeiouAEIOU':
#         result += char + ' '
# print("Vowels in Give String: ", result)

# print("\nQ3. WAP to replace space by an underscore in a given string")
# s = input("Enter any String: ")
# result_s = ''
# for char in s:
#     if char == ' ':
#         result_s += '_'
#     else:
#         result_s += char
# print(result_s)

# print("\nQ4. WAP to check whether the given string is palindrome or ")
# s = input("Enter any String: ")
# result = ''
# for char in s:
#     result = char + result
# if s == result: print("Give string is Palindrome")
# else: print ("Give striing is not Palindrome")

# print("\nQ5. Extract all integers which are multiple of 5 and 3 digits in it from given list")
# l = eval(input("Enter any list: "))
# print("Multiple of 5 and 3 in given list : ", end=" ")
# for i in l:
#     if type(i) == int:
#         if i % 5 == 0 and i % 3 == 0:
#             print(i,end=" ")

# print("\nQ6. WAP to remove duplicate values from list.")
# l = eval(input("Enter any List: "))
# updated_l = []
# for i in l:
#     if i not in updated_l:
#         updated_l.append(i)
# print("Updated List: ", updated_l)

# print('''\nQ7. WAP to get the following outpt
#       t = (12,3.4, 'hai', 8 + 9j, 'Python', 'ab', 9+6j)
#       output: {'hai' :3, 'Python':6, 'ab':2 }''')
# t = (12,3.4, 'hai', 8 + 9j, 'Python', 'ab', 9+6j)
# rs= {}
# for i in t:
#     if type(i) == str:
#         rs[i] = len(i)
# print(rs)

# print('''\nQ8. WAP to get following output: 
#       l = [12, 3.4, 'data', 'science']
#       output: {''data': 'da', 'science': 'se}''')
# l = [12, 3.4, 'data', 'science']
# rs= {}
# for i in l:
#     if type(i) == str:
#         rs[i] = i[:3]
# print(rs)

# print('''\nQ9. WAP to get following output:
#       a = 'aPPE#23'
#       output: {'a':'A', 'P':'p', 'l': 'L', 'E' : 'e'}''')
# a = 'aPPE#23'
# output = {}
# for i in a:
#     if 'a' <= i <= 'z':
#         if i not in output.keys():
#             output[i] = chr(ord(i) - 32) 
# print(output)   

# print("\nQ10. WAP to creat the string with uppercase character from A to Z.")
# for i in range(65, 91):
#     print(chr(i), end=" ")


# split() method
# The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
# syntax: str.split(separator, maxsplit)
# separator: Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit: Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

# print('''\nQ1. WAP to get the following output:
#       s = 'hey hello how are you'
#       output: {'hey' : 3, 'hello' : 5, 'how' : 3 , 'are' : 3,  'you' : 3}''')
# s = 'hey hello how are you'
# output = {}
# for word in s.split():
#     output[word] = len(word)
# print(output)

# print('''\nQ2. WAP to get the following output:
#       l = ['python.py' , 'proj.html', 'google.com']
#       output: ['py', 'html', 'com']''')
# l = ['python.py' , 'proj.html', 'google.com']
# output = []
# for i in l:
#     output.append(i.split('.')[-1])
# print(output)

# print('''\nQ3. WAP to get the following output:
#       l = ['python.py' , 'proj.html', 'google.com', 'file.txt]
#       output: {'py' : 'python', 'html' : 'proj', 'com' : 'google', 'txt' : 'file'}''')
# l = ['python.py' , 'proj.html', 'google.com', 'file.txt']
# output = {}
# for i in l:
#     output[i.split('.')[-1]] = i.split('.')[0]
# print(output)

# join() method
# Syntax: string.join(iterable)

# print('''\nQ4. WAP to get the following output:
#       s = 'Do code by yourself'
#       output: 'oD edoc yb flesruoy' ''')
# s = 'Do code by yourself'
# output = []
# l = s.split()
# for i in l:
#     output.append(i[::-1])
# output = ' '.join(output)
# print(output)
# OR
# output = ' '.join([i[::-1] for i in s.split()])
# print(output)
# OR
# output = ''
# for i in s.split():
#     output += i[::-1] + ' '
# print(output)

# count() method
# The count() method returns the number of times a specified value occurs in a string.
# Syntax: string.count(value, start, end)

# print('''\nQ5. WAP to get the following output:
#       s = 'example on for loop'
#       output: 'ee on fr lp' ''')
# s = 'example on for loop'
# output = ''
# for i in s.split():
#     output += i[0] + i[-1] + ' '
# print(output)

# print('''\nQ6. WAP to get the following output:
#       s = 'abcabccbcc'
#       output: 'a2b3c5' ''')
# s = 'abcabccbcc'
# output = ''
# for i in set(s):
#     output += i + str(s.count(i))
# print(output)
# OR    
# output = ''
# for i in s:
#     if i not in output:
#         output += i + str(s.count(i))
# print(output)

# print('''\nQ7. WAP to ectract only unique values from the given list, here unique refers to the values which are present only once in the list.''')
# l = eval(input("Enter any list: "))
# output = []
# for i in l:
#     if l.count(i) == 1:
#         output.append(i)
# print("Unique values in the list are : ", output)

# print('''\nQ8. WAP to get the following output:
#       s = 'abcabccbcc'
#       output: {'a' : 2, 'b' : 3, 'c' : 5} ''')
# s = 'abcabccbcc'
# output = {}
# for i in set(s):
#     output[i] = s.count(i)
# print(output)

# print('''\nQ9. WAP to get the following output:
#       l= ['p1.py', 'File.txt', 'google.com', 'data.txt', 'ques.py']
#       output: {'py' : ['p1', 'ques'], 'txt' : ['File', 'data'], 'com' : ['google']} ''')
# l= ['p1.py', 'File.txt', 'google.com', 'data.txt', 'ques.py']
# output = {}
# for i in l:
#     ext = i.split('.')[-1]
#     name = i.split('.')[0]
#     if ext not in output:
#         output[ext] = [name]
#     else:
#         output[ext].append(name)
# print(output)

# print("\nQ10. WAP to find factorial of a given number.")
# num = int(input("Enter the number : "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(f"Factorial of {num} is : {fact}")

# print("\nQ11 find divisors of a given number.")
# num = int(input("Enter the number : "))
# divisors = ''
# for i in range(1, num + 1):
#     if num % i == 0:
#         divisors += str(i) + ' '
# print(f"Divisors of {num} are : {divisors}")

# print('''\nQ12. WAP to check whether the given number is perfect number or not. 
#       ex: n=8 -> 1+2+4=7
#       ex: n=6 -> 1+2+3=6 perfect number''')
# num = int(input("Enter the number : "))
# sum = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum += i
# if sum == num:
#     print(f"{num} is a perfect number.")
# else:
#     print(f"{num} is not a perfect number.")

# Nested Looping
# Nested Looping is a loop inside another loop. The inner loop will be executed one time for each iteration of the outer loop.
# Nested For Loop
# Syntax:
# for var1 in collection1:
#    statement
#     for var2 in collection2:
#         statements

# print("\nQ1. WAP to check whether the given number is strong number or not.")
# num = int(input("Enter the number : "))
# sum = 0
# temp = num
# for i in range(len(str(num))):
#     digit = temp % 10
#     fact = 1
#     for j in range(1, digit + 1):
#         fact *= j
#     sum += fact
#     temp //= 10
# if num == sum:
#     print(num, "is a strong number.")
# else:
#     print(num, "is not a strong number.")
    
# print('''\nQ2. WAP to get following output:
#       l = [12, 'program', 6+8j, 'break', 9]
#       output: {'program' : 'pm', 'breal' : 'bk'}''')
# l = [12, 'program', 6+8j, 'break', 9]
# output = {}
# for i in l:
#     if type(i) == str:
#         output[i] = i[1::2]
# print(output)

# print('''\nQ3. WAP to get following output:
#       l = [10, 13, 4, 6]
#       output: [23, 20, 29, 27]''')
# l = [10,13,4,6]
# result = []
# for i in l:
#     sum = 0
#     for j in l:
#         if i != j: 
#             sum += j
#     result.append(sum)
# print(result)

# print('''\nQ4 WAP to get following output
# l = [1000, 700, 100, 300, 900, 200]
# n = 1000
# output: [[1000], [700,300],[100,900]]''')
# l = [1000, 700, 100, 300, 900, 200]
# lenght = len(l)
# n = 1000
# output = []
# for i in range(lenght):
#     for j in range(i,lenght):
#         if i == j and l[j] == n:
#             output.append(l[j])
#         elif l[i] + l[j] == n:
#             output.append([l[i], l[j]])
# print(output)

# Intermediate Termination
# break, continue, pass

# break:

print("\nQ1. WAP to guess the enter mnumber ( Number game)")
# import random 
# number = random.randint(0, 100)
# print(number)
# guess = 0
# while True:
#     n = int(input("Enter any number: "))
#     guess += 1
#     if n == number:
#         print("You guessed the number in ", guess, "tries.")
#         break
#     elif n > number:
#         print("Enter a greater number.")
#     else:
#         print("Enter a smaller number.")


# print("\nQ2. WAP to login to phone pay account by entering the proper otp")
# import random
# otp = random.randint(1000, 9999)
# print("Your otp is: ", otp) 
# while True:
#     n = int(input("Enter the otp: "))
#     if n == otp:
#         print("Login successful.")
#         break
#     else:
#         print("Incorrect otp. Please try again.")


# print("\nQ3. WAP to unlock the phone by entering the correct pin, program should allow us to enter wrong pin 5 times. After that it should make wait for 5 seconds to enter pin once again.")
# import time
# pin = 1234
# attempts = 0
# while True:
#     attempts += 1
#     num = int(input("Enter the pin: "))
#     if num == pin:
#         print("Phone unlocked.")
#         break
#     elif attempts > 5:
#         print("Too many attempts. Please wait for 5 seconds.")
#         time.sleep(5)
#         attempts = 0
#     else:
#         print("Incorrect pin. Please try again.")
        
print("\nQ4. WAP to check whethervthe given int is prime or not and break the loop after storing the prime num in new list (atleast 5 prime numbers).")
num = int(input("Enter the number: "))
prime_numbers = []
i = 2
while True:
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)
    if len(prime_numbers) >= num:
        break
    i += 1
print("Prime numbers are: ", prime_numbers)
