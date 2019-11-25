# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.


def main():
    with open('task_10_2.txt', 'w') as my_file:
        for line in range(6):
            my_file.write(f"{input()}\n")
    with open('task_10_2.txt', 'r') as my_file:
        print(my_file.readlines())


if __name__ == "__main__":
    main()
