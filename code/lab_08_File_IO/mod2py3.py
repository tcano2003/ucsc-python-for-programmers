#!/usr/bin/env python3
"""You can keep your identifiers from being imported with
from ... import * by prefixing a '_' to the name."""

_immutable = 1    
_mutable = [1, 2, 3]

def PrintImmutable():
    print (_immutable)

def PrintMutable():
    print (_mutable)

