#Name: Philip Stewart
#Student Number: L00187850
#Date: 02 Dec 2024
#Purpose: Multicast


'''
Multicast client by: Philip Stewart

This script will send multicast packets to a certain ip address and port.

note that you may need to run as "Sudo python3 mc_client.py"
'''
import socket
import time
from datetime import datetime
import settings.mc as settings

# Set multicast information
MCAST_GRP = settings.MultiCast_Client["Multicast_Group"]
MCAST_PORT = settings.MultiCast_Client["PORT_NUMBER"]
MCAST_IF_IP = settings.MultiCast_Client["IPV4"]

print(f'This is the client, make sure its IP address matches {MCAST_IF_IP} in settings.')
print(f'This selects which interface is used for multicast to {MCAST_GRP}.')
print('This script has no error handling, by design')

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
        # inet_aton converts IPv4 from the a dotted decimal string to 32 bit packed binary format
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) + socket.inet_aton(MCAST_IF_IP))
        message_text = f"Hi John. This is Philip Sending Multicast Packets.  {datetime.now()}"
        message = message_text.encode('utf-8')
        s.sendto(message, (MCAST_GRP, MCAST_PORT))
        print(f'Sent {message_text} to {MCAST_GRP}:{MCAST_PORT}')
        time.sleep(4)

