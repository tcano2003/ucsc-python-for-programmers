#!/usr/bin/env python3
"""Demonstrates the key keyword for list.sort.
"""

def MagicNumber(string): # this is string manipulation. A key is generated based on the added value of positions of all char in the names.
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
    print ("MagicNumber keys:", sort_keys)
        
def main():
    names = ["June", "Alejandro", "Ann", "I", "Izzy"]

    print ("            Names list:", names)
    print ("          Default sort:", sorted(names)) #new list where sorted alpha
    print ("      Sorted by length:", sorted(names, key=len)) #new list sorted by length of string (# of characters). By default, in the case of same length, the string that came first will be first, not by alpha, would have to specify this
    ReportInternalSortKey(names)
    names.sort(key=MagicNumber)
    print ("Sorted by magic number:", names)

main()
