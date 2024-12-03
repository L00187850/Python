#Name: Philip Stewart
#Student Number: L00187850
#Date: 28 Nov 2024
#Purpose: FTP

#This script is used to show the importing of the FTP library module. It also shows how to use FTP to
#connect to a website, change directory and retrieve the file found in the directory. It then shows how to #close an FTP connection.

import ftplib

# Set the path
file_path = '/mirrors/ubuntu-cdimage/releases/22.04/release'

# What file to download
my_file = 'SHA256SUMS'

# Make the connection
ftp = ftplib.FTP("ftp.heanet.ie")

# Anonymous login
ftp.login() 

# Change to the correct directory
ftp.cwd(file_path)

# Retrieve the file
with open(my_file, 'wb') as file:
    ftp.retrbinary("RETR " + my_file, file.write)

ftp.quit()  # Close the connection
print(f"{my_file} downloaded successfully.")
