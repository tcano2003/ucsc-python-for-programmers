#!/usr/bin/env python 
"""Function with one argument and one return value."""

def DoubleIt(x):

    """Function doc comes first, if the name (which
    is a verb according to the style guide) isn't
    sufficient documentation.
    """
    return 2 * x

print DoubleIt(2)
print DoubleIt("Hi")
print DoubleIt(2.2)
