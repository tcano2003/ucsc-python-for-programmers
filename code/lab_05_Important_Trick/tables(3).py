#!/usr/bin/env python3
"""Unwraps and prints out a 2-D sequence.
Note that the testing only happens when this module
is the "__main__" module.
"""
def PrintTable(table):
    """Prints out a 2-D sequence"""
    for row in table:
        for column in row:
            print (column, end='')
        print ()
    print ()

def Test():
    tests = (["Hi", "Hola"], 
             (('H','i'), ('H','o','l','a')), 
             [["Hi"], ["Hola"]]
             )
    for test in tests:
        print (test)
        PrintTable(test)

if __name__ == '__main__': # prevents the test code from being run if the module is being imported
    Test()
