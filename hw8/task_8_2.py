# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
# т. е. таким, которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)


def palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        res = True
    else:
        res = False
    return res


def main():
    words = ["казак", "комок", "привет"]
    print({word: palindrome(word) for word in words})


if __name__ == "__main__":
    main()
