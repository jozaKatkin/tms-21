# Дан список имен, отфильтровать все имена, где есть буква k

# filter()


def main():
    func = filter(lambda name: "k" in name, ["Joza", "karina", "kawfwk", "olya"])
    print(list(func))


if __name__ == "__main__":
    main()