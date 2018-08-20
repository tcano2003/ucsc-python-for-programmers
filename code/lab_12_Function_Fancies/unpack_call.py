#!/usr/bin/env python
"""Sequences and dictionaries can be unpacked into 
a argument list with the * and ** operators.
"""
def AddNewWords(translate_d, name, language='Spanish',
                *extra_args, **extra_keyworded_args): 
    print "%s translating to %s" % (name, language) 
    for word in extra_args:
        translate_d[word] = raw_input('%s: ' % word)
    if extra_keyworded_args:
        print "New words:"
        for word in extra_keyworded_args:
            print "%s -> %s" % (word,
                              extra_keyworded_args[word])
        translate_d.update(extra_keyworded_args)

def PrintDictionary(any_dictionary):
    print "\n".join(["%+10s -> %s" % (k,any_dictionary[k])
                     for k in sorted(any_dictionary)])
def main():
    english_spanish = {}
    sequence = english_spanish, 'Ana'
    AddNewWords(*sequence)
    bigger_sequence = (english_spanish, 'Emeliano',
                       'espa~ol', 'carrot', 'peanut')
    AddNewWords(*bigger_sequence)
    numbers_d = {'one':'uno', 'two':'dos', 
                 'three':'tres', 'four':'cuatro'}
    sequence = list(sequence) + ['Spanish']
    sequence[1] = 'Pancho'
    print "sequence =", sequence
    AddNewWords(*sequence, **numbers_d)
    food_d = {'bread':'pan', 'cheese':'queso'}
    AddNewWords(english_spanish, 'Margarita', 'Spanish', *food_d)
    # This gets a SyntaxError
    # AddNewWords(*sequence, *food_d)
    sequence[1] = 'Raul'
    words = ['grapefruit', 'orange']
    AddNewWords(*(sequence + words))
    PrintDictionary(english_spanish)

if __name__ == '__main__':
    main()
