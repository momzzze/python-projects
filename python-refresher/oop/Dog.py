from Animal import Animal


class Dog(Animal):
    can_shed: bool
    domestic_name: str

    def talk(self):
        print("Bark!")
