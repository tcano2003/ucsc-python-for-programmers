#!/usr/bin/env python3
"""Receives a format string for the first argument
and then it receives any number of additional arguemnts
as, one for each %d or other"""

import sys

def Printf(format, *args):
    sys.stdout.write(format % args)

def Printfx(format, *args):
    print (format % args)

def main(Function):
    print('Testing', Function.__name__)
    Function("%s and %s ate %d %s.", "Lynn", "Mary", 22, "grapes")
    Function("%s slid %d times.", "John", 3)

if __name__ == '__main__':
    main(Printfx)
    main(Printf)
