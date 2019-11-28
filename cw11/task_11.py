class Dog:
    def bark(self):
        print("Woof-woof!")

    def jump(self):
        print("Jump!")

    def run(self):
        print("Run!")


def main():
    dog1 = Dog()
    print(dog1)
    dog2 = Dog()
    print(dog2)
    dog1.bark()


if __name__ == "__main__":
    main()
