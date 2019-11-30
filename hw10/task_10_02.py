# Создать csv файл с данными о ежедневной погоде. Стурктура:
# Дата, Место, Градусы, Скорость ветра. Найти среднюю погоду
# (скорость ветра и градусы) для Минск за последние 7 дней.


from csv_utils import (
    write_csv,
    converter,
    read_csv,
    print_csv
)
from datetime import (
    date,
    timedelta,
    datetime
)


def count(rows):
    week_ago = date.today() - timedelta(days=7)
    wind_speed = 0
    degrees = 0
    counter = 0
    for row in rows:
        date_string = datetime.strptime(row[0], "%d.%m.%y").date()
        if week_ago <= date_string < date.today() and row[1] == "Minsk":
            degrees += int(row[2])
            wind_speed += int(row[3])
            counter += 1
    avg_degrees = round(degrees / counter, 2)
    avg_speed = round(wind_speed / counter, 2)
    return avg_degrees, avg_speed


def main():
    fields = "date,place,degrees,wind speed"
    rows = [
        "21.11.19,Minsk,1,15",
        "21.11.19,Moscow,-1,11",
        "21.11.19,Kiev,2,10",
        "22.11.19,Minsk,1,5",
        "22.11.19,Moscow,1,16",
        "22.11.19,Kiev,-2,20",
        "23.11.19,Minsk,-3,20",
        "23.11.19,Moscow,-2,18",
        "23.11.19,Kiev,0,8",
        "24.11.19,Minsk,-1,16",
        "24.11.19,Moscow,-2,12",
        "24.11.19, Kiev,0,17",
        "25.11.19, Minsk,-2,19",
        "25.11.19,Moscow,-3,10",
        "25.11.19,Kiev,1,10",
        "26.11.19,Minsk,0,17",
        "26.11.19,Moscow,-2,7",
        "26.11.19,Kiev,0,9",
        "27.11.19,Minsk,3,10",
        "27.11.19,Moscow,-3,10",
        "27.11.19,Kiev,1,8"
    ]

    filename = "Weather.csv"
    fields, rows = converter(fields, rows)
    write_csv(filename, fields, rows)
    print_csv(filename)
    fields, rows = read_csv(filename)
    print(count(rows))


if __name__ == "__main__":
    main()
