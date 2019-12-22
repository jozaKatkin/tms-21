from hw17.hw17_02.test_validation import ValidateTestCase
from hw17.hw17_02.test_funcs import CalcTestCase


def main():
    ValidateTestCase().test_error()
    CalcTestCase().test_sum()
    CalcTestCase().test_diff()
    CalcTestCase().test_mult()
    CalcTestCase().test_div()
    CalcTestCase().test_error_div()


if __name__ == "__main__":
    main()