#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: Explaining Typed hints

#This code explains the concept of typed hints


def calculate_circumference(radius: float) -> float:
    
    #Python is dynamically typed, so I could easily pass a string to the function and generate a bug! 
    # From Python v3.5 onwards, we have type hints. I could tell the function that I am passing a float and expect it to return a float.
