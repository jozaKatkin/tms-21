# Создать csv файл с данными следующей структуры:
# Имя, Фамилия, Восраст. Создать отчетный файл с информацией
# по количеству людей входящих в ту или иную возрастную группу.
# Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.

import csv
from csv_utils import write_csv


def main():
    write_csv("people.csv", ["name", "surname", "age"],
              ["Petr", "Vasiliev", 59], ["Masha", "Kot", 13],
              ["Doomer", "Wojak", 28], ["Mariya", "Fapka", 23],
              ["Danny", "Casale", 35], ["David", "Firth", 40],
              ["Takuya", "Okada", 4], ["Danil", "Sibirsky", 25],
              ["Suri", "Noel", 3], ["Tanya", "Saharchuk", 45],
              ["Pavel", "Ostapov", 29], ["Ruslan", "Koshchey", 20])

    with open("people.csv", 'r') as in_file:
        csvreader = csv.reader(in_file)
        people_1_12 = []
        people_13_18 = []
        people_19_25 = []
        people_26_40 = []
        people_40_more = []
        for i, row in enumerate(csvreader):
            if i == 0:
                pass
            elif int(row[2]) <= 12:
                people_1_12.append(row[2])
            elif 13 <= int(row[2]) <= 18:
                people_13_18.append(row[2])
            elif 19 <= int(row[2]) <= 25:
                people_19_25.append(row[2])
            elif 26 <= int(row[2]) <= 40:
                people_26_40.append(row[2])
            elif int(row[2]) > 40:
                people_40_more.append(row[2])
        people_1_12 = [len(people_1_12), "1-12"]
        people_13_18 = [len(people_13_18), "13-18"]
        people_19_25 = [len(people_19_25), "19-25"]
        people_26_40 = [len(people_26_40), "26-40"]
        people_40_more = [len(people_40_more), "40+"]

    write_csv("ages.csv", ["number of people", "age group"], people_1_12, people_13_18,
              people_19_25, people_26_40, people_40_more)


if __name__ == "__main__":
    main()