import pytest

# Test cases to test Calulator methods
# You always create  a child class derived from unittest.TestCase
from entity.calculator import Calculator


class TestCalculator:
    # setUp method is overridden from the parent class TestCase
    def setup(self):
        self.calculator = Calculator()

    # Each test method starts with the keyword test_
    def test_add(self):
        assert self.calculator.add(4, 7) == 11

    def test_subtract(self):
        assert self.calculator.subtract(10, 5) == 5

    def test_multiply(self):
        assert self.calculator.multiply(3, 7) == 21

    def test_divide(self):
        assert self.calculator.divide(10, 2) == 5
