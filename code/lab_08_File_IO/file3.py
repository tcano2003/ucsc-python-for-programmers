#!/usr/bin/env python
"""Demonstrates the 'finally' clause -- and making it happen.
"""    
def PrintFile(file_name, fail_on_read=False):
    try:
        open_file = file(file_name) #file is an alias for open
        try:                 
            for line in open_file:
                print line,
                if fail_on_read:
                    raise IOError, "Failed while reading."
        finally:
            print "Finally"
            open_file.close()
    except IOError, info:
        print info

def main(file_name="ram.tzu"):
    print """\nCalling PrintFile("%s")""" % (file_name)
    PrintFile(file_name)
    print """\nCalling PrintFile("%s", fail_on_read=True)""" % (
        file_name)
    PrintFile(file_name, fail_on_read=True)
    print """\nCalling PrintFile("absent_file")"""
    PrintFile("absent_file")

if __name__ == '__main__':
    main() 
