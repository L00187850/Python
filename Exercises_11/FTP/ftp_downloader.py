#Name: Philip Stewart
#Student Number: L00187850
#Date: 02 DEC 2024
#Purpose: FTP: TESTING

"""
FTP File downloader.
Tested with Python 3.13.
By: Philip Stewart
"""
import ftplib
import settings.ftp as settings

# Make the connection. 
ftp = ftplib.FTP(settings.FTP['LINK']) #This connects to the FTP server  

ftp.login() #This lets your perform an anonymous login

ftp.cwd(settings.FTP["FILEPATH"]) # This brings it to the correct directory.
# Retrieve the file
ftp.retrbinary("RETR " + settings.FTP["MYFILE"], open(settings.FTP["MYFILE"], 'wb').write)
ftp.quit()
print(f"File '{settings.FTP['MYFILE']}' downloaded successfully.") #Added a print command to show that it completed successfully.
