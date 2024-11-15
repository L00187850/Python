#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: using float as value:width.precision. Also using float to add 4 numbers and print it to 2 decimal places spaced by 7 spaces.

Number = 12345
Divisor = 333
Result = Number/Divisor
print("Result of {} divided by {} is {}".format(Number, Divisor, Result ))
print("Limiting to a float with 4 decimal places would give {r:1.4f}".format(r=Result))

number1 = 20
number2 = 15
number3 = 19
number4 = 100
Final = number1 + number2 + number3 + number4
print("Final numbers are {s:7.2f}".format(s=Final))