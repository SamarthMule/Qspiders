# Polymorphism
# Polymorphism is the ability of different objects to respond to the same method call in different ways.
# It allows for flexibility and reusability in code, as the same method can be used with different objects without needing to know their specific types.
# In Python, polymorphism can be achieved through method overriding and duck typing.
# Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class.
# Duck typing is a concept where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type.
# This means that if an object behaves like a certain type (i.e., it has the required methods and properties), it can be treated as that type, regardless of its actual class.
# This allows for more flexible and dynamic code, as objects can be used interchangeably as long as they implement the required methods.
# Polymorphism is a powerful feature of object-oriented programming that allows for code reuse and the creation of flexible and dynamic systems.
# It is important to use polymorphism judiciously, as it can lead to complex and hard-to-maintain code if overused.

# Types of Polymorphism
# 1. Compile-time Polymorphism (Method Overloading): The same method name can be used with different parameters or argument types.
#    This is not supported in Python, as Python does not support method overloading in the same way as some other languages (e.g., Java, C++).
# 2. Runtime Polymorphism (Method Overriding): A child class can provide a specific implementation of a method that is already defined in its parent class.
#    This allows for different behaviors based on the object type at runtime.
# 3. Duck Typing: The type or class of an object is determined by its behavior (methods and properties) rather than its explicit type.
#    This means that if an object behaves like a certain type (i.e., it has the required methods and properties), it can be treated as that type, regardless of its actual class.
#    This allows for more flexible and dynamic code, as objects can be used interchangeably as long as they implement the required methods.
#    Duck typing is a key feature of Python and is widely used in Python programming.

# 4. Operator Overloading: The ability to define custom behavior for operators (e.g., +, -, *, /) for user-defined classes.
#    This allows for more intuitive and natural use of objects in expressions and calculations.
# #    Operator overloading is achieved by defining special methods (also known as magic methods or dunder methods) in the class.
#    These methods have names that start and end with double underscores (e.g., __add__, __sub__, __mul__, __truediv__).
#    By defining these methods, we can specify how the operators should behave when applied to instances of the class.
#    This allows for more intuitive and natural use of objects in expressions and calculations.
#    Operator overloading is a powerful feature of Python that allows for more expressive and readable code.
#    It is important to use operator overloading judiciously, as it can lead to complex and hard-to-maintain code if overused.



# # Method Overriding
# def sam():
#     print("Method Overriding")

# def sam(a, b):
#     # print("Method Overriding")
#     print(a + b)

# def sam(a, b, c):
#     # print("Method Overriding")
#     print(a + b + c)
    
# sam() # sam() missing 3 required positional arguments: 'a', 'b', and 'c' 
# sam(1, 2) # sam() missing 1 required positional argument: 'c'
# sam(1, 2, 3)

# Monkey Patching
# Monkey patching is a technique to modify or extend the behavior of libraries or classes at runtime.
# It allows developers to change the behavior of existing code without modifying the original source code.
# This can be useful for fixing bugs, adding new features, or changing the behavior of third-party libraries.
# However, monkey patching can lead to code that is difficult to understand and maintain, as it can introduce unexpected behavior and make it harder to track changes.
# It is important to use monkey patching judiciously and to document any changes made to the original code.

# def sample():
#     print("Method Overriding")
# a = sample

# def sample(a,b):
#     print(a + b)
# b = sample

# def sample(a,b,c):
#     print(a + b + c)
# c = sample

# print(a, "\t", id(a)) # <function sample at 0x7f8c1c3e2d30> 0x7f8c1c3e2d30
# print(b, "\t", id(b)) # <function sample at 0x7f8c1c3e2d30> 0x7f8c1c3e2d30
# print(c, "\t", id(c)) # <function sample at 0x7f8c1c3e2d30> 0x7f8c1c3e2d30
# print(sample, "\t", id(sample)) # <function sample at 0x7f8c1c3e2d30> 0x7f8c1c3e2d30
# a() # Method Overriding
# b(5,4) # 9
# c(5,4,3) # 12

# l = len
# print(l) # <built-in function len> 0x7f8c1c3e2d30
# print(l("Hello")) # 5


# class AB:
#     def __init__(self, value):
#         self.value = value
    
# obj1 = AB(10)
# obj2 = AB(20)
# print(obj1 + obj2) # TypeError: unsupported operand type(s) for +: 'A' and 'A'

# Magic Methods
# Magic methods (also known as dunder methods) are special methods in Python that have names starting and ending with double underscores (e.g., __init__, __str__, __add__).
# They allow developers to define custom behavior for built-in operations (e.g., addition, subtraction, string representation) for user-defined classes.
# Magic methods are a powerful feature of Python that allows for more expressive and readable code.

class A:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return self.value + other.value
    
    def __truediv__(self, other):
        return self.value / other.value
    
    def __mul__(self, other):
        return self.value * other.value
    
    def __sub__(self, other):
        return self.value - other.value
    
    def __floordiv__(self, other):
        return self.value // other.value
    
    def __mod__(self, other):
        return self.value % other.value
    
    def __pow__(self, other):
        return self.value ** other.value

object1 = A(50)
object2 = A(20)
print(object1 + object2) # 70
print(object1 - object2) # 30
print(object1 * object2) # 1000
print(object1 / object2) # 2.5
print(object1 // object2) # 2
print(object1 % object2) # 10
print(object1 ** object2) # 953674316406250


# class B:
#     def __init__(self, l):
#         self.l = l

# obj1 = B([1, 2, 3])
# print(len(obj1)) # TypeError: object of type 'B' has no len()

class B:
    def __init__(self, l):
        self.l = l
    
    def __len__(self):
        return len(self.l)

obj2 = B([1, 2, 3])
print(len(obj2)) # 3

# Create a class Arithmetic with methods for addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.
# Create a class Bitwise with methods for bitwise AND, OR, XOR, NOT, left shift, and right shift.
# Create a class Collection with methods for lenght , getitem, setitem, delitem, and iter.