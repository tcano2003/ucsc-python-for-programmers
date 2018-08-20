#!/usr/bin/env python
"""
Reports the number of vowels in the directory structure given.
"""
import os, sys
import lab08_2 as count_vowels_in_file

def CountVowelsInDir(dir_name):
    total = 0
    for this_dir, dir_names, file_names in os.walk(dir_name):
        for file_name in file_names:
            whole_path = os.path.join(this_dir, file_name)
            total += \
            count_vowels_in_file.CountVowelsInFile(whole_path)
    return total

def main(dir_name="cats"):
    print "%d vowels in %s directory"  % (
        CountVowelsInDir(dir_name), dir_name)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
