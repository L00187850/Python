#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Program to spell out sentences using variables and .format().
# Also added three more variables and added a space between variables.

a = "Good"
b = "Philip"
c = "Morning"

d = "Nice"
e = "Day"
f = "isn't it"
print("Message is: {first} {third} {second}".format(first=a, second=c, third=b))

print("Message is: {fourth} {fifth} {sixth}".format(fourth=d, fifth=e + " " + b + ",", sixth=f))