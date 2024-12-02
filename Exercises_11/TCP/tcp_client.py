#Name: Philip Stewart
#Student Number: L00187850
#Date: 02 Dec 2024
#Purpose: TCP

'''
TCPClient by: Philip Stewart
This script sends tcp packets to anv ip address and port.

#Note add sudo to the command "python3 tcp_client.py to ensure it runs correctly.
'''

import socket
import time
from datetime import datetime
import settings.tcp as settings #This is importing tcp.py in the settings file and giving it the alias/name or #settings in this one.

TCP_IP = settings.TCP["SERVER_TCP"]
TCP_PORT = settings.TCP["SERVER_PORT"]

print(f'This is the TCP client, it will try to connect to a server at {TCP_IP}:{TCP_PORT} in the settings file.')
print('This script has no error handling, by design')

BUFFER_SIZE = 1024
while True:
    print(f'Trying to open a socket to {TCP_IP}:{TCP_PORT}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        message_text = f"Hi John, Philip Here sending TCP packets {datetime.now()}"
        message = message_text.encode('utf-8')
        s.connect((TCP_IP, TCP_PORT))
        s.send(message)
        print(f'Sent {message_text} to {TCP_IP}:{TCP_PORT}')
        data = s.recv(BUFFER_SIZE)
        print('Server echoed:', data)
        time.sleep(4)

