#!/usr/bin/env python
"""
lab13_1.py  Implement a Stack class.  It should
have two functions: you add things to the top of your
stack (usually called push), and you take things from
the top of your stack, (usually called pop)."""

class Stack:
    def __init__(self):
        self.things = []

    def Push(self, thing):
        self.things += [thing]

    def Pop(self):
        try:
            return self.things.pop()
        except IndexError:
            return None
def main():
    box = Stack()
    print box.Pop()
    box.Push('nickel')
    box.Push('dime')
    print box.Pop()
    print box.Pop()
    print box.Pop()

if __name__ == '__main__':
    main()

