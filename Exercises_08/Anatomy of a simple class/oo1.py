#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: Anatomy of a simple class

"""
Adding classes. A simple class introduction by Philip Stewart.
Using the camel case to name classes.

Write and test a class like the one above and save it as oo1.py.
In addition to MyClass1, write some code to create and exercise an instance of your class called MyClass2.
"""

# Create a class
class L00187850sClass():
    
    # Constructor, called whenever an instance of the class is created.
    def __init__(self, greeting):
        print("Running constructor for L00187850sClass")
        # Create attributes and set initial values
        self.message = greeting

    def my_method(self):
        print(self.message)


my_class1 = L00187850sClass("Good Morning Philip. How are you?")
my_class1.my_method()
print(type(my_class1))

# Define a new class called MyClass2
class MyClass2():
    
    # Constructor for MyClass2. Called whenever an instance of the class is created.
    def __init__(self, name, age):
        print("Running constructor for MyClass2")

        self.name = name
        self.age = age

    def introduction(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


my_class2_instance = MyClass2("Philip", 27)
my_class2_instance.introduction()
print(type(my_class2_instance))
