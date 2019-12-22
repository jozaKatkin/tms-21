from unittest import TestCase
from funcs import calc_sum


class SumTestCase(TestCase):
    def test_sum_normal(self):
        result = calc_sum(3, 2)
        self.assertEqual(result, 5)

    def test_sum_type(self):
        result = calc_sum(8, 4)
        self.assertIsInstance(result, (int, float))