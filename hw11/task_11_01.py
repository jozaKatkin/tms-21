# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.


class Mattress:
    def __init__(self, color, material, name="Hovog", style="flexy"):
        self.__name = name
        self.color = color
        self.__style = style
        self.__material = material

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            print("Name is too long")

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style):
        if len(style) < 10:
            self.__style = style
        else:
            print("Too long to be stylish")

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material=None):
        if material:
            self.__material = material
        else:
            print("Too good to change, bud")

    def change_color(self, color):
        self.color = color

    def do_flex(self, jump):
        if jump:
            print("..Bouncing...")
        else:
            print("Thought you want to have fun")

    def hit(self):
        print("Don't push me like that!")


class Blanket:
    def __init__(self, material, name="Tusson", style="warm", weight=0.5):
        self.weight = weight
        self.__name = name
        self.__style = style
        self.__material = material

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            print("Name is too long")

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style):
        if len(style) < 10:
            self.__style = style
        else:
            print("Too long to be stylish")

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material=None):
        if material:
            self.__material = material
        else:
            print("Too good to change, bud")

    def change_weight(self, weight):
        self.weight = weight

    def warm_up(self, warm):
        if warm:
            print("Hey, you comfy?")

    def make_bed(self, make_bed):
        print("I'm such a mess! Do something with this")
        if make_bed:
            print("Thanx, bud")
        else:
            print("Sad")


class Chair:
    def __init__(self, material, name="Teodores", style="solid",
                 chair_legs=3):
        self.__chair_legs = chair_legs
        self.__name = name
        self.__style = style
        self.__material = material

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            print("Name is too long")

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style):
        if len(style) < 10:
            self.__style = style
        else:
            print("Too long to be stylish")

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material=None):
        if material:
            self.__material = material
        else:
            print("Too good to change, bud")

    @property
    def chair_legs(self):
        return self.__chair_legs

    @chair_legs.setter
    def chair_legs(self, chair_legs):
        self.__chair_legs = chair_legs

    def sit(self):
        if self.chair_legs < 3:
            print("Not enough legs. I'm falling!")
        elif self.chair_legs > 4:
            print("I'm a centipede now...")
        else:
            print("Chilling..")

    def break_chair(self):
        print("It hurts...")


class Computer:
    def __init__(self, color, name="Macintosh", RAM=8, SSD=12):
        self.__color = color
        self.__name = name
        self.__SSD = SSD
        self.RAM = RAM

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            print("Name is too long")

    @property
    def SSD(self):
        return self.SSD

    @SSD.setter
    def SSD(self, SSD):
        if SSD < 1024:
            self.__SSD = SSD
        else:
            print("Not enough slots")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def change_RAM(self, diff=2):
            self.RAM += diff

    def plug_in(self):
        print("Whrrrrr....")


class Cup:
    def __init__(self, color, name="Usual cup", comment="electric heating", vol=300):
        self.color = color
        self.__name = name
        self.__comment = comment
        self.__vol = vol

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment):
        self.__comment = comment

    def change_color(self, color):
        self.color = color

    @property
    def vol(self):
        return self.__vol

    @vol.setter
    def vol(self, vol):
        if vol < 250:
            self.__name = "Coffee cup"
            self.__vol = vol
        elif vol > 450:
            self.__name = "Boss's cup"
            self.__vol = vol
        else:
            self.__vol = vol

    def heating(self):
        print("Temperature is 50 degrees")

    def break_cup(self, break_cup=True):
        if break_cup:
            print("I'm broken now :[")
        if not break_cup:
            print("Good")


def main():
    matress = Mattress("black", "cotton")
    matress.do_flex(True)
    matress.material = ""
    print(matress.material)
    matress.style = "heyheyheyyy"
    matress.name = "Fuuuuuuuuuu"
    #
    blanket = Blanket("Light", "fabric")
    print(blanket.weight)
    blanket.make_bed(True)
    blanket.weight = 2
    #
    chair = Chair("wood", chair_legs=6)
    chair.sit()
    chair.chair_legs = 2
    print(chair.chair_legs)
    #
    computer = Computer("black")
    computer.SSD = 2048
    computer.change_RAM()
    print(computer.RAM)
    #
    cup = Cup("white")
    cup.vol = 200
    print(cup.name)
    cup.break_cup(False)


if __name__ == '__main__':
    main()
