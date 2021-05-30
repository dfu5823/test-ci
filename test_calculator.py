"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_spit_float(self):
        assert 1.0 == calculator.spit_float()

    def test_pow(self):
        # assert isinstance(second_term, int)
        assert 8 == calculator.pow(2, 3)
