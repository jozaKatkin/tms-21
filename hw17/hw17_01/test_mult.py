from unittest import TestCase
from funcs import calc_mult


class MultTestCase(TestCase):
    def test_mult_normal(self):
        result = calc_mult(3, 2)
        self.assertEqual(result, 6)

    def test_mult_type(self):
        result = calc_mult(8, 4)
        self.assertIsInstance(result, (int, float))