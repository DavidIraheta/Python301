# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

import unittest
from mymath import subtract_divide, CustomZeroDivsionError

class TestSubtractDivide(unittest.TestCase):
    def test_subtract_divide(self):
        self.assertEqual(subtract_divide(10, 5, 3), 5)
        self.assertEqual(subtract_divide(10, 5, 4), 10)
    
    def test_custom_zero_division_error(self):
        with self.assertRaises(CustomZeroDivsionError):
            subtract_divide(10, 5, 5)



if __name__ == "__main__":
    unittest.main()
