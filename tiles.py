import items
import enemies
import actions
import world


# Base Room Types
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def lootprompt(self):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Heal())
        moves.append(actions.LookAround())
        moves.append(actions.Status())
        return moves


'''
class LootRoom(MapTile):
    def __init__(self, x, y, item, gold_amount):
        self.item = item
        self.gold_amount = gold_amount
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)
        player.gold += self.gold_amount

    def modify_player(self, player, gold_amount):
        self.add_loot(player)

    def intro_text(self):
        pass
'''


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))

    def intro_text(self):
        pass

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy), actions.Heal()]
        else:
            return self.adjacent_moves()

    def lootprompt(self):
        pass


class StartingRoom(MapTile):
    hasloot = False
    visited = False

    def modify_player(self, player):
        pass

    def intro_text(self):
        return """
        With your eyes slowly blinking open, you find yourself in a room illuminated by the sparks of electricity coming
        from the walls. The room smells of burnt flesh and you remember nothing. You look down to see blood coming from 
        your uniform but your adrenaline distracts you from the pain. You must find a way to stop the bleeding and 
        figure out what is going on.
        There is a door on each wall of the room.
        """

    def lootprompt(self):
        pass


# Specific Rooms
class EmptyRoom(MapTile):
    hasloot = False
    visited = False

    def intro_text(self):
        return """
        An empty room with sparking wires and a foul stench. There is nothing of interest in here.
        The only door is the one you came from to the East.
        """

    def modify_player(self, player):
        pass

    def lootprompt(self):
        pass


class EmptyShipHall(MapTile):
    hasloot = False
    visited = False

    def intro_text(self):
        return """
        An empty hallway aboard the ship. Nothing interesting sticks out to you.
        You can continue North or go back the the last room to the South.
        """

    def modify_player(self, player):
        pass

    def lootprompt(self):
        pass


class FindDaggerRoom(MapTile):
    hasloot = True
    visited = False

    def intro_text(self):
        return """
        As you step foot into the room, you see a fellow crewmember lying dead on the floor. In their hand is a 
        dagger. You take the dagger from their hand.
        The only door is the one you came from to the North.
        """

    def lootprompt(self):
        pass

    def modify_player(self, player):
        if world.tile_exists(player.location_x, player.location_y).visited is False:
            player.inventory.append(items.Dagger)
        else:
            pass


class FindBandageRoom(MapTile):
    hasloot = False
    visited = False

    def modify_player(self, player):
        if world.tile_exists(player.location_x, player.location_y).visited is False:
            player.inventory.append(items.Bandage)
            player.credits += 10
        else:
            pass

    def intro_text(self):
        return """
        You walk into a small room off of the main corrider. There is a small table in the room with a bandage sitting 
        on top. You collect the bandage. You also collect 10 Gold scattered across the table.
        The only door is the one you came from to the West.
        """

    def lootprompt(self):
        pass


class FirstEncounter(EnemyRoom):
    hasloot = False
    visited = False

    def __init__(self, x, y):
        super().__init__(x, y, enemies.AchariGrunt())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A small, skinny creature jumps towards you, leaving its half-eaten flesh dinner behind.
            """
        else:
            return """
            The corpse of an Achari Grunt squirms on the floor.
            """

    def lootprompt(self):
        pass


class LeaveShip(MapTile):
    hasloot = False
    visited = False

    def intro_text(self):
        return """
        As you walk into the room, bright lights blind you. You heard the sound of heavy footsteps approach.
        It's the rescue team! They have saved you from the alien invasion!
        """

    def modify_player(self, player):
        player.victory = True

    def lootprompt(self):
        pass
