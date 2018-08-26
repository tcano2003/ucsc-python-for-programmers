#!/usr/bin/env python3
"""static.py (Optional) Class variables are supported and
work nicely, as expected, but there is no obvious way to
call a method unless you have an object."""  

class Static:
    number = 0

    def __init__(self):
        Static.number += 1
        self.number = self.number
        # or, more explicitly: self.number = Static.number


    def __str__(self):
        return "%d of %d" % (self.number, Static.number) #Static.number reports 3, self.number reports 1-3

def main():
    objects = [Static() for i in range(3)]
    print (', '.join([str(obj) for obj in objects]))

if __name__ == '__main__':
    main()
