# Name: Philip Stewart
# Student Number: L00187850
# Date: 21 Nov 2024
# Purpose: Building a class from scratch

"""
A Template for a class 
"""

class MyTemplate():
    """
    A simple example class to demonstrate object-oriented programming.
    """

    # Constructor, called whenever an instance of the class is created.
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        # Assign attributes
        self.attr1 = attribute1
        self.attr2 = attribute2



#I added a part where it is checking the variable and the type. It is an example of making an instance instide of a class and giving it a variable name.
# Instantiate the class
my_object = MyTemplate("Philip", True)
print(type(my_object))