class Dog:
    def __init__(self, name, age, height, weight, master):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__master = master

    def get_master(self):
        return self.__master

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
    dog1.bark()
    dog1.jump()
    dog1.run()
    print(f"Height: {dog1.height}")
    print(f"Name: {dog1.name}")
    dog1.change_height(50)
    dog1.change_name("Charlie")
    print(f"New height: {dog1.height}")
    print(f"New name: {dog1.name}")


if __name__ == "__main__":
    main()
