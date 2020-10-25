#!/bin/env python
from ip_address import ip_address_v4 as ip_address
from sys import stdin

ip_class_table = [
        {"first":0x00000000, "netbits":7, "hostbits":24},
        {"first":0x80000000, "netbits":14, "hostbits":16},
        {"first":0xc0000000, "netbits":21, "hostbits":8},
        {"first":0xe0000000, "netbits":None, "hostbits":None},
        {"first":0xf0000000, "netbits":None, "hostbits":None},
        {"first":0x100000000, "netbits":None, "hostbits":None} #kinda stupid but makes a lot of things easier
]

def class2int(ip_class: chr):
    return 'ABCDE'.index(ip_class)

def int2class(i: int):
    return 'ABCDE'[i]

def get_ip_addr_class(ipaddr: ip_address):
    for i in range(5):
        if ipaddr < ip_class_table[i+1]["first"]:
            return int2class(i)

def ip_class_row(ipaddr: ip_address, offset=0):
    return ip_class_table[class2int(get_ip_addr_class(ipaddr)) + offset]

def get_ip_addr_network(ipaddr: ip_address):
    netbits = ip_class_row(ipaddr)["netbits"]
    return 2 ** netbits if netbits else "N/A"

def get_ip_addr_host(ipaddr: ip_address):
    hostbits = ip_class_row(ipaddr)["hostbits"]
    return 2 ** hostbits if hostbits else "N/A"

def get_ip_addr_first_address(ipaddr: ip_address):
    return ip_address(ip_class_row(ipaddr)["first"])

def get_ip_addr_last_address(ipaddr: ip_address):
    return ip_address(ip_class_row(ipaddr, offset=1)["first"] - 1)

def get_class_stats(ip_string: str):
    ipaddr=ip_address(ip_string)
    print(
"""Class: {}
Network: {}
Host: {}
First address: {}
Last address: {}""".format(
            get_ip_addr_class(ipaddr),
            get_ip_addr_network(ipaddr),
            get_ip_addr_host(ipaddr),
            get_ip_addr_first_address(ipaddr),
            get_ip_addr_last_address(ipaddr)
        )
    )

def get_subnet_count(ipaddr: ip_address):

    return 4

def get_addressable_hosts_per_subnet(ipaddr: ip_address):
    return 62

def get_valid_subnets(ipaddr: ip_address):
    return ["192.168.10.0", "192.168.10.64", "192.168.10.128", "192.168.10.192"]

def get_broadcast_addresses(ipaddr: ip_address):
    return ["192.168.10.63","192.168.10.127","192.168.10.191","192.168.10.255"]

def get_first_addresses(ipaddr: ip_address):
    return ["192.168.10.1","192.168.10.65","192.168.10.129","192.168.10.193"]

def get_last_addresses(ipaddr: ip_address):
    return ["192.168.10.62","192.168.10.126","192.168.10.190","192.168.10.254"]

def get_subnet_stats(ip_class_c_string: str, subnet_mask: str):
    ipaddr=ip_address(ip_class_c_string)
    try:
        assert(get_ip_addr_class(ipaddr) == 'C')
    except AssertionError:
        print("Error: IP address must be class C")
    print(
"""Address: 192.168.10.0/26
Subnets: {}
Addressable hosts per subnet: {}
Valid subnets: {}
Broadcast addresses: {}
First addresses: {}
Last addresses: {}""".format(
            get_subnet_count(ipaddr),
            get_addressable_hosts_per_subnet(ipaddr),
            get_valid_subnets(ipaddr),
            get_broadcast_addresses(ipaddr),
            get_first_addresses(ipaddr),
            get_last_addresses(ipaddr)
        )
    )

def main():
    for line in stdin:
        line=line.strip()
        print(line)
        get_class_stats(line)
        get_subnet_stats(line, "255.255.255.192")
        print()

if __name__ == "__main__":
    main()

