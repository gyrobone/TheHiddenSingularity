# Base Classes
class Item:
    name = None
    description = None
    value = 0


class HealingItem(Item):
    healamount = 0


class Weapon(Item):
    damage = 0


class CraftingItem(Item):
    pass


# Crafting Items and Weapon Classes
class Dagger(Weapon):
    itemtype = "Weapon"
    name = "Dagger"
    description = "Standard Issue UEIC military dagger. Can be used as a weapon or for cutting things."
    value = 10
    damage = 8


class Rubble(CraftingItem):
    damage = None
    healamount = None
    itemtype = "Crafting Item"
    name = "Rubble"
    description = "A piece of debris from the crashed ship. Can be used for crafting."
    value = 0
    tier = 0


# Healing Items
class Gauze(HealingItem):
    itemtype = "Healing Item"
    name = "Gauze"
    description = "A small piece of gauze that can patch up small wounds."
    value = 5
    healamount = 5


class Bandage(HealingItem):
    itemtype = "Healing Item"
    name = "Bandage"
    description = "A medium-sized bandage that can slow bleeding and cover up larger cuts."
    value = 10
    healamount = 10


class FirstAidKit(HealingItem):
    itemtype = "Healing Item"
    name = "First Aid Kit"
    description = "A first aid kit that can stop bleeding and patch major incisions."
    value = 20
    healamount = 20


class Splint(HealingItem):
    itemtype = "Healing Item"
    name = "Splint"
    description = "A metal split that can repair broken limbs."
    value = 15
    healamount = 8
