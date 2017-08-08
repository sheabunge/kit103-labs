"""
For KIT103/KMA115 Practical 3: Set combinations & bitsets
Revised: 2015-07-14
Author: James Montgomery (james.montgomery@utas.edu.au)

A small collection of functions for converting sets to bitsets and
bitsets back to sets. Useful for verifying that a hand-crafted binary
string really does represent the set you think it does.
"""


# Some bitset routines
def set2bits(s, u):
    """Converts the set s to a compact integer representation given
    the universe u. u may be any collection type, but if it is a list
    then it must contain no duplicates and already be sorted.
    """
    ulist = sorted_universe(u)
    bitset = 0
    for e in s:
        # FYI: << (left shift) moves the bits (for the number 1 in this case)
        #     left to the location corresponding to the element e
        i = 1 << ulist.index(e)
        bitset = bitset | i
    return bitset


def bits2set(bitset, u):
    """Returns a set from a compact bitset, given the universe u.
    u may be any collection type, but if it is a list then it must
    contain no duplicates and already be sorted.
    """
    ulist = sorted_universe(u)
    s = set()
    for i in range(len(u)):
        if bitset & (1 << i):
            s.add(ulist[i])
    return s


def sorted_universe(u):
    """Returns a sorted list of the elements of u, unless u is a list,
    in which case it is returned unchanged.
    """
    return u if isinstance(u, list) else sorted(u)


# Some alternative versions of the above that behave the same but are compact
# and a little cryptic. They've been included for the programmers who'd like to
# learn a little more Python while learning maths, which is what this unit is
# actually about.

from functools import reduce


def alt_set2bits(s, u):
    """A 'Pythonic' version of set2bits."""
    ulist = sorted_universe(u)
    return reduce(lambda r, e: r | (1 << ulist.index(e)), s, 0)


def alt_bits2set(bs, u):
    """A 'Pythonic' version of bits2set."""
    ulist = sorted_universe(u)
    return {ulist[i] for i in range(len(u)) if bs & (1 << i)}
