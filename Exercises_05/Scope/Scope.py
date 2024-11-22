#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: Scope

My_Inspiration_Level = "universal"

def my_function():
    My_Inspiration_Level = "expanding"
    def nested_function():
        My_Inspiration_Level = "global"
        print(My_Inspiration_Level)
    nested_function()
    def nested_function():
        My_Inspiration_Level = "Non-existant"
        print(My_Inspiration_Level)
    nested_function()
    return My_Inspiration_Level

# Print the variable my_inspiration_Level
print(My_Inspiration_Level)
# Print the output of the function, my_function
print(my_function())

print("")

print("")

print("")

print("")
# I added another nested function called non-existant and changed the names of the variables.

my_string = "Non-existant"

def my_function():
    global my_string
    print(f"At the moment, my_string is: {my_string}")
    #Changing the function variable from now.
    my_string = "All good"
my_function()
print(f"Now the global value of my_string is: {my_string}")


#Exercise 1
#Briefly explain and comment this code. What values in the final statement will result in the function returning True? Why?

def divisible(numerator: int, denominator: int)->bool:     # This function checks if the numerator is divisible by the denominator without a remainder on it.
    return numerator % denominator == 0                     # Returns True if no remainder, otherwise False


print(divisible(30,4)) #Calls the function divisible with 30 and 4 as arguments

#Why do you get the value None? 

# What values in the final statement will result in the function returning True? 

# Why? 

# Can you modify this function to return False instead of None if the value is not found?
def find_num(number_list: list, number: int) -> bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
    return False

result = find_num([1, 2, 3, 4, 5, 6, 7, 8], 9)
print(result)


def even_number(number_list: list) -> bool:
    for number in number_list:
        if number % 2 == 0:
            return True
    return False

result = even_number([2, 4, 6, 8, 10])
print(result)


# Running the lambda function
cylinder_volume = lambda radius, height: 3.14159 * radius**2 * height

result = cylinder_volume(4, 7)
print(result)
