from hw17.hw17_05.funcs import *
from unittest import TestCase

fields = 'Product Name,Price,Amount,Comment'
rows = [
        'Apple,1.5,10,With worms (O_o)',
        'Lemon,2,15,Sour',
        'Tomato,1.75,20,Red',
        'Cucumber,0.75,25,Prickly',
    ]
filename = "/home/joza/PycharmProjects/tms-21/hw17/hw17_05/test.csv"
row = "Water,0.4,56,Mineral"


class ReadCSVTestCase(TestCase):
    def read_type_test(self):
        fields, rows = read_csv(filename)
        self.assertIsInstance(fields, list)
        self.assertIsInstance(rows, list)
        for r in rows:
            self.assertIsInstance(r, list)

    def read_length_test(self):
        fields, rows = read_csv(filename)
        self.assertGreater(len(fields), 0)
        self.assertGreater(len(rows), 0)


class PrepareCSVTestCase(TestCase):
    def prepare_type_test(self):
        prepared_fields, prepared_rows = prepare_csv_data(fields, rows)
        self.assertIsInstance(prepared_fields, list)
        self.assertIsInstance(prepared_rows, list)
        for r in prepared_rows:
            self.assertIsInstance(r, list)

    def prepare_length_test(self):
        prepared_fields, prepared_rows = prepare_csv_data(fields, rows)
        self.assertGreater(len(prepared_fields), 0)
        self.assertGreater(len(prepared_rows), 0)


class PrintCSVTestCase(TestCase):
    def print_test(self):
        print_csv(filename)


class WriteTestCase(TestCase):
    def write_test(self):
        prepared_fields, prepared_rows = prepare_csv_data(fields, rows)
        write_csv(filename, prepared_fields, prepared_rows)
        test_fields, test_rows = read_csv(filename)
        self.assertListEqual(test_fields, prepared_fields)
        self.assertListEqual(test_rows, prepared_rows)


class AddRowTestCase(TestCase):
    def add_row_fields(self):
        add_row_to_csv(filename, row)
        fields, _ = read_csv(filename)
        self.assertEqual(len(fields), 4)

    def add_row_test(self):
        _, old_rows = read_csv(filename)
        add_row_to_csv(filename, row)
        _, new_rows = read_csv(filename)
        self.assertIn(row.split(","), new_rows)

    def add_row_length(self):
        _, old_rows = read_csv(filename)
        add_row_to_csv(filename, row)
        _, new_rows = read_csv(filename)
        self.assertEqual(len(old_rows), len(new_rows) - 1)


class DelRowTestCase(TestCase):
    def del_row_fields(self):
        fields, rows = read_csv(filename)
        self.assertEqual(len(fields), 4)
        self.assertGreater(len(rows), 0)
        del_row_from_csv(filename)

    def del_row_length(self):
        _, old_rows = read_csv(filename)
        del_row_from_csv(filename)
        _, new_rows = read_csv(filename)
        self.assertEqual(len(old_rows), len(new_rows) + 1)


class CountTotalAmountTestCase(TestCase):
    def test_type_product_amount(self):
        res = count_total_products_amount(filename)
        self.assertIsInstance(res, int)

    def test_value_product_amount(self):
        res = count_total_products_amount(filename)
        self.assertGreaterEqual(res, 0)


class MaxPriceTestCase(TestCase):
    def test_type_max_price(self):
        _, res = find_max_price_product(filename)
        self.assertIsInstance(res, (int, float))

    def test_value_max_price(self):
        _, res = find_max_price_product(filename)
        self.assertGreaterEqual(res, 0)


class MinPriceTestCase(TestCase):
    def test_type_min_price(self):
        _, res = find_min_price_product(filename)
        self.assertIsInstance(res, (int, float))

    def test_value_min_price(self):
        _, res = find_min_price_product(filename)
        self.assertGreaterEqual(res, 0)


class ReduceAmountTestCase(TestCase):
    def test_reduce_amount(self):
        _, old_rows = read_csv(filename)
        reduce_product_amount(filename, "Apple")
        fields, rows = read_csv(filename)
        amount_index = fields.index('Amount')
        self.assertGreater(int(old_rows[0][amount_index]), int(rows[0][amount_index]))