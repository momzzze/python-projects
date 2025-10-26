class Enemy:
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy
        self.__health_points = health_points
        self.__attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"{self.get_type_of_enemy()} says: 'I will defeat you!'")

    # def attack(self, target):
    #     print(
    #         f"{self.type_of_enemy} attacks {target.type_of_enemy} for {self.attack_damage} damage!"
    #     )

    def walk_forward(self):
        print(f"{self.__type_of_enemy} walks forward.")

    def get_health_points(self):
        return self.__health_points

    def get_attack_damage(self):
        return self.__attack_damage
