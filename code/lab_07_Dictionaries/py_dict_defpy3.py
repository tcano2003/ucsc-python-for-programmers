#!/usr/bin/env python3
"""Dictionary implementation for demonstrating a
   Python dictionary."""

def SetUpPyDict():
    py_dict = {}   # empty dictionary

    # initializing a dictionary

    py_dict2 = {'break':'break from a loop and skip the else',
                'continue':'go to the next iteration',
                'for':'set up looping'} 

    # Updating py_dict1 with py_dict2's keys and values.  
    # If py_dict2 has keys already in py_dict, py_dict2's
    # values will replace the old values for the key.

    py_dict.update(py_dict2)     #update is a method of dictionary

    # And you can just add an entry

    py_dict['pass'] = 'throw the ball' #[key], value

    # If you add an entry with a duplicate key, the new 
    # meaning will be the one that sticks:

    py_dict['pass'] = 'do nothing' #[key], value. Overwrites the previous value

    return py_dict #returning the value to the py_dict{}


def CollectEntries(py_dict):
    """Collects a bunch of new entries for the dictionary"""
    while True:
        word = input('Word: ')
        if not word:
            return
        meaning = input('Meaning: ')
        py_dict[word] = meaning # [word] is the key

def FindDefinitions(py_dict):
    """Reports a key:value pair for a given key"""
    while True:
        word = input('Word to find: ')
        if not word:
            return
        try:
            print ('%s : %s' % (word, py_dict[word]))
        except KeyError:
            print ('%s is not in the dictionary.' % word)

def MakePrompt(choices):
    choice_list = sorted(choices)
    guts = ', '.join(['(%s)%s' % (choice[0], choice[1:])
                      for choice in choice_list])
    return 'Choose ' + guts + ' (enter to quit) '

def PrintEntries(py_dict):
    """Prints out the dictionary entries, sorted by key"""
    for word in sorted(py_dict):
        print ('%s : %s' % (word, py_dict[word]))

def RunMenu(py_dict):
    """Runs the user interface for dictionary manipulation."""
    # The choices dictionary has function names for values.
    choices = {'add': CollectEntries, 'find': FindDefinitions,
               'print': PrintEntries} #key is the label, values are identifiers of functions
    prompt = MakePrompt(choices)

    while True:
        raw_choice = input(prompt)
        if not raw_choice:
            break
        given_choice = raw_choice[0].lower() #make the input lowercase
        for maybe_choice in choices: #pass keys (can sort: sorted(choices))
            if maybe_choice[0] == given_choice: #maybe_choice[0] is the key
                # The appropriate function is called
                # using the dictionary value for the name
                # of the function.    
                choices[maybe_choice](py_dict) #
                break
        else:
            print ('%s is not an acceptable choice.' % raw_choice)

def main():
    py_dict = SetUpPyDict()
    RunMenu(py_dict)

if __name__ == '__main__':
    main()
