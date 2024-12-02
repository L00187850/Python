#Name: Philip Stewart
#Student Number: L00187850
#Date: 02 dec 2024
#Purpose: NTP

'''
NTPClient by: Philip Stewart
This script tests if an NTP Server is functional

In this script i took work from a previous section and added a try/catch to give an error.
NTPException is a part of ntplib and i'm declaring it as the variable
'''
# Note that you need to run pip install both pip (sudo apt install python3-pip) and ntplib (pip install ntplib) before running this script.
import ntplib
from time import ctime

ntpServer = "ie.pool.ntp.org"

ntp = ntplib.NTPClient()
try:
    ntpResponse = ntp.request(ntpServer)
    
    if ntpResponse:
        print(f"NTP Time: {ctime(ntpResponse.tx_time)}")
        print(f"Precision: {ntpResponse.precision}")
        print(f"Version: {ntpResponse.version}")
        print(f"Offset: {ntpResponse.offset}")
        print(f"Root delay: {ntpResponse.root_delay}")
        print(f"Root dispersion: {ntpResponse.root_dispersion}")
        print(f"Delay: {ntpResponse.delay}")
        print(f"Leap: {ntpResponse.leap}")
        print(f"Stratum of NTP server: {ntpResponse.stratum}")
except ntplib.NTPException as exception:
    print(f"Error occurred while attempting to find the NTP time: {exception}")
    

