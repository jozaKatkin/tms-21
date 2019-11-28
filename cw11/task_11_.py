# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы:
# run, jump, birthday(увеличивает age на 1),
# sleep. Класс Parrot имеет дополнительный метод fly.
# Cat - meow, Dog - bark.


class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def change_weight(self, weight):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.2

    def change_height(self, height):
        self.height = height
        if height:
            self.height = height
        else:
            self.height += 0.2

    def run(self):
        print("Run!")

    def jump(self):
        print("Jump!")

    def sleep(self):
        print("Sleep...")

    def birthday(self):
        self.age += 1


class Dog(Pet):
    def bark(self):
        print("Woof-woof")


class Cat(Pet):
    def meow(self):
        print("Meow")


class Parrot(Pet):
    def fly(self):
        if self.weight > 0.1:
            print("This parrot cannot fly")
        else:
            print("Flies away...")


parrot = Parrot("Yasha", 3, "Joza", 0.2, 10)
parrot.fly()
cat = Cat("Stas", 2, "Katkin", 5, 20)
cat.meow()
print(parrot.weight)