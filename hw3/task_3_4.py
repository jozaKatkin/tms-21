from math import ceil

your_string = input("Enter a string\n")
central_letter = ceil((len(your_string)) / 2)
'''округлили в большую сторону,
чтобы для нечетного числа символов получить середину.
тк для четных четкой середины нет,
это будет символ, ближний к правой стороне'''
central_letter -= 1  # получаем из символа индекс
print(f"Центральная буква: {your_string[central_letter]}")
if your_string[central_letter] == your_string[0]:
    print(f"Строка между первым и центральным символами: {your_string[1:central_letter]}")
'''если хотим вывести строку,
не включая одинаковые символы'''
