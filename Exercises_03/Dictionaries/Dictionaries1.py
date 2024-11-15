#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Introduction to the Dictionaries data structure. They are unordered structures for storing objects.

My_dictionary = {"First Name":"Phliip", "Surname":"Stewart", "Occupation": "Game of Thrones Enthusiast"}
# My_second_dictionary = {"First Name": "Ted", "Surname":"Crilly", "Occupation": "Priest"}
print(My_dictionary)
print("Works as a typical " + My_dictionary["Occupation"])

#Part where we add a key:value pair: basically where we add a section to the dictionary.

My_dictionary["Knowledge of books"] = "None!"
print(My_dictionary)

# Editing a value at this point.
My_dictionary["Occupation"] = "House of the Dragon fan!"
print(My_dictionary)
print("")
print("")
print("")
print("")

#Printing the keys of the dictionary (My_Dictionary.keys())
print("Dictionary Keys: ", (My_dictionary.keys()))
# Or you can do this: 
print("Listed keys of the Dictionary:", list(My_dictionary.keys()))
print("")
print("")
print("")
print("")

print("Dictionary Values:", (My_dictionary.values()))
# Or you can do this: 
print("Values of the updated dictionary:", list(My_dictionary.values()))
print("")
print("")
print("")
print("")
print("Dictionary Items:",(My_dictionary.items()))
print("Dictionary Items:", list(My_dictionary.items()))