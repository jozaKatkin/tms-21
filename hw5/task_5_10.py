# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
# время пребывания в пути которых превышает 7 часов 20 минут
from datetime import datetime

trains = [
    {
        "Train": "001",
        "start point": "Minsk",
        "end point": "Moscow",
        "departure": datetime(2019, 11, 2, 12, 30),
        "arrival": datetime(2019, 11, 3, 9, 30),
    },
    {
        "Train": "002",
        "start point": "Minsk",
        "end point": "Baranovichi",
        "departure": datetime(2019, 11, 2, 19, 30),
        "arrival": datetime(2019, 11, 2, 23, 30),
    },
    {
        "Train": "003",
        "start point": "Minsk",
        "end point": "Unknown City",
        "departure": datetime(2019, 11, 2, 10, 30),
        "arrival": datetime(2019, 11, 2, 19, 45),
    },
    {
        "Train": "004",
        "start point": "Minsk",
        "end point": "Town",
        "departure": datetime(2019, 11, 2, 23, 20),
        "arrival": datetime(2019, 11, 3, 3, 45),
    },
    {
        "Train": "005",
        "start point": "Minsk",
        "end point": "Kiev",
        "departure": datetime(2019, 11, 3, 9, 10),
        "arrival": datetime(2019, 11, 3, 17, 00),
    },
]

for train in trains:
    departure = train["departure"]
    arrival = train["arrival"]
    delta = arrival - departure
    var = delta.total_seconds()
    if var > 26400:
        start = train["start point"]
        end = train["end point"]
        train = train["Train"]
        print(f"{train} {start}-{end}: Время в пути: {delta}\nОтправление: {departure}\nПрибытие:    {arrival}\n")
