from unittest import TestCase
from hw17.hw17_02.exceptions import WrongInputError
from hw17.hw17_02.funcs_methods import validate_args


class ValidateTestCase(TestCase):
    def test_error(self):
        with self.assertRaises(WrongInputError):
            validate_args(9, "h")
            validate_args("h", 9)
            validate_args("h", "9hh")