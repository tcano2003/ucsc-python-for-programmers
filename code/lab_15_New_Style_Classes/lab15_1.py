#!/usr/bin/env python
"""lab15_1.py A SortedDictionary class with only "description"
allowed as an attribute -- using __setattr__"""

class SortedDictionary(dict): 

    allowed_attributes = 'description',

    def keys(self):
        return sorted(dict.keys(self))
        # return sorted(super(type(self), self).keys())

    def __iter__(self):
        """If we don't define this, it will use the regular
        dictionary __iter__ which does not call
        SortedDictionary.keys()."""

        for each in self.keys():
            yield each

    def __setattr__(self, attribute_name, value):
        if attribute_name not in SortedDictionary.allowed_attributes:
            raise TypeError, "can't set attributes of class %s" % self.__class__.__name__
        self.__dict__[attribute_name] =  value

def main():
    # d is a tuple of contructs that will initialize
    # a regular dictionary.
    for initializer in (
            {'Zero':0, 'False':0, 'None':0, 'True':1}, 
            {},                                
            (('calling birds', 4), ('french hens', 3), 
            ('turtle doves', 2),
            ('partridge in a pear tree', 1))):
        regular_dict = dict(initializer)
        sorted_dict = SortedDictionary(initializer)
        print " regular_dict.keys():", regular_dict.keys()
        print "  sorted_dict.keys():", sorted_dict.keys()
        print "sorted_dict for-loop:", ', '.join([
            str(k) for k in sorted_dict])

    sorted_dict.description = "Fourth Day of Christmas"
    print "sorted_dict.description =", sorted_dict.description
    try:
        regular_dict.description = "Fourth Day of Christmas"
    except AttributeError:
        pass
    else:
        print "Unexpected behavior!"
    sorted_dict.x = 3

if __name__ == '__main__':
    main()

