class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif len(args) == 1 and isinstance(args[0], str):
            self.hours, self.minutes, self.seconds = map(int, args[0].split("-"))
        elif len(args) == 1 and isinstance(args[0], MyTime):
            my_time = args[0]
            self.hours, self.minutes, self.seconds = my_time.hours, my_time.minutes, my_time.seconds
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0

        if self.seconds > 59:
            self.seconds = self.seconds % 60
            self.minutes = self.seconds // 60
        if self.minutes > 59:
            self.minutes = self.minutes % 60
            self.hours = self.minutes // 60

    def __eq__(self, other):
        return self.hours and self.minutes and self.seconds == other.hours and other.minutes and other.seconds

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds
        if self.seconds > 59:
            self.seconds = self.seconds % 60
            self.minutes = self.seconds // 60
        if self.minutes > 59:
            self.minutes = self.minutes % 60
            self.hours = self.minutes // 60
        return self.hours, self.minutes, self.seconds

    def __sub__(self, other):
        return self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds

    def __str__(self):
        s = f'{self.hours}-{self.minutes}-{self.seconds}'
        return s

    def __lt__(self, other):
        return self.hours and self.minutes and self.seconds < other.hours and other.minutes and other.seconds

    def __gt__(self, other):
        return self.hours and self.minutes and self.seconds > other.hours and other.minutes and other.seconds

    def __le__(self, other):
        return self.hours and self.minutes and self.seconds <= other.hours and other.minutes and other.seconds

    def __ge__(self, other):
        return self.hours and self.minutes and self.seconds >= other.hours and other.minutes and other.seconds

    def __mul__(self, other):
        self.hours *= other
        self.minutes *= other
        self.seconds *= other
        if self.seconds > 59:
            self.seconds = self.seconds % 60
            self.minutes = self.seconds // 60
        if self.minutes > 59:
            self.minutes = self.minutes % 60
            self.hours = self.minutes // 60
        return self.hours, self.minutes, self.seconds


def main():
    my_time1 = MyTime(1, 1, 1)
    print(my_time1 * 70)


if __name__ == "__main__":
    main()
