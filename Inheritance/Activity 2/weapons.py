
class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage

    def get_stats(self):
        print(f"Name: {self.name}, Category: {self.category}, Damage: {self.damage}")


class Sword(Weapon):
    def __init__(self, name, damage, damage_category):
        super().__init__(name, "Sword", damage)
        self.damage_category = damage_category
    
    def get_stats(self):
        crit_damage = self.damage * 3
        print(f"Name: {self.name}, Category: {self.category}, Damage: {self.damage}, Damage Type: {self.damage_category}, Crit Damage: {crit_damage}")
