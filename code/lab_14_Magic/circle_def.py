#!/usr/bin/env python
"""A Circle class, acheived by overriding __getitem__
which provides the behavior for indexing, i.e., [].
This also provides the correct cyclical behavior whenever
an iterator is used, i.e., for, enumerate() and sorted().
reversed() needs __reversed__ defined.
"""

class Circle: 

    def __init__(self, data, times):
        """Put the 'data' in a circle that goes around
        'times' times."""
        self.data = data
        self.times = times

    def __getitem__(self, i): 
        """circle[i] --> Circle.__getitem__(circle, i)."""
        l_self = len(self)
        if i >= self.times * l_self:
            raise IndexError, "Circle object goes around %d times" % (self.times)
        return self.data[i % l_self]

    def __len__(self):
        return len(self.data)

def main():
    circle = Circle("around", 3)

    print "Works with circle[i], for i > len(circle) too:"
    for i in range(3 * len(circle) + 1):
        try:
            print "circle[%2d] = %s" % (i, circle[i])
        except IndexError, info:
            print info
            break

    print "Works with sorted:"
    print sorted(circle)

    print "Works for loops:"
    small_circle = Circle("XO", 2)
    for i, elementi in enumerate(small_circle):
        print "small_circle[%d] = %s" % (i, elementi)

        
    print "Works for nested loops:"
    for i, elementi in enumerate(small_circle):
        for j, elementj in enumerate(small_circle):
            print "%3d:%3d -> %s%s" % (i, j,
                                    elementi, elementj)

if __name__ == '__main__':
    main()

