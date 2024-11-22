#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: creating a programme to detect a working directory.

"""
directory_utilities.py
By: L00187850
Date: 21 Nov 2024
"""

import os, platform

# Define global variables
current_directory = None

def detect_os() -> str:
    return platform.system()

def working_directory() -> str:
    return os.getcwd()

def create_directory(directory_name: str) -> bool:
    try:
        os.mkdir(directory_name)
        return True
    except:
        print(f"Error creating directory {directory_name}")
        return False

if __name__ == '__main__':
    print(f"This module executes as a standalone script")
    
    my_os = detect_os().lower()
    
    if create_directory("L00187850"):
        print("Creating a directory worked. Created folder L00187850")
    else:
        print("Directory creation unsuccessful.")
    
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    elif my_os == "darwin":
        print("Your system is MacOS")
    elif my_os == "centos":
        print("Your system is CentOS")
    else:
        print(f"Cannot continue, unidentified system = {my_os}")
        sys.exit()

    current_directory = working_directory()
    print(f"You are coding in: {current_directory}")

else:
    print(f"This module is called {__name__} and is being called by another script")

def create_directory(directory_name: str) -> int: 
    # Check to see if the directory already exists
    if os.path.isdir(directory_name):
        print("The directory already exists")
        return 2
    else:
        # Use try/except to catch errors
        try:
            os.mkdir(directory_name)
            # If this worked, return 0
            return 0
        except:
            # Give an explicit error message
            print(f"Error creating directory {directory_name}")
            # If this did not work, return 1
            return 1

if create_directory("L00187850") == 0:
    print("Creating a directory worked")
    # Do other stuff
elif create_directory("L00187850") == 1:
    print("You couldn't create a directory!")
    # Do other stuff
elif create_directory("L00187850") == 2:
    print("Directory already existed!")
    # Do other stuff
