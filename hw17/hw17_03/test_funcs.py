from unittest import TestCase
from hw17.hw17_03.funcs import *
from hw17.hw17_03.exceptions import *


class PagesTestCase(TestCase):
    def test_type_pages(self):
        with self.assertRaises(WrongPagesTypeError):
            validate_pages(6.7)
            validate_pages("6.7")

    def test_amount_pages(self):
        with self.assertRaises(WrongPagesAmountError):
            validate_pages(0)
            validate_pages(-9)


class YearTestCase(TestCase):
    def test_type_year(self):
        with self.assertRaises(WrongYearTypeError):
            validate_year(6.7)
            validate_year("6.7")
            validate_year(-6)

    def test_future_year(self):
        with self.assertRaises(FutureBookError):
            validate_year(2050)


class AuthorTestCase(TestCase):
    def test_type_author(self):
        with self.assertRaises(WrongAuthorTypeError):
            validate_author(6)
            validate_author(False)

    def test_length_author(self):
        with self.assertRaises(ZeroLengthAuthorError):
            validate_author("")


class PriceTestCase(TestCase):
    def test_type_price(self):
        with self.assertRaises(WrongPriceTypeError):
            validate_price(False)
            validate_price("j")

    def test_value_price(self):
        with self.assertRaises(WrongPriceValueError):
            validate_price(-9)