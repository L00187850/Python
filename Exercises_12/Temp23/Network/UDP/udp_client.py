#Name: Philip Stewart
#Student Number: L00187850
#Date: 02 Dec 2024
#Purpose: UDP
'''
UDPClient by: Philip Stewart
Sending UDP packets to a particular address and port.

'''

import socket
import time
from datetime import datetime
import settings.udp as settings

SERVER_UDP = settings.UDP["SERVER_UDP"]
Server_PORT = settings.UDP["SERVER_PORT"]

print(f'This is the UDP client, it will try to connect to a server at {SERVER_UDP}:{Server_PORT} in the settings file.')
print('This script has no error handling, by design')

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        message_text = f"Hello John, this is Philip sending packets {datetime.now()}"
        message = message_text.encode('utf-8')
        s.sendto(message, (Server_IP, Server_PORT))
        print(f'Sent {message_text}')
        time.sleep(4)
