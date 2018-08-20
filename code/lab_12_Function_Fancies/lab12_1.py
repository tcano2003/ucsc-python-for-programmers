#!/usr/bin/env python
"""lab12_1.py -- a Printf function"""
import sys

def Printf(format, *args):
    """Emulates C-like printf function."""
    sys.stdout.write(format % args)

def Printfx(format, *args):
    """This one almost always works."""
    print format % args,

def main(Function):
    print 'Testing', Function.__name__
    Function('%d black cats drank %d plates of milk.\n', 4, 2)
    Function('%d', 3)
    Function('%d\n', 3)
    Function('Hello World\n')

if __name__ == '__main__':
    main(Printfx)
    main(Printf)

