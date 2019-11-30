# Создать csv файл с данными следующей структуры:
# Имя, Фамилия, Восраст. Создать отчетный файл с информацией
# по количеству людей входящих в ту или иную возрастную группу.
# Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.


from csv_utils import (
    write_csv, converter, read_csv, print_csv
)


def people(rows):
    people_dict = {
        "1_12": 0,
        "13_18": 0,
        "19_25": 0,
        "26_40": 0,
        "40+": 0,
    }

    for row in rows:
        age = int(row[2])
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

    with open("report.csv", "w") as csvfile:
        for key, value in people_dict.items():
            csvfile.write(f"{key}: {value}\n")


def main():
    fields = "name, surname, age"
    rows = [
        "Petr,Pchyolkin,59", "Masha,Kot,13",
        "Doomer,Wojak,28", "Mariya,Fapka,23",
        "Danny,Casale,35 ", "David,Firth,40",
        "Takuya,Okada,4", "Danil,Sibirsky,25",
        "Suri,Noel,3", "Tanya,Saharchuk,45",
        "Pavel,Ostapov,29", "Ruslan,Koshchey,20"
    ]

    fields, rows = converter(fields, rows)
    write_csv(f"people.csv", fields, rows)
    print_csv("people.csv")
    fields, rows = read_csv("people.csv")
    people(rows)
    # print_csv("report.csv")


if __name__ == "__main__":
    main()
