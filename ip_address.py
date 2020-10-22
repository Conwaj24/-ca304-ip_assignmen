#!/bin/env python

class ip_address_v4():
    def __init__(self, addr):
        #TODO type checking of input
        self.set_addr_string(addr)

    def set_addr_string(self, addr: str):
        octets = [int(octet) for octet in addr.split('.')]
        assert len(octets) == 4
        assert all([0 <= i and i <= 0xff for i in octets])

        self.string = addr
        self.octets = octets
        self.value = sum([self.octets[i] * 0x100 ** (3-i) for i in range(4)])

    def set_addr_int(self, addr: int):
        assert 0 <= addr and addr <= 0xffffffff
        self.value = addr

        #self.octets = [self.value & (0xff000000 << 0o10 *) for i in range(4)
        self.octets = [
                self.value & 0xff000000 >> 24,
                self.value & 0xff0000 >> 16,
                self.value & 0xff00 >> 8,
                self.value & 0xff
                ]
        self.string = str(self)


    def __int__(self):
        return self.value

    def __str__(self):
        if self.string:
            return self.string
        elif self.octets:
            return '.'.join([str(octet) for octet in self.octets])
        else:
            return

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
    ip0 = ip_address_v4("0.0.0.0")
    ip1 = ip_address_v4("0.0.0.1")
    ip2 = ip_address_v4("0.0.0.255")
    ip3 = ip_address_v4("192.168.1.2")
    ip4 = ip_address_v4("255.255.255.255")

    assert(ip0 == 0)
    assert(ip0 < ip1)
    assert(ip4 > ip3)
    assert(ip0 <= ip2)
    assert(ip3 >= ip3)
    assert(ip4 == 0xffffffff)

    print(ip4)
    print(int(ip0), int(ip1), int(ip2), int(ip4))
    print(ip3[1])

if __name__ == "__main__":
    main()

