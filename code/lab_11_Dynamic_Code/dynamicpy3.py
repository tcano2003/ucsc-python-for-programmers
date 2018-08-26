#!/usr/bin/env python3
"""Demonstrates the exec statement and eval function, used
for dynamic code generation.
""" 
import sys 

ATTRIBUTES = ("name", "zip", "phone", "SSN")

def GetAttributes(attributes):
    for each in attributes:
        answer = input("%s please: " % each)
        exec("%s = '%s'" % (each, answer) in globals()) """globals that gives
        dictionary of all global identifiers (keys are strings and values are values)"""

def PrintAttributes(attributes):
    for each in attributes:
        print (each, '=', eval(each))

def main():
    if len(sys.argv) > 1:
        attributes = sys.argv[1:]
    else:
        attributes = ATTRIBUTES
    GetAttributes(attributes)
    PrintAttributes(attributes)

main()
