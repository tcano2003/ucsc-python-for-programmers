#!/usr/bin/env python
"""lab08_3 again.  This time using the builtin file
iterator, so that all the file isn't in memory at one time,
and using tempfile."""
import os
import shutil
import tempfile   
import do_swap

def Swapper(file_name, apple, orange):
    """ Changes the text in the file, replacing apples with
    oranges and oranges with apples."""
    try:
        open_file = open(file_name)
    except IOError, info:
        print "Cannot open", file_name, 'because', info
        return
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    try:
        for line in open_file:
            swapped_line = do_swap.DoSwap(line, apple, orange)
            temp_file.write(swapped_line)
    finally:
        open_file.close()
        temp_file.close()
    os.rename(temp_file.name, file_name) # For Windows, first:
                                         # os.remove(file_name)
def main():                              
    shutil.copy('cats.txt', 'cats2.txt')
    Swapper('cats2.txt', 'cat', 'dog')
    Swapper('www.txt', 'www', 'yyy')

if __name__ == '__main__':
    main()
