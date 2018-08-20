#!/usr/bin/env python
"""A Circle class, derived from the builtin list class.

All the facilities of a list are available for free,
for using or overridding.
"""             

class Circle(list):

    def __init__(self, data, times):
        list.__init__(self, data)
        self.times = times

    def __getitem__(self, i):
        """circle[i] --> Circle.__getitem__(circle, i)."""
        l_self = len(self)
        if i >= self.times * l_self:
            raise IndexError, "Circle object goes around %d times" % self.times
        return list.__getitem__(self, i % l_self)

    def __iter__(self):
        """Because we are inheriting from list, and it has
        its own __iter__, we need to override it to get all
        the functionality we had before.
        """
        for i in range(self.times * len(self)):
            yield self[i]

def main():
    """Same main as lab_13_Magic.circle_def
    """
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
def TestList():
    circle = Circle("tic", 3)

    print "Testing list functions:", circle
    circle += 'k'
    print [x for x in circle]
    circle.sort()
    print circle

if __name__ == '__main__':
    main()
    TestList()

