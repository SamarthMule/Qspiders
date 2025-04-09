# There are 4 types of conditional statements in python
# 1. if statement
# 2. if-else statement
# 3. if-elif-else statement
# 4. Nested if statement

# 1. if statement
# Syntax:
# if condition:
#     statement(s)

# print("1. WAP to check user is eligible for voting or not.")
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible for voting.")

# print("2. WAP to check the given number is positive or not.")
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The given number is even.")


# print("3. WAP to check whether given number is odd or not.")
# num = int(input("Enter a number: "))
# if num % 2 != 0:
#     print("The given number is odd.")


# print("4. WAP to check whether give string is palindrome or not.")
# string = input("Enter a string: ")
# if string == string[::-1]:
#     print("The given string is palindrome.")


# print("5. WAP to check the given string is start with vowel or not.")
# string = input("Enter a string: ")
# if string[0] in "aeiouAEIOU":
#     print("The given string is start with vowel.")
    

# print("6. WAP to check whether the give data is float or not.")
# data = eval(input("Enter a data: "))
# if type(data) == float:
#     print("The given data is float.")
    

# print("7. WAP to print a square of a number only if it is number.")
# num = eval(input("Enter a number: "))
# if type(num) == int:
#     print(f"The square of {num} is {num**2}.")


# print("8. WAP to print a cube of a number only if it is divisible by 9 or 6.")
# num = eval(input("Enter a number: "))
# if num % 9 == 0 or num % 6 == 0:
#     print(f"The cube of {num} is {num**3}.")


# print("9. WAP to askey key value is char only if it is in upper case.")
# char = input("Enter a char: ")
# if char.isupper():
#     print(f"The askey key value of {char} is {ord(char)}.")


# print("10. WAP to check whether the given char is lower case or not.")
# char = input("Enter a char: ")
# if char.islower():
#     print(f"The given char is lower case.")


# print("11. WAP to check whether the given char is special char or not.")
# char = input("Enter a char: ")
# if not char.isalnum():
#     print(f"The given char is special char.")


# print("12. WAP to check whether the given digit is 3 digit number or not.")
# num = eval(input("Enter a number: "))
# if 100 <= num <= 999:
#     print("The given number is 3 digit number.")


# print("13. WAP to check whether a last digit of a number is 5 using type casting.")
# num = eval(input("Enter a number: "))
# if str(num)[-1] == "5":
#     print("The last digit of a number is 5.")


# print("14. WAP to check whether if the data is single valued datatype or not.")
# data = eval(input("Enter a data: "))
# if type(data) in [int, float, str, bool]:
#     print("The given data is single valued datatype.")
    
# if-else statement
# Syntax:
# if condition:
#     statement(s)
# else:
#     statement(s)

# print("1. WAP to ccheck given number is even or odd.")
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The given number is even.")
# else:
#     print("The given number is odd.")
    
# print("2. WAP to check whether the given data is mutable or immutable.")
# data = eval(input("Enter a data: "))
# if type(data) in [int, float, str, bool]:
#     print("The given data is immutable.")
# else:
#     print("The given data is mutable.")

# print("3. WAP to whether the given char is digit or not.")
# char = input("Enter a char: ")
# if char.isdigit():
#     print("The given char is digit.")
# else:
#     print("The given char is not digit.")

# print("4. WAP to check whether the given char is special char or not.")
# char = input("Enter a char: ")
# if not char.isalnum():
#     print("The given char is special char.")
# else:
#     print("The given char is not special char.")

# print("5. WAP to check whether the given number is divisible by 5, 3 or not.")
# num = eval(input("Enter a number: "))
# if num % 5 == 0 and num % 3 == 0:
#     print("The given number is divisible by 5 and 3.")
# else:
#     print("The given number is not divisible by 5 and 3.")
    
# print("6. WAP to check whether the list consist middele element or not. And if it consist then print it.")
# lst = eval(input("Enter a list: "))
# if len(lst) % 2 == 0:
#     print("The given list does not consist middle element.")
# else:
#     print(f"The middle element of the given list is {lst[len(lst)//2]}.")

# print("7. WAP to check whether the value are pointing to same memory location or not.")
# a = eval(input("Enter a: "))
# b = eval(input("Enter b: "))
# if id(a) == id(b):
#     print("The given values are pointing to same memory location.")
# else:
#     print("The given values are not pointing to same memory location.")

# print("8. Consider a tuple as lenght 2 and check whether the given tuple is homogeneous data type or not.")
# k = eval(input("Enter a tuple: "))
# if type(k[0]) == type(k[1]):
#     print("The given tuple is homogeneous data type.")
# else:
#     print("The given tuple is not homogeneous data type.")
    
# print("9. WAP to check whether the given number is positive or negative.")
# num = eval(input("Enter a number: "))
# if num > 0:
#     print("The given number is positive.")
# else:
#     print("The given number is negative.")

# print("10. WAP to check whether the given string is palindrome or not.")
# string = input("Enter a string: ")
# if string == string[::-1]:
#     print("The given string is palindrome.")
# else:
#     print("The given string is not palindrome.")

# elif statement 
# Syntax:
# if condition1:
#     statement1
# elif condition2:
#     statement2
# elif condition_n:
#     statement_n
# else:
#     statement_f

# print("\nQ1. WAP to check whether the char is uppercase, lowercase, digit or special char.")
# s = input("Enter a char: ")
# if 'A' <= s <= 'Z':
#     print(f"The given {s} is uppercase.")
# elif 'a' <= s <= 'z':
#     print(f"The given {s} is lowercase.")
# elif '0' <= s <= '9':
#     print(f"The given {s} is digit.")
# else:
#     print(f"The given {s} is special char.")
    
# print("\nQ2. WAP to check whether the given integer is single digit or two digit or three digit or more than three digit")
# num = eval(input("Enter a number: "))
# if 0 <= num <= 9:
#     print("The given number is single digit.")
# elif 10 <= num <= 99:
#     print("The given number is two digit.")
# elif 100 <= num <= 999:
#     print("The given number is three digit.")
# else:
#     print("The given number is more than three digit.")


# print("\nQ3. WAP to check the given points are lying in the quadrant.")
# x = eval(input("Enter x: "))
# y = eval(input("Enter y: "))
# if x > 0 and y > 0:
#     print("The given points are lying in the first quadrant.")
# elif x < 0 and y > 0:
#     print("The given points are lying in the second quadrant.")
# elif x < 0 and y < 0:
#     print("The given points are lying in the third quadrant.")
# elif x > 0 and y < 0:
#     print("The given points are lying in the fourth quadrant.")
# else:
#     print("The given points are lying in the origin.")


# print("\nQ4. WAP to find the greatest among 3 numbers.")
# a = eval(input("Enter a: "))
# b = eval(input("Enter b: "))
# c = eval(input("Enter c: "))
# if a >= b and a > c:
#     print(f"{a} is greatest.")
# elif b > a and b >= c:
#     print(f"{b} is greatest.")
# else:
#     print(f"{c} is greatest.")


# print("\nQ5. WAP to find the smallest among 3 numbers.")
# a = eval(input("Enter a: "))
# b = eval(input("Enter b: "))
# c = eval(input("Enter c: "))
# if a < b and a < c:
#     print(f"{a} is smallest.")
# elif b < a and b < c:
#     print(f"{b} is smallest.")
# else:
#     print(f"{c} is smallest.")


# print("\nQ6. WAP to check the relation between two integers. ex. the given input is equal to other or it is greater or smaller")
# a = eval(input("Enter a: "))
# b = eval(input("Enter b: "))
# if a == b:
#     print(f"{a} is equal to {b}.")
# elif a > b:
#     print(f"{a} is greater than {b}.")
# else:
#     print(f"{a} is smaller than {b}.")


# print("\nQ7. WAP to convert the given char into uppercase if it is lowercase, convert it into lowercase if it is uppercase, print the reminder when it is divided by 3 if it is digit, print the ascii value if it is special char.")
# s = input("Enter a char: ")
# if 'A' <= s <= 'Z':
#     ns = chr(ord(s) + 32)
#     print(f"The given {s} in lowercase: {ns}")
# elif 'a' <= s <= 'z':
#     ns = chr(ord(s) - 32)
#     print(f"The given {s} in uppercase: {ns}")
# elif '0' <= s <= '9':
#     print(f"The reminder when {s} is divided by 3: {int(s) % 3}")
# else:
#     print(f"The ascii value of {s} is {ord(s)}.")
    


# print("\nQ8. Wap to print 'Fizz' if the given number is multiple of 3, print 'buzz' if the given number is multiple of 5 and print 'Fizzbuzz' if the number is multiple of 3 and 5.")
# num = eval(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("Fizzbuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print("The given number is not multiple of 3 and 5.")


# print("\nQ9. Wap to check greatest among 4 numbers.")
# a = eval(input("Enter a: "))
# b = eval(input("Enter b: "))
# c = eval(input("Enter c: "))
# d = eval(input("Enter d: "))
# if a > b and a > c and a > d:
#     print(f"{a} is greatest.")
# elif b > a and b > c and b > d:
#     print(f"{b} is greatest.")
# elif c > a and c > b and c > d:
#     print(f"{c} is greatest.")
# else:
#     print(f"{d} is greatest.")


# print("\nQ10. Wap to check smallest among 4 numbers.")
# a = eval(input("Enter a: "))
# b = eval(input("Enter b: "))
# c = eval(input("Enter c: "))
# d = eval(input("Enter d: "))
# if a < b and a < c and a < d:
#     print(f"{a} is smallest.")
# elif b < a and b < c and b < d:
#     print(f"{b} is smallest.")
# elif c < a and c < b and c < d:
#     print(f"{c} is smallest.")
# else:
#     print(f"{d} is smallest.")

# Nested if statement
# Syntax:
# if condition1:
#     statement1
#     if condition2:
#         statement2
#     else:
#         statement3
# else:
#     statement4

# print("\nQ1. WAP to check whether the char is vowel or not")
# char = input("Enter a char: ")
# if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
#     if char in "aeiouAEIOU":
#         print(f"The given char {char} is vowel.")
#     else:
#         print(f"The given char {char} is not vowel.")
# else:
#     print(f"The given char {char} is not alphabet.")
        
# print("\nQ2. WAP to print the middle value of list only if that value is string")
# lst = eval(input("Enter a list: "))
# if len(lst) % 2 != 0:
#     if type(lst[len(lst)//2]) == str:
#         print(f"The middle value of the given list is {lst[len(lst)//2]}.")
#     else:
#         print("The middle value of the given list is not string.")
# else:
#     print("The given list does not consist middle value.")


# print("\nQ3. WAP to print the value as it is if the lenght of the value is even")
# value = eval(input("Enter a value: "))
# if type(value) in [str, list, tuple, set, dict]:
#     if len(value) % 2 == 0:
#         print(f"The given value is {value}.")
#     else:
#         print(f"The given lenght value is not even.")
# else:
#     print("The given value is not iterable.")

    
# print('''\n Q4. WAP that ask user to input their age and country residence. Based on the user's inputs, the program should print different messages.
#       1. if user is under 18 and living in USA, so print you arer minor living in USA
#       2. if user us under 18 and living in canada, so print you are minor living in canada
#       3. otherwise print you are minor living in other country
#       4. if user is above 18 and living in USA, so print you are adult living in USA
#       5. if user is above 18 and living in canada, so print you are adult living in canada
#       6. otherwise print you are adult living in other country. \n''')

# age = int(input("Enter your age: "))
# if age < 18:
#     country = input("Enter your country: ")
#     if country.lower() == "usa":
#         print("You are minor living in USA.")
#     elif country.lower() == "canada":
#         print("You are minor living in Canada.")
#     else:
#         print("You are minor living in other country.")
# else:
#     country = input("Enter your country: ")
#     if country.lower() == "usa":
#         print("You are adult living in USA.")
#     elif country.lower() == "canada":
#         print("You are adult living in canada.")
#     else:
#         print("You are adult living in other country.")

# print('''\nQ5. Grade range checker (90-100) print Excellent, 
#             (80-89) print Good, (60-79) print Average, (below the 60) print Fail, 
#             and if the grade is outside the range (0-100) print invalid grade.''')

# grade = eval(input("Enter your grade: "))
# if 0 <= grade <= 100:
#     if 90 <= grade <= 100:
#         print("Excellent")
#     elif 80 <= grade <= 89:
#         print("Good")
#     elif 60 <= grade <= 79:
#         print("Average")
#     else:
#         print("Fail")
# else:
#     print("Invalid grade.")