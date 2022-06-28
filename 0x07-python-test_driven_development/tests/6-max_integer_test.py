import unittest


class Test_Max_Integer(unittest.TestCase):
    def test_equal(self):
        #Test if cases equal to predetermined answers
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

