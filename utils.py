"""Exemplary calculator functions module.
Provides basic arithmetic operations: add, subtract, multiply, divide.
"""


def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract the second integer from the first and return the result."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result."""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide the first integer by the second and return the result as a float."""
    return a / b


def to_binary(n: int) -> str:
    """Convert a natural number (0–100) to binary string. Raise if invalid."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if not 0 <= n <= 100:
        raise ValueError("Input must be in range 0 to 100.")
    return bin(n)
