#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Introduction to tuples. Tuples are like lists, but immutable. Once an element has been assigned to a tuple, it cannot be changed. 
#Tuples are defined by regular brackets.

# I'm adding case-sensitivity to it so that it mentions it in lower and upper case. I've also added a second "two" for the tuple to count it"

My_Tuple = ("one", "two", "three", "two")
# How Many times does "One" appear in the tuple"
print(My_Tuple.count("two"))
print(My_Tuple.count("two".lower()))
# At what position in the tuple can i first find "one"
print(My_Tuple.index("three"))


#I'm also adding to the length of the tuple. essentially counts the elements in the tuple.
print("Tuple Length:", len(My_Tuple))