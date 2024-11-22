#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: creating a programme to validate an integer

"""
Validating integer
By: L00187850
Date: 21 Nov 2024
"""

from re import A

def validate_integer():
    # Loop forever
    while True:
        try:
            user_input = int(input("Please enter an integer value for this programme. Note whole numbers only, decimals will fail: "))
        except:
            # Bad value, 
            print("Error")
            continue
        else:
            print("Valid input")
            # Good value, exit the loop
            break
        finally:
            # Continue
            print("This message shows every time, regardless of the programme flow")
            

validate_integer()

#for defining the endurance function, i'm adding two paramters called duel and fuel consumption. I also added a while loop for a bit of flair
def Endurance_calculation( message, fuel_consumption):
    while True:
        try:
            if fuel_consumption == 0:
                #ValueError is a built in feature within python. It doesn't require an import.
                raise ValueError("Fuel consumption cannot be zero.")
            endurance = fuel / fuel_consumption
            return endurance
            # Exception is another built in feature within python.
        except Exception as e:
            print(f"Unexpected error: {e}")
            break  # Exit the loop after handling the error

# Example usage
fuel = 100  # Litres
fuel_consumption = 5  # Litres per minute
print("Number of minutes left before fuel runs out:", Endurance_calculation(fuel, fuel_consumption))

#Example below of Exception being used.
"""
# Take an input number as a string and convert it to an integer
my_value = int(input("Enter an integer greater than 0"))

if my_value <= 0:
    raise Exception("Values must be > 0")
else:
    print("Validation checks passed")
"""