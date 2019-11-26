# Имеется текстовый файл. Все четные строки этого файла записать во второй файл,
# а нечетные — в третий файл. Порядок следования строк сохраняется.


def main():
    with open('task_10_5.txt', 'r') as in_file:
        old_lines = in_file.readlines()
        even = []
        odd = []
        for i, old_line in enumerate(old_lines):
            # if not i % 2:
            #     even.append(old_line)
            # elif i % 2 != 0:
            #     odd.append(old_line)
            even.append(old_line) if not i % 2 else odd.append(old_line)
        with open('task_10_5_1.txt', 'w') as even_file:
            even_file.writelines(even)
        with open('task_10_5_2.txt', 'w') as odd_file:
            odd_file.writelines(odd)


if __name__ == "__main__":
    main()
