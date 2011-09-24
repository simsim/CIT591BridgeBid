'''
Unit Test for Bridge Bid

@author: xinl@seas.upenn.edu, kishin@seas.upenn.edu
'''

from bridgebid import *
import unittest

class TestBridgeBid(unittest.TestCase):
    def testHighCardPoints(self):
        self.assertEqual(12, highCardPoints("5C 7H AS JD 9D 2C KH 10H 4C 8H 8C AD 10C"))
        self.assertEqual(52, highCardPoints("AC AH AS AD AD AC AH AH AC AH AC AD AC"))
        
    def testDistributionPoints(self):
        self.assertEqual(1, distributionPoints("5C 7H AS JD 9D 2C KH 10H 4C 8H 8C AD 10C"))
        self.assertEqual(5, distributionPoints("5C 7S AS JS 9S 2C KS 10S 4C 8S 8C AS 10C"))
        self.assertEqual(0, distributionPoints("5C 7H AS JD 9D 2D KH 10H 4C 8H 8C AD 10C"))
    
    def testOpeningBid(self):
        self.assertEqual(1, openingBid("5C 7H AS JD 9D 2C KH 10H 4C 8H 8C AD 10C"))
    
unittest.main()
