#!/bin/env python

def first_0(num):
    num = int(num)
    return bin(num)[2:].index('0')

def leading_1s(num):
    num = int(num)
    try:
        return first_0(num)
    except ValueError:
        return len(bin(num)) - 2

def n1s_then_n0s(ones, zeros):
    """return a number represented in binary as the given number of 1s followed by the givewn number of 0s"""
    return (2 ** ones - 1) * 2 ** zeros

def xnor_all_with_verbose(compare, mask, *args):
    for arg in args:
        xnor = ~(compare ^ arg)
        print("{} ^ {} = {}".format(
            bin(int(compare)),
            bin(int(arg)),
            bin(int(xnor))
        ))
        newmask = mask & xnor
        print("{} & {} = {}".format(
            bin(int(mask)),
            bin(int(xnor)),
            bin(int(newmask))
        ))
        mask = newmask
    return mask

def xnor_all_with(compare, mask, *args):
    for arg in args:
        mask &= ~(compare ^ arg)
    return mask

def xnor_all(*args):
    """returns a number containing 1s in all bits that all args have in common and 0s in all other bits"""
    compare = args[-1]
    mask = ~(max(args) & 0)
    return xnor_all_with(compare, mask, *args[:-1])


def main():
    assert(leading_1s(0b000000) == 0)
    assert(leading_1s(0b110000) == 2)
    assert(leading_1s(0b111111) == 6)
    assert(leading_1s(0b1111110) == 6)
    pass

if __name__ == "__main__":
    main()

