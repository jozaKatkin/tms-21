from unittest import TestCase
from hw17.hw17_04.funcs import *
from hw17.hw17_04.classes import Matrix


class MaxElemTestCase(TestCase):
    def test_max(self):
        res = matrix_max_elem(Matrix())
        self.assertEqual(res, 0)

    def test_max_type(self):
        res = matrix_max_elem(Matrix(3, 4, 0, 10))
        self.assertIsInstance(res, int)


class MinElemTestCase(TestCase):
    def test_min(self):
        res = matrix_min_elem(Matrix())
        self.assertEqual(res, 0)

    def test_min_type(self):
        res = matrix_min_elem(Matrix(3, 4, 0, 10))
        self.assertIsInstance(res, int)


class SumTestCase(TestCase):
    def test_sum(self):
        res = matrix_sum(Matrix())
        self.assertEqual(res, 0)

    def test_sum_type(self):
        res = matrix_sum(Matrix(3, 4, 0, 10))
        self.assertIsInstance(res, int)
