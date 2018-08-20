#!/usr/bin/env python
"""Using the OpenClose context manager class. """

import context  

def WriteFile(file_name, text):
    try:
        with context.OpenClose(file_name, "w") as file_object:
            file_object.write(text)
    except IOError, info:
        print info

if __name__ == '__main__':
    WriteFile("sometimes", "Sometimes you win.\n")

