#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Introduction to If, Elif and Else statements

a = False
b = False
c = False
d = True

#Basically if A conditions are not met, attempt to verify Bs conditions, if that fails, attempt to verify Cs conditions, otherwise print out a code.

# I added a D variable with true, showing that the false statements work.
if a:
    print("a was false")
elif b:
    print("b was false")
elif c:
    print("c was true")
elif d:
    print("d was true")
else:
    print("None of our boolean variables were true")
