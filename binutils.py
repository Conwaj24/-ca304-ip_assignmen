#!/bin/env python

def first_0(num):
    return bin(num)[2:].index('0')

def leading_1s(num):
    try:
        return first_0(num)
    except ValueError:
        return len(bin(num)) - 2

def main():
    assert(leading_1s(0b000000) == 0)
    assert(leading_1s(0b110000) == 2)
    assert(leading_1s(0b111111) == 6)
    assert(leading_1s(0b1111110) == 6)
    pass

if __name__ == "__main__":
    main()

