class Dog:
    def __init__(self, name, age, height, weight, master, address="Minsk"):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__master = master
        self.__address = address

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age





    def bark(self):
        print("Woof-woof!")

    def jump(self):
        print("Jump!")

    def run(self):
        print("Run!")


def main():
    dog1 = Dog("Bob", 3, 40, 3, "Joza")
    print(f"Master: {dog1.get_master()}")
    dog1.set_master("Katkin")
    print(f"New master: {dog1.get_master()}")
    dog1.bark()
    dog1.jump()
    dog1.run()
    print(f"Height: {dog1.height}")
    print(f"Name: {dog1.name}")
    dog1.change_height(50)
    dog1.change_name("Charlie")
    print(f"New height: {dog1.height}")
    print(f"New name: {dog1.name}")
    print(f"Address: {dog1.get_address()}")
    dog1.set_address("Kiev")
    print(f"New address: {dog1.get_address()}")


if __name__ == "__main__":
    main()
