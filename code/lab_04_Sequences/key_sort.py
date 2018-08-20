#!/usr/bin/env python
"""Demonstrates the key keyword for list.sort.
"""

def MagicNumber(string):
    """Returns the sum of the mapping of each
    character into its place in the alphabet.
    """
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    total = 0
    for char in string.lower():
        total += ALPHABET.index(char)
    return total

def ReportInternalSortKey(names):
    """Reports the tuple that the sort will use when this
    function is named as the 'key'.
    """
    sort_keys = []
    for name in names:
        sort_keys += [(MagicNumber(name), name)]
    print "MagicNumber keys:", sort_keys
        
def main():
    names = ["June", "Alejandro", "Ann", "I", "Izzy"]

    print "            Names list:", names
    print "          Default sort:", sorted(names)
    print "      Sorted by length:", sorted(names, key=len)
    ReportInternalSortKey(names)
    names.sort(key=MagicNumber)
    print "Sorted by magic number:", names

main()
