#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Explaining the python standard library

#Importing the math standard library and using it to find the hypotenuse of a right angled triangle.
import math
print("Input lengths of the two short triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse to four places is: {hypo:1.4f}".format(hypo=c))