#!/usr/bin/env python
"""
Copy the cats.txt into your area.  Change the file so
that all the cats become dogs and dogs become cats.
"""
import do_swap
import shutil  

def Swapper(file_name, apple, orange):
    """ Changes the text in the file, replacing apples with
    oranges and oranges with apples."""
    try:
        open_file = open(file_name, "r+")
    except IOError, info:
        print "Can't open", file_name, 'because', info
        return
    try:  # Putting the whole file in memory!
        text = open_file.read()  
        text = do_swap.DoSwap(text, apple, orange)
        open_file.seek(0, 0)
        open_file.truncate() 
        open_file.write(text)
    finally:
        open_file.close()

def main():
    shutil.copy('cats.txt', 'cats2.txt')
    Swapper('cats2.txt', 'cat', 'dog')
    Swapper('www.txt', 'www', 'yyy')

if __name__ == '__main__':
    main()
