# 2) Создайте класс Робот  создайте 2 типа оружия: меч, автомат
# Создайте 2 типа амуниции: броня, шлем
# Добавьте оружию и амуниции свои характеристики(например урон, прочность)
# Создайте своего робота с каким либо оружием (может быть несколько и брони может быть несколько.
# Так же может быть ничего) Выведите весь арсенал робота на экран

class Robot:
    def __init__(self, name, weapons, armor):
        self.name = name
        self.weapons = weapons
        self.armor = armor

class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

class Armor:
    def __init__(self, name, protection, durability):
        self.name = name
        self.protection = protection
        self.durability = durability

# Создание робота и его арсенала
robot = Robot("X-1000", [Weapon("Sword", 50, 100), Weapon("Gun", 80, 150)], [Armor("Shield", 30, 200), Armor("Helmet", 20, 100)])

# Вывод арсенала робота
print("Robot Arsenal:")
print("Name:", robot.name)
print("Weapons:")
for weapon in robot.weapons:
    print(weapon.name, "- Damage:", weapon.damage, "Durability:", weapon.durability)
print("Armor:")
for armor in robot.armor:
    print(armor.name, "- Protection:", armor.protection, "Durability:", armor.durability)

