#Name: Philip Stewart
#Student Number: L00187850
#Date: 25 Nov 2024
#Purpose: Data log files.

""""
This script detects what operating system is running, then a logfiles program is started.    
"""
# pip install psutil 
import psutil
import platform

def detect_os()->str:
    # Detect the OS in use
    return platform.system()

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    
    # Check the OS in use, lower case
    my_os = detect_os()
    my_os = my_os.lower()
    
    # Parse the response
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
        print(f"Unidentified system = {my_os}")
else:
    pass
    #print(f"This module is called {__name__} and is being called by another script")

def cpu_load():
    # Return significant numbers relating to the CPU
    #print(f"Number of CPUs: {psutil.cpu_count()}" )
    #print(f"CPU load: {psutil.cpu_percent()}")
    return(psutil.cpu_count(), psutil.cpu_percent())

def storage_capacity():
    disk_usage = psutil.disk_usage('/')  
    total_gb = disk_usage.total / (1024 ** 3) 
    used_gb = disk_usage.used / (1024 ** 3)
    free_gb = disk_usage.free / (1024 ** 3)
    percent_used = disk_usage.percent
    return total_gb, used_gb, free_gb, percent_used