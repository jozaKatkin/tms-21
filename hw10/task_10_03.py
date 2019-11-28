# Дан файл, содержащий различные даты.
# Каждая дата - это число, месяц и год.
# Найти самую раннюю дату. [02-8.1-ML-29]

import csv
from csv_utils import write_csv
from datetime import datetime

write_csv("dates.csv", [2019, 11, 20], [2018, 1, 30], [2019, 1, 29],
          [2017, 12, 13], [2018, 1, 1], [2000, 5, 5], [2007, 10, 8], [2009, 9, 11],
          [2016, 5, 17], [2003, 7, 20], [2000, 2, 1], [2000, 12, 6])

with open("dates.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    a = 0
    for row in csvreader:
        if a == 0 or a > datetime(int(row[0]), int(row[1]), int(row[2])):
            a = datetime(int(row[0]), int(row[1]), int(row[2]))

    print(f"The earliest date: {a}")