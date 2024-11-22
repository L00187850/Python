#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: Passing and returning variables to a function
def My_First_Name(Last_Name):
    """
    Simple test function
    """
    print(f"Yoo hoo, hello Mr {Last_Name}!")

My_First_Name("Stewart")

#########################################################
def calculate_diameter(radius):
    """
    Calculate the diameter of a circle based on its radius
    """
    return 2 * radius

a = calculate_diameter(5)
print(a)

##########################################################
def calculate_diameter(radius=1):
    """
    Calculate the diameter of a circle based on its radius
    """
    return 2 * radius

a = calculate_diameter()
print(a)

####################################################################

def calculate_diameter(radius):
    """
    Calculate the diameter of a circle based on its radius
    """
    return 2 * radius

# Get a radius value as a string
r = input("Provide a radius value: ")
# Convert it to a float
r_float = float(r)
# Call the function and create the variable for the return value
a = calculate_diameter(r_float)
print("The Diameter is: ", a)

#######################################################################
def Counter(*my_numbers):
    final_number = 0
    for number in my_numbers:
        final_number = final_number + number
    return final_number

print(Counter(5, 15, 25, 35, 45, 55))

#########################################################################