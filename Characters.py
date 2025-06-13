# Hero
class Hero:
    def __init__(self, name, health, attack_power, status, accuracy, defense, luck, stealth):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.status = status
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
        print(f"Status   |  {self.status}")
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
hero = Hero("ArKara", 100, 10, "healthy", .8, 1, .1, .5)
# Data check. Also, display when there are changes to stats.
hero.display_info()

# Demon (Can be used to create all demon types)
class Demon:
    def __init__(self, name, health, attack_power, status, accuracy, defense, luck, blood_loss, blindness):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.status = status
        self.accuracy = accuracy
        self.defense = defense
        self.luck = luck
        self.blood_loss = blood_loss
        self.blindness = blindness

    def display_info(self):
        print(f"Name: {self.name}")
        print("---------------------------------")
        print(f"Health   |  {self.health}  ")
        print("---------------------------------")
        print(f"AP       |  {self.attack_power}")
        print("---------------------------------")
        print(f"Status   |  {self.status}")
        print("---------------------------------")
        print(f"Defense  |  {self.defense}  ")
        print("---------------------------------")
        print(f"Accuracy |  {self.accuracy}  ")
        print("---------------------------------")
        print(f"Luck     |  {self.luck}  ")
        print("---------------------------------")

# Default Hero
demon1 = Demon("Watchful Demon", 60, 10, "healthy", .99, 3, .1, .2, .01)
# Data check. Also, display when there are changes to stats.
demon1.display_info()