#Name: Philip Stewart
#Student Number: L00187850
#Date: 21 Nov 2024
#Purpose: Writing Main for Data Log Files



from file_utilities import path_name, log_file_name
from os_utilities import detect_os, cpu_load, storage_capacity
from time import sleep

# Check the OS in use, and figure out a log file name and path
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".log")
print(log_path + filename)

# Loop forever
while True:
    # Sleep for 4 seconds
    sleep(4)
    # Get a time stamp for this line
    timestamp = log_file_name("")
    # Get some information
    information = cpu_load()
    # Create a line for the logfile, convert the integer values to string

    # Get storage information
    storage_info = storage_capacity()
    logline = timestamp + ":" + str(information[0]) + "," + str(information[1]) + "\n"
    # Now write it to the logfile
    
    logline = (
        f"{timestamp}: "
        f"CPU: {information[0]} CPUs, {information[1]}% load | "
        f"Storage: {storage_info[0]:.2f}GB total, {storage_info[1]:.2f}GB used, "
        f"{storage_info[2]:.2f}GB free, {storage_info[3]:.2f}% used\n"
    )    
    try:
        with open(filename, "a") as file_handle:
            print(f"logging to {filename}")
            file_handle.write(logline)
    except IOError as err:
        print(f"IOError was {err}")
    except EOFError as err:
        print(f"End of file error was {err}")
    except OSError:
        print("OS Error")
    except:
        print("General Error")