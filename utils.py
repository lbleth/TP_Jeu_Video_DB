import db_init
import random
import time

def center(texte: str):
    print("=" * 20)
    print(texte.center(20))
    print("=" * 20)
    
def print_menu():
    texte = "JEU DE OUF"
    center(texte)

    print("1. Démarrer une partie")
    print("2. Classement")
    print("3. Quitter")


def input_choice():
    choice = int(input("Quel est votre choix ? (1, 2, ou 3)"))
    choices = [1, 2, 3]
    if choice not in choices:
        print("Choix invalide.")
        return input_choice()
    return choice

def fill_team():
    team = []
    while len(team) < 3:
        print(f'Tu peux choisir {3 - len(team)} personnage(s)')
        team_choice = input('Quel personnage choisissez-vous ?')
        find_player = db_init.database("characters")
        player = find_player.find_one({'name' : team_choice})
        if player == None:
            print("Erreur, veuillez recommencer")
        elif player in team:
            print("Ce personnage est déjà dans ton équipe.")
        else:
            team.append(player)
    current_team(team)
    return team

def username():
    name = input('Quel pseudo voulez-vous mettre ?')
    return name

def choose_character():
    collection = db_init.database("characters")
    found_character = collection.find()
    for character in found_character:
        print (f"NOM : {character['name']} | ATK : {character['atk']} | DEF : {character['def']} | PV : {character['hp']}")
    team = fill_team()
    return team 

def choose_enemy():
    random_enemy = random.randint(0,9)
    find_enemy = db_init.database("enemy")
    enemy = find_enemy.find_one({'nb' : random_enemy})
    show_enemy(enemy)
    return enemy

def show_enemy(enemy):
    center('ADVERSAIRE')
    print (f'NOM : {enemy['name']} | ATK : {enemy['atk']} | DEF : {enemy['def']} | PV : {enemy['hp']}')
    time.sleep(1)

def current_team(team):
    center('MON EQUIPE')
    for character in team:
        print (f"NOM : {character['name']} | ATK : {character['atk']} | DEF : {character['def']} | PV : {character['hp']}")
    time.sleep(1)
