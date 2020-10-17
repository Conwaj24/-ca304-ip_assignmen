#!/bin/env python

class ip_address_v4():
    def __init__(self, addr: str):
        self.octets = [int(octet) for octet in addr.split('.')]
        assert len(self.octets) == 4
        assert all([0 <= i and i <= 255 for i in self.octets])

        self.value = sum([self.octets[i] * 255 ** (3-i) for i in range(4)])

    def __int__(self):
        return self.value

    def __str__(self):
        return '.'.join([str(octet) for octet in self.octets])

    def __lt__(self, other):
        return int(self) < int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __le__(self, other):
        return int(self) <= int(other)

    def __ge__(self, other):
        return int(self) >= int(other)

    def __eq__(self, other):
        return int(self) == int(other)

    def __getitem__(self,i):
        return self.octets[i]



def main():
    ip0 = ip_address("0.0.0.0")
    ip1 = ip_address("0.0.0.1")
    ip2 = ip_address("0.0.0.255")
    ip3 = ip_address("192.168.1.2")
    ip4 = ip_address("255.255.255.255")

    assert(ip0 == 0)
    assert(ip0 < ip1)
    assert(ip4 > ip3)
    assert(ip0 <= ip2)
    assert(ip3 >= ip3)

    print(ip4)
    print(int(ip0), int(ip1), int(ip2), int(ip4))
    print(ip3[1])

if __name__ == "__main__":
    main()

