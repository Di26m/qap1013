import pytest

from app.calc import Calculator

class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_adding_sucsess(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_substraction_sucsess(self):
        assert self.calc.subtraction(self, 2, 1) == 1

    def test_devision_sucsess(self):
        assert self.calc.devision(self, 4, 2) == 2

    def test_multiply_sucsess(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_zerodevision_sucsess(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.devision(self, 2, 0)

    def teardown(self):
        print("Тесты завершены")


