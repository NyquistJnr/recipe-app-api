"""
Sample test
"""

from django.test import SimpleTestCase
from app.calc import add


class CalcTest(SimpleTestCase):
    def test_adding_two_numbers(self):
        result = add(20, 7)
        self.assertEqual(result, 27)
