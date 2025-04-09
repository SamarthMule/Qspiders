# Pattern Programming
# We can use nested loops to print patterns in Python.
# Example: Print a square pattern of stars
# for i in range(5): # Outer loop for rows
#     for j in range(5): # Inner loop for columns
#         print("*", end=" ") # Print star without newline
#     print() # Print newline after each row
# # Output:
# # * * * * *
# # * * * * *
# # * * * * *
# # * * * * *
# # * * * * *
# # Example: Print a right triangle pattern of stars
# for i in range(5):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print() # Print newline after each row
# # Output:
# # *
# # * *
# # * * *
# # * * * *
# # * * * * *

# # Print Following Patterns:
# # * * *
# # * * *
# # * * *
# # * * *
# for i in range(4):
#     for j in range(3):
#         print("*", end=" ")
#     print()

# # Print Following Patterns:
# # * * * * *
# # * * * * *
# for i in range(2):
#     for j in range(5):
#         print("*", end=" ")
#     print()

# # Pattern : Primary Diagonal of n x n matrix
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if i == j:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# # *
# #   *
# #     *
# #       *   
# #         *

# # Pattern : Secondary Diagonal of n x n matrix
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if i + j == num - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# #         * 
# #       *
# #     *
# #   *
# # *

# # Pattern : Triangle of n rows
# # num = int(input("Enter the number of rows: "))
# # for i in range(num):
# #     for j in range(i + 1):
# #         print("*", end=" ")
# #     print()
# # OR
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if j <= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# # *
# # * *
# # * * *
# # * * * *
# # * * * * *

# # Pattern: Mirror Triangle of n rows
# num = int(input("Enter the number of rows: ")) 
# for i in range(num):
#     for j in range(num - i - 1):
#         print(" ", end=" ")
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()
# # OR 
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if j >= num - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# #         *
# #       * *
# #     * * *
# #   * * * *
# # * * * * *

# # Pattern: Inverted Mirror Triangle of n rows
# num = int(input("Enter the number of rows: "))  
# for i in range(num):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(num - i):
#         print("*", end=" ")
#     print()
# # OR
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if j >= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# # * * * * *
# #   * * * *
# #     * * *
# #       * *
# #         *

# # Pattern: Inverted Triangle of n rows
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num - i):
#         print("*", end=" ")
#     print() 
# # OR
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if j < num - i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print() 
# # Output:
# # Enter the number of rows: 5   
# # * * * * *
# # * * * *
# # * * * 
# # * *
# # *

# # Pattern: Pyramid of n rows
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num - i - 1):
#         print(" ", end=" ")
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     print()
# # OR
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num * 2 - 1):
#         if j + i >= num - 1 and j - i <= num - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# #         *
# #       * * *
# #     * * * * *
# #   * * * * * * *
# # * * * * * * * * *

# # Pattern: Inverted Pyramid of n rows
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(2 * (num - i) - 1):
#         print("*", end=" ")
#     print()
# # OR
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if j >= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(num - i - 1):
#         print("*", end=" ")
#     print()
# # OR
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num * 2 - 1):
#         if j >= i and j + i <= (num * 2) - 2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# # * * * * * * * * *
# #   * * * * * * *
# #     * * * * *
# #       * * *
# #         *

# # Pattern : Diomand of n 
# num = int(input("Enter the number : "))
# for i in range(num):
#     for j in range(num * 2 - 1):
#         if j + i >= num - 1 and j - i <= num - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(num-1):
#     print(" ",end=" ")
#     for j in range((num-1) * 2 - 1):
#         if j >= i and j + i <= ((num-1) * 2) - 2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # OR
# # num = int(input("Enter the number : "))

# Output : 
# Enter the number : 5
# #         *
# #       * * *
# #     * * * * *
# #   * * * * * * *
# # * * * * * * * * *
# #   * * * * * * *
# #     * * * * *
# #       * * *
# #         *

# # Pattern : Vertical Triangle of n rows
# num = int(input("Enter the number : "))
# for i in range(num):
#     for j in range(num):
#         if j >= num - i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(num-1):
#     print(" ", end=" ")
#     for j in range(num-1):
#         if j >= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Output :
# Enter the number : 5
#         *
#       * * 
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# OR

# # Pattern : Square + Triangle of n rows
# num = int(input("Enter the number : "))
# for i in range(num):
#     for j in range(num):
#         print("*", end=" ")
#     print()
# for i in range(num-1):
#     print(" ", end=" ")
#     for j in range(num-1):
#         if j >= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Output :
# Enter the number : 5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# # Pattern : Triangle + Triangle
# num = int(input("Enter the number : "))
# for i in range(num):
#     for j in range(num):
#         if j <= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(num-1):
#     print(" ", end=" ")
#     for j in range(num-1):
#         if j >= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
# # Pattern : Plus of n rows
# num = int(input("Enter the number : "))
# for i in range(num):
#     for j in range(num):
#         if i == num // 2 or j == num // 2:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output :
#     * 
#     * 
# * * * * *
#     *  
#     *

# # Pattern : Cross of n rows
# num = int(input("Enter the number : "))
# for i in range(num):
#     for j in range(num):
#         if i == j or i + j == num - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Output :
# Enter the number : 5
# *       *
#   *   *
#     *
#   *   *
# *       *


# # Easy Way to Print Patterns (Using One For loop)
# # Pyramid Pattern
# num = int(input("Enter the number of rows: "))
# for i in range(num + 1):
#     print(" " * (num - i) + "* " * i)
# print()
# # Output:
# # Enter the number of rows: 5
# #     *
# #    * *
# #   * * *
# #  * * * *
# # * * * * *

# # Inverted Pyramid Pattern
# num = int(input("Enter the number of rows: "))
# for i in range(num + 1):
#     print(" " * i + "* " * (num - i))
# print()
# # Output:
# # Enter the number of rows: 5
# # * * * * *
# #  * * * *
# #   * * *
# #    * *
# #     *

# # Left sided Pyramid Pattern
# num = int(input("Enter the number of rows: "))
# for i in range(num + 1):
#     print("* " * i)
# print()

# # Right sided Pyramid Pattern
# num = int(input("Enter the number of rows: "))
# for i in range(num + 1):
#     print(" " * (num - i) + "* " * i)
# print()
# # Output:
# # Enter the number of rows: 5
# #         *
# #       * *
# #     * * *
# #   * * * *
# # * * * * *

# # Patterm : Matrix of n x n matrix with numbers
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         print(f"({i},{j})", end="  ")
#     print("\n")
# # Output:
# # Enter the number of rows: 5
# # (0,0)  (0,1)  (0,2)  (0,3)  (0,4)
# #
# # (1,0)  (1,1)  (1,2)  (1,3)  (1,4)
# #
# # (2,0)  (2,1)  (2,2)  (2,3)  (2,4)
# #
# # (3,0)  (3,1)  (3,2)  (3,3)  (3,4)
# #
# # (4,0)  (4,1)  (4,2)  (4,3)  (4,4)


# # Pattern : Hollow Square of n x n matrix
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if i == 0 or i == num - 1 or j == 0 or j == num - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# # * * * * *
# # *       *
# # *       *
# # *       *
# # * * * * *

# # # Pattern : Hollow Rectangle of n x n matrix with numbers
# num1 = int(input("Enter the number of rows: "))
# num2 = int(input("Enter the number of columns: "))
# for i in range(num1):
#     for j in range(num2):
#         if i == 0 or i == num1 - 1 or j == 0 or j == num2 - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# Enter the number of columns: 10
# * * * * * * * * * * * *
# *                     *
# *                     *
# *                     *
# * * * * * * * * * * * *

# # Pattern : Hollow Square of n x n matrix with diagonals
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if i == 0 or i == num - 1 or j == 0 or j == num - 1 or i == j or i + j == num - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# # * * * * *
# # * *   * *
# # *   *   *
# # * *   * *
# # * * * * * 

# # Pattern: Make 'A' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         # if i == 0 and j != 0 and j != num-1:
#         #     print("*", end=" ")
#         # elif i == num // 2:
#         #     print("*", end=" ")
#         # elif i > 0 and (j == 0 or j == num-1):
#         #     print("*", end=" ")
#         # else:
#         #     print(" ", end=" ")
#         if (i == 0 and j != 0 and j != num-1) or (i == num // 2) or (i > 0 and (j == 0 or j == num-1)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# #   * * *  
# # *       *
# # * * * * *
# # *       *
# # *       *

# # Pattern : Make 'B' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if j == 0 or (i == 0 and j < num-1) or (i == num // 2 and j < num-1) or (i == num-1 and j < num-1) or (j == num-1 and (i != 0 and i != num // 2 and i != num - 1)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# # * * * * 
# # *       *
# # * * * * 
# # *       *
# # * * * * 

# # Pattern : Make 'C' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0 and j != num-1) or (i == num-1 and j != num-1) or (j == 0 and i != 0 and i != num-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output: 
# # Enter the number of rows: 5
# # * * * *
# # *
# # *
# # *
# # * * * *

# # Pattern : Make 'D' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if j == 0 or (i == 0 and j < num-1) or (i == num-1 and j < num-1) or (j == num-1 and (i != 0 and i != num - 1)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# # Enter the number of rows: 5
# # * * * *
# # *       *
# # *       *
# # *       *
# # * * * *

# Pattern : Make 'E' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0 and j != num) or (i == num // 2 and j < (num // 2) + 1) or (i == num-1 and j != num) or (j == 0):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
# Output:
# Enter the number of rows: 5
# * * * * *
# *
# * * * 
# *
# * * * * *

# Pattern : Make 'F' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0 and j != num) or (i == num // 2 and j < (num // 2) + 1) or (j == 0):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# * * * * *
# *
# * * * 
# *
# *

# Pattern : Make 'G' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0 and j != num) or (i == num-1 and j != num-1) or (j == 0 and i != 0 and i != num-1) or (i == num // 2 and j >= num//2) or (j == num-1 and i >= num // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # Output:
# Enter the number of rows: 5

# Pattern : Make 'H' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (j == 0 or j == num-1) or (i == num // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# *       *
# *       *
# * * * * *
# *       *
# *       *

# Pattern : Make 'I' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0 or i == num-1) or (j == num // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# * * * * *
#     *
#     *
#     *
# * * * * *

# # Pattern : Make 'J' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0) or (i == num-1 and j <= num // 2) or (j == num // 2 ) or (j == 0 and i > num // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# * * * * *
#     *
#     *
# *   *
# * * *

# # Pattern : Make 'K' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         # if (j == 0) or (i + j == num // 2 + 1) or (i - j == num // 2 - 1):
#         if (j == 0) or (i + j == num // 2 ) or (i - j == num // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# *   *
# * *
# *
# * *
# *   *

# # Pattern : Make 'L' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (j == 0) or (i == num-1 and j <= num // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# *
# *
# *
# *
# * * * * *

# Pattern : Make 'M' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (j == 0 or j == num-1) or (i == j and i <= num // 2) or (i + j == num - 1 and i <= num // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# *       *
# * *   * *
# *   *   *
# *       *
# *       *

# Pattern : Make 'N' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (j == 0 or j == num-1) or (i == j):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# *       *
# * *     *
# *   *   *
# *     * *
# *       *

# # # Pattern : Make 'O' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0 and j != num-1 and j != 0) or (i == num-1 and j != num-1 and j != 0) or (j == 0 and i != 0 and i != num-1) or (j == num-1 and i != 0 and i != num-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
#   * * * 
# *       *
# *       *
# *       *
#   * * * 

# Pattern : Make 'P' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (j == 0) or (i == 0 and j < num-1) or (i == num // 2 and j < num-1) or (j == num-1 and (i != 0 and i != num // 2 and i < num//2)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# * * * *
# *       *
# * * * *
# *
# *

# Pattern : Make 'Q' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0 and j != num-1 and j != 0) or (i == num-1 and j != num-1 and j != 0) or (j == 0 and i != 0 and i != num-1) or (j == num-1 and i != 0 and i != num-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# Pattern : Make 'R' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (j == 0) or (i == 0 and j < num-1) or (i == num // 2 and j < num-1) or (j == num-1 and (i != 0 and i != num // 2)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# * * * *
# *       *
# * * * *
# *       *
# *       *

# Pattern : Make 'S' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0 or i == num-1 or i == num//2) or (j == 0 and i <= num//2) or (j == num-1 and i >= num//2) :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# * * * * *
# *
# * * * * *
#         *
# * * * * *

# Pattern : Make 'T' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0) or (j == num // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:   
# Enter the number of rows: 5
# * * * * *
#     *
#     *
#     *
#     *

# Pattern : Make 'U' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (j == 0 or j == num-1) or (i == num-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# *       * 
# *       *
# *       *
# *       *
# * * * * *

# Pattern : Make 'V' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num - 1):
#     for j in range(2 * num - 1):
#         if j == i or j == (2 * num - 2) - i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# print(" " * (2 * (num - 1)) + "*")

# Pattern : Make 'W' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (j == 0 or j == num-1) or (i == j and i >= num // 2) or (i + j == num - 1 and i >= num // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# *       *
# *       *
# *   *   *
# * *   * *
# *       *

# # Pattern : Make 'X' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if i == j or i + j == num - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# *       *
#   *   *
#     *
#   *   *
# *       *

# # Pattern : Make 'Y' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (j == i and i <= num // 2) or (j == num - i - 1 and i <= num // 2) or (j == num//2 and i > num // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# *       *
#   *   *
#     *
#     *
#     *

# Pattern : Make 'Z' using stars
# num = int(input("Enter the number of rows: "))
# for i in range(num):
#     for j in range(num):
#         if (i == 0 or i == num-1) or (i + j == num - 1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Output:
# Enter the number of rows: 5
# * * * * *
#       *
#     *
#   *
# * * * * *