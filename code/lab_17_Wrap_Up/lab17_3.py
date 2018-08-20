#!/usr/bin/env python
"""lab17_3.py (Optional)-- collects 2 sides of a right 
triangle and prints the hypotenuse."""

import math

def GetXY(prompt):
    """Returns a tuple of 2 floats, or None if the user just
    hits the enter key or enters q."""

    while True:
        try:
            incoming = raw_input(prompt)
        except (KeyboardInterrupt, EOFError):
            return None
        if incoming == '' or incoming[0].lower() == 'q':
            return None
        try:
            x, y = [float(x) for x in incoming.split(',')]
        except (TypeError, NameError, ValueError, SyntaxError):
            print "Two numbers are required."
        else:
            return x,y

def Hypot(x, y):
    """Returns sqrt(x**2 + y**2)"""
    return math.hypot(x, y)  # or sqrt(x * x + y * y)

def main():
    while True:
        xy = (GetXY("Give me 2 sides of a right triangle:"
                " (x, y) "))
        if not xy:
            print
            break
        answer = Hypot(*xy)
        if answer < 0:
            continue
        print 'Hypotenuse is %.2f' % (answer)

if __name__ == '__main__':
    main()

