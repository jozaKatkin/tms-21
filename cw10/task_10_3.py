# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.


def main():
    with open('task_10_3.txt', 'a') as my_file:
        for line in range(3):
            my_file.write(f"{input()}\n")
    with open('task_10_3.txt', 'r') as my_file:
        print(my_file.readlines())


if __name__ == "__main__":
    main()
