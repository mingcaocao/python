# import everything from numbertheory.py file
from numbertheory import *
#you have to have this line to unit test
import unittest

class Test_numbertheory(unittest.TestCase):
    #self is a keyword
    def test_get_divisors(self):
        self.assertEqual([1,2,3,4,6,12], get_divisors(12), 'bad stuff happened')
unittest.main()
