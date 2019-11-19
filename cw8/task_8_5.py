def count(num):
    res = (num ** 0.5 + num) / 2
    return res


def main():
    x = count(5) + count(12) + count(19)
    print(x)


if __name__ == "__main__":
    main()
