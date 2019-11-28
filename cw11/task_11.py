class Dog:
    def __init__(self, name, age, height, weight, master, address="Minsk"):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__master = master
        self.__address = address

    def get_master(self):
        return self.__master

    def set_master(self, master):
        self.__master = master

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def change_name(self, name):
        self.name = name

    def change_height(self, height):
        self.height = height

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
