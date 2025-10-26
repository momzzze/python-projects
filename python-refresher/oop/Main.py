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
def battle(e: Enemy, target: Enemy):
    round = 1
    e.talk()
    target.talk()
    print("Battle commences!")
    while e.get_health_points() > 0 and target.get_health_points() > 0:
        print(f"\n--- New Battle Round ---{round}---")
        e.attack(target)
        e.special_attack(target)
        target.attack(e)
        target.special_attack(e)
        round += 1
        print(
            f"{e.get_type_of_enemy()} has {e.get_health_points()} health points left."
        )
        print(
            f"{target.get_type_of_enemy()} has {target.get_health_points()} health points left."
        )
        print(f"--- End of Battle Round ---{round}---\n")


zombie = Zombie(100, 15)
ogre = Ogre(100, 15)

# print(
#     f"{zombie.get_type_of_enemy()} has {zombie.get_health_points()} health points and {zombie.get_attack_damage()} attack damage."
# )
# print(
#     f"{ogre.get_type_of_enemy()} has {ogre.get_health_points()} health points and {ogre.get_attack_damage()} attack damage."
# )
# zombie.talk()
# ogre.talk()
battle(zombie, ogre)
battle(ogre, zombie)
