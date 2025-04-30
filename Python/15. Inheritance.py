# Inheritance
# Inheritance is a way to form new classes using classes that have already been defined.
# The new class is a specialized version of the old class, and it inherits all the attributes and methods of the old class.
# The old class is called the base class or parent class, and the new class is called the derived class or child class.
# Inheritance allows us to reuse code and create a hierarchy of classes.
# In Python, inheritance is implemented by passing the parent class as an argument to the child class definition.
# The child class can override methods of the parent class and add new methods and attributes.
# The child class can also call methods of the parent class using the super() function.
# Inheritance is a powerful feature of object-oriented programming that allows for code reuse and the creation of complex data structures.
# It is important to use inheritance judiciously, as it can lead to complex and hard-to-maintain code if overused.

# Types of Inheritance
# 1. Single Inheritance: A child class inherits from a single parent class.
# 2. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
# 3. Multiple Inheritance: A child class inherits from multiple parent classes.
# 4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
# 5. Hybrid Inheritance: A combination of two or more types of inheritance.

# 1. Single Inheritance
class Bank:
    name = "Bank Of Maharashtra"
    location = "Pune"
    
    def __init__(self, balance, phone, account_number):
        self.account_number = account_number
        self.balance = balance
        self.phone = phone
    
    def display_info(self):
        print(f"\nAccount Number: {self.account_number}, Balance: {self.balance}, Phone: {self.phone}", end=" ")
    
    @classmethod
    def display_class_info(cls):
        print(f"\nBank Name: {cls.name}, Location: {cls.location}", end=" ")


Bank.display_class_info()
customer1 = Bank(1000, 1234567890, 101)
customer1.display_info()

class Bank_update(Bank):
    IFSC_code = "BOMH0001234"
    
    def __init__(self, balance, phone, account_number, email, aadhar, pan):
        super().__init__(balance, phone, account_number)
        self.email = email
        self.aadhar = aadhar
        self.pan = pan

    def display_info(self):
        super().display_info()
        print(f"Email: {self.email}, Aadhar: {self.aadhar}, PAN: {self.pan}") 
    
    @classmethod
    def display_class_info(cls):
        super().display_class_info()
        print(f"IFSC Code: {cls.IFSC_code}")

Bank_update.display_class_info()
customer2 = Bank_update(2000, 9876543210, 102, "example@example.com", "1234-5678-9012", "ABCDE1234F")
customer2.display_info()

