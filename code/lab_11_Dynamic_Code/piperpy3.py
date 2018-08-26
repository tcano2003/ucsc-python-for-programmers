#!/usr/bin/env python3
"""piper.py (Optional) -- demonstrates running a shell-level
command.  Stdout is collected and piped into a file object 
which can be read as if it was an open file.
"""
import os, sys   
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))

import lab_10_Packages.apple.banana.total_text as total_text
import subprocess 

def Total_ps():
    """Returns the sum of all the numbers in a list
    of the processes running."""

    popen_obj = subprocess.Popen(("ps", "-ef"),
                                 stdout=subprocess.PIPE)
    open_pipe = popen_obj.stdout
    try:
        return total_text.TotalText(open_pipe.read())
    finally:
        open_pipe.close()

if __name__ == '__main__':
    print ("Your lucky number:", Total_ps())

