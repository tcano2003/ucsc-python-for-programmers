#!/usr/bin/env python3
"""(Optional) This example of unittest is taken from
http://www.python.org/doc/lib/module-unittest.html."""
import random
import unittest 

class TestSequenceFunctions(unittest.TestCase): #must start with capital "Test". superclass(unittest.TestCase).
    # find the methods available by typing: dir(unittest.TestCase)

    def setUp(self):
        self.seq = range(10)

    def testShuffle(self):
        # make sure the shuffled sequence does not
        # lose any elements
        random.shuffle(self.seq) #shuffling and then sorting again
        self.seq.sort()
        self.assertEqual(self.seq, range(10)) #asset will raise an error, want to report, but don't quit. makes sure equal to range(10)

    def testChoice(self):
        element = random.choice(self.seq)
        self.assert_(element in self.seq) # _ is good practice when want to use dir, but can't since dir is a keyword

    def testSample(self): #if methods that do not start with test, they will be ignored
        self.assertRaises(ValueError, random.sample, self.seq, 20) #raise the error, when random.sample is called, self.seq (is 10), 20 (testing for 20) are the arguments. asking for 20 elements out of self.seq, but there's only 10.
        for element in random.sample(self.seq, 5):
            self.assert_(element in self.seq)

if __name__ == '__main__':
    unittest.main()
