#!/usr/bin/env python
"""__all__ specifies attributes for export"""

__all__ = ("PrintImmutable", "PrintMutable")  

immutable = 1        
mutable = [1, 2, 3]  

def PrintImmutable():  
    print immutable

def PrintMutable():
    print mutable
