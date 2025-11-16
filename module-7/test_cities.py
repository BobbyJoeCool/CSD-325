# Breutzmann, Robert
# CSD 325 - Advanced Python
# Assignment 7.2
# Due Date - 11/24/25

from city_functions import combineCity
import unittest

class UnitTestCase(unittest.TestCase):
    def test_city_country(self):
        result = combineCity("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")

unittest.main()