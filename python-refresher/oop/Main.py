from Enemy import *
from Dog import *
from Animal import *
from Zombie import *
from Ogre import *

# zombie = Enemy("Zombie", health_points=20, attack_damage=2)

# print(zombie.talk())
# print(
#     f"{zombie.type_of_enemy} has {zombie.health_points} health points and {zombie.attack_damage} attack damage."
# )
# zombie.talk()
# print(zombie.get_type_of_enemy())

dog = Dog(30.0, "brown", 5, "dog")
dog.talk()
dog.eat()
dog.sleep()

# zombie = Enemy("Zombie", 10, 1)
# print(zombie.get_type_of_enemy())

zombie = Zombie(10, 1)
ogre = Ogre(100, 15)

print(
    f"{zombie.get_type_of_enemy()} has {zombie.get_health_points()} health points and {zombie.get_attack_damage()} attack damage."
)
print(
    f"{ogre.get_type_of_enemy()} has {ogre.get_health_points()} health points and {ogre.get_attack_damage()} attack damage."
)
zombie.talk()
ogre.talk()
