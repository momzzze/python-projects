import random
from Enemy import Enemy


class Ogre(Enemy):
    def __init__(self, health_points=50, attack_damage=10):
        super().__init__(
            type_of_enemy="Ogre",
            health_points=health_points,
            attack_damage=attack_damage,
        )

    def talk(self):
        print(f"{self.get_type_of_enemy()} growls: 'Grrrr...'")

    def smash(self):
        print("The ogre smashes the ground with immense force!")

    def special_attack(self, target):
        bonus_damage = random.randint(0, 5)
        vamp_healing = random.randint(1, 10)
        print(
            f"{self.get_type_of_enemy()} performs a powerful smash on {target.get_type_of_enemy()}!"
        )
        target.take_damage(self.get_attack_damage() + bonus_damage)
        self.increase_health(vamp_healing)
        self.healing()
