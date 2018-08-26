#!/usr/bin/env python3
"""Using the OpenClose context manager class. """

import contextpy3 as context 

def WriteFile(file_name, text):
    try:
        with context.OpenClose(file_name, "w") as file_object:
            file_object.write(text)
    except IOError as e:
        print (e)

if __name__ == '__main__':
    WriteFile("sometimes", "Sometimes you win.\n")

