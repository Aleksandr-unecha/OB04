from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец делает выстрел из лука."

class Fighter:
    def __init__(self):
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        weapon_name = self.get_weapon_name(weapon)
        print(f"Боец выбирает {weapon_name}.")

    def get_weapon_name(self, weapon):
        if isinstance(weapon, Sword):
            return "меч"
        elif isinstance(weapon, Bow):
            return "лук"
        else:
            return "неизвестное оружие"

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print("Боец безоружен!")

class Monster:
    def __init__(self):
        self.is_defeated = False

    def defeat(self):
        self.is_defeated = True
        print("Монстр побежден!")

def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeat()

fighter = Fighter()
monster = Monster()

sword = Sword()
fighter.change_weapon(sword)
battle(fighter, monster)

bow = Bow()
fighter.change_weapon(bow)
battle(fighter, monster)