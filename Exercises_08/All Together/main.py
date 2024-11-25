#Name: Philip Stewart
#Student Number: L00187850
#Date: 25 Nov 2024
#Purpose: Applying all OO coding features together into one script


from Devices import Firewall, Switch, LoadBalancer

# Create a firewall instance.
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()

# Creating another instance of a firewall.
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Creating an instance of a switch.
switch1 = Switch("switch1")
switch1.configure_switch()
switch1.calculate_crc("dummy data")

# Creating an instance of a load balancer.
lb1 = LoadBalancer("load_balancer1")
lb1.configure_load_balancer()
lb1.calculate_crc("dummy data")