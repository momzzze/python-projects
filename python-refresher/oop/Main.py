from Enemy import *

zombie = Enemy("Zombie", health_points=20, attack_damage=2)

# print(zombie.talk())
# print(
#     f"{zombie.type_of_enemy} has {zombie.health_points} health points and {zombie.attack_damage} attack damage."
# )
zombie.talk()
print(zombie.get_type_of_enemy())
