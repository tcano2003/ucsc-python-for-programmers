#!/usr/bin/env python
"""Variable length argument lists are supported big time.
"""  

def AddNewWords(translate_d, name, language='Spanish',   
                *extra_args, **extra_keyworded_args):   
    print "%s translating to %s" % (name, language)
    for word in extra_args:
        translate_d[word] = raw_input('%s: ' % word)
    if extra_keyworded_args:
        print "New words:"
        for word in extra_keyworded_args:
            print "%s: %s" % (word,
                              extra_keyworded_args[word])
        translate_d.update(extra_keyworded_args)

def PrintDictionary(any_dictionary):
    print """
Your Dictionary:
"""
    print "\n".join(["%+10s:%s" % (k,any_dictionary[k])
                     for k in sorted(any_dictionary)])
def main():
    english_spanish = {}
    AddNewWords(english_spanish, 'Ana')
    AddNewWords(english_spanish, 'Emeliano', 'espa~ol',
                'carrot', 'peanut')
    AddNewWords(english_spanish, 'Pancho', 'carrot',
                'grapefruit')
    AddNewWords(english_spanish, 'Joaquin', 'Spanish',
                'orange', 'butter',
                bread='el pan', cheese='el queso')
    AddNewWords(english_spanish, 'Maria', strawberry='la fresa')
    PrintDictionary(english_spanish)

if __name__ == '__main__':
    main()

