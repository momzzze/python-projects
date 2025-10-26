import random
from Enemy import *


class Zombie(Enemy):
    def __init__(
        self,
        health_points,
        attack_damage,
    ):
        super().__init__(
            type_of_enemy="Zombie",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        print(f"{self.get_type_of_enemy()} groans: 'Braaaains...'")

    def spread_disease(self):
        print("The zombie is trying to spread infection!")

    def special_attack(self, target):
        bonus_damage = random.randint(0, 5)
        vamp_healing = random.randint(1, 10)
        print(f"{self.get_type_of_enemy()} bites {target.get_type_of_enemy()}!")
        target.take_damage(self.get_attack_damage() + bonus_damage)
        self.increase_health(vamp_healing)
        self.healing()
