# 100 Programs on Loops using While Loop

# print("\nQ1. WAP to print the following using while loop. First 10 even numbers.")
# i = 0
# count = 0
# while count < 10:
#     print(i)
#     i += 2
#     count += 1

# print("\nQ2. WAP to print the following using while loop. First 10 odd numbers.")
# i = 1
# count = 0
# while count < 10:
#     print(i)
#     i += 2
#     count += 1
    
# print("\nQ3. WAP to print the following using while loop. First 10 Natural number.")
# i = 1
# while i < 11:
#     print(i)
#     i += 1

# print("\nQ4. WAP to print the following using while loop. First 10 Whole numbers.")
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# print("\nQ5. Write a program to print first 10 integers and their squares using while loop.")
# i = 0
# while i < 10:
#     print(i, ' -> ', i**2)
#     i += 1

# print("\nQ6. Write while loop statement to print the following series: 10, 20, 30 … … 300")
# i = 10
# while i <= 300:
#     print(i)
#     i += 10

# print("\nQ7. Write a while loop statement to print the following series 105, 98, 91 ……… 7")
# i = 105
# while i >= 7:
#     print(i)
#     i -= 7

# print("\nQ8. Write a program to print the first 10 natural number in reverse order using while loop.")
# i = 10
# while i > 0:
#     print(i)
#     i -= 1

# print("\nQ9. Write a program to print sum of first 10 Natural numbers.")
# i = 1
# sum = 0
# while i < 11:
#     sum += i
#     i += 1
# print("Sum of first 10 Natural Number: ", sum)

# print("\nQ10. Write a program to print sum of first 10 Even numbers.")
# i = 0
# count = 0
# sum = 0 
# while count < 10:
#     sum += i
#     i += 2
#     count += 1
# print("Sum of first 10 Even numbers : ", sum)

# print("\nQ11. Write a program to print table of a number entered from the user.")
# num = int(input("Enter any number : "))
# i = 1
# print("Table of ",num)
# while i <= 10:
#     print(num, ' X ', i , ' = ', num*i)
#     i += 1

# print("\nQ12. Write a program to print all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop")
# print("Enter range (Both number are exclusive) ")
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number: "))

# if num1 > num2 : 
#     num1 , num2 = num2, num1
# i = num1 + 1
# while i < num2:
#     if i % 2 == 0: 
#         print(i)
#     i += 1

# print("\nQ13. Write a program to check whether a number is prime or not using while loop.")
# num = int(input("Enter any number: "))
# i = 2
# prime = True
# while i <= (num//2 + 1):
#     if num % i == 0:
#         prime = False
#         break
#     i += 1
# if prime: print(num, 'is prime')
# else : print(num, "is not prime")

# print("\nQ14. Write a program to find the sum of the digits of a number accepted from the user")
# num = int(input("Enter the number : "))
# sum = 0 
# while num != 0:
#     digit = num % 10
#     sum += digit
#     num //= 10
# print("Sum of Digits : ", sum)

# print("\nQ15. Write a program to find the product of the digits of a number accepted from the user.")
# num = int(input("Enter the number : "))
# product = 1
# while num != 0:
#     digit = num % 10
#     product *= digit
#     num //= 10
# print("Product of Digits : ", product)

# print("\nQ16. Write a program to reverse the number accepted from user using while loop")
# num = int(input("Enter the number : "))
# reversed_num = 0
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num*10 + digit
#     num //= 10
# print("Reversed Number : ", reversed_num)

# print("\nQ17. Write a program to display the number names of the digits of a number entered by user, for example if the number is 231 then output should be Two Three One")
# numbers = {
#     0 : 'Zero',
#     1 : 'One',
#     2 : 'Two',
#     3 : 'Three',
#     4 : 'Four',
#     5 : 'Five',
#     6 : 'Six',
#     7 : 'Seven',
#     8 : 'Eight',
#     9 : 'Nine'
# }
# num = int(input("Enter any number : "))
# Output = ""
# while num != 0:
#     digit = num % 10
#     Output = numbers[digit] +" "+ Output
#     num //= 10
# print("Output : " , Output)

# print("\nQ18. Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop")
# n = int(input("Enter any number : "))
# a, b = 0, 1
# i = 0
# print("Fibonacci series: ")
# while i < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     i += 1

# print("\nQ19. Write a program to print the factorial of a number accepted from user.")
# i = 1
# num = int(input("Enter any number : "))
# fact = 1
# while i <= num:
#     fact *= i
#     i += 1
# print(fact)

# print("\nQ20. Write a program to check whether a number is Armstrong or not. (Armstrong number isa number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)")
# num = int(input("Enter any number : "))
# temp = num
# sum = 0
# while temp != 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if sum == num:
#     print(num, "is Armstrong number")
# else:
#     print(num, "is not Armstrong number")
    
# print("\nQ21. Write a program to add first n terms of the following series using a while loop: 1/1! + 1/2! + 1/3! + …….. + 1/n!")
# n = int(input("Enter any number : "))
# i = 1
# sum = 0
# fact = 1
# while i <= n:
#     fact *= i
#     sum += 1 / fact
#     i += 1
# print("Sum of series : ", sum)

# print("\nQ22. Write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered.")
# sum = 0
# while True:
#     num = int(input("Enter any number : "))
#     sum += num
#     choice = input("Do you want to continue (y/n) : ")
#     if choice == 'n':
#         break
# print("Sum of all numbers : ", sum)

# print("\nQ23. Write a program to enter the numbers till the user enter ZERO and at the end it should display the count of positive and negative numbers entered.")
# pos_count = 0
# neg_count = 0
# while True:
#     num = int(input("Enter any number : "))
#     if num == 0:
#         break
#     elif num > 0:
#         pos_count += 1
#     else:
#         neg_count += 1
# print("Positive numbers count : ", pos_count)
# print("Negative numbers count : ", neg_count)

# print("\nQ24. Write a program to find the HCF of two numbers entered from the user.")
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# if num1 > num2:
#     smaller = num2
# else:
#     smaller = num1
# hcf = 1
# while smaller > 0:
#     if num1 % smaller == 0 and num2 % smaller == 0:
#         hcf = smaller
#         break
#     smaller -= 1
# print("HCF of ", num1, " and ", num2, " is : ", hcf)

# print("\nQ25. Write a program to convert Decimal to Binary.")
# num = int(input("Enter any number : "))
# binary = ""
# while num > 0:
#     binary = str(num % 2) + binary
#     num //= 2
# print("Binary : ", binary)

# print("\nQ26. Write a program to convert Binary to Decimal.")
# num = int(input("Enter any number : "))
# binary = num
# decimal = 0
# i = 0
# while num > 0:
#     digit = num % 10
#     decimal += digit * (2 ** i)
#     num //= 10
#     i += 1
# print("Decimal : ", decimal)

# print("\nQ27. Write a program to check whether a number is palindrome or not")
# num = int(input("Enter any number : "))
# temp = num
# reversed_num = 0
# while temp != 0:
#     digit = temp % 10
#     reversed_num = reversed_num*10 + digit
#     temp //= 10
# if reversed_num == num:
#     print(num, "is palindrome")
# else:
#     print(num, "is not palindrome")
    
# print("\nQ28. Write a python program to sum the sequence: 1 + 1/1! + 1/2! + 1/3! + …….. + 1/n!")
# n = int(input("Enter any number : "))
# i = 1
# sum = 1
# fact = 1
# while i <= n:
#     fact *= i
#     sum += 1 / fact
#     i += 1
# print("Sum of series : ", sum)

# print("\nQ29. Write a program to accept 10 numbers from the user and display it’s average.")
# sum = 0
# i = 0
# while i < 10:
#     num = int(input("Enter any number : "))
#     sum += num
#     i += 1
# average = sum / 10
# print("Average : ", average)

# print("\nQ30. Write a program to accept 10 numbers from the user and display the largest & smallest number number.")
# largest = 0
# smallest = 0
# i = 0
# while i < 10:
#     num = int(input("Enter any number : "))
#     if largest == 0 or num > largest:
#         largest = num
#     if smallest == 0 or num < smallest:
#         smallest = num
#     i += 1
# print("Largest number : ", largest)
# print("Smallest number : ", smallest)

# print("\nQ31. Write a program to display sum of odd numbers and even numbers separately that fallbetween two numbers accepted from the user.(including both numbers) using while loop.")
# print("Enter range (Both number are inclusive) ")
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number: "))
# if num1 > num2 : 
#     num1 , num2 = num2, num1
# i = num1
# even_sum = 0
# odd_sum = 0
# while i <= num2:
#     if i % 2 == 0: 
#         even_sum += i
#     else:
#         odd_sum += i
#     i += 1
# print("Sum of Even numbers : ", even_sum)

# print("\nQ32. Write a program to display all the numbers which are divisible by 13 but not by 3 between 100 and 500.(exclusive both numbers)")
# i = 101
# while i < 500:
#     if i % 13 == 0 and i % 3 != 0:
#         print(i)
#     i += 1

# print("\nQ33. Write a program to print the following series till n terms. : 2 , 22 , 222 , 2222 _ _ _ _ _ n terms")
# n = int(input("Enter any number : "))
# i = 1
# num = 2
# print("Series : ", end="")
# while i <= n:
#     print(num, end=" ")
#     num = num * 10 + 2
#     i += 1

# print("\nQ34. Write a program to print the following series till n terms. 1 4 9 16 25 _ _ _ _ _ n terms.")
# n = int(input("Enter any number : "))
# i = 1
# print("Series : ", end="")
# while i <= n:
#     print(i**2, end=" ")
#     i += 1
    
# print("\nQ35. Write a program to find the sum of the following series(accept values of x and n fromuser) 1 + x/1! + x2/2! + ……….xn/n!")
# x = int(input("Enter any number : "))
# n = int(input("Enter any number : "))
# i = 1
# sum = 1
# fact = 1
# while i <= n:
#     fact *= i
#     sum += (x * i) / fact
#     i += 1
# print("Sum of series : ", sum)

# print("\nQ36. Write a program to find the sum of following series : x + x2/2 + ……….xn/n")
# x = int(input("Enter any number : "))
# n = int(input("Enter any number : "))
# i = 1
# sum = 0
# while i <= n:
#     sum += (x * i) / i
#     i += 1
# print("Sum of series : ", sum)

# print("\nQ37. Write a program to find the sum of following series: 1 + 8 + 27 …………n terms")
# n = int(input("Enter any number : "))
# i = 1
# sum = 0
# while i <= n:
#     sum += i ** 3
#     i += 1
# print("Sum of series : ", sum)

# print("\nQ38. Write a program to find the sum of following series: 1 + 2 + 6 + 24 + 120 . . . . . n terms")
# n = int(input("Enter any number : "))
# i = 1
# sum = 0
# fact = 1
# while i <= n:
#     fact *= i
#     sum += fact
#     i += 1
# print("Sum of series : ", sum)

# print("\nQ39. Write a program to find the sum of following series: S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms")
# n = int(input("Enter any number : "))
# i = 1
# sum = 0
# while i <= n:
#     if i % 2 == 0:
#         sum += i ** 2
#     else:
#         sum -= i ** 2
#     i += 1
# print("Sum of series : ", sum)

# print("\nQ40. Write a Program to print all the characters in the string ‘PYTHON’ using while loop")
# string = "PYTHON"
# i = 0
# while i < len(string):
#     print(string[i])
#     i += 1

# print("\nQ41. Write a program to print only odd numbers from the given list using while loop. L = [23, 45, 32, 25, 46, 33, 71, 90]")
# L = [23, 45, 32, 25, 46, 33, 71, 90]
# i = 0
# while i < len(L):
#     if L[i] % 2 != 0:
#         print(L[i])
#     i += 1

# print("\nQ42. Write a program to print all the factors of a number using while loop.")
# num = int(input("Enter any number : "))
# i = 1
# print("Factors of ", num, " are : ", end="")
# while i <= num:
#     if num % i == 0:
#         print(i, end=" ")
#     i += 1

# print(''' \nQ43.Write a python program to get the following output
# 1—-49
# 2—-48
# 3—-47
# …
# …
# 48—-2
# 49—-1 ''')
# num = 49
# i = 1
# while i <= 49:
#     print(i, "———", num)
#     i += 1
#     num -= 1

# print("\nQ44. Write a program to extract all the upper case character from the given string: s=input(‘enter the string:’)")
# s = input("Enter the string : ")
# i = 0
# upper_case = ""
# while i < len(s):
#     if s[i].isupper():
#         upper_case += s[i]
#     i += 1
# print("Upper case characters : ", upper_case)

# print("\nQ45. .Write a Program to separate positive and negative number from a list. x = eval(input('enter the list:'))")
# x = eval(input("Enter the list : "))
# i = 0
# pos = []
# neg = []
# while i < len(x):
#     if x[i] >= 0:
#         pos.append(x[i])
#     else:
#         neg.append(x[i])
#     i += 1
# print("Positive numbers : ", pos)
# print("Negative numbers : ", neg)

# print("\nQ46. Write a program that appends the type of elements from a list. n = [23, 'Python',23.98]")
# n = [23, 'Python', 23.98]
# i = 0
# types = []
# while i < len(n):
#     types.append(type(n[i]))
#     i += 1
# print("Types of elements : ", types)

# print("\nQ47. Write a program to fetch only even values from a dictionary. dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 }")
# dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 }
# i = 0
# even_values = []
# keys = list(dic.keys())
# while i < len(dic):
#     if dic[keys[i]] % 2 == 0:
#         even_values.append(dic[keys[i]])
#     i += 1
# print("Even values : ", even_values)

# print("\nQ48. Write a program to extract all the string data items from the given list only if string is palindrome")
# L = ['abc', 'aba', 23, 45, '12321', 'xyz']
# i = 0
# palindrome_strings = []
# while i < len(L):
#     if type(L[i]) == str:
#         temp = L[i]
#         reversed_string = ""
#         while temp != "":
#             reversed_string += temp[-1]
#             temp = temp[:-1]
#         if reversed_string == L[i]:
#             palindrome_strings.append(L[i])
#     i += 1
# print("Palindrome strings : ", palindrome_strings)

# print("\nQ49. Write a program to extract all the special characters from the given string")
# s = input("Enter the string : ")
# i = 0
# special_characters = ""
# while i < len(s):
#     if not s[i].isalnum() and not s[i].isspace():
#         special_characters += s[i]
#     i += 1
# print("Special characters : ", special_characters)

# print("\nQ50. Write a program to extract all the upper case character ,lower case character ,numbers and special characters into four different output variables from the given string")
# s = input("Enter the string : ")
# i = 0
# upper_case = ""
# lower_case = ""
# numbers = ""
# special_characters = ""
# while i < len(s):
#     if 'A' <= s[i] <= 'Z':
#         upper_case += s[i]
#     elif 'a' <= s[i] <= 'z':
#         lower_case += s[i]
#     elif '0' <= s[i] <= '9':
#         numbers += s[i]
#     else:
#         special_characters += s[i]
#     i += 1
# print("Upper case characters : ", upper_case)
# print("Lower case characters : ", lower_case)
# print("Numbers : ", numbers)
# print("Special characters : ", special_characters)

# print("\nQ51. ")

# print("\nQ52. Write a program to convert all the lower case charater to upper case characters present in a given string ")
# s = input("Enter the string : ")
# i = 0
# while i < len(s):
#     if 'a' <= s[i] <= 'z':
#         s = s[:i] + s[i].upper() + s[i+1:]
#     i += 1
# print("Converted string : ", s)

# print("\nQ53. Write a program to convert all the lower case character to upper case character and upper case character to lower  case character by keeping number and special character as it is ")
# s = input("Enter the string : ")
# i = 0
# while i < len(s):
#     if 'a' <= s[i] <= 'z':
#         s = s[:i] + s[i].upper() + s[i+1:]
#     elif 'A' <= s[i] <= 'Z':
#         s = s[:i] + s[i].lower() + s[i+1:]
#     i += 1
# print("Converted string : ", s)

# print("\nQ54. Write a program to extract all the lower case character from the given string only if its ascii value is even ")
# s = input("Enter the string : ")
# i = 0
# lower_case = ""
# while i < len(s):
#     if 'a' <= s[i] <= 'z' and ord(s[i]) % 2 == 0:
#         lower_case += s[i]
#     i += 1
# print("Lower case characters with even ascii value : ", lower_case)

# print('''\nQ55. Write a program to get the following output 
#        input='abcd' 
#        output={'a':97,'b':98,'c':99,'d':100} ''')
# # s = input("Enter the string : ")
# s = 'abcd'
# i = 0
# output = {}
# while i < len(s):
#     output[s[i]] = ord(s[i])
#     i += 1
# print("Output : ", output)

# print('''\nQ56. Write a program to get the following output 
#        input='hello'
#        output={0:'h' , 1:'e' , 2:'l' , 3:'l' , 4:'o'} ''')
# # s = input("Enter the string : ")
# s = 'hello'
# i = 0
# output = {}
# while i < len(s):
#     output[i] = s[i]
#     i += 1
# print("Output : ", output)

# print('''\nQ57. Write a program to get the following output
#       input=['hai', 89, 3.4, 'hello', 90, 'py']
#       output={'hai':'hi', 'hello':'ho','py' : 'py'} ''')
# # x = eval(input("Enter the list : "))
# x = ['hai', 89, 3.4, 'hello', 90, 'py']
# i = 0
# output = {}
# while i < len(x):
#     if type(x[i]) == str:
#         output[x[i]] = x[i][0] + x[i][-1]
#     i += 1
# print("Output : ", output)

# print('''\nQ58. Write a program to get the following output
#       input='hai hello'
#       output='olleh iah' ''')
# # s = input("Enter the string : ")
# s = 'hai hello'
# i = 0
# reversed_string = ""
# while i < len(s):
#     reversed_string = s[i] + reversed_string
#     i += 1
# print("Reversed string : ", reversed_string)

# print("\nQ59. write a program to count the number of vowels present in a given string")
# s = input("Enter the string : ")
# i = 0
# vowels = "aeiouAEIOU"
# count = 0
# while i < len(s):
#     if s[i] in vowels:
#         count += 1
#     i += 1
# print("Number of vowels : ", count)

# print('''\nQ60. Write a program to get the following output
#       input='hai hello good morning'
#       output={'hai':'a', 'hello':'l', 'good:'gd','morning':'n'} ''')

# s = "hai hello good morning"
# # s = input("Enter the string : ")
# s = s.split()
# i = 0
# output = {}
# while i < len(s):
#     if len(s[i]) % 2 == 0:
#         output[s[i]] = s[i][0] + s[i][-1]
#     else:
#         output[s[i]] = s[i][len(s[i]) // 2]
#     i += 1
# print("Output : ", output)

# print('''\nQ61. Write a program to get the following output
#       input=['jiocinema.com', 'file.py', 'web.html']
#       output=['com', 'py', 'html'] ''')
# # x = eval(input("Enter the list : "))
# x = ['jiocinema.com', 'file.py', 'web.html']
# i = 0
# output = []
# while i < len(x):
#     output.append(x[i].split(".")[-1])
#     i += 1
# print("Output : ", output)

# print('''\nQ62. .Write a program to get the following output 
#        input=['jiocinema.com' , 'file.py' , 'web.html' , 'amazon.com' , 'text.py'] 
#        output={'com':['jiocinema' , 'amazon'] , 'py':[ 'file' , 'text'] ,  'html':['web']} ''')
# # x = eval(input("Enter the list : "))
# x = ['jiocinema.com' , 'file.py' , 'web.html' , 'amazon.com' , 'text.py']
# i = 0
# output = {}
# while i < len(x):
#     temp = x[i].split(".")
#     if temp[-1] not in output:
#         output[temp[-1]] = []
#     output[temp[-1]].append(temp[0])
#     i += 1
# print("Output : ", output)

# print('''\nQ63. Write a program to get the following output(count no of vowels) 
#        input='hai hello'
#        output={'hai':2 , 'hello':2} ''')
# # s = input("Enter the string : ")  
# s = 'hai hello'
# output = {}
# i = 0
# while i < len(s):
#     if s[i] == ' ':
#         i += 1
#         continue
#     count = 0
#     while i < len(s) and s[i] != ' ':
#         if s[i] in "aeiouAEIOU":
#             count += 1
#         i += 1
#     output[s[i - 1]] = count
# print("Output : ", output)

# print("\nQ64. Write a program to extract all the string values present in the list collection only if the last character is upper case. Concatenate the extracted output using '*' ")
# x = eval(input("Enter the list : "))
# # x = ['hai', 'hello', 'good', 'morning', 'PYTHON']
# i = 0
# output = ""
# while i < len(x):
#     if type(x[i]) == str and x[i][-1].isupper():
#         output += x[i] + "*"
#     i += 1
# print("Output : ", output[:-1])

# print("\nQ65. Write a program to extract all the list data items present in list collection only if it is having middle value , that value is integer and having even number  at start ")
# x = eval(input("Enter the list : "))
# i = 0
# output = []
# while i < len(x):
#     if type(x[i]) == list and len(x[i]) % 2 != 0 and type(x[i][len(x[i]) // 2]) == int and x[i][0] % 2 == 0:
#         output.append(x[i])
#     i += 1  
# print("Output : ", output)

# print('''\nQ66. Write a program to get the following output 
#        input= 'just looking like wow' 
#        output= 'jusT LOOKING Like a wow' ''')
# s = 'just looking like wow'
# # s = input("Enter the string : ")
# i = 0
# output = ""
# while i < len(s):

# print('''\nQ67. Program to find the common elements in two sets using a while loop 
# set1 = {1, 2, 3, 4, 5} 
# set2 = {3, 4, 5, 6, 7} ''')
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# i = 0
# common_elements = set()
# while i < len(set1):
#     if set1[i] in set2:
#         common_elements.add(set1[i])
#     i += 1
# print("Common elements : ", common_elements)

# print("\nQ68. Program to check if a number is a perfect number or not using while loop ")
# num = int(input("Enter any number : "))
# i = 1
# sum_of_divisors = 0
# while i <= num // 2:
#     if num % i == 0:
#         sum_of_divisors += i
#     i += 1
# if sum_of_divisors == num:
#     print(num, "is a perfect number")
# else:
#     print(num, "is not a perfect number")
    
# print("\nQ69.Program to find the length of the longest substring without repeating characters in a given string using while loop")
# s = input("Enter the string : ")
# i = 0
# max_length = 0
# current_length = 0
# char_index = {}
# while i < len(s):
#     if s[i] in char_index:
#         current_length = i - char_index[s[i]]
#     else:
#         current_length += 1
#     char_index[s[i]] = i
#     max_length = max(max_length, current_length)
#     i += 1
# print("Length of longest substring without repeating characters : ", max_length)

# print("\nQ72. Program to find the maximum and minimum elements in a tuple using while loop ")
# t = eval(input("Enter the tuple : "))
# maxi = t[0]
# mini = t[0]
# i = 1
# while i < len(t):
#     if t[i] > maxi:
#         maxi = t[i]
#     if t[i] < mini:
#         mini = t[i]
#     i += 1
# print("Maximum element : ", maxi)
# print("Minimum element : ", mini)

# print("\nQ73.Program to find the union, intersection, and difference of two sets using while loop ")
# set1= eval(input("Enter first set : "))
# set2= eval(input("Enter second set : "))
# i = 0
# union = set()
# intersection = set()
# difference = set()
# while i < len(set1):
#     union.add(set1[i])
#     if set1[i] in set2:
#         intersection.add(set1[i])
#     else:
#         difference.add(set1[i])
#     i += 1
# while i < len(set2):
#     union.add(set2[i])
#     if set2[i] not in set1:
#         difference.add(set2[i])
#     i += 1
# print("Union : ", union)
# print("Intersection : ", intersection)
# print("Difference : ", difference)

# print("\nQ74.Program to count the number of occurrences of each character in a string using a dictionary and while loop")
# s = input("Enter the string : ")
# i = 0
# count_dict = {}
# while i < len(s):
#     if s[i] in count_dict:
#         count_dict[s[i]] += 1
#     else:
#         count_dict[s[i]] = 1
#     i += 1
# print("Character count : ", count_dict)

# print("\nQ75. Write a program to remove duplicate value from collection without converting to set")
# k = eval(input("Enter the collection : "))
# i = 0
# output = []
# while i < len(k):
#     if k[i] not in output:
#         output.append(k[i])
#     i += 1
# print("Output : ", output)

# print("\nQ76.Write a program to find the length of collection without using len function")
# k = eval(input("Enter the collection : "))
# count = 0
# while True:
#     count += 1
#     try:
#         k[count]
#     except IndexError:
#         break
# print("Length of collection : ", count)

# print("\nQ77. Write a program to extract all the integers from a list only if the integer is starting from even number and ending as odd number and having length more than 3 ")
# x = eval(input("Enter the list : "))
# # x = [1234, 5678, 91011, 121314, 151617]
# i = 0   
# output = []
# while i < len(x):
#     if type(x[i]) == int and len(str(x[i])) > 3:
#         if str(x[i])[0] in "02468" and str(x[i])[-1] in "13579":
#             output.append(x[i])
#     i += 1
# print("Output : ", output)

# print("\nQ78.Write a program to extract all the individual data items of a list if the length of extracted output is more than 4 print the first value of the output else print last value of the output list and add 10 to it ")
# l = eval(input("Enter the list : "))
# i = 0
# output = []
# while i < len(l):
#     if type(l[i]) == list:
#         j = 0
#         while j < len(l[i]):
#             output.append(l[i][j])
#             j += 1
#     else:
#         output.append(l[i])
#     i += 1
# if len(output) > 4:
#     print("First value : ", output[0])
# else:
#     print("Last value + 10 : ", output[-1] + 10)

# print('''\nQ79. Write a program to get the following output 
#        input1='11001010' 
#        input2='01110010'
#        output=4 (to count how many positions are having same value) ''')
# input1 = '11001010'
# input2 = '01110010'
# i = 0
# count = 0
# while i < len(input1):
#     if input1[i] == input2[i]:
#         count += 1
#     i += 1
# print("Count of same positions : ", count)

# print('''\nQ80. Write a program to get the following output 
#        input=[1,2,3,4,5,6] 
#        value=3 
#        output=[1,2,3][4,5,6] 
#        If value=2 
#        output=[1,2][3,4][5,6] ''')
# input_list = eval(input("Enter the list : "))
# value = int(input("Enter the value : "))
# i = 0
# output = []
# while i < len(input_list):
#     sublist = []
#     j = 0
#     while j < value and i < len(input_list):
#         sublist.append(input_list[i])
#         j += 1
#         i += 1
#     output.append(sublist)
    
# print("Output : ", output)

# print("\nQ81. Write a program to check weather the given number is spy number or not i.e, 1*2*3=1+2+3")
# num = int(input("Enter any number : "))
# i = 0
# product = 1
# sum = 0
# while num != 0:
#     digit = num % 10
#     product *= digit
#     sum += digit
#     num //= 10
# if product == sum:
#     print("Spy number")
# else:
#     print("Not a spy number")
    
# print("\nQ82.Write a program to check weather the given number is Xylem number or not i.e, 1234 → 1+4=2+3")
# num = int(input("Enter any number : "))
# i = 0
# sum1 = 0
# sum2 = 0
# length = len(str(num))
# i = 0
# while num != 0:
#     digit = num % 10
#     if i < length // 2:
#         sum1 += digit
#     else:
#         sum2 += digit
#     num //= 10
#     i += 1
# if sum1 == sum2:
#     print("Xylem number")
# else:
#     print("Not a xylem number")
    
print("\nQ83. Write a program to check weather the given number is phloem number or not. i.e, 12345→ 1+5!=2+3+4 ")
num = int(input("Enter any number : "))
i = 0
sum1 = 0
sum2 = 0
length = len(str(num))
while num != 0:
    digit = num % 10
    if i == 0 or i == length - 1:
        sum1 += digit
    else:
        sum2 += digit
    num //= 10
    i += 1
if sum1 == sum2:
    print("Phloem number")
else:
    print("Not a phloem number")

print("\nQ84. Write a program to check weather the given number is neon number or not i.e. 9 is number, 9**2=81→8+1=9")
num = int(input("Enter any number : "))
i = 0
sum = 0
square = num ** 2
while square != 0:
    digit = square % 10
    sum += digit
    square //= 10
if sum == num:
    print("Neon number")
else:
    print("Not a neon number")

print("\nQ85. Write a program to check weather the given number is automorphic or not I.e.5 is number 5**2=25 last digit of 25 is the number itself")
num = int(input("Enter any number : "))
i = 0
square = num ** 2
last_digit = 0
while square != 0:
    last_digit = square % 10
    square //= 10
if last_digit == num:
    print("Automorphic number")
else:
    print("Not an automorphic number")

print("\nQ86. Write a program to count number of words in the given string. s=input('enter the str:').split() ")
s = input("Enter the string : ")
s = s.split()
i = 0
count = 0
while i < len(s):
    count += 1
    i += 1
print("Number of words : ", count)

print("\nQ87. Write a program to find the length of the longest word")
s = input("Enter the string : ")
s = s.split()
i = 0
longest_word = ""
while i < len(s):
    if len(s[i]) > len(longest_word):
        longest_word = s[i]
    i += 1
print("Longest word : ", longest_word)

print("\nQ88. Write a program to count number of consonants in the given string. s=input('enter the str:')")
s = input("Enter the string : ")
i = 0
count = 0
while i < len(s):
    if s[i] not in "aeiouAEIOU" and 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
        count += 1
    i += 1
print("Number of consonants : ", count)

print("\nQ89. Write a program to check the type of data entered by the users")
s = input("Enter the string : ")
i = 0
while i < len(s):
    if s[i].isdigit():
        print(s[i], "is digit")
    elif s[i].isalpha():
        print(s[i], "is alphabet")
    elif s[i].isspace():
        print(s[i], "is space")
    else:
        print(s[i], "is special character")
    i += 1


print("\nQ90. Write a program to check weather the given tuple is palindrome or not ")
t = eval(input("Enter the tuple : "))
i = 0
j = len(t) - 1
is_palindrome = True
while i < j:
    if t[i] != t[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
if is_palindrome:
    print("Palindrome tuple")
else:
    print("Not a palindrome tuple")

print("\nQ91. Write a program to check weather the given collection is having nested collection or not")
k = eval(input("Enter the collection : "))
i = 0
is_nested = False
while i < len(k):
    if type(k[i]) == list or type(k[i]) == tuple or type(k[i]) == set or type(k[i]) == dict or type(k[i]) == str:
        is_nested = True
        break
    i += 1
if is_nested:
    print("Nested collection found")
else:
    print("Not any a nested collection found")

print("\nQ92. Write a program to return the positions of vowels present in the given string ")
s = input("Enter the string : ")
i = 0
positions = []
while i < len(s):
    if s[i] in "aeiouAEIOU":
        positions.append(i)
    i += 1
print("Positions of vowels : ", positions)

print("\nQ93. Write a program to find length of collection without using len function ")
k = eval(input("Enter the collection : "))
count = 0
while True:
    try:
        k[count]
    except IndexError:
        break
    count += 1
print("Length of collection : ", count)

print("Write a program to whether the entered username  and password is correct or not if not correct print enter again")
username = 'samarthmule'
password = 'jbdij@%&272'
while True:
    username_n = input("Enter username : ")
    if username == username_n:
        break
    else :
        print("Not Correct. Try Again")
while True:
    pass_n = input("Enter Password: ")
    if password == pass_n:
        break
    else :
        print("Not correct. Try Again")

print("\nQ95. Write a program to extract all integer data items from tuple ")
t = eval(input("Enter the tuple : "))
i = 0
output = []
while i < len(t):
    if type(t[i]) == int:
        output.append(t[i])
    i += 1
print("Output : ", output)

print("\nQ96. Write a  program to extract all the non default values from the list ")
x = eval(input("Enter the list : "))
i = 0
output = []
while i < len(x):
    if x[i] != 0 and x[i] != 1 and x[i] != -1 and x[i] != None:
        output.append(x[i])
    i += 1
print("Output : ", output)

print('''\nQ97. Write a program to get the following output: 
Input='hai hello how are you' 
output='hai**hello**how**are**you' ''')
# s = input("Enter the string : ")
s = 'hai hello how are you'
output = ""
i = 0
while i < len(s):
    if s[i] != ' ':
        output += s[i]
    else:
        output += '**'
    i += 1
print("Output : ", output)

print("\nQ98. Write a program to reverse the given list")
x = eval(input("Enter the list : "))
i = 0
output = []
while i < len(x):
    output.insert(0, x[i])
    i += 1
print("Output : ", output)

print("\nQ99. Write a program for number game")
import random
number = random.randint(1, 100)
while True:
    guess = int(input("Guess the number between 1 and 100 : "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        break

print("\nQ100. Write a program to print 'Thank you' for n times")
n = int(input("Enter any number : "))
i = 0
while i < n:
    print("Thank you")
    i += 1


# Same 100 Programs in for loop
print("\n\n\nSame 100 Programs in for loop")
# print("\nQ1. Write a program to print the following using while loop First 10 Even numbers ")
# for i in range(0, 20, 2):
#     print(i, end=" ")

# print("\nQ2. Write a program to print the following using while loop First 10 Odd numbers ")
# for i in range(1, 20, 2):
#     print(i, end=" ")

# print("\nQ3. Write a program to print the following using while loop First 10 Natural numbers ")
# for i in range(1, 11):
#     print(i, end=" ")

# print("\nQ4. Write a program to print the following using while loop First 10 Whole numbers ")
# for i in range(0, 11):
#     print(i, end=" ")

# print("\nQ5. Write a program to print first 10 integers and their squares using while loop. ")
# for i in range(0, 10):
#     print(i, "->", i ** 2)

# print("\nQ6. Q6. Write while loop statement to print the following series: 10, 20, 30 … … 300")
# for i in range(10, 301, 10):
#     print(i, end=" ")

# print("\nQ7. Write a while loop statement to print the following series 105, 98, 91 ………7. ")
# for i in range(105, 6, -7):
#     print(i, end=" ")

# print("\nQ8. Q8. Write a program to print the first 10 natural number in reverse order using while loop.")
# for i in range(10, 0, -1):
#     print(i, end=" ")
    
# print("\nqQ9. Write a program to print sum of first 10 Natural numbers. ")
# sum = 0
# for i in range(1, 11):
#     sum += i
# print("Sum of first 10 natural numbers : ", sum)

# print("\nQ10. Write a program to print sum of first 10 even numbers.")
# sum = 0
# for i in range(0, 20, 2):
#     sum += i
# print("Sum of first 10 even numbers : ", sum)

# print("\nQ11. Write a program to print table of a number entered from the user. ")
# num = int(input("Enter any number : "))
# for i in range(1, 11):
#     print(num, "*", i, "=", num * i)

# print("\nQ12. Write a program to print all even numbers that falls between two numbers (exclusive both numbers) entered from the user using for loop.")
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# if num1 > num2:
#     num1, num2 = num2, num1
# print("Even numbers between", num1, "and", num2, "are : ", end="")
# for i in range(num1 + 1, num2):
#     if i % 2 == 0:
#         print(i, end=" ")

# print("\nQ13. Write a program to check whether a number is prime or not using for loop.")
# num = int(input("Enter any number : "))
# i = 2
# while i <= num // 2:
#     if num % i == 0:
#         print(num, "is not a prime number")
#         break
#     i += 1
# else:
#     print(num, "is a prime number")

# print("\nQ14. Write a program to find the sum of the digits of a number accepted from the user")
# num = int(input("Enter any number : "))
# sum = 0
# for i in str(num):
#     sum += int(i)
# print("Sum of digits : ", sum)

# print("\nQ15. Write a program to find the product of the digits of a number accepted from the user.")
# num = int(input("Enter any number : "))
# product = 1
# for i in str(num):
#     product *= int(i)
# print("Product of digits : ", product)

# print("\nQ16. Write a program to reverse the number accepted from user using for loop. ")
# num = int(input("Enter any number : "))
# reverse_num = 0
# for i in range(len(str(num))):
#     reverse_num = reverse_num * 10 + num % 10
#     num //= 10
# print("Reversed number : ", reverse_num)

# print("\nQ17. Write a program to display the number names of the digits of a number entered by user, for example if the number is 231 then output should be Two Three One ")
# num = int(input("Enter any number : "))
# number_names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
# output = ""
# for i in str(num):
#     output += number_names[int(i)] + " "
# print("Number names : ", output.strip())

# print("\nQ18. Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop. ")
# n = int(input("Enter the number of terms: "))
# a, b = 0, 1
# print("Fibonacci series: ", end="")
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# print("\nQ19. Write a program to print the factorial of a number accepted from user.")
# num = int(input("Enter any number : "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i

# print("\nQ20. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.) ")
# num = int(input("Enter any number : "))
# sum = 0
# for i in str(num):
#     sum += int(i) ** 3
    
# if sum == num:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")
    
# print("\nQ21. Write a program to add first n terms of the following series using a while loop: 1/1! + 1/2! + 1/3! + …….. + 1/n! ")
# n = int(input("Enter the number of terms : "))
# sum = 0
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
#     sum += 1 / factorial

# print("Sum of series : ", sum)

# print("\nQ22. Write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered. ")
# num = 0
# sum = 0
# for _ in range(100):
#     num = int(input("Enter any number : "))
#     sum += num
#     choice = input("Do you want to continue (y/n) : ")
#     if choice.lower() != 'y':
#         break
# print("Sum of numbers : ", sum)

# print("\nQ23. Write a program to enter the numbers till the user enter ZERO and at the end it should display the count of positive and negative numbers entered. ")
# positions = 0
# negatives = 0
# num = 0
# for _ in range(100):
#     num = int(input("Enter any number : "))
#     if num == 0:
#         break
#     elif num > 0:
#         positions += 1
#     else:
#         negatives += 1
# print("Count of positive numbers : ", positions)
# print("Count of negative numbers : ", negatives)

# print("\nQ24. Write a program to find the HCF of two numbers entered from the user. ")
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# for i in range(1, min(num1, num2) + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i
# print("HCF of", num1, "and", num2, "is : ", hcf)

# print("\nQ25. Write a program to convert Decimal to Binary. ")
# num = int(input("Enter any number : "))
# binary = ""
# for i in range(8):
#     binary = str(num % 2) + binary
#     num //= 2
# print("Binary : ", binary)

# print("\nQ26. Write a program to convert Binary to Decimal.")
# num = input("Enter binary number : ")
# decimal = 0
# for i in range(len(num)):
#     decimal += int(num[i]) * (2 ** (len(num) - 1 - i))
# print("Decimal : ", decimal)

# print("\nQ27. Write a program to check whether a number is palindrome or not. ")
# num = int(input("Enter any number : "))
# reverse_num = 0
# for i in range(len(str(num))):
#     reverse_num = reverse_num * 10 + num % 10
#     num //= 10
# if reverse_num == num:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

# print("\nQ28. Write a python program  to sum the sequence: 1 + 1/1! + 1/2! + 1/3! + …….. + 1/n! ")
# n = int(input("Enter the number of terms : "))
# sum = 1
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
#     sum += 1 / factorial
# print("Sum of series : ", sum)

# print("\nQ29. Write a program to accept 10 numbers from the user and display it’s average")
# sum = 0
# for i in range(10):
#     sum += int(input("Enter any number : "))
# average = sum / 10
# print("Average : ", average)

# print("\nQ30. Write a program to accept 10 numbers from the user and display the largest & smallest number number. ")
# largest = smallest = int(input("Enter any number : "))
# for i in range(9):
#     num = int(input("Enter any number : "))
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print("Largest number : ", largest)
# print("Smallest number : ", smallest)

# print("\nQ31. Write a program to display sum of odd numbers and even numbers separately that fall between two numbers accepted from the user.(including both numbers) using while loop. ")
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# if num1 > num2:
#     num1, num2 = num2, num1
# sum_even = 0    
# sum_odd = 0
# for i in range(num1, num2 + 1):
#     if i % 2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i
# print("Sum of even numbers : ", sum_even)

# print("\nQ32. Write a program to display all the numbers which are divisible by 13 but not by 3 between 100 and 500.(exclusive both numbers) ")
# for num in range(101, 500):
#     if num % 13 == 0 and num % 3 != 0:
#         print(num)
    
# print("\nQ33. Q33. Write a program to print the following series till n terms. 2 , 22 , 222 , 2222 _ _ _ _ _ n terms ")
# n = int(input("Enter the number of terms : "))
# num = 2
# for i in range(n):
#     print(num, end=" ")
#     num = num * 10 + 2

# print("\nQ34. Write a program to print the following series till n terms. : 1 4 9 16 25 _ _ _ _ _ n terms.")
# n = int(input("Enter the number of terms : "))
# for i in range(1, n + 1):
#     print(i ** 2, end=" ")

# print("\nQ35. Write a program to find the sum of the following series(accept values of x and n from user): 1 + x/1! + x2/2! + ……….xn/n!")
# x = int(input("Enter the value of x : "))
# n = int(input("Enter the value of n : "))
# sum = 1
# for i in range(1, n + 1):
#     factorial = 1
#     for j in range(1, i + 1):
#         factorial *= j
#     sum += (x ** i) / factorial
# print("Sum of series : ", sum)

# print("\nQ36. Write a program to find the sum of following series : x + x2/2 + ……….xn/n")
# x = int(input("Enter the value of x : "))
# n = int(input("Enter the value of n : "))
# sum = 0
# for i in range(1, n + 1):
#     sum += (x ** i) / i
# print("Sum of series : ", sum)

# print("\nQ37. Write a program to find the sum of following series: 1 + 8 + 27 …………n terms")
# n = int(input("Enter the number of terms : "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i ** 3
# print("Sum of series : ", sum)

# print("\nQ38. Write a program to find the sum of following series: 1 + 2 + 6 + 24 + 120 . . . . . n terms ")
# n = int(input("Enter the number of terms : "))
# sum = 0
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
#     sum += factorial
# print("Sum of series : ", sum)

# print("\nQ39. Write a program to find the sum of following series:S = 1 + 4 - 9 + 16 - 25 + 36 - … … n terms ")
# n = int(input("Enter the number of terms : "))
# sum = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sum -= i ** 2
#     else:
#         sum += i ** 2
# print("Sum of series : ", sum)

# print("\nQ40. Write a Program to print all the characters in the string 'PYTHON' using for loop. ")
# s = "PYTHON"
# i = 0
# for i in range(len(s)):
#     print(s[i], end=" ")

# print("\nQ41. Write a program to print only odd numbers from the given list using for loop. L = [23, 45, 32, 25, 46, 33, 71, 90]")
# L = [23, 45, 32, 25, 46, 33, 71, 90]
# for i in L:
#     if i % 2 != 0:
#         print(i, end=" ")
# print("\nQ42. Write a program to print all the factors of a number using for loop.")
# num = int(input("Enter any number : "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, end=" ")
    
# print(''' \nQ43.Write a python program to get the following output
# 1—-49
# 2—-48
# 3—-47
# …
# …
# 48—-2
# 49—-1 ''')
# num = 49
# for i in range(1, num + 1):
#     print(i, "—-", num - i + 1)

# print("\nQ44. Write a program to extract all the upper case character from the given string: s=input(‘enter the string:’)")
# s = input("Enter the string : ")
# upper_case = ""
# for i in s:
#     if i.isupper():
#         upper_case += i
# print("Upper case characters : ", upper_case)

# print("\nQ45. .Write a Program to separate positive and negative number from a list. x = eval(input('enter the list:'))")
# x = eval(input("Enter the list : "))
# positive = []
# negative = []
# for i in x:
#     if i >= 0:
#         positive.append(i)
#     else:
#         negative.append(i)
# print("Positive numbers : ", positive)
# print("Negative numbers : ", negative)

# print("\nQ46. Write a program that appends the type of elements from a list. n = [23, 'Python',23.98]")
# n = [23, 'Python', 23.98]
# types = []
# for i in n:
#     types.append(type(i))
# print("Types of elements : ", types)

# print("\nQ47. Write a program to fetch only even values from a dictionary. dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 }")
# dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 }
# even_values = {}
# for key, value in dic.items():
#     if value % 2 == 0:
#         even_values[key] = value
# print("Even values : ", even_values)

# print("\nQ48. Write a program to extract all the string data items from the given list only if string is palindrome")
# L = ['abc', 'aba', 23, 45, '12321', 'xyz']
# palindrome_strings = []
# for i in L:
#     if isinstance(i, str) and i == i[::-1]:
#         palindrome_strings.append(i)
# print("Palindrome strings : ", palindrome_strings)

# print("\nQ49. Write a program to extract all the special characters from the given string")
# s = input("Enter the string : ")
# special_characters = ""
# for i in s:
#     if not i.isalnum() and not i.isspace():
#         special_characters += i

# print("Special characters : ", special_characters)

# print("\nQ50. Write a program to extract all the upper case character ,lower case character ,numbers and special characters into four different output variables from the given string")
# s = input("Enter the string : ")
# upper_case = ""
# lower_case = ""
# numbers = ""
# special_characters = ""
# for i in s:
#     if 'A' <= i <= 'Z':
#         upper_case += i
#     elif 'a' <= i <= 'z':
#         lower_case += i
#     elif '0' <= i <= '9':
#         numbers += i
#     else:
#         special_characters += i

# print("\nQ51. ")

# print("\nQ52. Write a program to convert all the lower case charater to upper case characters present in a given string ")
# s = input("Enter the string : ")
# upper_case = ""
# for i in s:
#     if 'a' <= i <= 'z':
#         upper_case += chr(ord(i) - 32)
#     else:
#         upper_case += i
# print("Upper case string : ", upper_case)

# print("\nQ53. Write a program to convert all the lower case character to upper case character and upper case character to lower  case character by keeping number and special character as it is ")
# s = input("Enter the string : ")
# output = ""
# for i in s:
#     if 'a' <= i <= 'z':
#         output += chr(ord(i) - 32)
#     elif 'A' <= i <= 'Z':
#         output += chr(ord(i) + 32)
#     else:
#         output += i
# print("Output string : ", output)

# print("\nQ54. Write a program to extract all the lower case character from the given string only if its ascii value is even ")
# s = input("Enter the string : ")
# lower_case = ""
# for i in s:
#     if 'a' <= i <= 'z' and ord(i) % 2 == 0:
#         lower_case += i
# print("Lower case characters with even ascii value : ", lower_case)

# print('''\nQ55. Write a program to get the following output 
#        input='abcd' 
#        output={'a':97,'b':98,'c':99,'d':100} ''')
# # s = input("Enter the string : ")
# s = 'abcd'
# output = {}
# for i in s:
#     output[i] = ord(i)
# print("Output : ", output)

# print('''\nQ56. Write a program to get the following output 
#        input='hello'
#        output={0:'h' , 1:'e' , 2:'l' , 3:'l' , 4:'o'} ''')
# # s = input("Enter the string : ")
# s = 'hello'
# output = {}
# for i in range(len(s)):
#     output[i] = s[i]
# print("Output : ", output)

# print('''\nQ57. Write a program to get the following output
#       input=['hai', 89, 3.4, 'hello', 90, 'py']
#       output={'hai':'hi', 'hello':'ho','py' : 'py'} ''')
# # x = eval(input("Enter the list : "))
# x = ['hai', 89, 3.4, 'hello', 90, 'py']
# output = {}
# for i in x:
#     if type(i) == str:
#         if len(i) > 2:
#             output[i] = i[0] + i[-1]
#         else:
#             output[i] = i
# print("Output : ", output)

# print('''\nQ58. Write a program to get the following output
#       input='hai hello'
#       output='olleh iah' ''')
# # s = input("Enter the string : ")
# s = 'hai hello'
# reversed_string = ""
# for i in s:
#     reversed_string = i + reversed_string
# print("Output : ", reversed_string.strip())

# print("\nQ59. write a program to count the number of vowels present in a given string")
# s = input("Enter the string : ")
# vowels = "aeiouAEIOU"
# count = 0
# for i in s:
#     if i in vowels:
#         count += 1
# print("Number of vowels : ", count)

# print('''\nQ60. Write a program to get the following output
#       input='hai hello good morning'
#       output={'hai':'a', 'hello':'l', 'good:'gd','morning':'n'} ''')

# s = "hai hello good morning"
# # s = input("Enter the string : ")
# s = s.split()
# output = {}
# for i in s:
#     if len(i) > 2:
#         output[i] = i[1] + i[-1]
#     else:
#         output[i] = i
# print("Output : ", output)

# print('''\nQ61. Write a program to get the following output
#       input=['jiocinema.com', 'file.py', 'web.html']
#       output=['com', 'py', 'html'] ''')
# # x = eval(input("Enter the list : "))
# x = ['jiocinema.com', 'file.py', 'web.html']
# output = []
# for i in x:
#     if '.' in i:
#         output.append(i.split('.')[-1])
# print("Output : ", output)

# print('''\nQ62. .Write a program to get the following output 
#        input=['jiocinema.com' , 'file.py' , 'web.html' , 'amazon.com' , 'text.py'] 
#        output={'com':['jiocinema' , 'amazon'] , 'py':[ 'file' , 'text'] ,  'html':['web']} ''')
# # x = eval(input("Enter the list : "))
# x = ['jiocinema.com' , 'file.py' , 'web.html' , 'amazon.com' , 'text.py']
# output = {}
# for i in x:
#     if '.' in i:
#         key = i.split('.')[-1]
#         value = i.split('.')[0]
#         if key not in output:
#             output[key] = []
#         output[key].append(value)
# print("Output : ", output)

# print('''\nQ63. Write a program to get the following output(count no of vowels) 
#        input='hai hello'
#        output={'hai':2 , 'hello':2} ''')
# # s = input("Enter the string : ")  
# s = 'hai hello'
# output = {}
# for i in s.split():
#     count = 0
#     for j in i:
#         if j in "aeiouAEIOU":
#             count += 1
#     output[i] = count
# print("Output : ", output)

# print("\nQ64. Write a program to extract all the string values present in the list collection only if the last character is upper case. Concatenate the extracted output using '*' ")
# x = eval(input("Enter the list : "))
# # x = ['hai', 'hello', 'good', 'morning', 'PYTHON']
# output = ""
# for i in x:
#     if type(i) == str and 'A' <= i[-1] <= 'Z':
#         output += i + "*"
# print("Output : ", output.strip('*'))

# print("\nQ65. Write a program to extract all the list data items present in list collection only if it is having middle value , that value is integer and having even number  at start ")
# x = eval(input("Enter the list : "))
# output = []
# for i in x:
#     if type(i) == list and len(i) % 2 != 0 and i[len(i) // 2] % 2 == 0 and i[0] % 2 == 0:
#         output.append(i)
# print("Output : ", output)

# print('''\nQ66. Write a program to get the following output 
#        input= 'just looking like wow' 
#        output= 'jusT LOOKING Like a wow' ''')
# s = input("Enter the string : ")
# s = 'just looking like wow'
# s = s.split()   
# output = ""

# print('''\nQ67. Program to find the common elements in two sets using a for loop 
# set1 = {1, 2, 3, 4, 5} 
# set2 = {3, 4, 5, 6, 7} ''')
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# common_elements = set()
# for i in set1:
#     if i in set2:
#         common_elements.add(i)
# print("Common elements : ", common_elements)

# print("\nQ68. Program to check if a number is a perfect number or not using for loop ")
# num = int(input("Enter any number : "))
# sum_of_divisors = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum_of_divisors += i
# if sum_of_divisors == num:  
#     print(num, "is a perfect number")
# else:
#     print(num, "is not a perfect number")
    
# print("\nQ69.Program to find the length of the longest substring without repeating characters in a given string using for loop")
# s = input("Enter the string : ")
# max_length = 0
# current_length = 0
# char_index = {}
# for i in range(len(s)):
#     if s[i] in char_index:
#         current_length = i - char_index[s[i]]
#     else:
#         current_length += 1
#     char_index[s[i]] = i
#     max_length = max(max_length, current_length)
# print("Length of longest substring without repeating characters : ", max_length)

# print("\nQ72. Program to find the maximum and minimum elements in a tuple using for loop ")
# t = eval(input("Enter the tuple : "))
# maxi = t[0]
# mini = t[0]
# for i in t:
#     if i > maxi:
#         maxi = i
#     if i < mini:
#         mini = i
# print("Maximum element : ", maxi)
# print("Minimum element : ", mini)

# print("\nQ73.Program to find the union, intersection, and difference of two sets using while loop ")
# set1= eval(input("Enter first set : "))
# set2= eval(input("Enter second set : "))
# union = set()
# intersection = set()
# difference = set()

# for i in set1:
#     union.add(i)
#     if i in set2:
#         intersection.add(i)
#     else:
#         difference.add(i)
# for i in set2:
#     union.add(i)
#     if i not in set1:
#         difference.add(i)

# print("Union : ", union)
# print("Intersection : ", intersection)
# print("Difference : ", difference)


# print("\nQ74.Program to count the number of occurrences of each character in a string using a dictionary and while loop")
# s = input("Enter the string : ")
# count_dict = {}
# for i in s:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
# print("Character occurrences: ", count_dict)

# print("\nQ75. Write a program to remove duplicate value from collection without converting to set")
# k = eval(input("Enter the collection : "))
# output = []
# for i in k:
#     if i not in output:
#         output.append(i)
# print("Collection without duplicates: ", output)

# print("\nQ76.Write a program to find the length of collection without using len function")
# k = eval(input("Enter the collection : "))
# count = 0
# for i in k:
#     count += 1
# print("Length of collection: ", count)
# print("\nQ77. Write a program to extract all the integers from a list only if the integer is starting from even number and ending as odd number and having length more than 3 ")
# x = eval(input("Enter the list : "))
# output = []
# for i in x:
#     if type(i) == int and len(str(i)) > 3 and i % 2 == 1 and str(i)[0] in "02468":
#         output.append(i)
# print("Output : ", output)

# print("\nQ78.Write a program to extract all the individual data items of a list if the length of extracted output is more than 4 print the first value of the output else print last value of the output list and add 10 to it ")
# l = eval(input("Enter the list : "))
# output = []
# for i in l:
#     if type(i) == list:
#         for j in i:
#             output.append(j)
#     else:
#         output.append(i)

# if len(output) > 4:
#     print("First value of output : ", output[0])
# else:
#     print("Last value + 10 : ", output[-1] + 10)
    
# print('''\nQ79. Write a program to get the following output 
#        input1='11001010' 
#        input2='01110010'
#        output=4 (to count how many positions are having same value) ''')
# input1 = '11001010'
# input2 = '01110010'
# count = 0
# for i in range(len(input1)):
#     if input1[i] == input2[i]:
#         count += 1
# print("Count of same position : ", count)

# print('''\nQ80. Write a program to get the following output 
#        input=[1,2,3,4,5,6] 
#        value=3 
#        output=[1,2,3][4,5,6] 
#        If value=2 
#        output=[1,2][3,4][5,6] ''')
# input_list = eval(input("Enter the list : "))
# value = int(input("Enter the value : "))
# output = []

# for i in range(0, len(input_list), value):
#     output.append(input_list[i:i + value])
    
# print("Output : ", output)

# print("\nQ81. Write a program to check weather the given number is spy number or not i.e, 1*2*3=1+2+3")
# num = int(input("Enter any number : "))
# product = 1
# sum = 0
# for i in str(num):
#     product *= int(i)
#     sum += int(i)
# if product == sum:
#     print(num, "is a spy number.")
# else:
#     print(num, "is not a spy number.")
    
    
# print("\nQ82.Write a program to check weather the given number is Xylem number or not i.e, 1234 → 1+4=2+3")
# num = int(input("Enter any number : "))
# sum1 = 0
# sum2 = 0
# for i in str(num):
#     sum1 += int(i)
#     sum2 += int(str(num)[-1 - str(num).index(i)])
# if sum1 == sum2:
#     print(num, "is a Xylem number.")
# else:
#     print(num, "is not a Xylem number.")