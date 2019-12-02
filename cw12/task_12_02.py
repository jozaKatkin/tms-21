class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif len(args) == 1 and isinstance(args[0], str):
            args = args[0].split("-")
            self.hours = int(args[0])
            self.minutes = int(args[1])
            self.seconds = int(args[2])
            # self.hours, self.minutes, self.seconds = args[0].split("-")
        elif len(args) == 1 and isinstance(args[0], MyTime):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
            # self.hours, self.minutes, self.seconds = my_time.hours

        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0



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
    my_time2 = MyTime("1-1-1")
    my_time3 = MyTime(13, 14, 14)
    print(my_time1 + my_time2)
    print(my_time1 != my_time2)
    print(my_time3 - my_time2)
    print(my_time3)


if __name__ == "__main__":
    main()
