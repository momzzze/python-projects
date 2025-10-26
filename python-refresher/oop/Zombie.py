from Enemy import *


class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy="Zombie",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        print(f"{self.get_type_of_enemy()} groans: 'Braaaains...'")

    def spread_disease(self):
        print("The zombie is trying to spread infection!")
