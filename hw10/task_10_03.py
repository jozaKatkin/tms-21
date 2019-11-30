# Дан файл, содержащий различные даты.
# Каждая дата - это число, месяц и год.
# Найти самую раннюю дату. [02-8.1-ML-29]


from datetime import datetime


with open("dates.txt", 'r') as txt_file:
    a = 0
    for date in txt_file.readlines():
        d, m, y = map(int, date.split(","))
        if a == 0 or a > datetime(d, m, y):
            a = datetime(d, m, y)

    print(f"The earliest date: {a}")