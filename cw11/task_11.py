class Dog:
    def __init__(self, name, age, height, weight, ):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def change_name(self, name):
        self.name = name

    def bark(self):
        print("Woof-woof!")

    def jump(self):
        print("Jump!")

    def run(self):
        print("Run!")


def main():
    dog1 = Dog("Bob", 3, 40, 3)
    dog1.bark()
    dog1.jump()
    dog1.run()
    print(dog1.height)
    print(dog1.name)
    dog1.change_name("Charlie")
    print(dog1.name)


if __name__ == "__main__":
    main()
