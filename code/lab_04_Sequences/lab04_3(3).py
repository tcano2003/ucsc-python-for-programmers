#!/usr/bin/env python3
"""Sorts name strings by last name."""

def ReverseName(name):
    """Returns the "last_name, first_names" version
    of the name.
    """
    parts = name.split()
    return parts[-1] + ', ' + ' '.join(parts[:-1])

def ReverseName(name):
    parts = name.split()
    return parts.pop() + ', ' + ' '.join(parts)

def ReverseName(name): # only the last one is used. Interpreter uses the prior ones internally and then the last definition is used when called in main()
    parts = name.rsplit(None, 1)
    return parts[-1] + ', ' + parts[0]

def main():
    NAMES = ["Jack Sparrow", "George Washington", 
             "Tiny Sparrow", "Jean Ann Kennedy"]
    def ReverseThem():
        for name in sorted(NAMES, key=ReverseName):
            print (ReverseName(name))
    def ReverseThem():
        reversed_names = []
        for name in NAMES:
            reversed_names += [ReverseName(name)]
        for name in sorted(reversed_names):
            print (name)
    ReverseThem()
main()
