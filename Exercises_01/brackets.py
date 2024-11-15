#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Adding strip to a command which removes all brackets from a word.

text_with_brackets = "(Philip Stewart)"
text_without_brackets = text_with_brackets.strip('()')
print(text_without_brackets)

#I attempted to use the line 
#text_without_brackets = text_with_brackets,strip('(') 
#text_without_brackets = text_without_brackets.strip(')')

#However this was failing. I just added the full bracket into one line and it worked.