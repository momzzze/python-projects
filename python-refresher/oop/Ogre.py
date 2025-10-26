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
