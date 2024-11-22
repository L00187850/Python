#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose:


# Create a class 
class JORzClass():
    
# Constructor, called whenever an instance of the class is created.
    def __init__(self, my_greeting, attribute1, attribute2):
        print("Running constructor for JORzClass")
        self.attr1 = attribute1
        self.attr2 = attribute2
        # Create attributes and set initial values
        self.message = my_greeting
#Declaring a method which can be changed where needed.
    def my_method1(self):
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr1}")
            
    def my_method2(self, my_name:str):
        if self.attr2:
            print(f"Good morning {my_name}")
        else:
            print(f"No greeting {my_name}")


#stating the class and creating an object called my_object.
            
my_object = JORzClass("Hello", "Philip", True)
my_object.my_method1()
my_object.my_method2("Slartibartfast")


