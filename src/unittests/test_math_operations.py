import sys
import os
import unittest

# Get the absolute path of the src directory
current_dir = os.path.dirname(__file__)
src_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add src directory to sys.path
sys.path.insert(0, src_dir)

# Import Module
from math_module.math_operations import *

class TestMathOperations(unittest.TestCase):
    """Test suite for math operations.
    
    This class contains unit tests for basic mathematical operations.
    """
    
    def test_add(self):
        """Test the add function from the math_operations module.
        
        Ensures that the add function returns the correct sum for given inputs.
        """
        self.assertEqual(add(2, 3), 5, "Expected add(2, 3) to be 5")
        self.assertEqual(add(-1, 1), 0, "Expected add(-1, 1) to be 0")
        self.assertEqual(add(-1, -1), -2, "Expected add(-1, -1) to be -2")
        
    def test_subtract(self):
        """Test the subtract function from the math_operations module.

        Verifies that the subtract function correctly computes the difference
        between two numbers and returns the correct result for a variety of inputs.
        """
        self.assertEqual(subtract(3, 2), 1, "Expected subtract(3, 2) to be 1")
        self.assertEqual(subtract(-1, 1), -2, "Expected subtract(-1, 1) to be -2")
        self.assertEqual(subtract(3, 4), -1, "Expected subtract(3, 4) to be -1")
        
    def test_multiply(self):
        """Test the multiply function from the math_operations module.

        Verifies that the multiply function returns the correct product for given inputs.
        """
        self.assertEqual(multiply(3, 2), 6, "Expected multiply(3, 2) to be 6")
        self.assertEqual(multiply(-1, 1), -1, "Expected multiply(-1, 1) to be -1")
        self.assertEqual(multiply(-2, -2), 4, "Expected multiply(-2, -2) to be 4")
        self.assertEqual(multiply(0, 5), 0, "Expected multiply(0, 5) to be 0")

    def test_divide(self):
        """Test the divide function from the math_operations module.

        Verifies that the divide function returns the correct quotient for given inputs
        and raises an error when attempting to divide by zero.
        """
        self.assertEqual(divide(6, 2), 3, "Expected divide(6, 2) to be 3")
        self.assertEqual(divide(-1, 1), -1, "Expected divide(-1, 1) to be -1")
        self.assertEqual(divide(-2, -2), 1, "Expected divide(-2, -2) to be 1")
        self.assertRaises(ValueError, divide, 5, 0)  # Testing division by zero

        
if __name__ == "__main__":
    unittest.main()