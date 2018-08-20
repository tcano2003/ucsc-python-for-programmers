#!/usr/bin/env python
"""Making a context manager.""" 

class OpenClose:

    def __init__(self, file_name, mode="r"):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.obj = open(self.file_name, self.mode)
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "Like finally: in __exit__", exc_type
        self.obj.close()

def PrintFile(file_name, fail_on_read=False):
    try:
        with OpenClose(file_name) as file_object:
            for line in file_object:
                print line,
                if fail_on_read:
                    raise IOError, "Failed while reading."
    except IOError, info:
        print info

def main(file_name="ram.tzu"):
    """Same main as file3.py
    """
    print """\nCalling PrintFile("%s")""" % (file_name)
    PrintFile(file_name)
    print """\nCalling PrintFile("%s", fail_on_read=True)""" % (
        file_name)
    PrintFile(file_name, fail_on_read=True)
    print """\nCalling PrintFile("absent_file")"""
    PrintFile("absent_file")

if __name__ == '__main__':
    main()

