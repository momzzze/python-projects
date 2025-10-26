class Enemy:
    def __init__(
        self, type_of_enemy, health_points=10, attack_damage=1, special_attack=None
    ):
        self.__type_of_enemy = type_of_enemy
        self.__health_points = health_points
        self.__attack_damage = attack_damage
        self.__special_attack = special_attack

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"{self.get_type_of_enemy()} says: 'I will defeat you!'")

    def increase_health(self, amount):
        self.__health_points += amount
        print(
            f"{self.__type_of_enemy} increases health by {amount}! New health: {self.__health_points}"
        )

    def healing(self):
        print(f"{self.__type_of_enemy} is healing!")
        self.__health_points += 10

    def take_damage(self, damage):
        self.__health_points -= damage
        print(
            f"{self.__type_of_enemy} takes {damage} damage! Remaining health: {self.__health_points}"
        )
        if self.__health_points <= 0:
            self.death()

    def death(self):
        if self.__health_points <= 0:
            print(f"{self.__type_of_enemy} has been defeated!")

    def attack(self, target):
        print(
            f"{self.__type_of_enemy} attacks {target.get_type_of_enemy()} for {self.__attack_damage} damage!"
        )
        target.take_damage(self.__attack_damage)

    def walk_forward(self):
        print(f"{self.__type_of_enemy} walks forward.")

    def get_health_points(self):
        return self.__health_points

    def get_attack_damage(self):
        return self.__attack_damage

    def special_attack(self, target):
        # Optional base placeholder (can be overridden by subclasses)
        print(
            f"{self.get_type_of_enemy()} tries a special move, but nothing happens..."
        )
