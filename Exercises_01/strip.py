#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Adding strip to a command which removes all spaces from a word.

#rjust (or right align) is used to add spaces to the right of a string
#ljust (or left align) is used to align the string to the left.
text_with_spaces = "    Philip Stewart  "
text_without_spaces = text_with_spaces.strip()
print(text_without_spaces)


new_text_with_spaces = "L0018785"
new_text_with_right_spaces = new_text_with_spaces.rjust(30)

new_text_with_left_spaces = new_text_with_spaces.ljust(30)

print((new_text_with_right_spaces), "This is showing my student number with spaces before it, using rjust: ")
print((new_text_with_left_spaces), "This is showing my student number with spaces before it, using ljust:")