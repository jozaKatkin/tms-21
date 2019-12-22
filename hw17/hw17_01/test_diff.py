from unittest import TestCase
from funcs import calc_diff


class DiffTestCase(TestCase):
    def test_diff_normal(self):
        result = calc_diff(3, 2)
        self.assertEqual(result, 1)

    def test_diff_type(self):
        result = calc_diff(8, 4)
        self.assertIsInstance(result, (int, float))