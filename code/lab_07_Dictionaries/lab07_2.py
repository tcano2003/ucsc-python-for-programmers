#!/usr/bin/env python
"""Dictionary implementation for demonstrating a dictionary.

   ... with a new option will print out the dictionary 
   alphabetically by the meanings. """

from py_dict_def import *  # Careful of this!

def ListDefinitions(py_dict):
    """Prints out the dictionary, alphabetically by the
    meanings"""
    defs = [] 
    for k, v in py_dict.items(): 
        defs += [(v, k)]
    # or: defs = [(v, k) for (k, v) in py_dict.items()]        
    defs.sort()
    for (v, k) in defs:
        print v, ':', k

def ListDefinitions(py_dict):
    """Prints out the dictionary, alphabetically by
    the meanings -- implemented via the sort key option."""
    def ValueKey(k):
        return py_dict[k]

    for each in sorted(py_dict, key=ValueKey):
        print py_dict[each], ':', each

def RunMenu(py_dict):
    """Runs the user interface for dictionary manipulation."""
    choices = {'add': CollectEntries,
               'definitions': ListDefinitions,
               'find': FindDefinitions, 'print': PrintEntries}
    prompt = MakePrompt(choices)
    while True:
        raw_choice = raw_input(prompt)
        if not raw_choice:
            break
        given_choice = raw_choice[0].lower()
        for maybe_choice in choices:
            if maybe_choice[0] == given_choice:
                choices[maybe_choice](py_dict)
                break
        else:
            print '%s is not an acceptible choice.' % raw_choice

def main():
    py_dict = SetUpPyDict()
    RunMenu(py_dict)

if __name__ == '__main__':
    main()
