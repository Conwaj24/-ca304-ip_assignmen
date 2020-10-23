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


def main():
    for line in stdin:
        line=line.strip()
        print(line)
        get_class_stats(line)
        print()

if __name__ == "__main__":
    main()

