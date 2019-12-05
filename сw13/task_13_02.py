from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, master, weight, height, ):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    @abstractmethod
    def voice(self):
        pass


class FelineInterface(ABC):
    @abstractmethod
    def scratch(self):
        pass


class CanineInterface(ABC):
    @abstractmethod
    def swim(self):
        pass


class WildAnimal(ABC, Animal):
    pass


class Lion(WildAnimal, FelineInterface):
    def voice(self):
        print("Arrghh")

    def scratch(self):
        print("All lions can scratch!")


class Wolf(WildAnimal, CanineInterface):
    def voice(self):
        print("Awo-Awooo-hoooo")

    def swim(self):
        print("All wolfs can swim")


class Pet(ABC, Animal):
    pass


class Dog(Pet, CanineInterface):
    def voice(self):
        print("Woof-woof")

    def swim(self):
        print("All dogs can swim")


class Cat(Pet, FelineInterface):
    def voice(self):
        print("Meow")

    def scratch(self):
        print("All cats can scratch!")


class Parrot(Pet):
    def voice(self):
        print("You dummy")


def main():
    dog = Dog("Doggo", 3, "Joza", 5, 50)
    dog.swim()


if __name__ == "__main__":
    main()
