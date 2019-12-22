from test_div import *
from test_diff import *
from test_mult import *
from test_sum import *


def main():
    DivTestCase().test_div_normal()
    DivTestCase().test_div_type()
    DivTestCase().test_error()
    DiffTestCase().test_diff_normal()
    DiffTestCase().test_diff_type()
    MultTestCase().test_mult_normal()
    MultTestCase().test_mult_type()
    SumTestCase().test_sum_normal()
    SumTestCase().test_sum_type()


if __name__ == "__main__":
    main()

