#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Map and Lambda

# The mnap() function gives us a way to iterate through an iterable object without using a loop. 

# map(function, iterable) would be an example. See below a use case.

def double_number(n: int)->int:
    """
    Simple function to double a number
    """
    return n*n

# Create a list of numbers for testing
my_numbers = [2,4,6,8,10]
# Map my_numbers to the double_number function, return type is map
result = map(double_number, my_numbers)
# Print a list of the map 
print(list(result))
# Or iterate through it
for item in map(double_number, my_numbers):
    print(item)



#Changed the values and multiplied instead of added.