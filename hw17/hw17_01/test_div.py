from unittest import TestCase
from funcs import calc_div


class DivTestCase(TestCase):
    def test_div_normal(self):
        result = calc_div(2, 2)
        self.assertEqual(result, 1)

    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            calc_div(4, 0)

    def test_div_type(self):
        result = calc_div(8, 4)
        self.assertIsInstance(result, (int, float))
