#!/usr/bin/env python
"""(Optional) Here is the other way to make an iterator,
from scratch."""

import new_style_circle_def

class IterCircle(new_style_circle_def.Circle):

    def __iter__(self):
        """Returns an object that has a next() method that 
        raises a StopIteration error when it has exhausted
        all the data.
        """
        class CircleIter:
            def __init__(inner_self):
                inner_self.starting_data = self[:]
                inner_self.data_to_pop = self[:]
                inner_self.times = self.times

            def next(inner_self):
                while True:
                    try:
                        return inner_self.data_to_pop.pop(0)
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
