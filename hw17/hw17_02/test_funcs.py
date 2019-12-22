from hw17.hw17_02.funcs_methods import (
    Math
)
from unittest import TestCase


class CalcTestCase(TestCase):
    def test_sum(self):
        res = Math(6, 0).calc_sum()
        self.assertEqual(res, 6)

    def test_diff(self):
        res = Math(6, 0).calc_diff()
        self.assertEqual(res, 6)

    def test_mult(self):
        res = Math(6, 0).calc_mult()
        self.assertEqual(res, 0)

    def test_div(self):
        res = Math(6, 3).calc_div()
        self.assertEqual(res, 2)

    def test_error_div(self):
        with self.assertRaises(ZeroDivisionError):
            Math(6, 0).calc_div()

