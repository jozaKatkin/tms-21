class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        elif len(args) == 1 and isinstance(args[0], str):
            self.hours, self.minutes, self.seconds = map(int, args[0].split("-"))
        elif len(args) == 1 and isinstance(args[0], MyTime):
            my_time = args[0]
            self.hours, self.minutes, self.seconds = my_time.hours, my_time.minutes, my_time.seconds
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0
        self.hours, self.minutes, self.seconds = self.seconds_to_time(self.time_to_seconds())

    def __eq__(self, other):
        return all([
            self.hours == other.hours,
            self.minutes == other.minutes,
            self.seconds == other.seconds
        ])

    def time_to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def seconds_to_time(self, seconds):
        hours = seconds // 3600
        minutes = seconds // 60 % 60
        seconds = seconds % 60
        return hours, minutes, seconds

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        total_seconds = self.time_to_seconds() + other.time_to_seconds()
        hours, minutes, seconds = self.seconds_to_time(total_seconds)
        return MyTime(hours, minutes, seconds)

    def __sub__(self, other):
        total_seconds = self.time_to_seconds() - other.time_to_seconds()
        hours, minutes, seconds = self.seconds_to_time(total_seconds)
        return MyTime(hours, minutes, seconds)

    def __str__(self):
        s = f'{self.hours}-{self.minutes}-{self.seconds}'
        return s

    def __lt__(self, other):
        return self.time_to_seconds() < other.time_to_seconds()

    def __gt__(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def __le__(self, other):
        return self.time_to_seconds() <= other.time_to_seconds()

    def __ge__(self, other):
        return self.time_to_seconds() >= other.time_to_seconds()

    def __mul__(self, other):
        total_seconds = self.time_to_seconds() + other
        hours, minutes, seconds = self.seconds_to_time(total_seconds)
        return MyTime(hours, minutes, seconds)


def main():
    default_time = MyTime()
    print(default_time)
    int_time = MyTime(12, 55, 12)
    print(int_time)
    str_time = MyTime('2-66-55')
    print(str_time)

    print(int_time + str_time)
    print(int_time - str_time)
    print(str_time * 2)

    print(str_time == int_time)
    print(str_time != int_time)
    print(str_time >= int_time)
    print(str_time <= int_time)
    print(str_time > int_time)
    print(str_time < int_time)


if __name__ == "__main__":
    main()
