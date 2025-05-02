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

# 2. Multilevel Inheritance
# Multiple Inheritance : result10th -> result12th, result12th -> result_graduation
class Result10th:
    def __init__(self, roll_number, name, marks10th):
        self.roll_number = roll_number
        self.name = name
        self.marks10th = marks10th
    
    def display_info(self):
        print(f"\nRoll Number: {self.roll_number}, Name: {self.name}, Marks10th: {self.marks10th}", end=" ")
        
class Result12th(Result10th):
    def __init__(self, roll_number, name, marks10th,marks12th, stream):
        super().__init__(roll_number, name, marks10th, marks12th)
        self.stream = stream
        self.marks12th = marks12th

    def display_info(self):
        super().display_info()
        print(f", Marks12th: {self.marks12th}, Stream: {self.stream}", end=" ")

    
class ResultGraduation(Result12th):
    def __init__(self, roll_number, name, marks10th, marks12th, stream, degree, degree_marks):
        super().__init__(roll_number, name, marks10th, marks12th, stream, degree_marks)
        self.degree = degree
        self.degree_marks = degree_marks
        

    def display_info(self):
        super().display_info()
        print(f", Degree: {self.degree}, Degree Marks: {self.degree_marks}", end=" ")

student1 = ResultGraduation(101, "John Doe", 85, 90, "Science", "B.Sc.", 88)
student1.display_info()

student2 = ResultGraduation(102, "Jane Smith", 78, 82, "Commerce", "B.Com.", 80)
student2.display_info()

student3 = ResultGraduation(103, "Alice Johnson", 92, 95, "Arts", "B.A.", 90)
student3.display_info()


# 3. Hierarchical Inheritance
# Hierarchical Inheritance : social media -> facebook, instagram, twitter
class SocialMedia:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def display_info(self):
        print(f"\nUsername: {self.username}, Password: {self.password}", end=" ")

class Facebook(SocialMedia):
    def __init__(self, username, password, friends_count):
        super().__init__(username, password)
        self.friends_count = friends_count

    def display_info(self):
        super().display_info()
        print(f", Friends Count: {self.friends_count}", end=" ")

class Instagram(SocialMedia):
    def __init__(self, username, password, followers_count):
        super().__init__(username, password)
        self.followers_count = followers_count

    def display_info(self):
        super().display_info()
        print(f", Followers Count: {self.followers_count}", end=" ")
        
class Twitter(SocialMedia):
    def __init__(self, username, password, tweets_count):
        super().__init__(username, password)
        self.tweets_count = tweets_count

    def display_info(self):
        super().display_info()
        print(f", Tweets Count: {self.tweets_count}", end=" ")

user1 = Facebook("john_doe", "password123", 150)
user1.display_info()

user2 = Instagram("jane_smith", "password456", 200)
user2.display_info()

user3 = Twitter("alice_johnson", "password789", 300)
user3.display_info()

# 4. Multiple Inheritance
# Multiple Inheritance : facebook, instagram, twitter -> user
class User(Facebook, Instagram, Twitter):
    def __init__(self, username, password, friends_count, followers_count, tweets_count):
        Facebook.__init__(self, username, password, friends_count)
        Instagram.__init__(self, username, password, followers_count)
        Twitter.__init__(self, username, password, tweets_count)

    def display_info(self):
        Facebook.display_info(self)
        Instagram.display_info(self)
        Twitter.display_info(self)
        print(f", Combined Info: {self.username}, {self.password}", end=" ")

UserCombined = User("john_doe", "password123", 150, 200, 300)
UserCombined.display_info()