#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: Explaining Packages

square_text = "Let's try to square an integer!"

# I'm defining the function square with x as the paramter.
def square(x): 
    return x ** 2

#This if statment checks if the module is being ran as the main program. If it is executed or printed as a standalone script, Otherwise print it as being called by another script.
if __name__ == '__main__':
    # Uncomment to test
    print(square(2))
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")
