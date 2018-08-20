#!/usr/bin/env python
"""Uses os.walk() and the previous exercise to change
all the cats to dogs and dogs to cats through a directory
structure."""

import os
import sys
import shutil
import lab08_3 as swapper   # was the previous exercise

def SwapTextFiles(starting_dir, swappers):
    """ Changes the text in a files in the starting_dir 
    directory structure. swappers is a tuple of strings
    to swap.
    """
    apple, orange = swappers # let errors raise to caller

    for this_dir, dir_names, file_names in os.walk(starting_dir):
        for file_name in file_names:
            whole_path = os.path.join(this_dir, file_name)
            swapper.Swapper(whole_path, apple, orange)

def PrintDeepFiles(starting_dir):
    for this_dir, dir_names, file_names in os.walk(starting_dir):
        for file_name in file_names:
            whole_path = os.path.join(this_dir, file_name)
            print whole_path + ':'
            file_object = open(whole_path)
            for line in file_object:
                print line,
            file_object.close()
            print "---"

def main():
    if len(sys.argv) > 1:
        starting_dir = sys.argv[1]
    else:
        try:
            shutil.rmtree("cats2")
        except OSError: # not there
            pass
        shutil.copytree("./cats", "./cats2")
        starting_dir = 'cats2'
    PrintDeepFiles(starting_dir)
    SwapTextFiles(starting_dir, ('cat', 'dog'))
    PrintDeepFiles(starting_dir)

if __name__ == '__main__':
    main()
