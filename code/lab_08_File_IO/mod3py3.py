#!/usr/bin/env python3
"""__all__ specifies attributes for export"""

__all__ = ("PrintImmutable", "PrintMutable")  # only these would be imported with the "from mod3 import *"

immutable = 1      # can import mod3 as other (or another name) to make it more readable  
mutable = [1, 2, 3]  

def PrintImmutable():  
    print (immutable)

def PrintMutable():
    print (mutable)
