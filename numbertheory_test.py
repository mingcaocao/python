# import everything from numbertheory.py file
from numbertheory import *
#you have to have this line to unit test
import unittest

class Test_numbertheory(unittest.TestCase):
    #self is a keyword
    def test_get_divisors(self):
        self.assertEqual([1,2,3,4,6,12], get_divisors(12), 'bad stuff happened')
        self.assertEqual([1], get_divisors(1), 'negative case')
    def test_is_abundant(self):
        self.assertTrue(is_abundant(12))
        self.assertTrue(is_abundant(18))
        self.assertFalse(is_abundant(6))
unittest.main()
