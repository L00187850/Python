#Name: Philip Stewart
#Student Number: L00187850
#Date: 25 Nov 2024
#Purpose: Applying all OO coding features together into one script

"""
Parent class Template
"""
# In any complex application, create a base class which will never be instantiated.
class Device():
    
    # Define a class object attribute, the same for any instance of the class
    pi = 3.142

    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        print("Running constructor for base class")
        # Create attributes and set initial values
        self.debug = False

    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")

    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from base")

        crc = 24681012 % sum(24 * 5)
        return crc


"""
Child class Template
"""
# Create child class which can access the methods and properties of the base class
class Firewall(Device):

    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, parameter) -> None:
        # Calling back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {parameter}")
        # Create attributes and set initial values
        self.parameter = parameter
        self.test_message = ""
    
    def configure_firewall(self):
        print("Configuring Firewall")

    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from child")

        crc = 24681012 % (24 * 4)
        return crc

"""
Philips own child class - Switches
"""
class Switch(Device):

    def __init__(self, parameter) -> None:
        Device.__init__(self)
        print(f"Running constructor for {parameter}")
        self.parameter = parameter
        self.ports = 24  

    def configure_switch(self):
        print("Configuring Switch")
    
    def calculate_crc(self, frame: str) -> int:
        print("Checking CRC from Switch")
        crc = 24681012 % (24 * 7)  
        return crc

"""
Philips child class - Load Balancer
"""
class LoadBalancer(Device):

    def __init__(self, parameter) -> None:
        Device.__init__(self)
        print(f"Running constructor for {parameter}")
        self.parameter = parameter
        self.algorithm = "Round Robin"

    def configure_load_balancer(self):
        print("Configuring Load Balancer with algorithm:", self.algorithm)
    
    def calculate_crc(self, frame: str) -> int:
        print("Checking CRC from LoadBalancer")
        crc = 24681012 % (24 * 2)
        return crc        