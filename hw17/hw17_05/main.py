from hw17.hw17_05.test_funcs import *


def main():
    ReadCSVTestCase().read_type_test()
    ReadCSVTestCase().read_length_test()
    PrepareCSVTestCase().prepare_type_test()
    PrepareCSVTestCase().prepare_length_test()
    PrintCSVTestCase().print_test()
    WriteTestCase().write_test()
    AddRowTestCase().add_row_fields()
    AddRowTestCase().add_row_test()
    AddRowTestCase().add_row_length()
    DelRowTestCase().del_row_fields()
    DelRowTestCase().del_row_length()
    CountTotalAmountTestCase().test_type_product_amount()
    CountTotalAmountTestCase().test_value_product_amount()
    MaxPriceTestCase().test_type_max_price()
    MaxPriceTestCase().test_value_max_price()
    MinPriceTestCase().test_type_min_price()
    MinPriceTestCase().test_value_min_price()
    ReduceAmountTestCase().test_reduce_amount()


if __name__ == '__main__':
    main()