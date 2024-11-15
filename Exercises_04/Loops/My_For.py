#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Loops are repeating code until a condition is met for them to break.

iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
    # For each item, execute this code block
    print(item)
    
    
print("")
print("")
print("")
print("")

#This code shows only the numbers which are odd.
iterable_variable1 = [1,2,3,4,5,6]

for item in iterable_variable1:
    if item %2 != 0:
        print(item)
print("")
print("")
print("")
print("")


#This code increments the total by the item number.
iterable_variable2 = [1,2,3,4,5,6]
total = 0

for item in iterable_variable2:
    total = total + item

print(total)

print("")
print("")
print("")
print("")


#This for loop keeps looking for a letter until it finds it. then it breaks. Until then it runs the command "No good, i don't need this letter:" and states the letter 
# Define a string to iterate over
for this_letter in "Philip Stewart":
    # Specify which letter to test for
    if this_letter == "W":
        # Found the test letter
        print(f"nice one! I found this letter {this_letter}!")
        # Exit the current loop
        break
        # I added another elif stating the lower cased letter.
    elif this_letter == "w":
        print(f"nice one! I found this letter {this_letter}!")
        break
    else:
        # Didn't find the test letter
        print(f"No good, I don't need this letter: {this_letter}!")


print("")
print("")
print("")
print("")


my_list = [1,2,3,0]

for my_number in my_list:
    if my_number == 1:
        pass
    if my_number == 2:
        continue
    if my_number == 3:
        print(f"Found the number {my_number}")
    if my_number == 0:
        break
        
print("")
print("")
print("")
print("")

list_of_tuples = [(1,2), (3,4), ("A", "B")]
for item in list_of_tuples:
    print(item)  

   
print("")
print("")
print("")
print("") 
    # Tuple unpacking
list_of_tuples1 = [(1,2), (3,4), ("A", "B")]
for a,b in list_of_tuples1:
    print(a)  
    print(b)

print("")
print("")
print("")
print("") 
for index in range(1, 100, 5):
    print(index)
    
    
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
    print(f"Found a service on {ipv4} at {port}")