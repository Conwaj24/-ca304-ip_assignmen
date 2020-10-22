#!/bin/env python
from ip_address import ip_address_v4 as ip_address

ip_class_table = {
        'A':{"netbits":7, "hostbits":24},
        'B':{"netbits":14, "hostbits":16},
        'C':{"netbits":21, "hostbits":8},
        'E':{"netbits":None, "hostbits":None},
        'F':{"netbits":None, "hostbits":None}
}

def get_ip_addr_class(ipaddr: ip_address):
    if ipaddr[0] < 0b1000000:
        return 'A'
    if ipaddr[0] < 0b1100000:
        return 'B'
    if ipaddr[0] < 0b1110000:
        return 'C'
    if ipaddr[0] < 0b1111000:
        return 'D'
    return 'E'

def get_ip_addr_network(ipaddr: ip_address):
    return 16384

def get_ip_addr_host(ipaddr: ip_address):
    return 65523

def get_ip_addr_first_address(ipaddr: ip_address):
    return "224.0.0.0"

def get_ip_addr_last_address(ipaddr: ip_address):
    return "239.255.255.255"

def get_class_stats(ip_string: str):
    ipaddr=ip_address(ip_string)

    print(
"""Class: %s
Network: %i
Host: %i
First adress: %s
Last address: %s """ % (
            get_ip_addr_class(ipaddr),
            get_ip_addr_network(ipaddr),
            get_ip_addr_host(ipaddr),
            get_ip_addr_first_address(ipaddr),
            get_ip_addr_last_address(ipaddr)
        )
    )


def main():
    get_class_stats("136.206.18.7")
    get_class_stats("0.206.18.7")
    get_class_stats("224.192.16.5")

if __name__ == "__main__":
    main()

