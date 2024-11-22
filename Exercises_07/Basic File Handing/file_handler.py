#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: creating a programme to create and edit files

"""
Basic File Handing
By: L00187850
Date: 21 Nov 2024
"""

#I changed this bit to create a powershell script and i changed the vaiable to filename.
filename = "my_Script.ps1"

try:
    with open(filename, "a") as file_handle:
        print(f"Writing a test line to {filename}")
        file_handle.write("This is to show that a powershell file can be created with python.")
except IOError as err:
    print(f"IOError was {err}")
except EOFError as err:
    print(f"End of file error was {err}")
except OSError:
    print("OS Error")
except:
    print("General Error")
else:
    print("File created")
finally:
    print("Wrapping up!")
    # close not needed because with statement
    # file_handle.close()
    
    """
    When you open a file, you can open to write (”w”) or read (“r”). In the open command, change the “w” to an “r”, 
    you are now opening the file read only. When you attempt to write to the file, this will generate an operating system error. 
    But more specifically, it generates an IO Error.
    """