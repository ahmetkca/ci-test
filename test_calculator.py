import Calculator


class TestCalculator:

    def test_addition(self):
        assert 20 == Calculator.add(10, 10)

    def test_subtraction(self):
        assert 5 == Calculator.subtract(10, 5)

    def test_multiplication(self):
        assert 36 == Calculator.multiply(6, 6)
