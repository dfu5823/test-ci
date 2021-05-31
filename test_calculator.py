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
        assert 8 == calculator.calc_pow(2, 3)


class TestCalculatorData:
    def test_setUp(self):
        # Load data for any test case (pair of numbers)
        self.data = [4, 2]

    def test_addition(self):
        assert self.data(1) + self.data(2) == \
               calculator.add(self.data(1), self.data(2))

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_spit_float(self):
        assert 1.0 == calculator.spit_float()

    def test_pow(self):
        assert 8 == calculator.calc_pow(2, 3)
