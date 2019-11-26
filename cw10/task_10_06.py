# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки.
# Если нет, то получить номер первой строки,
# в которой эти файлы отличаются друг от друга.


def main():
    with open('task_10_06_01.txt', 'r') as file1, open('task_10_06_02.txt') as file2:
        lines = file1.readlines()
        for i, line in enumerate(lines):
            line2 = file2.readline()
            if line != line2:
                print(f"string number: {i + 1}\nfile1: {line}file2: {line2}")
                return
        print("Files are the same")


if __name__ == "__main__":
    main()
