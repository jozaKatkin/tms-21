# Создать csv файл с данными о ежедневной погоде. Стурктура:
# Дата, Место, Градусы, Скорость ветра. Найти среднюю погоду
# (скорость ветра и градусы) для Минск за последние 7 дней.

import csv
from csv_utils import write_csv


def main():
    write_csv("Weather.csv", ["date", "place", "degrees", "wind speed"],
              ["21.11.19", "Minsk", 1, 15],
              ["21.11.19", "Moscow", -1, 11],
              ["21.11.19", "Kiev", 2, 10],
              ["22.11.19", "Minsk", 1, 5],
              ["22.11.19", "Moscow", 1, 16],
              ["22.11.19", "Kiev", -2, 20],
              ["23.11.19", "Minsk", -3, 20],
              ["23.11.19", "Moscow", -2, 18],
              ["23.11.19", "Kiev", 0, 8],
              ["24.11.19", "Minsk", -1, 16],
              ["24.11.19", "Moscow", -2, 12],
              ["24.11.19", "Kiev", 0, 17],
              ["25.11.19", "Minsk", -2, 19],
              ["25.11.19", "Moscow", -3, 10],
              ["25.11.19", "Kiev", 1, 10],
              ["26.11.19", "Minsk", 0, 17],
              ["26.11.19", "Moscow", -2, 7],
              ["26.11.19", "Kiev", 0, 9],
              ["27.11.19", "Minsk", 3, 10],
              ["27.11.19", "Moscow", -3, 10],
              ["27.11.19", "Kiev", 1, 8])

    with open("Weather.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        sum_degrees = 0
        sum_speed = 0
        for row in csvreader:
            if row[1] == "Minsk":
                sum_degrees += int(row[2])  # degrees
                sum_speed += int(row[3])  # wind speed
        average_t = sum_degrees / 7
        average_speed = sum_speed / 7
        print(f"average wind speed: {average_speed}")
        print(f"average temperature: {average_t}")


if __name__ == "__main__":
    main()
