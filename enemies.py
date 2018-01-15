# Base Enemy Alien Race Classes
class Achari:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


# Achari Enemies
class AchariGrunt(Achari):
    def __init__(self):
        super().__init__(name="Achari Grunt", hp=10, damage=5)


class AchariSpitter(Achari):
    def __init__(self):
        super().__init__(name="Achari Spitter", hp=20, damage=12)
