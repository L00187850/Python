#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: while loops continue to execute a block of code until the condition is no longer true.

#sample while loop.
#while condition:
    # Execute code block
#else:
    # Execute something else
    
x = 0
while x < 10:
    print(f"X is = {x}")
    x = x + 1
else:
    print(f"As x is now = {x}, we are all finished")

#code output.
#X is = 0
#X is = 1
#X is = 2
#X is = 3
#X is = 4
#X is = 5
#X is = 6
#X is = 7
#X is = 8
#X is = 9
#As x is now = 10, we are all finished


#Adding a while loop which requests users input. It won't break until "Exit" is entered.

My_input = ""  

while My_input != "Exit":  
    My_input = input("Enter a command (type 'Exit' to quit): ")
    print(f"You typed: {My_input}. Now exiting") 


#How to run a program forever:
print("press [ctrl][c] to exit")
while 1:
    pass
    
    