# import everything from isPositive.py file
from isPositive import *
#you have to have this line to unit test
import unittest
class Test_numbertheory(unittest.TestCase):
    #self is a keyword
    def test_get_divisors(self):
        #asserting an error when isPositive(cis)
        self.assertRaises(ValueError, isPositive, 'cis')
        self.assertEqual(True, isPositive(2))

unittest.main()
