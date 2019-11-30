# Создать csv файл с данными следующей структуры:
# Имя, Фамилия, Восраст. Создать отчетный файл с информацией
# по количеству людей входящих в ту или иную возрастную группу.
# Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.

import csv
from csv_utils import write_csv


# people = {
#     ["name", "surname", "age"],
#     ["Petr", "Vasiliev", 59], ["Masha", "Kot", 13],
#     ["Doomer", "Wojak", 28], ["Mariya", "Fapka", 23],
#     ["Danny", "Casale", 35], ["David", "Firth", 40],
#     ["Takuya", "Okada", 4], ["Danil", "Sibirsky", 25],
#     ["Suri", "Noel", 3], ["Tanya", "Saharchuk", 45],
#     ["Pavel", "Ostapov", 29], ["Ruslan", "Koshchey", 20])
# }

def people(fields, rows):
    people_dict = {
        "1_12": 0,
        "13_18": 0,
        "19_25": 0,
        "26_40": 0,
        "40+": 0,
    }

    for row in rows:
        age = row[2]
        if 1 <= age <= 12:
            people_dict["1_12"] += 1
        elif 13 <= age <= 18:
            people_dict["13_18"] += 1
        elif 19 <= age <= 25:
            people_dict["19_25"] += 1
        elif 26 <= age <= 40:
            people_dict["26_40"] += 1
        elif age >= 40:
            people_dict["40+"] += 1





def main():


if __name__ == "__main__":
    main()
