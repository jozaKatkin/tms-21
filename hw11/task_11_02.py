class Car:
    def __init__(self, manufacturer, model, year, speed=0):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, turn):
        self.__speed = turn

    def print_speed(self):
        print(self.__speed)

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0


def main():
    car = Car("Audi", 80, 2005)
    car.increase_speed()
    print(car.speed)
    car.print_speed()
    car.stop()
    car.print_speed()
    car.speed = 90
    car.print_speed()


if __name__ == "__main__":
    main()
