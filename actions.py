from player import Player


class Action:
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey="e", enemy=enemy)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move North', hotkey='w')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move South', hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move East', hotkey='d')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move West', hotkey='a')


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View Inventory', hotkey='i')


class Heal(Action):
    def __init__(self):
        super().__init__(method=Player.heal, name='Use Best Healing Item', hotkey='h')


class LookAround(Action):
    def __init__(self):
        super().__init__(method=Player.look_around, name='Look Around', hotkey='l')


class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)


class Status(Action):
    def __init__(self):
        super().__init__(method=Player.print_status, name="Check Health Status", hotkey='q')


class CraftMenu(Action):
    def __init__(self):
        super().__init__(method=Player.craftmenu, name="Open Crafting Menu", hotkey="c")
