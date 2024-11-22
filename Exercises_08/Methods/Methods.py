#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose:Methods. Adding methods within classes which act on attributes within the class.

#My change to this is that i added a class called MyClass and declared my_object.my_method2("Slartibartfast") as a variable.
class MyClass:

    def __init__(self, attr1: str, attr2: bool) -> None:
        self.attr1 = attr1
        self.attr2 = attr2

    
    def my_method1(self):
        if self.attr2:
            print(f"Good morning {self.attr1}")
        else:
            print(f"No greeting {self.attr2}")
        

        
    def my_method2(self, my_name:str):
        if self.attr2:
            print(f"Good morning {my_name}")
        else:
            print(f"No greeting {my_name}")



    
my_object = MyClass("Philip", True)
my_object.my_method2("Slartibartfast")
print(my_object.my_method2("Slartibartfast"))