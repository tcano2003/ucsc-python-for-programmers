#!/usr/bin/env python3
"""
Demonstrates the setattr and getattr functions for dynamic
code generation, which is preferred to exec and eval.

The first argument to setattr and getattr is the namespace
where you expect the variable to land.  sys.modules is
helpful here if you want it in the current namespace.
""" 
import sys 

ATTRIBUTES = ("name", "zip", "phone", "SSN")

def GetAttributes(attributes):
    for each in attributes:
        answer = input("%s please: " % each)
        setattr(sys.modules[__name__], each, answer) # becomes an identifer for the value (answer)

def PrintAttributes(attributes):
    for each in attributes:
        print (each, '=', getattr(sys.modules[__name__], each))

def main():
    """Same main() as dynamic.py.
    """
    if len(sys.argv) > 1:
        attributes = sys.argv[1:]
    else:
        attributes = ATTRIBUTES
    GetAttributes(attributes)
    PrintAttributes(attributes)

if __name__ == '__main__':
    main()

