from datetime import datetime

from hw17.hw17_03.exceptions import (
    WrongPagesTypeError,
    WrongPagesAmountError,
    WrongYearTypeError,
    FutureBookError,
    WrongAuthorTypeError,
    ZeroLengthAuthorError,
    WrongPriceTypeError,
    WrongPriceValueError
)


def validate_pages(pages):
    if not isinstance(pages, int):
        raise WrongPagesTypeError
    elif pages < 1:
        raise WrongPagesAmountError


def validate_year(year):
    if not isinstance(year, int):
        raise WrongYearTypeError
    elif year > datetime.now().year:
        raise FutureBookError


def validate_author(author):
    if not isinstance(author, str):
        raise WrongAuthorTypeError
    elif not author:
        raise ZeroLengthAuthorError


def validate_price(price):
    if not (isinstance(price, (int, float))):
        raise WrongPriceTypeError
    elif price < 0:
        raise WrongPriceValueError
