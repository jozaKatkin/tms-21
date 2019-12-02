class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def change_weight(self, diff=0.2):
        self.weight += diff

    def change_height(self, height):
        self.height = height
        if height:
            self.height = height
        else:
            self.height += 0.2

    def run(self):
        print("Run!")

    def jump(self, height):
        print(f"Jump\n{height}!")

    def sleep(self):
        print("Sleep...")

    def birthday(self):
        self.age += 1


class Dog(Pet):
    def bark(self):
        print("Woof-woof")

    def jump(self, height):
        if height > 0.5:
            print("Dogs cannot jump so high")
        else:
            super().jump(height)


class Cat(Pet):
    def meow(self):
        print("Meow")

    def jump(self, height):
        if height > 0.5:
            print("Cats cannot jump so high")
        else:
            super().jump(height)


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species


    def fly(self):
        if self.weight > 0.1:
            print("This parrot cannot fly")
        else:
            print("Flies away...")

    def jump(self, height):
        if height > 0.5:
            print("Parrots cannot jump so high")
        else:
            super().jump(height)

    def change_weight(self, diff=0.05):
        self.weight += diff

    def change_height(self, height=0.05):
        self.height += height


#
parrot = Parrot("Yasha", 3, "Joza", 0.2, 10, "Some parrot")
print(parrot.species)
print(parrot.weight)
parrot.change_weight()
print(parrot.weight)
parrot.jump(0.6)
#
dog = Dog("Yasha", 3, "Joza", 0.2, 10)
dog.jump(0.5)
#
