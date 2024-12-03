#Name: Philip Stewart
#Student Number: L00187850
#Date: 02 Dec 2024
#Purpose: Multicast


'''
Multicast client by: JOR

This script will listen for multicast packets on a certain ip address and port.

note that you may need to run as "Sudo python3 mc_client.py"
'''
import socket
import struct
import settings.mc as settings

# Set multicast information. Effectively declaring variables found in mc.py script
MultiCast_Group = settings.MultiCast_Server["Multicast_Group"]
MCAST_IF_IP = settings.MultiCast_Server["IPV4"]
SERVER_ADDRESS = ('', settings.MultiCast_Server["PORT_NUMBER"])

print(f'This is the erver and port {SERVER_ADDRESS}')
print(f'Make sure its IP address matches {MCAST_IF_IP} in settings.')
print(f'This selects which interface is used to listen for multicast as {MultiCast_Group}.')
print('This script doesnt know the meaning of wrong, because I said so :D ')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(SERVER_ADDRESS)
    # inet_aton converts IPv4 from the a dotted decimal string to 32 bit packed binary format
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, 
                 socket.inet_aton(MultiCast_Group) + socket.inet_aton(MCAST_IF_IP))

    while True:
        print('Have you got my text mate? ')
        data, address = s.recvfrom(1024)
        print(f'The script received {len(data)} bytes from the IP address {address}')
        print(data)
