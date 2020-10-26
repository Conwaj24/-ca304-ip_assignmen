#!/bin/env python

from binutils import leading_1s

class ip_address_v4():
    def __init__(self, addr):
        if isinstance(addr, str):
            self.set_addr_string(addr)
        elif isinstance(addr, int):
            self.set_addr_int(addr)
        else:
            raise TypeError("addr must be of type str or int, not {}".format(type(addr)))

    def set_addr_string(self, addr: str):
        octets = [int(octet) for octet in addr.split('.')]
        assert len(octets) == 4
        assert all([0 <= i and i <= 0xff for i in octets])

        self.octets = octets
        self.value = sum([self.octets[i] * 0x100 ** (3-i) for i in range(4)])

    def set_addr_int(self, addr: int):
        assert 0 <= addr and addr <= 0xffffffff
        self.value = addr

        self.octets = [(self.value & (0xff << 8 * i)) >> 8 * i for i in range(4)][::-1]

    def __int__(self):
        return self.value

    def __str__(self):
        return '.'.join([str(octet) for octet in self.octets])

    def __lt__(self, other): # <
        return int(self) < int(other)

    def __gt__(self, other): # >
        return int(self) > int(other)

    def __le__(self, other): # <=
        return int(self) <= int(other)

    def __ge__(self, other): # >=
        return int(self) >= int(other)

    def __eq__(self, other): # ==
        return int(self) == int(other)

    def __add__(self, other): # +
        return type(self)(int(self) + int(other))

    def __sub__(self, other): # -
        return type(self)(int(self) - int(other))

    def __and__(self, other): # &
        return ip_address_v4((int(self) & int(other)))

    def __getitem__(self,i):
        return self.octets[i]

class ip_address_cidr(ip_address_v4):
    def __init__(self, addr, mask: ip_address_v4):
        super().__init__(addr)
        self.mask = mask
        self.network_bits = leading_1s(int(self.mask))
        self.host_bits = 34 - self.network_bits #TODO explain where 34 comes from


    def __str__(self):
        return "{}/{}".format(super().__str__(), self.network_bits)


def main():
    ip0 = ip_address_v4("0.0.0.0")
    ip1 = ip_address_v4("0.0.0.1")
    ip2 = ip_address_v4("0.0.0.255")
    ip3 = ip_address_v4("192.168.1.2")
    ip4 = ip_address_v4("255.255.255.255")

    try:
        ip_address_v4(0.1)
    except TypeError:
        pass


    assert(ip0 == 0)
    assert(ip0 < ip1)
    assert(ip4 > ip3)
    assert(ip0 <= ip2)
    assert(ip3 >= ip3)
    assert(ip4 == 0xffffffff)

    print(ip4)
    print(int(ip0), int(ip1), int(ip2), int(ip3), int(ip4))
    print(ip3[1])

    assert(str(ip0) == str(ip_address_v4(0)))
    assert(str(ip1) == str(ip_address_v4(1)))
    assert(str(ip2) == str(ip_address_v4(0xff)))
    assert(str(ip3) == str(ip_address_v4(3232235778)))
    assert(str(ip4) == str(ip_address_v4(0xffffffff)))

    ipc = ip_address_cidr("192.168.10.0", ip_address_v4("255.255.255.192"))
    print(ipc)

if __name__ == "__main__":
    main()
