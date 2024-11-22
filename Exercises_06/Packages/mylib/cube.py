#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: Explaining Packages




cube_text = "Time to cube some integers!"

def cube(x):
    return x*x*x

# Uncomment to test
print(cube(5))


# When a .py file is imported as a module, the variable __name__ is set to the name of the module. 


print(f"This module is called {__name__}") 

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
else:
    print(f"This module is called {__name__} and is being called by another script")
    
    
# If the module is ran by itself, it runs the cube.py code under the if statement and tells us that it is a standalone script.