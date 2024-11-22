#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: detecting the operating system on the device. This is an example of a program being used.

#A standard module in pythons library.
import platform 

def detect_os()->str:
    # Detect the OS in use
    return platform.system()


if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    
    # Check the OS in use, lower case
    my_os = detect_os()
    my_os = my_os.lower()
    
    # Parse the response. Using if statements here to print out the correct OS corresponding to what the python programme sees.
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    elif my_os == "darwin":
        print("Your Apple system is MacOS")
    elif my_os == "cygwin":
        print("Your Apple system is MacOS")
    elif my_os == "aix":
        print("Your IBM system is AIX")
    else:
        #If it can't identify the OS then run this line.
        print(f"Unidentified system = {my_os}")
else:
    #This command is printed when it is being used as a module in another script.
    print(f"This module is called {__name__} and is being called by another script")
