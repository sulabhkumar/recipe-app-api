""" 
sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """ Test the calc module """

    def test_add_numbers(self):
        """ Test adding number together """
        res = calc.add(8,6)

        self.assertEqual(res, 14)

    def test_subtract_numbers(self):
        """ Test subtracting numbers """
        res = calc.substract(5, 10)

        self.assertEqual(res, -5)
