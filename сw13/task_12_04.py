# Создать класс Book. Атрибуты: количество страниц, год издания, автор, цена.
# Добавить валидацию в конструкторе на ввод корректных данных. Создать иерархию ошибок.


class Book:
    def __init__(self, pages, year, price, author):
        digits = map(str, [pages, year, price])
        if not all(map(str.isdigit, digits)):
            raise CharacterError
        elif int(pages) < 1 or int(year) > 2019 or int(year) < 0 or int(price) < 0:
            raise InvalidNumberError
        else:
            self.pages = pages
            self.year = year
            self.price = price
        if str(author).isdigit():
            raise IsDigitError
        else:
            self.author = author


class InvalidNumberError(Exception):
    def __init__(self, message="Wrong number"):
        super().__init__(message)


class IsDigitError(Exception):
    def __init__(self, message="Digits not expected, type word instead"):
        super().__init__(message)


class CharacterError(Exception):
    def __init__(self, message="Type only digits"):
        super().__init__(message)


try:
    def main():
        book = Book(8, 9, 8, 8, 9)
        print(book.author)

    if __name__ == "__main__":
        main()
except (TypeError, NameError, ValueError):
    print("Something wrong with attributes!")
finally:
    print("Exceptions handled")
