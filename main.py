from game import Game
from exceptions import *
import ui

def start_game():
    Game.init_game()
    over = False
    win = False

    while not (over or win):

        action = ui.cli(Game.objects, Game.entities, Game.used_resources)
        if action:
            o = action(Game.project)
            Game.objects.append(o)

        for o in Game.objects:
            try:
                o.turn()
            except NotEnoughFundsException:
                over = True
            except WinException:
                win = True

        Game.used_resources.turn_count += 1

    print(chr(27) + "[2J")
    if over:
        print("---------")
        print("GAME OVER")
        print("---------")
        print(Game.project)
        print("Score: {}".format(Game.project.score))

    if win:
        print("---------")
        print("YOU WON")
        print("---------")
        print(Game.project)
        print("Score: {}".format(Game.project.score))

if __name__ == "__main__":
    start_game()
