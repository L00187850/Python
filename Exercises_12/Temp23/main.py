"""
File Name:main.py
By: Philip Stewart
Student Number: L00187850
Date: 03 Dec 2024
"""

from Source.directory_utilities import detect_os, detect_working_directory
print(detect_os())
print(detect_working_directory())
# At this point run pip install pathlib  
from mypaths import UDP_SETTINGS as udp_settings
print(udp_settings)

# I added one for TCP settings
from mypaths import TCP_SETTINGS as tcp_settings
print(tcp_settings)