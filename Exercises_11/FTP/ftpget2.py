#Name: Philip Stewart
#Student Number: L00187850
#Date: 28 Nov 2024
#Purpose: FTP


import ftplib

FTP = {
    "FILEPATH": '/mirrors/ubuntu-cdimage/releases/22.04/release',
    "MYFILE": 'SHA256SUMS',
    "LINK": 'ftp.heanet.ie'
}

# Make the connection
ftp = ftplib.FTP(FTP['LINK'])
# Anonymous login
ftp.login() 
# Change to the correct directory
ftp.cwd(FTP["FILEPATH"])
# Retrieve the file
ftp.retrbinary("RETR " + FTP["MYFILE"], open(FTP["MYFILE"], 'wb').write)
ftp.quit()

