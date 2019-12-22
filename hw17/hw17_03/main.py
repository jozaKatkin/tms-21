from hw17.hw17_03.test_funcs import (
    PagesTestCase,
    AuthorTestCase,
    YearTestCase,
    PriceTestCase,
)


def main():
    PagesTestCase().test_type_pages()
    PagesTestCase().test_amount_pages()
    YearTestCase().test_type_year()
    YearTestCase().test_future_year()
    AuthorTestCase().test_type_author()
    AuthorTestCase().test_length_author()
    PriceTestCase().test_value_price()
    PriceTestCase().test_type_price()


if __name__ == "__main__":
    main()
