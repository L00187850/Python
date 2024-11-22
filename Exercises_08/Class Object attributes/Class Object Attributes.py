#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose:

class MyTemplate():
    # Define class object attributes (these are shared by all instances)
    semi_major_axis = 6378137
    semi_minor_axis = 6356752 
    
    # I have added a constructor with information from a previous script. I added this to allow for assigning values to the attributes of the object.
    def __init__(self, attribute1: str, attribute2: bool) -> None:
        print("Constructor ran")
        # Instance-specific attributes
        self.attr1 = attribute1
        self.attr2 = attribute2

# Instantiate the class
my_object = MyTemplate("Philip", True)

# Access and print class-level attributes
print(my_object.semi_major_axis, my_object.semi_minor_axis)
