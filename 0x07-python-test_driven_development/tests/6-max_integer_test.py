"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_Max_Integer(unittest.TestCase):
    def test_equal(self):
        # Test if cases equal to predetermined answers
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-0.1, -92, 0]), 0)

    def test_string(self):
        # Test if case is a string/list of string
        self.assertEqual(max_integer("2"), '2')
        self.assertEqual(max_integer(['a', 'g', 'd']), 'g')

    def test_int(self):
        # Test if case is not an interable(string/array)
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, -9)
        self.assertRaises(TypeError, max_integer, [-1, 48, 'b'])

    def test_none(self):
        self.assertIsNone(max_integer([]), None)
