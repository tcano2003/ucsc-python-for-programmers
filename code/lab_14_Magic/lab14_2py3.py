#!/usr/bin/env python3
"""
lab14_2.py Tree and Forest classes with __str__.			  
"""
import random
import sys

class Tree:
    """Instantiate:  Tree(20) to make a tree 20 ft tall.
    """
    def __init__(self, height):
        self.height = height

    def __str__(self):
        return "tree, %.1f feet tall" % (self.height)

class Forest:
    """Instantiate: Forest(size="medium")
    if size == "large", it will have 8 trees.
            == "medium", it will have 5 trees.
            == "small", it will have 2 trees.
    """
    def __init__(self, size="medium"):
        if size not in ("small", "medium", "large"):
            raise ValueError ("""Instantiate with: Forest([size="medium"]) where size can be "small", "medium", or "large", not "%s".""" % size)
        self.size = size
        self.number_of_trees = 8 if self.size == "large" else 5 if self.size == "medium" else 2
        # Here comes the implementation of the containment:
        self.trees = [Tree(random.randrange(1,200)) 
                      for count in range(self.number_of_trees)]

    def __str__(self):
        say = "%s forest with %d trees: " % (self.size, self.number_of_trees)
        say += ", ".join([str(t) for t in self.trees])
        return say

def main():
    forest = Forest("small")
    print ("\nprinting:")
    print ("\t", forest, "\n")
    print ("Format replacement:\n%s" % "\t", forest, "\n")
    print ("And with str:\n" + "\t", str(forest))

#Original code
#def main():
#    forest = Forest("small")
#    print ("printing:")
#    print ("\t", forest) # results in an unwanted space after tab in Python 3
#    print ("Format replacement:\n\t%s" % forest)
#    print ("And with str:\n\t" + str(forest))

if __name__ == "__main__":
    main()
