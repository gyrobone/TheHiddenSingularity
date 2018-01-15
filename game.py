import world
from player import Player
from pygame import mixer
mixer.init()
mixer.music.load('ths_music.mp3')
mixer.music.play()
mixer.music.set_volume(.5)


def play():
    world.load_tiles()
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        room.visited = True
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
    print("===GAME OVER===")


if __name__ == "__main__":
    play()
