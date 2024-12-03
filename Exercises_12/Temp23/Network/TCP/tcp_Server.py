#Name: Philip Stewart
#Student Number: L00187850
#Date: 02 Dec 2024
#Purpose: TCP

'''
TCPClient by: Philip Stewart
This script listens for TCP packets on a certain ip address and port

#Note add sudo to the command "python3 tcp_client.py to ensure it runs correctly.
'''

import socket
import settings.tcp as settings

TCP_IP = settings.TCP["SERVER_TCP"]
TCP_PORT = settings.TCP["SERVER_PORT"]
BUFFER_SIZE = 1024

print(f'This is the TCP server, it will open a port at {TCP_IP}:{TCP_PORT} and being listening')
print(f'Make sure the actual server IP address matches {TCP_IP} in the settings file')
print('This script has no error coding, just because lol')

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((TCP_IP, TCP_PORT))
        print(f'Listening from ip address {TCP_IP}:{TCP_PORT}')
        while True:
            s.listen(1)
            conn, addr = s.accept()
            print(f'Connection address: {addr}')
            data = conn.recv(BUFFER_SIZE).decode()
            print(data)
            conn.send(data.encode())
except socket.error as e:
    print(f'Error: {e}')

