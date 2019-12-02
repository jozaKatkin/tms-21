class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return self.hours and self.minutes and self.seconds == other.hours and other.minutes and other.seconds

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds

    def __sub__(self, other):
        return self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds

    def __str__(self):
        s = f'{self.hours}-{self.minutes}-{self.seconds}'
        return s


def main():
    my_time1 = MyTime(1, 1, 1)
    my_time2 = MyTime(1, 1, 1)
    my_time3 = MyTime(13, 14, 14)
    print(my_time1 + my_time2)
    print(my_time1 != my_time2)
    print(my_time3 - my_time2)
    print(my_time3)


if __name__ == "__main__":
    main()
