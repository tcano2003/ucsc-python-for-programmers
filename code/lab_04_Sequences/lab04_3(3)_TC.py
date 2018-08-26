#!/usr/bin/env python3
"""Sorts name strings by last name."""

def ReverseName(name):
    """Returns the "last_name, first_names" version
    of the name.
    """
    parts = name.split() #default split is whitespace
    return parts[-1] + ', ' + ' '.join(parts[:-1]) # last
    #return parts[-1] + ', ' + ' '.join(parts[:-1])
    #

def ReverseName(name):
    parts = name.split()
    return parts.pop() + ', ' + ' '.join(parts) # take out last element and return 

def ReverseName(name): # only the last one is used. Interpreter uses the prior ones internally and then the last definition is used when called in main()
    parts = name.rsplit(None, 1) # Set None since we want default, which is whitespace. Two pieces from the right, we 
    return parts[-1] + ', ' + parts[0]

def main():
    NAMES = ["Jack Sparrow", "George Washington", 
             "Tiny Sparrow", "Jean Ann Kennedy"]
    def ReverseThem(): # local function (used by interpreter)
        for name in sorted(NAMES, key=ReverseName): #sort the names and give key function. Specifying a sort key and put each name. Reverse name will come out and assocaited with key. swaps the names in place.
            print (ReverseName(name))
    def ReverseThem(): # local function (will be called)
        reversed_names = []
        for name in NAMES:
            reversed_names += [ReverseName(name)] #string lastname, firstname; reversename.append would work too
        for name in sorted(reversed_names):
            print (name)
    ReverseThem()
main()
