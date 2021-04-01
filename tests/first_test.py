import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_multiply(self):
        assert self.calc.multiply(2, 3) == 6

    def test_division(self):
        assert self.calc.division(6, 3) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(5, 3) == 2

    def test_adding(self):
        assert self.calc.adding(3, 3) == 6