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

    def test_integration(self):
        # Confirm that 2 + 1 returns 3
        val = calculator.add(2, 1)
        assert 3 == val

        # Confirm that calc_pow(2,val) returns 8
        assert 8 == calculator.calc_pow(2, val)


class TestCalculatorData:
    def test_integrationCalc(self):
        # Load data for any test case (pair of numbers)
        self.data = [4, 2]
        # test addition
        assert self.data[0] + self.data[1] == \
               calculator.add(self.data[0], self.data[1])
        # test subtraction
        assert self.data[0] - self.data[1] == \
               calculator.subtract(self.data[0], self.data[1])
        # test multiplication
        assert self.data[0] * self.data[1] == \
               calculator.multiply(self.data[0], self.data[1])
        # test spit float
        assert 1.0 == calculator.spit_float()
        # test power
        assert self.data[0] ** self.data[1] == \
               calculator.calc_pow(self.data[0], self.data[1])
