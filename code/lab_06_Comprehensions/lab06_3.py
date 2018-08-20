#!/usr/bin/env python
"""
lab06_3.py Provides a MakeString function that receives a
sequence of any objects, and optionally, a glue string and
returns string containing all of the elements, each separated 
by the glue string.  The default glue string should be ', '.
"""
def MakeString(sequence, glue=', '):
    return glue.join([str(obj) for obj in sequence])

def main():
    print MakeString(range(10, 0, -1))
    print MakeString(('1', 2, 'word'), '*')

if __name__ == '__main__':
    main()
