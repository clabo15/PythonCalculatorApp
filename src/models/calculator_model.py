# import sys
# import os

# # Get the absolute path of the src directory
# current_dir = os.path.dirname(__file__)
# src_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# # Add src directory to sys.path
# sys.path.insert(0, src_dir)

# # Import Module
# from math_module.math_operations import *
from math_module.math_operations import *


class CalculatorModel:
    """Class method for creating a new Calculator model.
    """
    def __init__(self):
        """Initialize the test loop.
        """
        self.result = 0
        
    def calculate(self, a: float, b: float, operation: str) -> float:
        """
        Calculate the result of an arithmetic operation on two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.
            operation (str): The operation to perform. Supported operations are '+', '-', '*', '/'.

        Raises:
            ValueError: If 'operation' is not a supported operation.

        Returns:
            float: The result of the arithmetic operation.
        """
        
        operations = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }
        if operation in operations:
            self.result = operations[operation](a, b)
        else:
            raise ValueError("Invalid Operation.")
        
        return self.result
