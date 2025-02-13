# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)

import unittest
from test_discount import apply_discount

class TestApplyDiscount(unittest.TestCase):
     
     def test_valid_discount(self):
        """Test applying a valid discount."""
        self.assertEqual(apply_discount(100, 20), 80.0)
        

     def test_zero_discount(self):
        """Test when no discount is applied."""
        self.assertAlmostEqual(apply_discount(50, 0), 50.0)

     def test_full_discount(self):
        """Test when full discount is applied."""
        self.assertAlmostEqual(apply_discount(100, 100), 0.0)

     def test_invalid_discount(self):
        """Test applying an invalid discount."""
        with self.assertRaises(ValueError):
            apply_discount(100, 150)
    

if __name__ == "__main__":
    unittest.main()