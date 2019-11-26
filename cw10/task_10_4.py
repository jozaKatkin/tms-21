# Имеется текстовый файл. Переписать в другой файл все его
# строки с заменой в них символа 0 на символ 1 и наоборот.


def main():
    with open('task_10_4_1.txt', 'r') as in_file:
        old_lines = in_file.readlines()
        new_list = []
        for old_line in old_lines:
            string = ''
            for char in old_line:
                # if char == "0":
                #     string += "1"
                # elif char == "1":
                #     string += "0"
                # else:
                #     string += char
                string += "1" if char == "0" else "0" if char == "1" else char
            new_list.append(string)

    with open('task_10_4_2.txt', 'w') as out_file:
        out_file.writelines(new_list)

    with open('task_10_4_2.txt', 'r') as out_file:
        print(out_file.readlines())


if __name__ == "__main__":
    main()
