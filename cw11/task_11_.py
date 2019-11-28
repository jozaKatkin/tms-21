# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы:
# run, jump, birthday(увеличивает age на 1),
# sleep. Класс Parrot имеет дополнительный метод fly.
# Cat - meow, Dog - bark.


class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

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
        print("Flies away...")


parrot = Parrot("Yasha", 3, "Joza")
parrot.fly()
cat = Cat("Stas", 2, "Katkin")
cat.meow()