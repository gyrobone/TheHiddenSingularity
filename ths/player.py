import items
import world
import random


class Player:
    def __init__(self):
        self.inventory = [items.Rubble]
        self.hp = 50
        self.credits = 10
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_status(self):
        print("HP: " + str(self.hp))

    def print_inventory(self):
        print("Credits: " + str(self.credits))
        for item in self.inventory:
            print("{}\n======\n{}\nValue: {} Credits".format(item.name, item.description, item.value))
            if item.itemtype == "Weapon":
                print("Damage: {} dmg/hit\n".format(item.damage))
            elif item.itemtype == "Healing Item":
                print("Heals: {} HP\n".format(item.healamount))
            elif item.itemtype == "Crafting Item":
                print("Tier: {}\n".format(item.tier))

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if i.itemtype == "Weapon":
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        if best_weapon is None:
            print("You have no weapon to use.")
            pass
        else:
            print("You use {} against {} for {} damage!".format(best_weapon.name, enemy.name, best_weapon.damage))
            enemy.hp -= best_weapon.damage
            if not enemy.is_alive():
                print("You killed {}!".format(enemy.name))
            else:
                print("{} HP is {}".format(enemy.name, enemy.hp))

    def heal(self):
        best_healitem = None
        heal_amount = 0
        for i in self.inventory:
            if i.itemtype == "Healing Item":
                if i.healamount > heal_amount:
                    heal_amount = i.healamount
                    best_healitem = i
        if best_healitem is None:
            print("You have no healing item to use.")
            pass
        else:
            print("You used {} and healed {} HP".format(best_healitem.name, best_healitem.healamount))
            self.hp += best_healitem.healamount
            print("HP: " + str(self.hp))

    def look_around(self):
        currenttile = world.tile_exists(self.location_x, self.location_y)
        if currenttile.hasloot is True:
            currenttile.lootprompt()
        else:
            print("There is nothing of interest here.")

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self, tile):
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
