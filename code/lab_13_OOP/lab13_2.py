#!/usr/bin/env python3
"""
lab13_2.py A FruitTree class that inherits from the Tree class in 
the tree_def.py module. Also, three specific fruit trees classes 
are defined that inherit from the FruitTree class:  Apple, Banana, 
and Fig."""
import tree_defpy3

class FruitTree(tree_def.Tree):
    """Instantiate: FruitTree(size_in_feet) 
    """
    fruit = "forbidden fruit"

    def Print(self):
        print (self.__class__.__name__, tree_def.Tree.Print(self))
	print ("Eat my %s." % self.fruit)
	
class Apple(FruitTree):
    fruit = "apples"

class Banana(FruitTree):
    fruit = "bananas"

class Fig(FruitTree):
    fruit = "figs"

def main():
    trees = Apple(20), Banana(12), Fig(8)
    for tree in trees:
        tree.Print()

if __name__ == '__main__':
    main()
