class Animal:
    weight: float
    color: str
    age: int
    animal_type: str

    def __init__(self, weight: float, color: str, age: int, animal_type: str) -> None:
        self.weight = weight
        self.color = color
        self.age = age
        self.animal_type = animal_type

    def eat(self):
        print(f"The {self.color} {self.animal_type} is eating.")

    def sleep(self):
        print(f"The {self.color} {self.animal_type} is sleeping.")
