#CYB135 Week2 Lab 2.17
'''2.17 LAB: Network Automation (modules)
In network administration, many admins will use a VLAN (Virtual Local Area Network) to create logical subnetworks. The advantages of this type of a setup is better confinement of broadcast domains, reduced broadcast traffic and more efficient maintenance of the network. The admin can group network nodes that are physically dispersed into similar broadcast domains for improved network traffic management.

Configuration of VLANS on multiple switches can be very time consuming. Python scripts can help automate tasks reducing the need to physically go from switch to switch. Minimal configuration variables may include VLAN name, VLAN number, and Network device.

The main.py template provides a list of 5 network switch names. The script will simulate the configuration of those 5 devices.

Define the VLANSetup class in VLANSetup.py with a constructor to initialize a VLAN's information. The constructor should by default initialize the VLAN's name to "None" and the VLAN number to 0.

Define the NetManage class in NetManage.py with a constructor to initialize a device's hostname. The constructor should by default initialize the Network device to "None" and add a VLANSetup object. Add an import statement to import the VLANSetup class.

Add import statements to main.py to import the VLANSetup and NetManage classes.

Ex: If the input is:

Voice
10
the output is:

Configuring VLAN: 10
Connecting to: Switch1
Sending Config vlan: 10
Sending Config name: Voice

Configuring VLAN: 10
Connecting to: Switch2
Sending Config vlan: 10
Sending Config name: Voice

Configuring VLAN: 10
Connecting to: Switch3
Sending Config vlan: 10
Sending Config name: Voice

Configuring VLAN: 10
Connecting to: Switch4
Sending Config vlan: 10
Sending Config name: Voice

Configuring VLAN: 10
Connecting to: Switch5
Sending Config vlan: 10
Sending Config name: Voice
If the input is:

Data
20
the output is:

Configuring VLAN: 20
Connecting to: Switch1
Sending Config vlan: 20
Sending Config name: Data

Configuring VLAN: 20
Connecting to: Switch2
Sending Config vlan: 20
Sending Config name: Data

Configuring VLAN: 20
Connecting to: Switch3
Sending Config vlan: 20
Sending Config name: Data

Configuring VLAN: 20
Connecting to: Switch4
Sending Config vlan: 20
Sending Config name: Data

Configuring VLAN: 20
Connecting to: Switch5
Sending Config vlan: 20
Sending Config name: Data
'''

#main.py
from NetManage import NetManage
from VLANSetup import VLANSetup

if __name__ == "__main__":
    deviceList = ["Switch1", "Switch2", "Switch3", "Switch4", "Switch5"]
    user_VLAN_name = input()
    user_VLAN_number = int(input())

    for device in deviceList:
        user_device = VLANSetup(user_VLAN_name, user_VLAN_number)
        new_config = NetManage(device, user_device)
        new_config.print_info()


#VLANSetup.py
class VLANSetup:
    def __init__(self, name="None", number=0):
        self.name = name
        self.number = number

    def print_info(self):
        print('Sending Config vlan: {}'.format(self.number))
        print('Sending Config name: {}'.format(self.name))

#NetManage.py
from VLANSetup import VLANSetup
class NetManage:
    def __init__(self, device="None", config=VLANSetup):
        self.device = device
        self.config = config

    def print_info(self):
        print('Configuring VLAN: %s' % (self.config.number))
        print('Connecting to: {}'.format(self.device))
        self.config.print_info()
        print() 
