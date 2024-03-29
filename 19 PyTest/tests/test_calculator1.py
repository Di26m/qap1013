import pytest
from app.calculator import Calculator



class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_adding_sucsess(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsucsess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_devizion(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')