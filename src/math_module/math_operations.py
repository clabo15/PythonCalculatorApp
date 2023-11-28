# Basic Mathematical Operations

def add(a: float, b: float) -> float:
    """
    Return the sum of a and b.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Return the difference between a and b.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference between a and b.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Return the multiplication of a and b.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The multiplication of a and b.
    """
    return a * b
    
def divide(a: float, b: float) -> float:
    """
    Return the division of a and b.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The division of a and b.
    """ 
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero!")