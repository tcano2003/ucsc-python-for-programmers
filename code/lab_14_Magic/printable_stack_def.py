#!/usr/bin/env python  
"""printable_stack_def.py Extending our stack, providing a
"special method", __str__, which is called whenever:
   1.  "%s" % (printable_stack_object)
   2.  str(printable_stack_object)
   3.  print printable_stack_object """
    
import lab13_1 as stack_def  # copy of lab exercise
    
class PrintableStack(stack_def.Stack):
    """This class will reveal itself, and the result looks
    like a stack.
    """
    
    def __str__(self):
        try:
            min_width = max([len(thing) for thing in self.things])
        except ValueError: # self.things was empty
            min_width = 4
            center = ' [] '
        else:
            center = '|\n|'.join([thing.center(min_width) 
                                  for thing in self.things])
        top = ' '+ '-' * min_width + '\n|'
        bottom = '|\n ' + '-' * min_width 
        return top + center + bottom

def main():
    print 'Printing a Stack is not pleasant.'
    plain_box = stack_def.Stack()
    print plain_box
    print '\nPrintableStack shows its stack'
    pbox = PrintableStack()
    print pbox
    for food in ['bread','mayo','cheese']:
        print 'PrintableStack pushing', food
        pbox.Push(food)
        print pbox
    for i in range(3):
        print 'PrintableStack popping', pbox.Pop()
        print pbox

if __name__ == '__main__':
    main()

