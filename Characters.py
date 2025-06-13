# Hero
class Hero:
    def __init__(self, name, health, attack_power, accuracy, defense, luck, stealth):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.accuracy = accuracy
        self.defense = defense
        self.luck = luck
        self.stealth = stealth

    def display_info(self):
        print(f"Name: {self.name}")
        print("---------------------------------")
        print(f"Health   |  {self.health}  ")
        print("---------------------------------")
        print(f"AP       |  {self.attack_power}")
        print("---------------------------------")
        print(f"Defense  |  {self.defense}  ")
        print("---------------------------------")
        print(f"Accuracy |  {self.accuracy}  ")
        print("---------------------------------")
        print(f"Luck     |  {self.luck}  ")
        print("---------------------------------")
        print(f"Stealth  | {self.stealth}")
        print("---------------------------------")

# Default Hero
hero = Hero("ArKara", 100, 10, .8, 1, .1, .5)
# Data check. Also, display when there are changes to stats.
hero.display_info()