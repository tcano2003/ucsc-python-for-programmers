#!/usr/bin/env python
"""Using os.walk to accumulate total through the files walked.
"""

import os
# When this is run in the lab_10_Packages, work_here needs a
# __init__.py.  apple also needs a __init__.py OR you must:
# import sys
# sys.path.insert(0, "apple")
# import work_here.lab10_1 as totaler

import apple.work_here_.lab10_1 as totaler

def TotalDeep(starting_dir):
    """Returns (no_of_files, total) where no_of_files is the
    number of files founds in the directory structure starting 
    at starting_dir, and total is the sum of all the numbers 
    found in those files.
    """
    total = no_of_files = 0
    for (this_dir, dir_names,
         file_names) in os.walk(starting_dir):
        for this_file in file_names:
            path_name = os.path.join(this_dir, this_file)
            try:
                total += totaler.TotalFile(path_name)
                no_of_files += 1
            except IOError, info:
                print path_name, info
    return (no_of_files, total)

def main():
    stats = TotalDeep('..')
    print "That's %d files, totaling to %d." % stats

if __name__ == '__main__':
    main()

