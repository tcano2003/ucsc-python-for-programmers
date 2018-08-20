#!/usr/bin/env python
"""(Optional)
@staticmethod and @classmethod built-in decorators let you 
invoke methods without having objects."""

import static  
               
class Static2(static.Static):

    @classmethod                   
    def JumpUp(cls, number):      # cls will be the class
        print 'In classmethod(JumpUp), cls =', cls
        static.Static.number += number

    @staticmethod
    def StartOver():           # no self for a static method!
        static.Static.number = 0

def main():
    objects = [Static2() for i in range(3)]
    print """3 objects:
    """, ', '.join([str(obj) for obj in objects])
    Static2.StartOver()
    objects += [Static2() for i in range(3)]
    print """After StartOver() and 3 more objects:
    """, ', '.join([str(obj) for obj in objects])
    Static2.JumpUp(100)
    objects += [Static2() for i in range(3)]
    print """After JumpUp(100) and 3 more objects:
    """, ', '.join([
        str(obj) for obj in objects])

if __name__ == '__main__':
    main()
