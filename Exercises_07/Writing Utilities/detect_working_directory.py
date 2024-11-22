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

def detect_os()->str:
    # Detect the OS in use
    return platform.system()

def working_directory()->str:
    # Returns the directory this script was run from
    return os.getcwd()

if (__name__ == '__main__'):
    print(f"This module executes as a standalone script")
    
    # Check the OS in use, lower case
    my_os = detect_os()
    my_os = my_os.lower()
    
    # Parse the response, only check for Windows and Linux
if operating_system == "windows":
    print("Your system is Windows")
elif operating_system == "linux":
    print("Your system is Linux")
elif operating_system == "darwin": 
    print("Your system is MacOS")
elif operating_system == "centos":
    print("Your system is CentOS")
else:
    print(f"Cannot continue, unidentified system = {operating_system}")
    sys.exit()

# I added MacOS here, it would be identified as darwin usually. centOS is also added to find it since it is now obsolete and might need removing from the environment.
    # Get the current working directory
    current_directory = working_directory()
    print(f"You are coding in: {current_directory}")

else:
    print(f"This module is called {__name__} and is being called by another script")
