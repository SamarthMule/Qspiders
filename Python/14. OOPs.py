# Class
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# Objects are instances of classes. They are created from the class blueprint and can have their own unique values for the attributes defined in the class.
# In Python, classes are defined using the class keyword followed by the class name and a colon. The class body contains the attributes and methods of the class.

# class Sam:
#     a = 10  # class variable
#     b = 20  # class variable

# object1 = Sam()  # object of class Sam
# object2 = Sam()  # object of class Sam

# print(Sam.a, Sam.b)  # accessing class variable using class name
# print(object1.a, object1.b)  # accessing class variable using object
# print(object2.a, object2.b)  # accessing class variable using object

# Sam.a = 100  # changing class variable using class name
# print(Sam.a, Sam.b)  # accessing class variable using class name
# print(object1.a, object1.b)  # accessing class variable using object
# print(object2.a, object2.b)  # accessing class variable using object

# object1.b = 200  # changing class variable using object
# object1.a = 1000  # changing class variable using object
# print(Sam.a, Sam.b)  # accessing class variable using class name
# print(object1.a, object1.b)  # accessing class variable using object
# print(object2.a, object2.b)  # accessing class variable using object

# object2.a = 300  # changing class variable using object
# object2.b = 400  # changing class variable using object
# print(Sam.a, Sam.b)  # accessing class variable using class name
# print(object1.a, object1.b)  # accessing class variable using object
# print(object2.a, object2.b)  # accessing class variable using object

# # Example of class and object
# class SBI_Bank:
#     bankname = "State Bank India"
#     location = "Pune"
#     interest_rate = 5.0
#     mobile_number = 9912345678
#     website = "www.sbi.com"

# print(SBI_Bank.bankname, SBI_Bank.location, SBI_Bank.interest_rate, SBI_Bank.mobile_number, SBI_Bank.website)  

# customer1 = SBI_Bank() 
# customer1.location = "Mumbai" 
# customer1.interest_rate = 6.0 
# customer2 = SBI_Bank() 
# customer2.location = "Delhi" 
# customer2.interest_rate = 7.0 

# print(customer1.bankname, customer1.location, customer1.interest_rate, customer1.mobile_number, customer1.website) 
# print(customer2.bankname, customer2.location, customer2.interest_rate, customer2.mobile_number, customer2.website)

# SBI_Bank.bankname = "State Bank of India"
# SBI_Bank.mobile_number = 9912345679
# SBI_Bank.website = "www.sbi.co.in"
# print(SBI_Bank.bankname, SBI_Bank.location, SBI_Bank.interest_rate, SBI_Bank.mobile_number, SBI_Bank.website)  
# print(customer1.bankname, customer1.location, customer1.interest_rate, customer1.mobile_number, customer1.website) 
# print(customer2.bankname, customer2.location, customer2.interest_rate, customer2.mobile_number, customer2.website)  

# customer3 = SBI_Bank()
# customer3.location = "Chennai"
# customer3.interest_rate = 8.0
# print(customer3.bankname, customer3.location, customer3.interest_rate, customer3.mobile_number, customer3.website)


# # WAP to Create a Class called "Bank" with 4 class members and 10 object consists of 7 object members
# class Bank:
#     bank_name = "Bank of Maharashtra"
#     location = "Pune"
#     interest_rate = 5.5
#     phone_number = 1234567890

# print(Bank.bank_name, Bank.location, Bank.interest_rate, Bank.phone_number)

# customer1 = Bank()
# customer1.customer_name = "Aashish Kumar"
# customer1.account_number = 1001
# customer1.balance = 5000.0
# customer1.account_type = "Savings"
# customer1.email = "aashish1kumar@example.com"
# customer1.mobile_number = 9876543210
# customer1.address = "Lakshaman Nagar, Pune"

# print(customer1.customer_name, customer1.account_number, customer1.balance, customer1.account_type, customer1.email, customer1.mobile_number, customer1.address)

# customer2 = Bank()
# customer2.customer_name = "Virat Patil"
# customer2.account_number = 1002
# customer2.balance = 10000.0
# customer2.account_type = "Current"
# customer2.email = "viratpatil@example.com"
# customer2.mobile_number = 9876543211
# customer2.address = "Shivaji Nagar, Pune"
# print(customer2.customer_name, customer2.account_number, customer2.balance, customer2.account_type, customer2.email, customer2.mobile_number, customer2.address)

# customer3 = Bank()
# customer3.customer_name = "Rohit Joshi"
# customer3.account_number = 1003
# customer3.balance = 15000.0
# customer3.account_type = "Savings"
# customer3.email = "rohit.joshi@example.com"
# customer3.mobile_number = 9876543212
# customer3.address = "Kothrud, Pune"
# print(customer3.customer_name, customer3.account_number, customer3.balance, customer3.account_type, customer3.email, customer3.mobile_number, customer3.address)

# customer4 = Bank()
# customer4.customer_name = "Aaush Deshmukh"
# customer4.account_number = 1004
# customer4.balance = 20000.0
# customer4.account_type = "Current"
# customer4.email = "aaush@example.com"
# customer4.mobile_number = 9876543213
# customer4.address = "Viman Nagar, Pune"
# print(customer4.customer_name, customer4.account_number, customer4.balance, customer4.account_type, customer4.email, customer4.mobile_number, customer4.address)

# customer5 = Bank()
# customer5.customer_name = "Siddharth Jadhav"
# customer5.account_number = 1005
# customer5.balance = 25000.0
# customer5.account_type = "Savings"
# customer5.email = "jadhavS@example.com"
# customer5.mobile_number = 9876543214
# customer5.address = "Wakad, Pune"
# print(customer5.customer_name, customer5.account_number, customer5.balance, customer5.account_type, customer5.email, customer5.mobile_number, customer5.address)

# customer6 = Bank()
# customer6.customer_name = "Ajinkya Rane"
# customer6.account_number = 1006
# customer6.balance = 30000.0
# customer6.account_type = "Current"
# customer6.email = "AjinkyaRane@example.com"
# customer6.mobile_number = 9876543215
# customer6.address = "Baner, Pune"
# print(customer6.customer_name, customer6.account_number, customer6.balance, customer6.account_type, customer6.email, customer6.mobile_number, customer6.address)

# customer7 = Bank()
# customer7.customer_name = "Shivam Deshmukh"
# customer7.account_number = 1007
# customer7.balance = 35000.0
# customer7.account_type = "Savings"
# customer7.email = "Deshmukh@example.com"
# customer7.mobile_number = 9876543216
# customer7.address = "Aundh, Pune"
# print(customer7.customer_name, customer7.account_number, customer7.balance, customer7.account_type, customer7.email, customer7.mobile_number, customer7.address)

# customer8 = Bank()
# customer8.customer_name = "Nikhil Lokhande"
# customer8.account_number = 1008
# customer8.balance = 40000.0
# customer8.account_type = "Current"
# customer8.email = "nikhil.lokhande@example.com"
# customer8.mobile_number = 9876543217
# customer8.address = "Hadapsar, Pune"
# print(customer8.customer_name, customer8.account_number, customer8.balance, customer8.account_type, customer8.email, customer8.mobile_number, customer8.address)

# customer9 = Bank()
# customer9.customer_name = "Vishal Kadam"
# customer9.account_number = 1009
# customer9.balance = 45000.0
# customer9.account_type = "Savings"
# customer9.email = "Kadam1@example.com"
# customer9.mobile_number = 9876543218
# customer9.address = "Kharadi, Pune"
# print(customer9.customer_name, customer9.account_number, customer9.balance, customer9.account_type, customer9.email, customer9.mobile_number, customer9.address)

# customer10 = Bank()
# customer10.customer_name = "Bhushan Kale"
# customer10.account_number = 1010
# customer10.balance = 50000.0
# customer10.account_type = "Current"
# customer10.email = "BhushanKale@example.com"
# customer10.mobile_number = 9876543219
# customer10.address = "Pimple Saudagar, Pune"
# print(customer10.customer_name, customer10.account_number, customer10.balance, customer10.account_type, customer10.email, customer10.mobile_number, customer10.address)

# WAP to Create a Class called "School" with 5 class members and 5 object consists of 5 object members
# class School:
#     school_name = "XYZ High School"
#     location = "Pune"
#     principal_name = "Mr. Sharma"
#     contact_number = 1234567890
#     website = "www.xyzhighschool.com"


# def to_in(obj, name, roll_number, grade, email, mobile_number, address):
#     obj.name = name
#     obj.roll_number = roll_number
#     obj.grade = grade
#     obj.email = email
#     obj.mobile_number = mobile_number
#     obj.address = address
    
# def to_out(obj):
#     print("\nSchool Details:\n")
#     print("School Name:", obj.school_name)
#     print("Location:", obj.location)
#     print("Principal Name:", obj.principal_name)
#     print("Contact Number:", obj.contact_number)
#     print("Website:", obj.website)
    
#     print("\nStudent Details:\n")
#     print("Name:", obj.name)
#     print("Roll Number:", obj.roll_number)
#     print("Grade:", obj.grade)
#     print("Email:", obj.email)
#     print("Mobile Number:", obj.mobile_number)
#     print("Address:", obj.address)

# # print(School.school_name, School.location, School.principal_name, School.contact_number, School.website)
# student1 = School()
# to_in(student1, "John Doe", 1, "10th", "john.doe@example.com", 9876543210, "Main Street, Pune")
# # print(student1.name, student1.roll_number, student1.grade, student1.email, student1.mobile_number, student1.address)
# to_out(student1)

# student2 = School()
# to_in(student2, "Jane Smith", 2, "9th", "jane.smith@example.com", 9876543211, "Second Street, Pune")
# # print(student2.name, student2.roll_number, student2.grade, student2.email, student2.mobile_number, student2.address)
# to_out(student2)

# student3 = School()
# to_in(student3, "Amit Patil", 3, "8th", "amit.patil@example.com", 9876543212, "Third Street, Pune")
# # print(student3.name, student3.roll_number, student3.grade, student3.email, student3.mobile_number, student3.address)
# to_out(student3)

# student4 = School()
# to_in(student4, "Harman Joshi", 4, "7th", "harmanjoshi@example.com", 9876543213, "Fourth Street, Pune")
# # print(student4.name, student4.roll_number, student4.grade, student4.email, student4.mobile_number, student4.address)
# to_out(student4)

# student5 = School()
# to_in(student5, "Raj Deshmukh", 5, "6th", "riyadeshmukh@example.com", 9876543214, "Fifth Street, Pune")
# # print(student5.name, student5.roll_number, student5.grade, student5.email, student5.mobile_number, student5.address)
# to_out(student5)

# class School:
#     school_name = "XYZ High School"
#     location = "Pune"
#     principal_name = "Mr. Sharma"
#     contact_number = 1234567890
#     website = "www.xyzhighschool.com"

#     def to_in(obj, name, roll_number, grade, email, mobile_number, address):
#         obj.name = name
#         obj.roll_number = roll_number
#         obj.grade = grade
#         obj.email = email
#         obj.mobile_number = mobile_number
#         obj.address = address
    
#     def to_out(obj):
#         print("\nSchool Details:\n")
#         print("School Name:", obj.school_name)
#         print("Location:", obj.location)
#         print("Principal Name:", obj.principal_name)
#         print("Contact Number:", obj.contact_number)
#         print("Website:", obj.website)
        
#         print("\nStudent Details:\n")
#         print("Name:", obj.name)
#         print("Roll Number:", obj.roll_number)
#         print("Grade:", obj.grade)
#         print("Email:", obj.email)
#         print("Mobile Number:", obj.mobile_number)
#         print("Address:", obj.address)
        
# student1 = School()
# School.to_in(student1, "John Doe", 1, "10th", "john.doe@example.com", 9876543210, "Main Street, Pune")
# School.to_out(student1)

# student1 = School()
# School.to_in(student1, "Jane Smith", 2, "9th", "jane.smith@example.com", 9876543211, "Second Street, Pune")
# School.to_out(student1)

# Constructors/ __init__ method / initization method
# The __init__ method is a special method in Python classes. It is called when an object of the class is created. It allows you to initialize the attributes of the object with specific values.
# The __init__ method is defined using the def keyword, just like any other method. It takes self as the first parameter, which refers to the instance of the class being created. You can also pass additional parameters to the __init__ method to initialize the attributes of the object.
# The __init__ method is not mandatory in a class. If you do not define it, Python will provide a default constructor that does nothing.
# However, if you want to initialize the attributes of the object with specific values, you need to define the __init__ method.
# The __init__ method is called automatically when an object of the class is created. You do not need to call it explicitly.
# The __init__ method can also have default values for its parameters. This allows you to create objects with default values for the attributes if you do not provide specific values when creating the object.
# The __init__ method can also be used to perform any setup or initialization tasks that are required when an object is created.
# This can include opening files, connecting to databases, or any other tasks that need to be done when the object is created.
# The __init__ method can also raise exceptions if there are any errors during the initialization process. This allows you to handle errors gracefully and provide meaningful error messages to the user.


# class Bank:
#     bank_name = "Bank of Maharashtra"
#     location = "Pune"
#     interest_rate = 5.5
#     phone_number = 1234567890

#     def __init__(self, customer_name, account_number, balance, account_type, email, mobile_number, address):
#         self.customer_name = customer_name
#         self.account_number = account_number
#         self.balance = balance
#         self.account_type = account_type
#         self.email = email
#         self.mobile_number = mobile_number
#         self.address = address

#     def display_details(self):
#         print("\nBank Details:\n")
#         print("Bank Name:", Bank.bank_name)
#         print("Location:", Bank.location)
#         print("Interest Rate:", Bank.interest_rate)
#         print("Phone Number:", Bank.phone_number)

#         print("\nCustomer Details:\n")
#         print("Customer Name:", self.customer_name)
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)
#         print("Account Type:", self.account_type)
#         print("Email:", self.email)
#         print("Mobile Number:", self.mobile_number)
#         print("Address:", self.address)

# customer1 = Bank("Aashish Kumar", 1001, 5000.0, "Savings", "aashish.kumar@example.com", 9876543210, "123 Main St, Pune")
# customer1.display_details()

# customer2 = Bank("Virat Patil", 1002, 10000.0, "Current", "virat.patil@example.com", 9876543211, "456 Second St, Pune")
# customer2.display_details()

# customer3 = Bank("Rohit Joshi", 1003, 15000.0, "Savings", "rohit.joshi@example.com", 9876543212, "789 Third St, Pune")
# customer3.display_details()

# Destructor / __del__ method
# The __del__ method is a special method in Python classes. It is called when an object of the class is about to be destroyed. It allows you to perform any cleanup tasks that are required before the object is removed from memory.
# The __del__ method is defined using the def keyword, just like any other method. It takes self as the first parameter, which refers to the instance of the class being destroyed. You can also pass additional parameters to the __del__ method if needed.
# The __del__ method is not mandatory in a class. If you do not define it, Python will provide a default destructor that does nothing.
# However, if you want to perform cleanup tasks when an object is destroyed, you need to define the __del__ method.
# The __del__ method is called automatically when an object of the class is destroyed. You do not need to call it explicitly.
# The __del__ method can also raise exceptions if there are any errors during the cleanup process. This allows you to handle errors gracefully and provide meaningful error messages to the user.
# The __del__ method can also be used to close files, release resources, or perform any other cleanup tasks that are required when the object is destroyed.
# This can include closing database connections, releasing memory, or any other tasks that need to be done when the object is destroyed.
# The __del__ method is called when the reference count of the object reaches zero. This means that there are no more references to the object in the program, and it can be safely destroyed.
# The __del__ method can also be used to perform any final tasks that need to be done before the object is destroyed. This can include logging messages, sending notifications, or any other tasks that need to be done before the object is removed from memory.
# The __del__ method can also be used to perform any final cleanup tasks that are required when the object is destroyed. This can include closing files, releasing resources, or performing any other cleanup tasks that are required when the object is destroyed.

# class Bank:
#     bank_name = "Bank of Maharashtra"
#     location = "Pune"
#     interest_rate = 5.5
#     phone_number = 1234567890

#     def __init__(self, customer_name, account_number, balance, account_type, email, mobile_number, address):
#         self.customer_name = customer_name
#         self.account_number = account_number
#         self.balance = balance
#         self.account_type = account_type
#         self.email = email
#         self.mobile_number = mobile_number
#         self.address = address

#     def display_details(self):
#         print("\nBank Details:\n")
#         print("Bank Name:", Bank.bank_name)
#         print("Location:", Bank.location)
#         print("Interest Rate:", Bank.interest_rate)
#         print("Phone Number:", Bank.phone_number)

#         print("\nCustomer Details:\n")
#         print("Customer Name:", self.customer_name)
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)
#         print("Account Type:", self.account_type)
#         print("Email:", self.email)
#         print("Mobile Number:", self.mobile_number)
#         print("Address:", self.address)

#     def __del__(self):
#         print(f"Destructor called for {self.customer_name}. Object is being destroyed.")

# customer1 = Bank("Aashish Kumar", 1001, 5000.0, "Savings", "aashish.kumar@example.com", 9876543210, "123 Main St, Pune")
# customer1.display_details()
# print(customer1)  # Accessing the customer name before deletion
# del customer1  # Explicitly deleting the object to call the destructor
# print(customer1.customer_name)  # This will raise an error because customer1 is deleted
# customer1.display_details()  # This will raise an error because customer1 is deleted

# Type of Methods in Python
# 1. Object Method
# 2. Class Method
# 3. Static Method

# 1. Object Method
# Object methods are the most common type of methods in Python classes. They are defined using the def keyword and take self as the first parameter. The self parameter refers to the instance of the class that is calling the method. Object methods can access and modify the attributes of the object they belong to. They can also call other object methods within the same class.
# Object methods are used to perform operations on the object and can be called using the object name followed by the method name and parentheses. They can also take additional parameters if needed.
# Object methods can return values or perform actions without returning anything. They are typically used to implement the behavior of the object and define how it interacts with other objects and the outside world.
# Object methods can also raise exceptions if there are any errors during the execution of the method. This allows you to handle errors gracefully and provide meaningful error messages to the user.

# class Bank:
#     bank_name = "Bank of Maharashtra"
#     location = "Pune"
#     interest_rate = 5.5
#     phone_number = 1234567890

#     # Constructor / __init__ method
#     def __init__(self, customer_name, account_number, balance, account_type, email, mobile_number, address):
#         self.customer_name = customer_name
#         self.account_number = account_number
#         self.balance = balance
#         self.account_type = account_type
#         self.email = email
#         self.mobile_number = mobile_number
#         self.address = address

#     # Object Method
#     def display_details(self):
#         print("\nCustomer Details:\n")
#         print("Customer Name:", self.customer_name)
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)
#         print("Account Type:", self.account_type)
#         print("Email:", self.email)
#         print("Mobile Number:", self.mobile_number)
#         print("Address:", self.address)

# customer1 = Bank("Aashish Kumar", 1001, 5000.0, "Savings", "aashish.kumar@example.com", 9876543210, "123 Main St, Pune")
# customer2 = Bank("Virat Patil", 1002, 10000.0, "Current", "virat.patil@example.com", 9876543211, "456 Second St, Pune")

# Bank.display_details(customer1) # Calling the class method to display customer details using the class name
# customer1.display_details()  # Calling the object method to display customer details using the object name

# customer2.display_details()


# 2. Class Method
# Class methods are methods that are bound to the class and not the instance of the class. They are defined using the @classmethod decorator and take cls as the first parameter. The cls parameter refers to the class itself, not the instance of the class. Class methods can access and modify class variables but cannot access instance variables directly.
# Class methods are typically used for factory methods, which are methods that return an instance of the class. They can also be used to perform operations that are related to the class itself rather than to a specific instance of the class.
# Class methods can be called using the class name or the instance of the class. They can also take additional parameters if needed.
# Class methods can return values or perform actions without returning anything. They are typically used to implement operations that are related to the class itself and define how it interacts with other classes and the outside world.
# Class methods can also raise exceptions if there are any errors during the execution of the method. This allows you to handle errors gracefully and provide meaningful error messages to the user.
# Class methods can also be used to create alternative constructors for the class. This allows you to create instances of the class using different sets of parameters or from different data sources.
# Class methods can also be used to implement class-level operations that are not specific to any instance of the class. This allows you to define operations that are related to the class itself and not to any specific instance of the class.

# class Bank:
#     bank_name = "Bank of Maharashtra"
#     location = "Pune"
#     interest_rate = 5.5
#     phone_number = 1234567890

#     # Constructor / __init__ method
#     def __init__(self, customer_name, account_number, balance, account_type, email, mobile_number, address):
#         self.customer_name = customer_name
#         self.account_number = account_number
#         self.balance = balance
#         self.account_type = account_type
#         self.email = email
#         self.mobile_number = mobile_number
#         self.address = address

#     # Class Method
#     @classmethod
#     def display_class_details(cls):
#         print("\nBank Details:\n")
#         print("Bank Name:", cls.bank_name)
#         print("Location:", cls.location)
#         print("Interest Rate:", cls.interest_rate)
#         print("Phone Number:", cls.phone_number)
    
#     @classmethod
#     def update_location(cls, new_location):
#         cls.location = new_location
#         print(f"Location updated to: {cls.location}")
    

# customer3 = Bank("Rohit Joshi", 1003, 15000.0, "Savings", "rohit.joshi@example.com", 9876543212, "789 Third St, Pune")
# customer4 = Bank("Aaush Deshmukh", 1004, 20000.0, "Current", "aaush.deshmukh@example.com", 9876543213, "101 Fourth St, Pune")

# customer3.display_class_details()  # Calling the class method to display bank details using the object name
# Bank.display_class_details()  # Calling the class method to display bank details using the class name

# Bank.location = "Mumbai"  # Changing the class variable using the class name
# Bank.display_class_details()  # Calling the class method to display bank details using the object name

# Bank.update_location("Delhi")  # Changing the class variable using the class method
# Bank.display_class_details()  # Calling the class method to display bank details using the class name

# class School:
#     School_name = "XYZ High School"
#     location = "Pune"
#     principal_name = "Mr. Sharma"
#     contact_number = 1234567890
#     website = "www.xyzhighschool.com"
    
#     def __init__(self, student_name, roll_number, grade, email, mobile_number, address):
#         self.student_name = student_name
#         self.roll_number = roll_number
#         self.grade = grade
#         self.email = email
#         self.mobile_number = mobile_number
#         self.address = address
    
#     def display_details(self):
#         print("\nStudent Details:\n")
#         print("Student Name:", self.student_name)
#         print("Roll Number:", self.roll_number)
#         print("Grade:", self.grade)
#         print("Email:", self.email)
#         print("Mobile Number:", self.mobile_number)
#         print("Address:", self.address)
    
#     @classmethod
#     def display_class_details(cls):
#         print("\nSchool Details:\n")
#         print("School Name:", cls.School_name)
#         print("Location:", cls.location)
#         print("Principal Name:", cls.principal_name)
#         print("Contact Number:", cls.contact_number)
#         print("Website:", cls.website)
    
#     @classmethod
#     def update_location(cls, new_location):
#         cls.location = new_location
#         print(f"Location updated to: {cls.location}")
    
#     @classmethod
#     def update_principal(cls, new_principal):
#         cls.principal_name = new_principal
#         print(f"Principal updated to: {cls.principal_name}")

# student1 = School("John Doe", 1, "10th", "john.doe@example.com", 9876543210, "123 Main St, Pune")
# student2 = School("Jane Smith", 2, "9th", "jane.smith@example.com", 9876543211, "456 Second St, Pune")
# student3 = School("Amit Patil", 3, "8th", "amit.patil@example.com", 9876543212, "789 Third St, Pune")

# School.display_class_details()
# student1.display_details() 

# student1.update_location("Mumbai")
# School.display_class_details()

# School.update_principal("Mrs. Gupta")
# School.display_class_details()


# 3. Static Method
# Static methods are methods that do not depend on the instance or class. They are defined using the @staticmethod decorator and do not take self or cls as the first parameter. Static methods cannot access or modify instance variables or class variables directly. They are typically used for utility functions that are related to the class but do not require access to instance or class variables.
# Static methods can be called using the class name or the instance of the class. They can also take additional parameters if needed.
# Static methods can return values or perform actions without returning anything. They are typically used to implement utility functions that are related to the class and do not require access to instance or class variables.
# Static methods can also raise exceptions if there are any errors during the execution of the method. This allows you to handle errors gracefully and provide meaningful error messages to the user.
# Static methods can also be used to implement utility functions that are related to the class but do not require access to instance or class variables. This allows you to define functions that are related to the class but do not depend on the instance or class itself.
# Static methods can also be used to implement functions that are related to the class but do not require access to instance or class variables. This allows you to define functions that are related to the class but do not depend on the instance or class itself.

class Bank:
    bank_name = "Bank of Maharashtra"
    location = "Pune"
    interest_rate = 5.5
    phone_number = 1234567890

    # Constructor / __init__ method
    def __init__(self, customer_name, account_number, balance, account_type, email, mobile_number, address):
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.email = email
        self.mobile_number = mobile_number
        self.address = address
    
    def display_details(self):
        print("\nCustomer Details:\n")
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Account Type:", self.account_type)
        print("Email:", self.email)
        print("Mobile Number:", self.mobile_number)
        print("Address:", self.address)
    
    @classmethod
    def display_class_details(cls):
        print("\nBank Details:\n")
        print("Bank Name:", cls.bank_name)
        print("Location:", cls.location)
        print("Interest Rate:", cls.interest_rate)
        print("Phone Number:", cls.phone_number)

    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"\nInterest rate updated to: {cls.interest_rate}")
    
    # @classmethod
    # def update_location(cls, new_location):
    #     cls.location = new_location
    #     print(f"Location updated to: {cls.location}")    
        
    # def update_address(self, new_address):
    #     self.address = new_address
    #     print(f"Address updated to: {self.address}")
    
    @classmethod
    def update_location(cls):
        cls.location = cls.get_loc_or_add() 
        print(f"\nLocation updated to: {cls.location}")
    
    def update_address(self):
        self.address = self.get_loc_or_add()
        print(f"\nAddress updated to: {self.address}")
        
    def deposit(self):
        amount = self.get_amount()
        self.balance += amount
        print(f"\nDeposited {amount}. New balance: {self.balance}")
        
    def withdraw(self):
        amount = self.get_amount()
        if amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrawn {amount}. New balance: {self.balance}")
        else:
            print("\nInsufficient balance.")
        
    @staticmethod
    def get_amount():
        return float(input("\nEnter the amount: "))
    
    # Static Method
    @staticmethod
    def calculate_interest(balance, rate, time):
        interest = (balance * rate * time) / 100
        return interest
    
    @staticmethod
    def get_loc_or_add():
        return input("\nEnter the location/address: ")


customer1 = Bank("Aashish Kumar", 1001, 5000.0, "Savings", "aashish.kumar@example.com", 9876543210, "123 Main St, Pune")
customer2 = Bank("Virat Patil", 1002, 10000.0, "Current", "virat.patil@example.com", 9876543211, "456 Second St, Pune")

customer2.display_details()
customer1.display_details()

Bank.display_class_details()

customer1.update_interest_rate(6.0)
Bank.display_class_details()

# Bank.update_location("Mumbai")
# Bank.display_class_details()

# customer2.update_address("789 New Address, Pune")
# customer2.display_details()

print("Calculating Interest:" , Bank.calculate_interest(10000, 5.5, 2))  # Static method call using class name
print("Calculating Interest:" , customer1.calculate_interest(20000, 6.0, 3))  # Static method call using object name

Bank.update_location()
Bank.display_class_details()

customer1.update_address()
customer1.display_details()

customer1.deposit()
customer1.display_details()

customer1.withdraw()
customer1.display_details()