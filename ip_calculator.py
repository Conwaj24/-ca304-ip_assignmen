#!/bin/env python
from ip_address import ip_address_v4 as ip_address
from sys import stdin

def get_ip_addr_class(ipaddr: ip_address):
    if ipaddr[0] < 0b10000000:
        return 'A'
    if ipaddr[0] < 0b11000000:
        return 'B'
    if ipaddr[0] < 0b11100000:
        return 'C'
    if ipaddr[0] < 0b11110000:
        return 'D'
    return 'E'

ip_class_table = {
        'A':{"netbits":7, "hostbits":24},
        'B':{"netbits":14, "hostbits":16},
        'C':{"netbits":21, "hostbits":8},
        'D':{"netbits":None, "hostbits":None},
        'E':{"netbits":None, "hostbits":None}
}

def ip_class_row(ipaddr: ip_address):
    return ip_class_table[get_ip_addr_class(ipaddr)]

def get_ip_addr_network(ipaddr: ip_address):
    netbits = ip_class_row(ipaddr)["netbits"]
    return 2 ** netbits if netbits else "N/A"

def get_ip_addr_host(ipaddr: ip_address):
    hostbits = ip_class_row(ipaddr)["hostbits"]
    return 2 ** hostbits if hostbits else "N/A"

def get_ip_addr_first_address(ipaddr: ip_address):
    return "224.0.0.0"

def get_ip_addr_last_address(ipaddr: ip_address):
    return "239.255.255.255"

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

