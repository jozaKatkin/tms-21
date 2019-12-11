from funcs import (
    prepare_args,
    my_generator,
    create_log
)


def main():
    first_name, last_name, (h, m, s) = prepare_args()
    create_log(first_name, last_name)
    generate = my_generator(h, m, s)

    for i in generate:
        print(i)


if __name__ == '__main__':
    main()



