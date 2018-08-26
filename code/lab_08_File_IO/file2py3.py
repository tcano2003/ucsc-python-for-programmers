#!/usr/bin/env python3
"""Demonstrates the 'finally' clause.

Finally happens whether or not there's an exception and it 
passes the exception up to the surrounding try/except.

*  You cannot put an except and finally with the same try ...
   unless you are running Python 2.5+.
+  The finally clause happens, no matter what, even if there 
   is a return in the try clause.
"""

def PrintFile(f_name):  
    file_obj = open(f_name)
    try:
        for line in file_obj:
            print (line, end='')
    finally:
        file_obj.close()

def main(file_name="ram.txt"):
    try:
        PrintFile(file_name)
    except IOError, info:
        print (info)

if __name__ == '__main__':
    import sys
    try:
        main(sys.argv[1])
    except IndexError:
        main()

