#!/usr/bin/env python3 
"""Function definitions come before any calls in the 0th
column. 
"""
def StrumGuitar(measures):
    for measure in range(measures):
        print ('strum. strum.')
    BeatDrum(measures)

def BeatDrum(measures):
    for measure in range(measures):
        print ('boom! boom!')

StrumGuitar(2)
