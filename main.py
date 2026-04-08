import os
import utils
import game

def main():
    os.system('cls')
    utils.print_menu()
    choice = utils.input_choice()
    if choice == 1:
        team = utils.choose_character()
        game.start_fight(team)
    elif choice == 2:
        print("Classement")
    elif choice == 3:
        print("Au revoir !")

main()
