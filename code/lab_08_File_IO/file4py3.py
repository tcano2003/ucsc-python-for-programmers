#!/usr/bin/env python3
"""The finally can be attached to the try/except since 
Python 2.5.  But, the finally always happens last, and
doesn't re-raise.
"""
def PrintFile(file_name, fail_on_read=False): 
    try:                                      
        file_obj = open(file_name)            
        for line in file_obj:
            print (line, end='')
            if fail_on_read:
                raise IOError, "Failed while reading."
    except IOError, info:
        print info
    finally:
        print ("Finally")
        try:
            file_obj.close()
        except UnboundLocalError:
            pass

def main(file_name="ram.tzu"):
    """Same main as file3.py
    """
    print ("""\nCalling PrintFile("%s")""" % (file_name))
    PrintFile(file_name)
    print ("""\nCalling PrintFile("%s", fail_on_read=True)""" % (
        file_name))
    PrintFile(file_name, fail_on_read=True)
    print ("""\nCalling PrintFile("absent_file")""")
    PrintFile("absent_file")

if __name__ == '__main__':
    main()
