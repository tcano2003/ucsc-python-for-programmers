#!/usr/bin/env python3
"""(Optional) Here is the other way to make an iterator,
from scratch."""

import new_style_circle_defpy3 as new_style_circle_def

class IterCircle(new_style_circle_def.Circle):

    def __iter__(self): #generator function returns CircleIter(), has a next() in it
        """Returns an object that has a next() method that 
        raises a StopIteration error when it has exhausted
        all the data.
        """
        class CircleIter:
            def __init__(inner_self):
                inner_self.starting_data = self[:] #copy of the starting data
                inner_self.data_to_pop = self[:] #another copy to prepare for popping
                inner_self.times = self.times

            def next(inner_self): # need a different self. When next is called, returns next thing to pop. Next function is builtin to Python 3. For open file and then do the for loop on it. c=CircleIter('around', 3) for item in c-i:
                while True:
                    try:
                        return inner_self.data_to_pop.pop(0) #if nothing left to pop
                    except IndexError:
                        pass
                    inner_self.times = inner_self.times - 1
                    if inner_self.times == 0:
                        raise StopIteration
                    inner_self.data_to_pop = inner_self.starting_data[:]

        return CircleIter()

"""
Same output as new_style_circle_def.py with same testing.
"""
def main():
