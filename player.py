import world
import items
import random
import os
import recipes


class Player:
    def __init__(self):
        self.inventory = {items.Rubble: 1}
        self.hp = 50
        self.credits = 10
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.unlocked_recipes = [recipes.MakeShiftKnife]

    def is_alive(self):
        return self.hp > 0

    def print_status(self):
        os.system('cls')
        print("HP: " + str(self.hp))

    def craftmenu(self):
        for recipe in self.unlocked_recipes:
            position = int(self.unlocked_recipes.index(recipe))
            print("{}. {}\n======\n{}\n{}\nDamage: {}\n".format(position + 1, recipe.name, recipe.required_materials,
                                                                recipe.itemclass.description, recipe.itemclass.damage))
        while True:
            try:
                inputselection = input("What item would you to craft?\n")
                numberselected = int(inputselection) - 1
                break
            except ValueError:
                print("Please enter a valid number selection.")
        itemselected = self.unlocked_recipes[numberselected]
        item = itemselected.req_item
        amt = itemselected.req_amt
        if self.inventory[item] == amt:
            print("Item Crafted!")
            self.inventory[item] -= amt
            if self.inventory[item] == 0:
                del self.inventory[item]
            self.inventory.update({itemselected.itemclass: 1})
        else:
            print("You do not have the required items.")

    def print_inventory(self):
        os.system('cls')
        print("Credits: " + str(self.credits))
        for item in self.inventory:
            print("{} x{}\n======\n{}\nValue: {} Credits".format(item.name, self.inventory[item], item.description, item.value))
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
        os.system('cls')
        self.move(dx=0, dy=-1)

    def move_south(self):
        os.system('cls')
        self.move(dx=0, dy=1)

    def move_east(self):
        os.system('cls')
        self.move(dx=1, dy=0)

    def move_west(self):
        os.system('cls')
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        os.system('cls')
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
        os.system('cls')
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
        os.system('cls')
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
        os.system('cls')
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])


'''
inputselection = input("What item would you to craft?\nOr type \"e\" to exit crafting menu.\n")
        if type(inputselection) == int:
            numberselected = int(inputselection) - 1
            recipeselected = self.unlocked_recipes[numberselected]
            item = recipeselected.req_item
            amt = recipeselected.req_amt
            if self.inventory[item] == amt:
                print("OK")
                self.inventory[item] -= amt
                print(self.inventory)
            else:
                print("You do not have the required items.")
        elif type(inputselection) == str:
            if inputselection == "e":
                pass
'''