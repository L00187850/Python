#Name: Philip Stewart
#Student Number: L00187850
#Date: 25 Nov 2024
#Purpose: Data log files.



from datetime import datetime
import sys, os

def path_name():
    """
    Determines the log directory based on the operating system.
    Creates the 'logs' folder if it does not exist.
    """
    this_os = sys.platform
    if this_os == 'win32':
        log_dir = 'c:\\logs'
    elif this_os == 'linux':
        log_dir = '/home/pi/logfiles'
    else:
        print(f'Unsupported OS: {this_os}')
        exit(0)
    
    # I created a directory in the log_dir which is c:\logs
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    return log_dir

def log_file_name(extension):
    """
    Makes a log file and puts it in the logs directory we just made. Its done within the if statement.
    """
    now = datetime.now()
    file_name = '%0.4d%0.2d%0.2d-%0.2d%0.2d%0.2d' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    return file_name + extension

if __name__ == '__main__':
    print(f"This module is called {__name__} and executes as a standalone script")
    log_path = path_name()  # Get the path to the log directory
    filename = log_file_name(".log")  # Generate the log file name
    full_path = os.path.join(log_path, filename)  # Combine path and filename
    print(f"Log file will be saved at: {full_path}")
else:
    pass
