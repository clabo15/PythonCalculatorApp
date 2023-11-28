from models.calculator_model import CalculatorModel

class CalculatorViewModel:
    def __init__(self):
        """Initialize the calculator.
        """
        self.model = CalculatorModel()
        
    def perform_calculation(self, a, b, operation):
        """
        Perform a calculation based on the provided operands and operation.

        Args:
            a (str): The first operand as a string.
            b (str): The second operand as a string.
            operation (str): The operation to perform. Supported values are '+', '-', '*', '/'.

        Returns:
            str: The result of the calculation as a string.
                If the operation is not supported or division by zero occurs, returns 'Error'.
        """
        if operation == '+':
            return str(float(a) + float(b))
        elif operation == '-':
            return str(float(a) - float(b))
        elif operation == '*':
            return str(float(a) * float(b))
        elif operation == '/':
            try:
                return str(float(a) / float(b))
            except ZeroDivisionError:
                return 'Error'
        else:
            return 'Invalid operation'