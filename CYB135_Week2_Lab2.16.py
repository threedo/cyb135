#CYB135 Week2 Lab 2.16

'''
2.16 LAB: Port Scan (Modules)
In network security, it is important to understand port scanning. Hackers use tools to scan a network and determine if there are open ports and if they contain some sort of vulnerability. To scan ports, you first have to find active hosts on a network. Once you find active hosts and discover a list of IP addresses for those hosts, a port scan can be performed to gather information about open ports and analyze services running on those ports. A port scan is the process of sending packets to an active host's ports and learning details that can help you gain access to that host or to discover open vulnerabilities on your network.

Some common ports are:
Port 20 - File Transfer Protocol or FTP
Port 22 - Secure Shell protocol or SSH
Port 23 - Telnet protocol for unencrypted transfer
Port 80 - HyperText Transfer Protocol or HTTP
Port 443 - HyperText Transfer Protocol Secure or HTTPS

The Well Known Ports are those from 0 through 1023

We are going to simulate a port scan by filling a list with 100 random port numbers. These values will be used as the keys in a dictionary where the values will be randomly generated integers 0 / 1. The 0 will be a closed port and a 1 will be an open port.

Your first TODO is to create a function called "create_host_IPs( )" that randomly generates a list of 10 IP addresses with 4 random octets values, concatenating the 4 values into a string and appending it to a host list. The function returns the generated host list. The random values can be limited to a range of 10 to 200.

Ex: IPv4 address should look like this:

192.168.34.23
Your next TODO is to create another function called "simulate_scan(h)" that iterates through the host list (received as h ) and then creates a new list called open_ports. The function should use a nested for loop that iterates through the host list, and then iterates through the returned list from a call to "create_random_open_ports()". If the returned list value is 1, then append it to your open_ports list. This simulates a scan of all the IPs in the host list and creates randomly generated open ports. Finally it should print the host IP and a list of open ports as displayed in this example output.

Ex: Your output should contain 10 IP reports. Here is and example of 2 of the 10 reports:

Host IP: 66.78.126.11
Open ports are:
[53, 87, 21, 57, 71, 37, 61, 38, 45, 94, 84, 26, 72, 52, 75, 41, 90, 88, 82, 59, 50, 36, 60, 16, 51, 76, 24, 66, 33, 63, 86, 93, 34, 85]

Host IP: 11.96.129.20
Open ports are:
[15, 77, 19, 72, 78, 37, 93, 42, 26, 30, 79, 16, 47, 48, 43, 50, 82, 60, 46, 10, 62, 96, 12, 99, 76, 51, 32, 24, 61, 87, 73, 65, 85, 67, 29]
'''


from random import randint

def create_host_IPs():
    hosts = []
    while len(hosts) < 10:
        ip_octets = []
        while len(ip_octets) < 4:
            ip_octets.append(str(randint(10,200)))
        host = '.'.join(ip_octets)
        hosts.append(host)
    return hosts

def create_random_open_ports():
    ports = []
    for i in range(100):
        r = randint(i, 100)
        try:
            ports.index(r)
            continue
        except Exception:
            ports.append(r)
    return ports
def simulate_scan(h):
    for host in h:
        open_ports = []
        for port in create_random_open_ports():
            r = randint(0, 1)
            if r == 1:
                open_ports.append(port)
        print(f'Host IP: {host}')
        print(f'Open ports are:\n{open_ports}\n\n')

simulate_scan(create_host_IPs())
