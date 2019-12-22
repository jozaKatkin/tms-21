from hw17.hw17_04.test_funcs import *


def main():
    MaxElemTestCase().test_max()
    MaxElemTestCase().test_max_type()
    MinElemTestCase().test_min()
    MinElemTestCase().test_min_type()
    SumTestCase().test_sum()
    SumTestCase().test_sum_type()


if __name__ == '__main__':
    main()