#!/usr/bin/env python3
"""A stack again, this time using the built-in "list" type.

A stack is just a list with a "push" method, since the list
already has a "pop".  When it is-a "list" it inherits all
the builtin facilities of the list.
""" 

class Stack(list): #when stack gets initalized, goes up to the list

    def push(self, thing): #self is a list (from Stack(list)
        # list.append(self, thing) works here.
        # Also, the following  works this time because
        # this class does not have an "append" already.
        self.append(thing) 

if __name__ == "__main__":
    stack = Stack()
    stack.push("Gone With The Wind")
    stack.push("Maltese Falcon")
    stack.push("Fifth Element")
    print ("The stack has a rather nice __str__ already:")
    print (stack)
    print ('The stack has all the list facilities, plus the "push":')
    print (dir(stack))
    print ("Sorting then popping:")
    stack.sort()
    print (stack.pop())
